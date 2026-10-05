#!/usr/bin/env python3
"""Build the Denno Watch browser catalog from OKF-flavoured Markdown.

The Markdown/OKF records remain the source of truth. This script extracts only
reader-facing metadata needed by the static GitHub Pages UI. It intentionally
uses the Python standard library so Pages builds do not depend on package
installation or third-party services.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ("incidents", "analysis", "methodology")
EXCLUDED_NAMES = {"index.md"}
SEARCH_TEXT_LIMIT = 9000

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
MARKDOWN_NOISE_RE = re.compile(r"[`*_>#|\[\]{}()]+")
SPACE_RE = re.compile(r"\s+")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return [unquote(value)] if value else []
    body = value[1:-1].strip()
    if not body:
        return []
    return [unquote(item.strip()) for item in body.split(",") if item.strip()]


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """Extract the subset of YAML used by the UI without implementing YAML.

    Denno Watch's public records use a stable, simple shape for the fields the
    UI consumes. Unknown/nested sections are left untouched rather than guessed.
    """
    match = FRONT_MATTER_RE.search(text)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end() :]
    meta: dict[str, Any] = {}
    section: str | None = None

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        # Ignore list items from complex sections such as sources.
        if stripped.startswith("-"):
            continue

        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        if indent == 0:
            section = key if not value else None
            if not value:
                meta.setdefault(key, {})
                continue

            if key == "tags":
                meta[key] = parse_inline_list(value)
            elif key == "generated":
                at_match = re.search(r"\bat:\s*([^,}]+)", value)
                by_match = re.search(r"\bby:\s*([^,}]+)", value)
                meta[key] = {
                    "at": unquote(at_match.group(1).strip()) if at_match else None,
                    "by": unquote(by_match.group(1).strip()) if by_match else None,
                }
            else:
                meta[key] = unquote(value)
            continue

        if indent == 2 and section == "incident" and value:
            incident = meta.setdefault("incident", {})
            incident[key] = (
                parse_inline_list(value) if key.endswith("_channels") else unquote(value)
            )

    return meta, body


def clean_text(value: str) -> str:
    value = re.sub(r"\[\^[^\]]+\]", " ", value)
    value = re.sub(r"https?://\S+", " ", value)
    value = MARKDOWN_NOISE_RE.sub(" ", value)
    return SPACE_RE.sub(" ", value).strip()


def first_paragraph(body: str) -> str:
    for block in re.split(r"\n\s*\n", body):
        candidate = block.strip()
        if not candidate or candidate.startswith("#") or candidate.startswith("|"):
            continue
        if candidate.startswith("[\^") or candidate.startswith("-"):
            continue
        cleaned = clean_text(candidate)
        if len(cleaned) >= 24:
            return cleaned[:360]
    return ""


def category_for(path: Path) -> str:
    if path.parts[0] == "incidents":
        return "incident"
    if path.parts[0] == "analysis":
        return "analysis"
    return "methodology"


def year_for(path: Path, meta: dict[str, Any]) -> int | None:
    if path.parts[0] == "incidents" and len(path.parts) > 1 and path.parts[1].isdigit():
        return int(path.parts[1])
    incident = meta.get("incident") or {}
    for key in ("first_disclosed_at", "detected_at", "earliest_known_activity"):
        value = str(incident.get(key, ""))
        match = re.match(r"(20\d{2})", value)
        if match:
            return int(match.group(1))
    return None


def document_from(path: Path) -> dict[str, Any]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    incident = meta.get("incident") if isinstance(meta.get("incident"), dict) else {}

    heading = HEADING_RE.search(body)
    title = str(meta.get("title") or (heading.group(1).strip() if heading else rel.stem))
    summary = str(meta.get("description") or meta.get("summary") or first_paragraph(body))
    generated = meta.get("generated") if isinstance(meta.get("generated"), dict) else {}

    latest_public_update = incident.get("latest_public_update")
    first_disclosed_at = incident.get("first_disclosed_at")
    generated_at = generated.get("at")
    updated_at = latest_public_update or first_disclosed_at or generated_at

    search_source = " ".join(
        filter(
            None,
            [
                title,
                summary,
                str(incident.get("organization", "")),
                str(incident.get("sector", "")),
                str(incident.get("attack_type", "")),
                " ".join(meta.get("tags") or []),
                clean_text(body[:SEARCH_TEXT_LIMIT]),
            ],
        )
    )

    return {
        "id": rel.as_posix(),
        "path": rel.as_posix(),
        "category": category_for(rel),
        "year": year_for(rel, meta),
        "type": meta.get("type"),
        "title": title,
        "summary": summary,
        "status": meta.get("status"),
        "tags": meta.get("tags") or [],
        "staleAfter": meta.get("stale_after"),
        "generatedAt": generated_at,
        "generatedBy": generated.get("by"),
        "updatedAt": updated_at,
        "incident": {
            "organization": incident.get("organization"),
            "sector": incident.get("sector"),
            "jurisdiction": incident.get("jurisdiction"),
            "incidentStatus": incident.get("incident_status"),
            "attackType": incident.get("attack_type"),
            "earliestKnownActivity": incident.get("earliest_known_activity"),
            "detectedAt": incident.get("detected_at"),
            "firstDisclosedAt": first_disclosed_at,
            "latestPublicUpdate": latest_public_update,
            "dataExposure": incident.get("data_exposure"),
            "availabilityImpact": incident.get("availability_impact"),
            "restorationState": incident.get("restoration_state"),
            "aiRelation": incident.get("ai_relation"),
        }
        if incident
        else None,
        "searchText": clean_text(search_source).casefold(),
    }


def collect_documents() -> list[dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    for dirname in SCAN_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name in EXCLUDED_NAMES:
                continue
            documents.append(document_from(path))

    documents.sort(
        key=lambda item: (
            item.get("updatedAt") or "",
            item.get("year") or 0,
            item.get("title") or "",
        ),
        reverse=True,
    )
    return documents


def build_catalog() -> dict[str, Any]:
    documents = collect_documents()
    counts = {
        "documents": len(documents),
        "incidents": sum(doc["category"] == "incident" for doc in documents),
        "analysis": sum(doc["category"] == "analysis" for doc in documents),
        "methodology": sum(doc["category"] == "methodology" for doc in documents),
    }
    years = sorted({doc["year"] for doc in documents if doc.get("year")}, reverse=True)
    return {
        "schemaVersion": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "counts": counts,
        "years": years,
        "documents": documents,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "site" / "catalog.json",
        help="Catalog output path (default: site/catalog.json)",
    )
    args = parser.parse_args()

    catalog = build_catalog()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        "catalog:",
        catalog["counts"]["documents"],
        "documents ->",
        output.relative_to(ROOT) if output.is_relative_to(ROOT) else output,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
