---
type: Cybersecurity Incident
title: 佐川急便 — お荷物問い合わせサービスへの不正アクセスと約100日分の配送関連情報の漏えい可能性
description: 2026年9月30日に確認された荷物追跡系Webサービスへの不正アクセス、送り主・届け先・契約顧客・Smart Club会員情報の漏えい可能性、9つのWebサービス停止を追跡する記録。
resource: https://www.sagawa-exp.co.jp/
tags: [japan, logistics, tracking, unauthorized-access, personal-data, availability, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 佐川急便株式会社
  sector: logistics
  jurisdiction: JP
  incident_status: web_services_suspended_investigation_continues
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-30"
  first_disclosed_at: "2026-09-30"
  latest_public_update: "2026-10-03 FAQ"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "お荷物問い合わせサービス and multiple related Web services"
  data_exposure: possible
  availability_impact: "nine Web services suspended; physical pickup and delivery operations continued"
  restoration_state: "investigation and Web-service suspension ongoing in latest public record"
  secondary_abuse: unknown
  downstream_impact: "senders and recipients can be affected even without owning a Sagawa account"
  regulatory_response: not_publicly_detailed
  notification_state: "dedicated inquiry channel opened; scope/count investigation ongoing"
  business_continuity: "physical collection and delivery remained operational while Web functions were restricted"
  data_sensitivity: "sender/recipient names, addresses and phone numbers; contracted-customer contacts; Smart Club identity/contact/member ID; no card data or passwords in announced scope"
sources:
  - id: sagawa-home
    resource: https://www.sagawa-exp.co.jp/
    title: 佐川急便 重要なお知らせ — お荷物問い合わせサービスへの不正アクセス関連
    author: organization:佐川急便株式会社
  - id: sagawa-secondary
    resource: https://www.itmedia.co.jp/news/article/2610/01/2000001933/
    title: 佐川急便、不正アクセスで個人情報流出か
    author: organization:ITmedia NEWS
---

# 概要

佐川急便は2026年9月30日、Webサイトの「お荷物問い合わせサービス」への第三者不正アクセスを確認した。10月1日の第2報で、顧客の個人情報が外部に流出した可能性があることを公表し、第3報では専用問い合わせ窓口を案内、10月3日にはFAQを公開した。公式サイト上ではこれらが最新の重要なお知らせとして掲載されている。[^sagawa-home]

流出可能性のある範囲には、9月30日から遡る約100日間の荷物について送り主・届け先の氏名（法人の場合は法人名・担当者名）、住所、電話番号が含まれる。また運賃契約顧客の連絡先、Smart Club会員の氏名・住所・電話番号・メールアドレス・会員IDも対象となり得る。対象件数は調査中で、クレジットカード情報とパスワードは対象外と説明されている。[^sagawa-secondary]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-30 | お荷物問い合わせサービスへの第三者不正アクセスを確認し、第1報を公表。サービスアクセスを制限。[^sagawa-home] |
| 2026-10-01 | 第2報で個人情報の外部流出可能性を公表。関連Webサービスを停止。第3報で専用窓口を案内。[^sagawa-home] |
| 2026-10-03 | FAQを公開。公式サイト上の最新関連更新として確認。[^sagawa-home] |

# 影響

## 荷物配送関連の個人情報

送り主・届け先情報は、佐川急便のWeb会員本人だけに限定されない。第三者から荷物を受け取った人物も、配送データの一部として対象になり得る点が重要である。約100日分という期間は累計対象期間であり、対象人数や荷物件数として読み替えない。[^sagawa-secondary]

## 契約・会員情報

運賃契約を結ぶ法人・個人顧客の氏名/法人名・担当者名・住所・電話番号、およびSmart Club会員の氏名・住所・電話番号・メールアドレス・会員IDも対象範囲に含まれる。クレジットカード情報とパスワードは含まれないとされた。[^sagawa-secondary]

## 可用性

被害拡大防止のため、荷物問い合わせ、API、宅配便受付など複数のWebサービス（公開報道では9サービス）が停止された。一方、物理的な荷物の集荷と配達は通常どおり継続した。[^sagawa-secondary]

# 技術的に確認できた事項

不正アクセスの具体的原因、侵入経路、脆弱性、資格情報、攻撃主体は10月3日時点で公表されていない。追跡番号検索という機能特性からAPI悪用や認証回避を推測しない。

# 対応と復旧

- 不正アクセス確認後、対象サービスのアクセスを制限。[^sagawa-home]
- 影響拡大防止のため関連Webサービスを停止。[^sagawa-secondary]
- 対象情報・件数を継続調査。[^sagawa-home]
- 専用問い合わせ窓口を開設し、なりすましメール/SMS/電話への注意を案内。[^sagawa-home]
- 物理配送を継続し、Web障害と物流本体を分離して事業継続。[^sagawa-secondary]

# 現在の状況と予後

10月3日のFAQ時点でも件数・原因・最終復旧状態は確定していないため、`web_services_suspended_investigation_continues` とする。

# 防御上の教訓

- **アカウント非保有者もデータ主体になる。** 物流では送り主・届け先データが業務上生成されるため、会員DBだけを個人情報境界と考えない。
- **保持期間がそのまま侵害時のブラスト半径になる。** 約100日分の追跡関連データが対象になり得る点は、オンライン照会に必要な保持期間と侵害リスクのバランスを示す。
- **デジタル機能停止と物理物流停止を分離する。** Web機能を止めても集配を継続できたことはBCP上重要である。

# 不明点・未公表事項

- 初期侵入経路・侵害開始日時
- 実際の外部取得件数・対象人数
- 約100日分の対象データの正確な始点とレコード数
- Webサービスの完全復旧時期
- 二次被害の有無

[^sagawa-home]: 佐川急便公式サイト「重要なお知らせ」2026-09-30〜10-03.
[^sagawa-secondary]: ITmedia NEWS「佐川急便、不正アクセスで個人情報流出か　送り主・届け先の氏名や住所など、約100日分の荷物データ対象」2026-10-01. 詳細項目は同社第2報の内容を報道。
