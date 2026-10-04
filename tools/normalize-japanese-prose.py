#!/usr/bin/env python3
"""Denno Watch本文に残った既知の英語混在・内部Jargonを保守的に正規化する。

一般翻訳器ではない。YAMLフロントマター、URLを含む出典行、コード、脚注の
正式な出典表記は変更せず、既に日本語化方針が決まった表現だけを置換する。
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASCII_LEFT = r"(?<![A-Za-z0-9_])"
ASCII_RIGHT = r"(?![A-Za-z0-9_])"

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

PHRASE_REPLACEMENTS = [
    ("mass credential-harvesting campaign", "大規模な認証情報収集キャンペーン"),
    ("software vulnerability exploitation", "ソフトウェア脆弱性悪用"),
    ("confirmed institutional treatment", "制度上確認済み"),
    ("confirmed historical observation", "過去事例として確認済み"),
    ("unknown / not confirmed", "不明／未確認"),
    ("confirmed observation", "確認済みの観測事実"),
    ("supported inference", "根拠に支えられた推論"),
    ("confirmed capability", "能力として確認済み"),
    ("confirmed benchmark", "ベンチマークとして確認済み"),
    ("confirmed policy", "公的方針として確認済み"),
    ("AI-enabled malicious breaches", "AIを利用した悪意ある侵害"),
    ("initial-access vector", "初期侵入経路"),
    ("agentic/code model", "エージェント型／コード向けモデル"),
    ("identity document controls", "本人確認書類の管理"),
    ("identity-document controls", "本人確認書類の管理"),
    ("identity documents", "本人確認書類"),
    ("identity document", "本人確認書類"),
    ("incident corpus", "インシデント事例集"),
    ("control-plane abuse", "制御プレーンの悪用"),
    ("control plane abuse", "制御プレーンの悪用"),
    ("standing privilege", "常設権限"),
    ("capacity-planning", "必要能力の見積もり"),
    ("account recovery", "アカウント復旧"),
    ("service retirement", "サービス廃止"),
    ("downloadable model", "ダウンロード可能なモデル"),
    ("local deployment", "ローカル配備"),
    ("fully offline", "完全オフライン"),
    ("model download", "モデルのダウンロード"),
    ("system outage", "システム停止"),
    ("blast radius", "被害範囲"),
    ("clean recovery", "クリーンな復旧"),
    ("data centers", "データセンター"),
    ("data center", "データセンター"),
    ("watch candidate", "監視候補"),
    ("bulk-access", "大量アクセス"),
    ("agent-enabled", "AIエージェントを利用した"),
    ("internet banking", "インターネットバンキング"),
    ("container terminal", "コンテナターミナル"),
    ("smartphone app", "スマートフォンアプリ"),
    ("call center", "コールセンター"),
    ("global average", "世界平均"),
    ("inputs/outputs", "入力／出力"),
    ("data retention", "データ保持"),
    ("data minimization", "データ最小化"),
    ("attack surface", "攻撃対象領域"),
    ("phishing-resistant", "フィッシング耐性のある"),
    ("fraud monitoring", "不正監視"),
    ("fraud analytics", "不正分析"),
    ("segregation of duties", "職務分離"),
]

TOKEN_REPLACEMENTS = {
    "accounts": "アカウント",
    "account": "アカウント",
    "records": "レコード",
    "record": "レコード",
    "providers": "提供事業者",
    "provider": "提供事業者",
    "recovery": "復旧",
    "loans": "ローン",
    "loan": "ローン",
    "credit": "クレジット",
    "risks": "リスク",
    "risk": "リスク",
    "reconnaissance": "偵察",
    "weaponization": "攻撃実用化",
    "subset": "部分集合",
    "actors": "攻撃主体",
    "actor": "攻撃主体",
    "throughput": "処理量",
    "automation": "自動化",
}

INLINE_CODE = re.compile(r"`[^`]*`")
LINK_TARGET = re.compile(r"\]\(([^)]+)\)")


def compile_term(term: str) -> re.Pattern[str]:
    return re.compile(
        ASCII_LEFT + re.escape(term) + ASCII_RIGHT,
        flags=re.IGNORECASE,
    )


PHRASE_PATTERNS = [
    (compile_term(term), replacement)
    for term, replacement in PHRASE_REPLACEMENTS
]
TOKEN_PATTERNS = [
    (compile_term(term), replacement)
    for term, replacement in TOKEN_REPLACEMENTS.items()
]


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
    line = LINK_TARGET.sub(keep, line)
    return line, saved


def restore(line: str, saved: list[str]) -> str:
    for i, value in enumerate(saved):
        line = line.replace(f"\u0000{i}\u0000", value)
    return line


def normalize_line(line: str) -> str:
    if line in HEADING_REPLACEMENTS:
        return HEADING_REPLACEMENTS[line]
    # 出典の正式名称やURLを含む行は自動変換しない。
    if re.match(r"^\[\^[^]]+\]:", line) or "http://" in line or "https://" in line:
        return line
    work, saved = protect(line)
    for pattern, replacement in PHRASE_PATTERNS:
        work = pattern.sub(replacement, work)
    for pattern, replacement in TOKEN_PATTERNS:
        work = pattern.sub(replacement, work)
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
    targets = list((ROOT / "analysis").glob("*.md"))
    targets += list((ROOT / "incidents" / "2026").glob("*.md"))
    return sorted(p for p in targets if p.name != "index.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="変更対象だけを表示する")
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
