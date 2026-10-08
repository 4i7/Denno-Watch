---
type: Analysis Log
title: サイバーインシデントの財務・事業影響 — 実測値、保険、長期費用を分離して追う
description: サイバー事故の費用を、直接対応費、事業中断、下流支援、訴訟・規制、保険、再発防止投資等へ分け、会社開示の実測値と推計・未確定額を混同しないための知識基盤。
tags: [analysis, financial-impact, business-impact, insurance, disclosure, long-tail, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: unh-2024-10k
    resource: https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm
    title: UnitedHealth Group 2024 Form 10-K
    author: organization:UnitedHealth Group
  - id: unh-2025-10k
    resource: https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm
    title: UnitedHealth Group 2025 Form 10-K
    author: organization:UnitedHealth Group
  - id: progress-2026q3
    resource: https://www.sec.gov/Archives/edgar/data/876167/000087616726000111/prgs-20260831.htm
    title: Progress Software Form 10-Q for quarter ended August 31 2026
    author: organization:Progress Software
  - id: progress-2025-10k
    resource: https://www.sec.gov/Archives/edgar/data/876167/000087616726000008/prgs-20251130.htm
    title: Progress Software 2025 Form 10-K
    author: organization:Progress Software
  - id: mgm-2023-8k
    resource: https://www.sec.gov/Archives/edgar/data/789570/000119312523251667/d461062d8k.htm
    title: MGM Resorts International Form 8-K, October 2023
    author: organization:MGM Resorts International
  - id: caesars-2025-10k
    resource: https://www.sec.gov/Archives/edgar/data/1590895/000159089526000011/czr-20251231.htm
    title: Caesars Entertainment 2025 Form 10-K
    author: organization:Caesars Entertainment
  - id: nichirei-initial
    resource: https://www.nichirei.co.jp/ir/news/2026/t_in226.html
    title: 当社グループでのシステム障害発生について
    author: organization:株式会社ニチレイ
  - id: nichirei-update7
    resource: https://www.nichirei.co.jp/news/2026/524.html
    title: 当社グループでのシステム障害発生について（第7報）
    author: organization:株式会社ニチレイ
---

# 目的

サイバー事故の「被害額」は一つの数字ではない。

同じ事故でも、初動の外部専門家費、売上減少、顧客支援、無利息融資、システム再構築、本人通知、訴訟、規制対応、保険金、数年後の和解まで、異なる時点・会計科目・主体に費用が分散する。

Denno Watchでは、**会社が実際に開示した値**、**会社自身の見積値**、**まだ合理的に見積もれない負債**、**外部の推計**を同じ「損失額」として合算しない。

# 財務影響を九つに分ける

| 区分 | 内容 | 例 |
| --- | --- | --- |
| 直接対応費 | フォレンジック、外部専門家、法律、通知、復旧 | 専門家費、ネットワーク復元 |
| 事業中断 | 売上減、取引停止、稼働率低下 | Web停止、出荷停止、予約停止 |
| 追加運用費 | 手作業、代替基盤、残業、仮環境 | 代替決済、仮サーバー |
| 顧客・下流支援 | 融資、補償、信用監視、再発行支援 | 医療提供者への資金支援 |
| データ対応 | 対象特定、本人通知、コールセンター | 大規模通知 |
| 法務・規制 | 訴訟、和解、調査、罰金・課徴 | 集団訴訟、監督調査 |
| 再発防止投資 | システム再構築、追加統制、人材 | ID再設計、監視強化 |
| 保険・求償 | 保険回収、第三者補償 | サイバー保険回収 |
| 長期事業影響 | 解約、信用、撤退、サービス終了 | 顧客行動変化、事業廃止 |

一つの支出が複数区分にまたがる場合、会社の会計開示の粒度を優先し、Denno Watch側で無理に再配分しない。

# 金額の証拠状態

| 状態 | 意味 |
| --- | --- |
| `reported_actual` | 会社が既に発生・計上した実績として開示 |
| `reported_estimate` | 会社自身の見積り |
| `reported_range` | 会社が範囲で開示 |
| `reasonably_possible_unestimated` | 損失可能性はあるが合理的見積り不能と会社が開示 |
| `insurance_recovery` | 受領済み又は会計上認識した保険回収 |
| `external_estimate` | 第三者推計。会社実績とは別枠 |
| `unknown` | 公開情報から把握できない |

「影響は軽微」「重要な影響なし」も金額ゼロを意味しない。

# 金額を合算するときの規則

1. 同一期間の累計値と四半期値を重複加算しない。
2. 総額と保険控除後純額を混在させない。
3. 事業中断の売上減と利益減を混在させない。
4. 融資・債権残高を、そのまま費用として扱わない。
5. 引当・準備金と実際の現金支出を分離する。
6. 訴訟請求額と会社が認識した負債を分離する。
7. 為替換算する場合は換算日・レートを明示し、原通貨も残す。
8. 複数社の下流損失を親事故の「一社の損失」に合算しない。

# 比較ケース1: Change Healthcare

UnitedHealth Groupは2024年Form 10-Kで、Change Healthcareへの攻撃について、2024年に**直接対応費22億ドル**を計上し、Optum Insightで**推定8.67億ドルの事業中断影響**があったと開示した。また医療提供者を支援するため、2024年末までに**90億ドル超の無利息融資**を提供した。融資額は費用額そのものではないため、別指標として保持する。[^unh-2024-10k]

2025年Form 10-Kでは、提供者向け融資その他の顧客残高について回収見込みを見直し、2025年第4四半期に**7.99億ドルの引当増加**を営業費用として計上した。これは2024年の直接対応費と同じ種類の数値ではない。[^unh-2025-10k]

この事例から分かるのは、事故費用が「復旧した年」で終わらず、下流支援の回収可能性まで後年度へ残ることである。

## 記録上の教訓

```text
直接対応費 ≠ 事業中断影響 ≠ 支援融資額 ≠ 後年度の回収不能見積り
```

一つの「総被害額」へ畳み込むより、時間軸と勘定の性質を残す方が再利用価値が高い。

# 比較ケース2: MOVEit / Progress Software

Progress SoftwareはMOVEit脆弱性関連について、2023年度150万ドル、2024年度560万ドル、2025年度280万ドルの**保険回収控除後費用**を開示した。2025年度末時点で、当時1500万ドルあったサイバー保険のうち約450万ドルが残っていた。[^progress-2025-10k]

2026年8月31日までの9か月では、MOVEit関連の保険回収控除後費用が**610万ドル**、同期間に認識した保険回収が**450万ドル**と開示され、同日時点で利用可能なサイバー保険枠を使い切ったとしている。また訴訟・政府調査に関連する将来損失は合理的な範囲を見積もれず、損失引当を計上していない。[^progress-2026q3]

これは重要な長期予後である。

- 事故から3年以上後も費用が継続する。
- 保険回収があるため、総費用と純費用は異なる。
- 保険枠は有限であり、長期訴訟が続く間に使い切る場合がある。
- 「引当なし」は「将来損失なし」を意味しない。

# 比較ケース3: MGM Resorts

MGM Resortsは2023年の事故について、2023年9月の運用障害によりLas Vegas Strip Resorts等のAdjusted Property EBITDARへ**約1億ドルのマイナス影響**を見込み、同年第3四半期にサイバー事故関連の一時費用を**1000万ドル未満**計上したと開示した。[^mgm-2023-8k]

ここでは、事故対応費よりも**サービス停止による営業影響の方が桁違いに大きい**。

したがって、防衛投資の比較で「IR・フォレンジック費だけ」を事故コストとすると、可用性の価値を過小評価する。

# 比較ケース4: Caesars Entertainment

Caesars Entertainmentは、事故対応・修復・調査費を負担し、保険会社からの回収を継続しているが、2025年Form 10-K時点でも総費用・保険による相殺・第三者への補償請求を含む全体影響は確定していないと説明している。一方、会社の評価では事故は重要な財務影響を与えていないとしている。集団訴訟や州規制当局からの照会は継続している。[^caesars-2025-10k]

「金額非公表だが長期法的尾部あり」という類型であり、金額がないことをゼロとして扱わない。

# 国内ケース: ニチレイで追うべきもの

ニチレイは2026年7月のサイバー攻撃初期公表で、冷蔵倉庫の入出庫業務と冷凍食品出荷業務への影響を説明し、「連結業績に与える影響は、判明次第、速やかに開示」とした。[^nichirei-initial]

9月18日の第7報では、全拠点が7月24日に通常稼働へ移行したこと、個人情報漏えい、通知、原因・影響範囲の継続調査が公表された。[^nichirei-update7]

Denno Watchでは、現段階で外部から事故損失額を推計して埋めるのではなく、今後の決算・適時開示で次を追う方がよい。

- 出荷・物流制限による売上・利益影響が事故要因として明示されるか。
- 外部セキュリティ専門家、復旧、通知等の費用が独立開示されるか。
- 業績予想へ織り込まれたか。
- 保険回収があるか。
- 再発防止投資が通常IT投資と分けて開示されるか。

公表がなければ `unknown` のまま保持する。

# 「重大性」と金額の関係

金額が小さくても重大な事故はある。

- 本人確認書類や医療情報の長期被害。
- 安全系・重要インフラへの影響。
- 顧客信頼・市場機能への影響。
- 認証情報の下流悪用。

逆に、情報流出が限定的でも大規模なサービス停止により営業損失が大きくなる場合がある。

そのため、財務影響は既存の機密性・完全性・可用性・安全・本人被害の**代替指標ではなく別軸**とする。

# 下流事業者の損失

Change Healthcareのような共有基盤事故では、被害主体の費用だけでなく顧客側へ資金繰り・請求遅延・代替システム導入等が波及する。

Denno Watchでは、次を分離する。

```yaml
financial_impact:
  primary_organization: []
  downstream_organizations: []
  customer_support: []
  insurance: []
```

下流企業が自社の財務影響を開示した場合、それを親事故の「総額」へ機械的に合算しない。母集団が不完全で、二重計上も起きやすいためである。

# 個別インシデントへ追加できるメタデータ

```yaml
financial_impact:
  status: disclosed_partial
  currency: JPY
  direct_response_costs: []
  business_interruption: []
  customer_support: []
  legal_regulatory: []
  remediation_investment: []
  insurance_recoveries: []
  contingent_losses: []
  latest_financial_update: null
```

各配列要素は、最低限次を持つ。

```yaml
- period: "2026-Q3"
  amount: null
  amount_type: reported_actual
  gross_or_net: gross
  description: "会社開示の表現を要約"
  source_id: example-source
```

金額非公表でも、`status: pending`、`reasonably_possible_unestimated` 等の状態を記録できる。

# 調査経路

国内上場会社の事故では、事故ページだけで調査を終えない。

1. 事故初報・続報。
2. TDnetの適時開示。
3. 決算短信。
4. 決算説明資料・質疑応答。
5. 半期・有価証券報告書。
6. 統合報告書。
7. 翌年度以降の訴訟・保険・特別損失・引当。

海外上場会社では、同様に8-K等の臨時開示、10-Q、10-Kを時系列で追う。

# 防衛予算への使い方

事故コストの実測値は、防衛予算の上限を単純決定する材料ではない。

使い方としては、次の方が適切である。

- 同じ失敗モードで発生した直接費と中断費の比率を見る。
- 一日・一週間の停止価値を業務側で事前に算出する。
- 保険だけでは吸収できない尾部を確認する。
- 復旧訓練、代替経路、データ最小化がどの費用類型を下げるか対応付ける。
- 低頻度だが極端な尾部を平均値だけで消さない。

[防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md)の想定損失と、本資料の会社開示実績は分離して利用する。

# 今後の国内台帳化

次の順で42件を追加調査する価値が高い。

1. 上場会社かつ業務停止を伴った事例。
2. 復旧が数日以上続いた事例。
3. 大規模通知・外部専門家対応を伴った事例。
4. サービス廃止・再構築まで至った事例。
5. 第三者障害で下流企業の業績へ影響した事例。

初回調査で金額が見つからない事例も「金額なし」で捨てず、`financial_status: not_publicly_disclosed` と次回確認時期を残す。

# 関連資料

- [知識基盤拡張監査](knowledge-base-map-2026-10-04.md)
- [インシデント後の長期予後](post-incident-long-tail-prognosis-2026-10-04.md)
- [サイバーインシデントの報告・通知・公表マップ](regulatory-reporting-and-disclosure-map-2026-10-04.md)
- [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md)
- [2026年 日本の重大サイバーインシデント — 防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md)
- [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md)

[^unh-2024-10k]: UnitedHealth Group, 2024 Form 10-K, Change Healthcare Cyberattack. https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm
[^unh-2025-10k]: UnitedHealth Group, 2025 Form 10-K. https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm
[^progress-2025-10k]: Progress Software, 2025 Form 10-K. https://www.sec.gov/Archives/edgar/data/876167/000087616726000008/prgs-20251130.htm
[^progress-2026q3]: Progress Software, Form 10-Q for the period ended August 31, 2026. https://www.sec.gov/Archives/edgar/data/876167/000087616726000111/prgs-20260831.htm
[^mgm-2023-8k]: MGM Resorts International, Form 8-K, October 2023. https://www.sec.gov/Archives/edgar/data/789570/000119312523251667/d461062d8k.htm
[^caesars-2025-10k]: Caesars Entertainment, 2025 Form 10-K. https://www.sec.gov/Archives/edgar/data/1590895/000159089526000011/czr-20251231.htm
[^nichirei-initial]: 株式会社ニチレイ「当社グループでのシステム障害発生について」2026-07-16. https://www.nichirei.co.jp/ir/news/2026/t_in226.html
[^nichirei-update7]: 株式会社ニチレイ「当社グループでのシステム障害発生について（第7報）」2026-09-18. https://www.nichirei.co.jp/news/2026/524.html
