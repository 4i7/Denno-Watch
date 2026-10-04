#!/usr/bin/env python3
"""日本語本文に残った英語Jargon候補を検出する。

全英単語を禁止するのではなく、Denno Watchで日本語表記へ統一すると決めた
表現と、人が読む見出しに残る不要な英語を検査する。YAMLフロントマター、
URL、インラインコード、コードブロック、脚注の正式な出典表記は対象外。
AI/IT/セキュリティ分野で一般化した略語や固有名は見出しでも許容する。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASCII_LEFT = r"(?<![A-Za-z0-9_])"
ASCII_RIGHT = r"(?![A-Za-z0-9_])"
JAPANESE = re.compile(r"[ぁ-んァ-ヶ一-龯]")

PHRASES = [
    "Executive summary",
    "Observable timeline",
    "Technical findings",
    "Response and recovery",
    "Prognosis / current state",
    "Defensive lessons",
    "Unknowns / withheld details",
    "incident corpus",
    "blast radius",
    "control-plane abuse",
    "control plane abuse",
    "standing privilege",
    "clean recovery",
    "watch candidate",
    "capacity-planning",
    "supported inference",
    "confirmed observation",
    "unknown / not confirmed",
    "confirmed capability",
    "confirmed institutional treatment",
    "confirmed historical observation",
    "confirmed policy",
    "confirmed benchmark",
    "identity document",
    "identity documents",
    "system outage",
    "data center",
    "data centers",
    "service retirement",
    "bulk-access",
    "mass credential-harvesting campaign",
    "initial-access vector",
    "software vulnerability exploitation",
    "AI-enabled malicious breaches",
    "agent-enabled",
    "agentic/code model",
    "local deployment",
    "fully offline",
    "downloadable model",
    "model download",
]

MIXED_TOKENS = [
    "account", "accounts", "record", "records", "provider", "providers",
    "recovery", "loan", "loans", "credit", "risk", "risks",
    "reconnaissance", "weaponization", "subset", "actor", "actors",
    "throughput", "automation",
]

# 見出しでそのまま使ってよい、一般化した略語・固有名。
HEADING_ALLOWED = {
    "AI", "BI", "API", "SaaS", "DNS", "GitHub", "Web", "LINE", "SMS", "VPN",
    "MFA", "FIDO", "FIDO2", "EDR", "SOC", "SIEM", "WAF", "CVE", "KPI",
    "MITRE", "ATT", "CK", "DB", "IT", "OT", "BPO", "CSS", "ID", "KYC",
    "POS", "EC", "HR", "ISP", "FAQ", "JICC", "CIC", "NISC", "NCO", "IBM",
    "KDDI", "ASKUL", "OZmall", "Helpfeel", "Gyazo", "LEAN", "BODY",
    "ApplyNow", "VOISING", "PeakManager", "Denno", "Watch", "Metabase",
    "Times", "Car", "MCL", "MTTR", "RTO", "RPO", "OKF",
}

INLINE_CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"https?://[^\s)>]+")
LINK_TARGET = re.compile(r"\]\(([^)]+)\)")
HEADING_ASCII = re.compile(
    r"(?<![A-Za-z0-9_])([A-Za-z][A-Za-z0-9+&.-]{1,})(?![A-Za-z0-9_])"
)


def ascii_term(term: str) -> re.Pattern[str]:
    return re.compile(
        ASCII_LEFT + re.escape(term) + ASCII_RIGHT,
        flags=re.IGNORECASE,
    )


PHRASE_PATTERNS = [(term, ascii_term(term)) for term in PHRASES]
TOKEN_PATTERNS = [(term, ascii_term(term)) for term in MIXED_TOKENS]


def body_only(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    marker = text.find("\n---\n", 4)
    return text[marker + 5 :] if marker >= 0 else text


def scrub(line: str) -> str:
    line = INLINE_CODE.sub(" ", line)
    line = URL.sub(" ", line)
    line = LINK_TARGET.sub("]", line)
    return line


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.name != "AGENTS.md"
    )


def main() -> int:
    failures: list[str] = []
    for path in markdown_files():
        body = body_only(path.read_text(encoding="utf-8"))
        in_fence = False
        for lineno, raw in enumerate(body.splitlines(), 1):
            if raw.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or re.match(r"^\[\^[^]]+\]:", raw):
                continue
            line = scrub(raw)
            if line.startswith("#"):
                for token in HEADING_ASCII.findall(line):
                    if token not in HEADING_ALLOWED:
                        failures.append(
                            f"{path.relative_to(ROOT)}:{lineno}: heading token '{token}'"
                        )
            for term, pattern in PHRASE_PATTERNS:
                if pattern.search(line):
                    failures.append(
                        f"{path.relative_to(ROOT)}:{lineno}: phrase '{term}'"
                    )
            if JAPANESE.search(line):
                for term, pattern in TOKEN_PATTERNS:
                    if pattern.search(line):
                        failures.append(
                            f"{path.relative_to(ROOT)}:{lineno}: mixed token '{term}'"
                        )
    if failures:
        print("日本語本文に未正規化の英語・Jargon候補があります:")
        print("\n".join(failures))
        return 1
    print("Japanese prose jargon check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
