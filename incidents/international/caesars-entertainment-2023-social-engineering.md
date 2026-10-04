---
type: Cybersecurity Incident
title: Caesars Entertainment — 委託IT支援へのソーシャルエンジニアリングから本人情報流出へ至った2023年侵害
summary: 2023年、Caesars Entertainmentで外部委託IT支援事業者へのソーシャルエンジニアリングを起点にネットワーク侵害が発生し、ロイヤルティプログラムDBが取得された。顧客向け業務停止を伴わなくても、高感度本人情報と長期訴訟・規制対応が残る比較ケース。
resource: https://www.sec.gov/Archives/edgar/data/1590895/000119312523235015/d537840d8k.htm
tags: [international, united-states, social-engineering, third-party, identity-data, litigation, 2023]
status: draft
stale_after: 2027-01-04T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T13:08:00+09:00 }
comparative_case: true
included_in_japan_corpus: false
incident:
  organization: Caesars Entertainment, Inc.
  sector: hospitality-and-gaming
  jurisdiction: US
  incident_status: long_tail_monitoring
  attack_type: social-engineering-and-data-theft
  earliest_known_activity: not_publicly_disclosed
  detected_at: "2023-09"
  first_disclosed_at: "2023-09-14"
  latest_public_update: "2026"
  public_record_checked_at: "2026-10-04T13:08:00+09:00"
  intrusion_vector: "social engineering attack on an outsourced IT support vendor"
  affected_services: "internal IT network and loyalty program database"
  data_exposure: confirmed
  availability_impact: "customer-facing operations not impacted"
  restoration_state: "containment and remediation completed; litigation and regulatory tail continued"
  secondary_abuse: not_observed-in-initial-disclosure
sources:
  - id: caesars-8k
    resource: https://www.sec.gov/Archives/edgar/data/1590895/000119312523235015/d537840d8k.htm
    title: Caesars Entertainment Form 8-K — 2023-09-14
  - id: caesars-2023
    resource: https://www.sec.gov/Archives/edgar/data/1590895/000159089524000051/czr-20231231.htm
    title: Caesars Entertainment Form 10-K — 2023
  - id: caesars-2024
    resource: https://www.sec.gov/Archives/edgar/data/1590895/000159089525000068/czr-20241231.htm
    title: Caesars Entertainment Form 10-K — 2024
  - id: caesars-2025
    resource: https://www.sec.gov/Archives/edgar/data/1590895/000159089526000011/czr-20251231.htm
    title: Caesars Entertainment Form 10-K — 2025
---

# 概要

Caesars Entertainmentは2023年9月14日、外部委託IT支援事業者を狙ったソーシャルエンジニアリングにより、攻撃者が同社ネットワークへ不正アクセスしたと公表した。調査の結果、ロイヤルティプログラムのデータベースが取得され、その中には相当数の会員について運転免許証番号および／または社会保障番号が含まれていた。[^caesars-8k]

一方、物理施設、オンライン・モバイルゲーム等の顧客向け業務は停止せず継続した。[^caesars-8k] これは「サービス停止がない事故」でも、高感度本人情報の流出と長期法的負債が重大になり得ることを示す。

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2023-09上旬 | CaesarsがITネットワークの不審活動を検知し、インシデント対応計画を発動。外部専門家、法執行機関、州のゲーミング規制当局と連携。[^caesars-8k][^caesars-2023] |
| 2023-09-07 | 調査により、攻撃者がロイヤルティプログラムDBを含むデータを取得したと判断。[^caesars-8k] |
| 2023-09-14 | SEC 8-Kで事故を公表。入口は外部委託IT支援事業者へのソーシャルエンジニアリングと説明。[^caesars-8k] |
| 2023-09以降 | 影響者への通知、信用監視・身元盗難保護サービスの提供を開始。[^caesars-8k] |
| 2023-2025 | 本件を巡る複数の集団訴訟、個別請求、州規制当局からの照会が年次報告で継続開示。[^caesars-2023][^caesars-2024][^caesars-2025] |

# 影響

## 個人情報

取得されたロイヤルティプログラムDBには、相当数の会員について運転免許証番号および／または社会保障番号が含まれていた。[^caesars-8k]

初期開示時点では、会員パスワード／PIN、銀行口座情報、決済カード情報が攻撃者に取得された証拠は確認されていないとされた。[^caesars-8k]

この区別は重要である。高感度な本人確認関連データが漏えいしても、決済情報が漏えいしていなければ事故が軽いという意味にはならない。

## 可用性

顧客向け施設、オンライン・モバイルゲーム等の業務は本件による停止を受けず継続した。[^caesars-8k]

## 長期法務・規制影響

Caesarsは後続の10-Kで、本件に関連する多数の集団訴訟、個別請求、州規制当局からの照会を継続して開示した。[^caesars-2023][^caesars-2024][^caesars-2025]

2024年10-Kでは、本件が同社の事業戦略、財務状態等へ重大な影響を与えたとは評価していない一方、事故費用について保険会社からの回収を進めていると説明している。[^caesars-2024]

# 技術的に確認できた事項

公表資料から確認できる入口は、**Caesars自身の従業員ではなく、利用していた外部委託IT支援事業者へのソーシャルエンジニアリング**である。[^caesars-8k]

公開資料だけでは、具体的ななりすまし手段、認証方式、権限取得手順、内部横展開の詳細までは確認できない。これらを報道や類似攻撃から推定して断定しない。

# 対応と復旧

Caesarsは不審活動検知後、インシデント対応計画を発動し、封じ込め・是正措置を実施した。外部のサイバーセキュリティ・フォレンジック専門家を起用し、法執行機関と州ゲーミング規制当局へ通知した。[^caesars-8k][^caesars-2023]

また、該当する委託IT支援事業者側にも再発防止措置を取らせたと説明している。[^caesars-8k]

本人向けには、法的義務に従った通知とともに、信用監視・身元盗難保護サービスを提供した。[^caesars-8k]

# 現在の状況と予後

技術的な封じ込め後も、後年のSEC開示に本件関連の集団訴訟が残っている。[^caesars-2025]

本件は、技術復旧が早く、顧客向けサービス停止もなくても、本人情報の性質によって**本人保護、規制、訴訟、保険**という長期予後が残ることを示す。

# 防御上の教訓

- **委託先のヘルプデスク・IT支援を強い認証境界として扱う。** 管理者リセット、MFA再登録、パスワード変更等の高権限手続は、通常の本人確認より強い多段確認を要求する。
- **委託先の権限を業務委託契約ではなく到達可能範囲で評価する。** 一つの委託先アカウントや端末から、どの管理面・データへ到達できるかを棚卸しする。
- **ソーシャルエンジニアリング耐性を技術統制で補強する。** FIDO2等のフィッシング耐性認証、端末信頼、JIT権限、重要操作の二者確認を組み合わせる。
- **本人確認関連データには長期保護策が必要。** パスワードのように変更できない識別子が漏えいした場合、通知だけでなく長期的な不正利用監視と本人支援を検討する。
- **可用性だけを重大度指標にしない。** サービス停止ゼロでも、機密性事故は長期の法務・信用コストを生み得る。

# 日本の事例へ読み替える際の注意

米国の社会保障番号、集団訴訟制度、ゲーミング規制は日本と異なる。法的影響を直接移植しない。

国内で再利用すべき知見は、**委託IT支援を狙うソーシャルエンジニアリング、高権限の本人確認手続、高感度本人情報、サービス停止がない事故の長期予後**である。

# 不明点・未公表事項

- ソーシャルエンジニアリングの具体的な手口と、攻撃者が最初に取得した権限は公表資料だけでは確定できない。
- 取得データがその後どこまで二次利用されたかを本資料から完全には確定できない。
- 個々の訴訟の最終結果・総費用は継続的に変動し得る。

[^caesars-8k]: Caesars Entertainment, Form 8-K, 2023-09-14.
[^caesars-2023]: Caesars Entertainment, Form 10-K for 2023.
[^caesars-2024]: Caesars Entertainment, Form 10-K for 2024.
[^caesars-2025]: Caesars Entertainment, Form 10-K for 2025. 本件関連の複数の集団訴訟を継続開示。
