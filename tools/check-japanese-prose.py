#!/usr/bin/env python3
"""日本語本文に残った不要な英語・独自Jargon候補を検出する。

方針:
- YAMLフロントマター、URL、コード、脚注の正式な出典表記は対象外。
- 正式な製品名・組織名・規格名と、AI/IT/セキュリティ分野で一般化した
  略語は許容する。
- 主要な分析文書では、日本語を含む行に残る一般的な英小文字語を原則検出する。
  これにより agent/model/local/system/cloud のような、既知語リストにない混在も
  新たに検出できる。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASCII_LEFT = r"(?<![A-Za-z0-9_])"
ASCII_RIGHT = r"(?![A-Za-z0-9_])"
JAPANESE = re.compile(r"[ぁ-んァ-ヶ一-龯]")
LOWER_ASCII_WORD = re.compile(
    r"(?<![A-Za-z0-9_])([a-z][a-z0-9]*(?:[-/][a-z0-9]+)*)(?![A-Za-z0-9_])"
)

# 過去に実際に混入した、または意味が曖昧になりやすい表現。
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
    "Times Car",
]

# 主要な人間向け分析文書。ここでは既知語方式ではなく、英小文字語を原則検出する。
STRICT_PROSE_PATHS = {
    Path("analysis/executive-ai-amplified-cyber-risk-report-2026-10-04.md"),
    Path("analysis/incident-defense-budget-analysis-2026-10-04.md"),
    Path("analysis/sector-worst-case-impact-matrix-2026-10-04.md"),
    Path("analysis/evidence-ledger-ai-cyber-risk-2026-10-04.md"),
    Path("methodology/corpus-audit-2026-10-04.md"),
}

# 小文字を含んでも一般的な技術表記として保持するもの。
# 原則は厳しくし、必要な語だけここへ追加する。
LOWER_ALLOWED = {
    "eKYC".lower(),  # 比較時はlower()する
}

# 見出し・本文でそのまま使ってよい、一般化した略語・固有名。
ASCII_ALLOWED = {
    "AI", "LLM", "GPU", "VRAM", "BI", "API", "SaaS", "DNS", "GitHub", "Web",
    "LINE", "SMS", "VPN", "MFA", "FIDO", "FIDO2", "EDR", "NDR", "SOC", "MDR",
    "SIEM", "WAF", "CVE", "KEV", "KPI", "MITRE", "ATT", "CK", "DB", "IT", "OT",
    "BPO", "MSP", "CSS", "ID", "KYC", "PII", "POS", "EC", "HR", "ISP", "FAQ",
    "JICC", "CIC", "NISC", "NCO", "IBM", "KDDI", "ASKUL", "OZmall", "Helpfeel",
    "Gyazo", "LEAN", "BODY", "ApplyNow", "VOISING", "PeakManager", "Denno", "Watch",
    "Metabase", "MCL", "MTTR", "MTTD", "RTO", "RPO", "OKF", "LOC", "SLA", "ASN",
    "IAM", "PAM", "JIT", "JEA", "OIDC", "PAT", "SSO", "DLP", "UEBA", "EASM", "VM",
    "TPRM", "SCADA", "MES", "ERP", "DR", "BCP", "LAPS", "AD", "IR", "SecOps",
    "Microsoft", "Google", "Anthropic", "Verizon", "Mistral", "Meta", "Park24", "IANS",
    "Artico", "Search", "LY", "Corporation", "APAC", "FAQ", "Llama", "Five", "Foxes",
    "REXT", "CEC", "JCOM", "DotGift",
}

# 正式な出典名として本文中の引用セルに現れる英小文字語。
# 一般本文での免罪符にしないため、quoted/source文脈だけで使う。
FORMAL_SOURCE_LOWER = {
    "results", "release", "summary",
}

INLINE_CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"https?://[^\s)>]+")
LINK_TARGET = re.compile(r"\]\(([^)]+)\)")
QUOTED = re.compile(r"[“\"]([^”\"]+)[”\"]")
ASCII_TOKEN = re.compile(
    r"(?<![A-Za-z0-9_])([A-Za-z][A-Za-z0-9+&.-]{1,})(?![A-Za-z0-9_])"
)


def ascii_term(term: str) -> re.Pattern[str]:
    return re.compile(ASCII_LEFT + re.escape(term) + ASCII_RIGHT, flags=re.IGNORECASE)


PHRASE_PATTERNS = [(term, ascii_term(term)) for term in PHRASES]


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


def scrub_formal_sources(raw: str, line: str) -> str:
    # URL付き箇条書きは出典一覧として扱う。脚注自体はmain()で除外済み。
    if raw.lstrip().startswith("-") and "http" in raw:
        return ""
    # 引用符で囲まれた正式な英語タイトルは本文の混在判定から外す。
    return QUOTED.sub(" ", line)


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.name != "AGENTS.md"
    )


def strict_mixed_words(path: Path, line: str) -> list[str]:
    rel = path.relative_to(ROOT)
    if rel not in STRICT_PROSE_PATHS or not JAPANESE.search(line):
        return []

    failures: list[str] = []
    allowed_lower = {token.lower() for token in ASCII_ALLOWED} | LOWER_ALLOWED
    for token in LOWER_ASCII_WORD.findall(line):
        if token.lower() in allowed_lower or token.lower() in FORMAL_SOURCE_LOWER:
            continue
        failures.append(token)
    return failures


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
            if not line.strip():
                continue

            if line.startswith("#"):
                for token in ASCII_TOKEN.findall(line):
                    if token not in ASCII_ALLOWED:
                        failures.append(
                            f"{path.relative_to(ROOT)}:{lineno}: heading token '{token}'"
                        )

            for term, pattern in PHRASE_PATTERNS:
                if pattern.search(line):
                    failures.append(
                        f"{path.relative_to(ROOT)}:{lineno}: phrase '{term}'"
                    )

            strict_line = scrub_formal_sources(raw, line)
            for token in strict_mixed_words(path, strict_line):
                failures.append(
                    f"{path.relative_to(ROOT)}:{lineno}: mixed lowercase token '{token}'"
                )

    if failures:
        print("日本語本文に未正規化の英語・Jargon候補があります:")
        print("\n".join(failures))
        return 1

    print("日本語本文の英語・Jargon検査: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
