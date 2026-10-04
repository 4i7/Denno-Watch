#!/usr/bin/env python3
"""Conservatively normalize human-readable Markdown prose to Japanese.

This tool intentionally leaves YAML frontmatter, URLs, inline code, fenced code,
footnote source lines, filenames, identifiers, product names, standards and
machine-readable enum values untouched where practical. It is not a general
translator. It only fixes recurring headings and known mixed-language jargon
that has appeared in Denno Watch prose.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEADING_REPLACEMENTS = {
    "# Executive summary": "# 概要",
    "# Observable timeline": "# 公開情報で確認できる時系列",
    "# Impact": "# 影響",
    "# Technical findings": "# 技術的に確認できた事項",
    "# Response and recovery": "# 対応と復旧",
    "# Prognosis / current state": "# 現在の状況と予後",
    "# Defensive lessons": "# 防御上の教訓",
    "# Unknowns / withheld details": "# 不明点・未公表事項",
    "## Integrity and availability": "## 完全性と可用性",
    "## Personal data at risk": "## 影響を受ける可能性のある個人情報",
    "## Confidentiality": "## 機密性",
    "## Availability": "## 可用性",
    "## Integrity": "## 完全性",
    "| Date | Observable event |": "| 日付 | 公開情報で確認できる出来事 |",
}

# Longer phrases must be replaced before shorter tokens.
PHRASE_REPLACEMENTS = [
    (r"\bincident corpus\b", "インシデント事例集"),
    (r"\bidentity documents?\b", "本人確認書類"),
    (r"\bdata centers?\b", "データセンター"),
    (r"\bsystem outage\b", "システム停止"),
    (r"\bblast radius\b", "被害範囲"),
    (r"\bcontrol-plane abuse\b", "制御プレーンの悪用"),
    (r"\bcontrol plane abuse\b", "制御プレーンの悪用"),
    (r"\bstanding privilege\b", "常設権限"),
    (r"\bclean recovery\b", "クリーンな復旧"),
    (r"\bwatch candidate\b", "監視候補"),
    (r"\bcapacity-planning\b", "能力計画"),
    (r"\bstress scenario\b", "ストレスシナリオ"),
    (r"\bsupported inference\b", "根拠に支えられた推論"),
    (r"\bconfirmed observation\b", "確認済みの観測事実"),
    (r"\bunknown / not confirmed\b", "不明／未確認"),
    (r"\bconfirmed capability\b", "能力として確認済み"),
    (r"\bconfirmed institutional treatment\b", "制度上確認済み"),
    (r"\bconfirmed historical observation\b", "過去事例として確認済み"),
    (r"\bconfirmed policy\b", "公的方針として確認済み"),
    (r"\bconfirmed benchmark\b", "ベンチマークとして確認済み"),
    (r"\baccount recovery\b", "アカウント復旧"),
    (r"\binternet banking\b", "インターネットバンキング"),
    (r"\bmass credential-harvesting campaign\b", "大規模な認証情報収集キャンペーン"),
    (r"\bvulnerability discovery\b", "脆弱性探索"),
    (r"\bpost-compromise\b", "侵害後活動"),
    (r"\binitial-access vector\b", "初期侵入経路"),
    (r"\bsoftware vulnerability exploitation\b", "ソフトウェア脆弱性悪用"),
    (r"\bAI-enabled malicious breaches\b", "AIを利用した悪意ある侵害"),
    (r"\bagent-enabled\b", "AIエージェントを利用した"),
    (r"\bagentic/code model\b", "エージェント型／コード向けモデル"),
    (r"\blocal deployment\b", "ローカル配備"),
    (r"\bfully offline\b", "完全オフライン"),
    (r"\bdownloadable model\b", "ダウンロード可能なモデル"),
    (r"\bmodel download\b", "モデルのダウンロード"),
    (r"\binputs/outputs\b", "入力／出力"),
    (r"\bglobal average\b", "世界平均"),
    (r"\bcontainer terminal\b", "コンテナターミナル"),
    (r"\bsmartphone app\b", "スマートフォンアプリ"),
    (r"\bcall center\b", "コールセンター"),
    (r"\bmail addresses?\b", "メールアドレス"),
    (r"\bservice retirement\b", "サービス廃止"),
    (r"\bbulk-access\b", "大量アクセス"),
    (r"\bdata retention\b", "データ保持"),
    (r"\bdata minimization\b", "データ最小化"),
    (r"\bdata lineage\b", "データ系譜"),
    (r"\battack surface\b", "攻撃対象領域"),
    (r"\binternet-facing\b", "インターネット公開"),
    (r"\bphishing-resistant\b", "フィッシング耐性のある"),
    (r"\bmanual fallback\b", "手作業への切り替え"),
    (r"\bmanual control\b", "手動制御"),
    (r"\bmanual dispatch\b", "手動配車"),
    (r"\btenant isolation\b", "テナント分離"),
    (r"\bfailure domain\b", "障害領域"),
    (r"\bidentity document controls\b", "本人確認書類の管理"),
    (r"\bidentity-document controls\b", "本人確認書類の管理"),
    (r"\bfraud monitoring\b", "不正監視"),
    (r"\bfraud analytics\b", "不正分析"),
    (r"\bsegregation of duties\b", "職務分離"),
]

TOKEN_REPLACEMENTS = {
    "account": "アカウント",
    "accounts": "アカウント",
    "record": "レコード",
    "records": "レコード",
    "provider": "提供事業者",
    "providers": "提供事業者",
    "risk": "リスク",
    "risks": "リスク",
    "recovery": "復旧",
    "loan": "ローン",
    "loans": "ローン",
    "credit": "クレジット",
    "local": "ローカル",
    "offline": "オフライン",
    "model": "モデル",
    "models": "モデル",
    "reconnaissance": "偵察",
    "phishing": "フィッシング",
    "weaponization": "攻撃実用化",
    "subset": "部分集合",
    "actor": "攻撃主体",
    "actors": "攻撃主体",
    "breach": "侵害",
    "breaches": "侵害事案",
}

INLINE_CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"https?://[^\s)>]+")
LINK_TARGET = re.compile(r"\]\(([^)]+)\)")


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    marker = text.find("\n---\n", 4)
    if marker < 0:
        return "", text
    return text[: marker + 5], text[marker + 5 :]


def protect(line: str) -> tuple[str, list[str]]:
    saved: list[str] = []

    def keep(match: re.Match[str]) -> str:
        saved.append(match.group(0))
        return f"\u0000{len(saved)-1}\u0000"

    line = INLINE_CODE.sub(keep, line)
    line = URL.sub(keep, line)
    line = LINK_TARGET.sub(keep, line)
    return line, saved


def restore(line: str, saved: list[str]) -> str:
    for i, value in enumerate(saved):
        line = line.replace(f"\u0000{i}\u0000", value)
    return line


def normalize_line(line: str) -> str:
    if line in HEADING_REPLACEMENTS:
        return HEADING_REPLACEMENTS[line]
    # Preserve bibliography/footnote source titles verbatim.
    if re.match(r"^\[\^[^]]+\]:", line):
        return line
    work, saved = protect(line)
    for pattern, replacement in PHRASE_REPLACEMENTS:
        work = re.sub(pattern, replacement, work, flags=re.IGNORECASE)
    for token, replacement in TOKEN_REPLACEMENTS.items():
        work = re.sub(rf"\b{re.escape(token)}\b", replacement, work, flags=re.IGNORECASE)
    return restore(work, saved)


def normalize_text(text: str) -> str:
    frontmatter, body = split_frontmatter(text)
    in_fence = False
    result: list[str] = []
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            result.append(line)
        elif in_fence:
            result.append(line)
        else:
            result.append(normalize_line(line))
    suffix = "\n" if text.endswith("\n") else ""
    return frontmatter + "\n".join(result) + suffix


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.name != "AGENTS.md"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report files that would change")
    args = parser.parse_args()
    changed: list[Path] = []
    for path in markdown_files():
        original = path.read_text(encoding="utf-8")
        normalized = normalize_text(original)
        if normalized == original:
            continue
        changed.append(path)
        if not args.check:
            path.write_text(normalized, encoding="utf-8")
    for path in changed:
        print(path.relative_to(ROOT))
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
