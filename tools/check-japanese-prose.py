#!/usr/bin/env python3
"""Detect recurring mixed-language jargon in human-readable Markdown prose.

The check is deliberately conservative. It does not reject every English word:
formal source titles, product names, standards and established AI/IT/security
terms are legitimate. Instead it detects expressions that Denno Watch has
chosen to write in Japanese because leaving them as raw English made the
reports harder to read or created project-local jargon.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN = [
    r"\bExecutive summary\b",
    r"\bObservable timeline\b",
    r"\bTechnical findings\b",
    r"\bResponse and recovery\b",
    r"\bPrognosis / current state\b",
    r"\bDefensive lessons\b",
    r"\bUnknowns / withheld details\b",
    r"\bincident corpus\b",
    r"\bblast radius\b",
    r"\bcontrol-plane abuse\b",
    r"\bstanding privilege\b",
    r"\bclean recovery\b",
    r"\bwatch candidate\b",
    r"\bcapacity-planning\b",
    r"\bsupported inference\b",
    r"\bconfirmed observation\b",
    r"\bunknown / not confirmed\b",
    r"\bconfirmed capability\b",
    r"\bconfirmed institutional treatment\b",
    r"\bconfirmed historical observation\b",
    r"\bconfirmed policy\b",
    r"\bconfirmed benchmark\b",
    r"\bidentity documents?\b",
    r"\bsystem outage\b",
    r"\bdata centers?\b",
    r"\bservice retirement\b",
    r"\bbulk-access\b",
    r"\bmass credential-harvesting campaign\b",
    r"\binitial-access vector\b",
    r"\bsoftware vulnerability exploitation\b",
    r"\bAI-enabled malicious breaches\b",
    r"\bagent-enabled\b",
    r"\bagentic/code model\b",
    r"\blocal deployment\b",
    r"\bfully offline\b",
    r"\bdownloadable model\b",
    r"\bmodel download\b",
]

# Single English words are checked only when adjacent to Japanese text. This
# avoids flagging official English source titles and normal technical acronyms.
MIXED_TOKENS = [
    "account", "accounts", "record", "records", "provider", "providers",
    "recovery", "loan", "loans", "credit", "risk", "risks",
    "reconnaissance", "weaponization", "subset", "actor", "actors",
]

INLINE_CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"https?://[^\s)>]+")
LINK_TARGET = re.compile(r"\]\(([^)]+)\)")
JAPANESE = r"ぁ-んァ-ヶ一-龯"


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
            for pattern in FORBIDDEN:
                if re.search(pattern, line, flags=re.IGNORECASE):
                    failures.append(f"{path.relative_to(ROOT)}:{lineno}: {pattern}")
            for token in MIXED_TOKENS:
                # Flag token when the same line is Japanese prose, not an
                # isolated English title/table cell.
                if re.search(rf"\b{re.escape(token)}\b", line, flags=re.IGNORECASE) and re.search(rf"[{JAPANESE}]", line):
                    failures.append(f"{path.relative_to(ROOT)}:{lineno}: mixed token '{token}'")
    if failures:
        print("日本語本文に未正規化の英語・Jargon候補があります:")
        print("\n".join(failures))
        return 1
    print("Japanese prose jargon check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
