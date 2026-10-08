#!/usr/bin/env python3
"""Audit Denno-Watch's complete Markdown/OKF corpus, without network access.

Scope: every Markdown file, all domestic/international incident front matters,
all internal Markdown links, source IDs and footnote references, and yearly
index coverage. This is a structural and provenance audit; it does not assert
that externally published facts or remote source URLs have been reverified.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", re.S)
LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
NOTE_RE = re.compile(r"^\[\^([^\]]+)\]:", re.M)
NOTE_USE_RE = re.compile(r"\[\^([^\]]+)\]")
SOURCE_ID_RE = re.compile(r"^  - id:\s*(.+?)\s*$", re.M)
INCIDENT_FIELD_RE = re.compile(r"^  ([a-z_][a-z_0-9]+):\s*(.*)$", re.M)
TOP_KEY_RE = re.compile(r"^([a-z][a-z_0-9]+):(?:\s|$)", re.M)
URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
REQUIRED_FIELDS = (
    "organization", "sector", "jurisdiction", "incident_status",
    "attack_type", "first_disclosed_at", "latest_public_update", "data_exposure"
)
CORE_DIRECTORIES = ("analysis", "methodology", "incidents")


def check() -> dict:
    docs = sorted(ROOT.rglob("*.md"))
    errors: list[dict] = []
    warnings: list[dict] = []
    by_kind: Counter[str] = Counter()
    domestic: Counter[str] = Counter()
    qa: list[dict] = []

    def add(level: str, path: Path, code: str, detail: str) -> None:
        item = {"path": path.relative_to(ROOT).as_posix(), "code": code, "detail": detail}
        (errors if level == "error" else warnings).append(item)

    for path in docs:
        rel = path.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts):
            continue
        text = path.read_text(encoding="utf-8-sig")
        parts = rel.parts
        kind = parts[0] if parts else "root"
        by_kind[kind] += 1
        is_incident = (len(parts) == 3 and parts[0] == "incidents"
                       and parts[1] in {"2023", "2024", "2025", "2026", "international"}
                       and path.name != "index.md")
        fm = FM_RE.match(text)
        if kind in CORE_DIRECTORIES and path.name != "index.md" and not fm:
            add("error", path, "missing_front_matter", "OKF front matter absent")
        if fm:
            header, body = fm.group(1), text[fm.end():]
            top = {m.group(1) for m in TOP_KEY_RE.finditer(header)}
            for key in ("type", "title", "status"):
                if key not in top:
                    add("warning", path, "missing_top_key", key)
            if is_incident:
                domestic[parts[1]] += 1
                if re.search(r"^type:\s*Cybersecurity Incident\s*$", header, re.M) is None:
                    add("error", path, "incident_type", "wrong or missing type")
                match = re.search(r"^incident:\s*\n(.*?)(?=^[a-z][a-z_0-9]+:|\Z)", header, re.M | re.S)
                if not match:
                    add("error", path, "missing_incident", "incident mapping absent")
                    fields = {}
                else:
                    fields = dict(INCIDENT_FIELD_RE.findall(match.group(1)))
                for field in REQUIRED_FIELDS:
                    if field not in fields:
                        add("warning", path, "missing_incident_field", field)
                if "public_record_checked_at" not in fields:
                    add("warning", path, "missing_checked_at", "last active source check not recorded")
                if "sources" not in top:
                    add("warning", path, "missing_sources", "sources front matter absent")
                if len(body.strip()) < 1100:
                    add("warning", path, "thin_body", f"only {len(body.strip())} characters")
                qa.append({
                    "path": rel.as_posix(), "date": fields.get("latest_public_update"),
                    "checked": fields.get("public_record_checked_at"),
                    "exposure": fields.get("data_exposure"),
                    "source_count": len(SOURCE_ID_RE.findall(header)),
                    "body_chars": len(body.strip()),
                })
            sources = SOURCE_ID_RE.findall(header)
            for source, count in Counter(sources).items():
                if count > 1:
                    add("error", path, "duplicate_source_id", source)
        else:
            header, body = "", text
        defs = NOTE_RE.findall(body)
        for fid, count in Counter(defs).items():
            if count > 1:
                add("error", path, "duplicate_footnote_definition", fid)
        note_uses = []
        for line in body.splitlines():
            if not NOTE_RE.match(line):
                note_uses.extend(NOTE_USE_RE.findall(line))
        for fid in sorted(set(note_uses) - set(defs)):
            add("warning", path, "unresolved_footnote", fid)
        for fid in sorted(set(defs) - set(note_uses)):
            add("warning", path, "unused_footnote", fid)
        for match in LINK_RE.finditer(body):
            dest = match.group(1).strip().split(" ")[0].strip("<>").strip('"').strip("'")
            dest = unquote(dest.split("#", 1)[0].split("?", 1)[0])
            if not dest or URL_SCHEME_RE.match(dest) or dest.startswith("//"):
                continue
            target = (path.parent / dest).resolve()
            if not target.is_relative_to(ROOT):
                add("error", path, "escaping_internal_link", dest)
            elif not target.exists():
                add("warning", path, "broken_internal_link", dest)
    # Index coverage: a file can exist on disk yet be invisible to readers.
    for year in ("2023", "2024", "2025", "2026", "international"):
        index = ROOT / "incidents" / year / "index.md"
        if not index.is_file():
            add("error", ROOT / "incidents" / "index.md", "year_index_missing", year)
            continue
        lines = index.read_text(encoding="utf-8-sig")
        for f in sorted((ROOT / "incidents" / year).glob("*.md")):
            if f.name != "index.md" and f.name not in lines:
                add("warning", index, "case_not_in_year_index", f.name)
    return {
        "files_scanned": len(docs), "kind_counts": dict(by_kind),
        "incident_counts": dict(domestic),
        "domestic_total": sum(domestic[k] for k in ("2023", "2024", "2025", "2026")),
        "international_total": domestic["international"],
        "errors": errors, "warnings": warnings, "incident_inventory": qa,
        "warning_types": dict(Counter(x["code"] for x in warnings)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, help="optional machine-readable report")
    parser.add_argument("--strict", action="store_true", help="fail on structural errors")
    args = parser.parse_args()
    result = check()
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Markdown files:", result["files_scanned"])
    print("Domestic by year:", {k: result["incident_counts"].get(k, 0) for k in ("2023", "2024", "2025", "2026")})
    print("International:", result["international_total"])
    print("Structural errors:", len(result["errors"]))
    print("Items to review:", len(result["warnings"]), result["warning_types"])
    for item in result["errors"]:
        print("ERROR", item["path"], item["code"], item["detail"])
    for item in result["warnings"][:40]:
        print("REVIEW", item["path"], item["code"], item["detail"])
    return 1 if args.strict and result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
