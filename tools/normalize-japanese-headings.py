#!/usr/bin/env python3
"""人が読むMarkdown見出しに残った英語混在を日本語へ正規化する。

本文・YAML・出典には触れず、既に意味が確定している見出しだけを変更する。
AI/IT/セキュリティ分野で一般的な略語や製品名は必要に応じて残す。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXACT = {
    "# Evidence ledger": "# 根拠資料台帳",
    "# Primary and authoritative sources": "# 一次情報・権威ある情報源",
    "# Evidence discipline": "# 根拠の扱い方",
    "# Executive synthesis": "# エグゼクティブサマリー",
    "# Observed recurring patterns": "# 観測された反復パターン",
    "# Defense budget model": "# 防御予算モデル",
    "## External benchmark": "## 外部ベンチマーク",
    "# Budget allocation recommendation": "# 予算配分の推奨",
    "# Budget decision rule": "# 予算判断ルール",
    "# Control-to-incident mapping examples": "# 統制とインシデントの対応例",
    "# Evidence notes": "# 根拠に関する注記",
    "# Limits": "# 限界",
    "# Maximum credible loss model": "# 最大想定損失モデル",
    "# Purpose and boundary": "# 目的と範囲",
    "# Related analysis": "# 関連分析",
    "# The strongest finding": "# 最も強い知見",
    "# What should have been funded first": "# 最優先で予算化すべき項目",
    "### Example conversion": "### 換算例",
    "## 1. Internet-facing and adjacent-tool vulnerability exploitation": "## 1. インターネット公開資産・周辺ツールの脆弱性悪用",
    "## 2. Credential / session / remote-access abuse": "## 2. 認証情報／セッション／リモートアクセスの悪用",
    "## 3. Ransomware + data theft + operational shutdown": "## 3. ランサムウェア＋データ窃取＋業務停止",
    "## 4. Provider / SaaS / entrusted-data concentration": "## 4. 提供事業者／SaaS／受託データの集中",
    "## 4. 提供事業者 / SaaS / entrusted-data concentration": "## 4. 提供事業者／SaaS／受託データの集中",
    "## 5. Analytics / BI as a hidden production boundary": "## 5. 分析／BI環境は隠れた本番データ境界",
    "## 6. Business-logic / legitimate-looking mass query abuse": "## 6. ビジネスロジック／正規利用に見える大量照会の悪用",
    "## 7. Destructive integrity attacks and database deletion": "## 7. 完全性を狙う破壊攻撃とデータベース削除",
    "## 8. Source-code / secrets / development-data leakage": "## 8. ソースコード／シークレット／開発データの漏えい",
    "## 9. Communications control-plane abuse": "## 9. 通信制御プレーンの悪用",
    "## 9. Communications 制御プレーンの悪用": "## 9. 通信制御プレーンの悪用",
    "## 10. Large-scale shared infrastructure / DNS / mail platform failures": "## 10. 大規模共有基盤／DNS／メール基盤の障害",
    "## 11. Historical, dormant and unnecessary data accumulation": "## 11. 過去・休眠・不要データの蓄積",
    "## 12. Business continuity and service retirement": "## 12. 事業継続とサービス廃止",
    "## 12. Business continuity and サービス廃止": "## 12. 事業継続とサービス廃止",
    "## Incremental control-gap budget by attack method": "## 攻撃手法別の追加統制予算",
    "## Denno Watch risk-adjusted annual floor": "## Denno Watch リスク調整後の年間下限",
    "## Denno Watch リスク-adjusted annual floor": "## Denno Watch リスク調整後の年間下限",
    "## Secondary abuse": "## 二次被害",
    "# Unknowns / follow-up required": "# 不明点・要追跡事項",
    "# Recovery and prognosis": "# 復旧と予後",
    "# 復旧 and prognosis": "# 復旧と予後",
    "# Unknowns / open questions": "# 不明点・未解決事項",
    "## Availability and business operations": "## 可用性と事業運営",
    "## Customer information": "## 顧客情報",
    "# Defensive observations": "# 防御上の観察事項",
    "## Availability and integrity": "## 可用性と完全性",
    "## Scale": "## 規模",
    "## Potentially affected population": "## 影響を受けた可能性のある対象者",
    "## Data categories": "## データ種別",
    "## Data explicitly outside scope": "## 明示的に対象外とされたデータ",
    "## Data fields": "## データ項目",
    "# Unknowns": "# 不明点",
    "## Integrity / destructive action": "## 完全性への影響／破壊的操作",
    "## Merchants and employees": "## 加盟店・従業員",
    "## Merchant-store information": "## 加盟店情報",
    "## Maximum affected population": "## 最大影響対象数",
    "## My Number": "## マイナンバー",
    "## Integrity / destructive impact": "## 完全性への影響／破壊的被害",
    "# Availability and business continuity": "# 可用性と事業継続",
    "## Geographic scope": "## 地理的範囲",
    "## Image metadata": "## 画像メタデータ",
    "## High-sensitivity employment data": "## 機微性の高い雇用関連データ",
    "## Operational impact": "## 業務への影響",
    "## Financial account data": "## 金融アカウント情報",
    "## Financial アカウント data": "## 金融アカウント情報",
    "## Excluded high-risk data": "## 対象外とされた高リスクデータ",
    "## Excluded high-リスク data": "## 対象外とされた高リスクデータ",
    "## Integrity / abuse": "## 完全性への影響／悪用",
    "## Other personal and account data": "## その他の個人情報・アカウント情報",
    "## Other personal and アカウント data": "## その他の個人情報・アカウント情報",
    "## Personal-data controls": "## 個人データ管理",
    "## Payment-card information": "## 決済カード情報",
    "## User data": "## 利用者データ",
    "## Shipment-related personal data": "## 荷物配送関連の個人情報",
    "## Services": "## サービス",
    "## Service impact": "## サービスへの影響",
    "## Secondary-abuse risk": "## 二次被害リスク",
    "## Secondary-abuse リスク": "## 二次被害リスク",
    "## Sales-management system": "## 販売管理システム",
    "## Retention / offboarding risk": "## 保持／利用終了時のリスク",
    "## Retention / offboarding リスク": "## 保持／利用終了時のリスク",
    "## Payment data and availability": "## 決済データと可用性",
    "## Rental Server environment": "## レンタルサーバー環境",
    "## Production systems": "## 本番システム",
    "## Potentially affected information": "## 影響を受けた可能性のある情報",
    "## Potentially affected data": "## 影響を受けた可能性のあるデータ",
    "## Population": "## 対象者数",
    "## End-user data boundary": "## エンドユーザーデータの範囲",
    "## Personal data": "## 個人情報",
    "## Personal and employment data": "## 個人情報・雇用関連情報",
    "## Purchaser and member information": "## 購入者・会員情報",
    "## Employee information": "## 従業員情報",
    "## Data categories and free-text risk": "## データ種別と自由記述欄のリスク",
    "## Data categories and free-text リスク": "## データ種別と自由記述欄のリスク",
    "## Data separation": "## データ分離",
    "## Business and availability impact": "## 事業・可用性への影響",
    "## Availability and staged recovery": "## 可用性と段階的復旧",
    "## Availability and staged 復旧": "## 可用性と段階的復旧",
    "## Availability and secondary abuse": "## 可用性と二次被害",
    "## Availability and operations": "## 可用性と事業運営",
    "## Availability and customer response": "## 可用性と顧客対応",
    "## Availability and business impact": "## 可用性・事業への影響",
    "## Availability and business functions": "## 可用性と業務機能",
    "## Availability / business operations": "## 可用性／事業運営",
    "## Affected provider and services": "## 影響を受けた提供事業者とサービス",
    "## Affected 提供事業者 and services": "## 影響を受けた提供事業者とサービス",
    "# Technical findings and evidence state": "# 技術的所見と証拠状態",
    "# Response": "# 対応",
    "# Relation to the earlier 2rinkan incident": "# 先行する2りんかん事案との関係",
    "# Confidentiality impact": "# 機密性への影響",
    "# Cause and evidence state": "# 原因と証拠状態",
    "# Availability and secondary abuse": "# 可用性と二次被害",
    "## Business continuity": "## 事業継続",
    "## Confidentiality and credentials": "## 機密性と認証情報",
    "## Confidentiality and fraud state": "## 機密性と不正利用の状況",
    "## Confidentiality and publication": "## 機密性と外部公開",
    "## Data explicitly outside the affected system": "## 影響を受けたシステムに含まれないデータ",
    "## Account-security impact": "## アカウントのセキュリティ影響",
    "## アカウント-security impact": "## アカウントのセキュリティ影響",
    "## Customer data": "## 顧客データ",
    "## Cross-customer exposure": "## 顧客横断の影響",
    "## Credential exposure": "## 認証情報の露出",
    "## Credential / GitHub controls": "## 認証情報／GitHubの管理",
    "## Count semantics: 33M → 22.18M records": "## 件数の意味: 3,300万レコード → 2,218万レコード",
    "## Count semantics: 33M → 22.18M レコード": "## 件数の意味: 3,300万レコード → 2,218万レコード",
    "## Downstream entrusted data": "## 下流の受託データ",
    "## Contract and membership data": "## 契約・会員情報",
    "## Confirmed personal-data exposure": "## 確認済みの個人情報露出",
    "## Confirmed leaked data": "## 漏えいが確認されたデータ",
    "## Confirmed exposed population": "## 露出が確認された対象者",
    "## Confirmed data leak": "## 確認済みのデータ漏えい",
    "## Confirmed data exposure": "## 確認済みのデータ露出",
    "## Confirmed acquisition": "## 取得が確認されたデータ",
    "## Confidentiality progression": "## 機密性影響の推移",
    "## Confirmed population": "## 確認済みの対象者数",
    "## Provider-side impact": "## 提供事業者側の影響",
    "## 提供事業者-side impact": "## 提供事業者側の影響",
}

FRAGMENTS = [
    (re.compile(r"^(##) Layer (\d+)\b", re.I), r"\1 第\2層"),
    (re.compile(r"^(##) Priority (\d+)\b", re.I), r"\1 優先度\2"),
    (re.compile(r"^(#) PART I\b", re.I), r"\1 第1部"),
    (re.compile(r"^(#) PART II\b", re.I), r"\1 第2部"),
    (re.compile(r"\bCase study\b", re.I), "ケーススタディ"),
    (re.compile(r"\bcapacity problem\b", re.I), "必要能力の問題"),
    (re.compile(r"\bhigh-(?:risk|リスク) operation\b", re.I), "高リスク操作"),
    (re.compile(r"\bpatch\b", re.I), "パッチ"),
    (re.compile(r"\bhours\b", re.I), "時間"),
    (re.compile(r"\brisk control\b", re.I), "リスク管理"),
    (re.compile(r"\bcredential\b", re.I), "認証情報"),
    (re.compile(r"\bdata\b", re.I), "データ"),
    (re.compile(r"\bbackup\b", re.I), "バックアップ"),
    (re.compile(r"\bsupplier\b", re.I), "供給事業者"),
    (re.compile(r"\bIdentity\b", re.I), "アイデンティティ"),
]


def normalize_heading(line: str) -> str:
    if line in EXACT:
        return EXACT[line]
    out = line
    for old, new in [
        ("capacity problem", "必要能力の問題"),
        ("Identity", "アイデンティティ"),
        ("patch", "パッチ"),
        ("hours", "時間"),
        ("risk control", "リスク管理"),
        ("control", "管理"),
        ("credential", "認証情報"),
        ("data", "データ"),
        ("backup", "バックアップ"),
        ("supplier", "供給事業者"),
        ("high-リスク operation", "高リスク操作"),
        ("high-risk operation", "高リスク操作"),
    ]:
        out = out.replace(old, new)
    for pattern, replacement in FRAGMENTS:
        out = pattern.sub(replacement, out)
    return EXACT.get(out, out)


def targets() -> list[Path]:
    files = list((ROOT / "analysis").glob("*.md"))
    files += list((ROOT / "incidents" / "2026").glob("*.md"))
    return sorted(p for p in files if p.name != "index.md")


def main() -> int:
    changed: list[Path] = []
    for path in targets():
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines()
        rewritten = [normalize_heading(line) if line.startswith("#") else line for line in lines]
        output = "\n".join(rewritten) + ("\n" if original.endswith("\n") else "")
        if output != original:
            path.write_text(output, encoding="utf-8")
            changed.append(path)
    for path in changed:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
