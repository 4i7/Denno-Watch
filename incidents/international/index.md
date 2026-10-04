# 海外比較インシデント

このディレクトリは、日本の2026年重大インシデント事例集を補完する**比較用ケース**である。国内事例の件数、傾向集計、業種別統計には含めない。

海外ケースを収録する目的は、国内事例ではまだ観測期間が短い、または制度・市場構造上観測しにくい次の領域を補うことにある。

- 技術復旧後に数年残る訴訟・保険・規制・信用の尾部。
- 高集中な第三者基盤が止まった場合の下流業務・資金繰りへの波及。
- SaaSの共有責任と顧客側認証管理。
- 委託IT支援・ヘルプデスクを狙うソーシャルエンジニアリング。
- ゼロデイ一斉悪用による製品・サプライチェーン集中リスク。

法制度、損害賠償、保険、市場構造は国ごとに異なるため、**海外ケースの金額・法的義務を日本へ直接移植しない**。比較するのは攻撃・依存・復旧・長期予後の構造である。

## 収録ケース

| ケース | 発生 | 主な比較軸 | 公開上の状態 |
| --- | --- | --- | --- |
| [Change Healthcare](change-healthcare-2024-ransomware.md) | 2024 | MFA未適用のリモート入口、医療取引基盤の集中、下流資金繰り、影響人数・財務負担の長期更新 | 長期予後観察 |
| [Snowflake顧客アカウント侵害 / UNC5537](snowflake-unc5537-2024.md) | 2024 | 窃取認証情報、MFA未適用、委託先端末、SaaS共有責任、評判・訴訟 | 長期予後観察 |
| [Caesars Entertainment](caesars-entertainment-2023-social-engineering.md) | 2023 | 委託IT支援へのソーシャルエンジニアリング、高感度本人情報、停止なしでも残る訴訟 | 長期予後観察 |
| [MOVEit Transfer](moveit-transfer-2023-mass-exploitation.md) | 2023 | ゼロデイ一斉悪用、製品集中、委託先経由の間接影響、訴訟・保険の数年単位尾部 | 長期予後観察 |

## 国内事例との接続

- Change Healthcare → KDDI、日本テレネット、両毛システムズ等の**共有基盤・BPO・下流波及**を考える比較材料。
- Snowflake → ApplyNow、LEAN BODY、VOISING、扶桑電通、イノベーション等の**SaaS・BI・クラウド・認証情報**を考える比較材料。
- Caesars → 委託先アクセス、本人確認情報、ヘルプデスク・管理者再認証の強度を考える比較材料。
- MOVEit → インターネット公開製品、ゼロデイ、委託先・再委託先が使う共通製品の集中リスクを考える比較材料。

## 調査・記録基準

海外ケースの選定と国内事例との分離ルールは、[海外比較ケース記録基準](../../methodology/international-comparative-case-standard.md)を参照する。

横断的な読み方は以下を参照する。

- [サイバーインシデントのライフサイクルと復旧判定](../../analysis/incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md)
- [第三者・認証・集中リスク](../../analysis/third-party-identity-concentration-risk-2026-10-04.md)
- [インシデント後の長期予後](../../analysis/post-incident-long-tail-prognosis-2026-10-04.md)
- [インシデント対応指標と経営判断トリガー](../../analysis/incident-response-metrics-and-decision-triggers-2026-10-04.md)
