---
type: Cybersecurity Incident
title: JCOM — 外部からの大量アクセスによるDNS高負荷と最大約408万世帯への通信障害
description: 2026年9月23日に約9時間発生したJ:COMの広域インターネット障害を、外部大量アクセス・DNS高負荷・最大約408万加入世帯への影響という観点から追跡する記録。
resource: https://newsreleases.jcom.co.jp/news/20260924_22551.html
tags: [japan, telecom, availability, dns, traffic-surge, outage, resilience, 2026]
status: stable
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:45:00Z }
incident:
  organization: JCOM株式会社
  sector: telecommunications
  jurisdiction: JP
  incident_status: service_restored
  attack_type: "external high-volume access; malicious intent not publicly established"
  earliest_known_activity: "2026-09-23 08:55 JST"
  detected_at: "2026-09-23"
  first_disclosed_at: "2026-09-23"
  latest_public_update: "2026-09-24"
  intrusion_vector: not_applicable_or_not_established
  affected_services: "J:COM NET, parts of J:COM TV interactive/video services, J:COM MOBILE internet connectivity, selected Personal ID services, partner cable internet services"
  data_exposure: not_observed
  availability_impact: "up to about 4.08 million subscribed households; approximately 9 hours of unavailable or degraded connectivity"
  restoration_state: "service recovery work completed around 18:00; all services confirmed normal by 20:00 on 2026-09-23"
  secondary_abuse: not_applicable
sources:
  - id: jcom-release
    resource: https://newsreleases.jcom.co.jp/news/20260924_22551.html
    title: インターネット接続がご利用できない、またはご利用しづらい状況について（9月24日16時00分時点）
    author: organization:JCOM
  - id: jcom-outage
    resource: https://notices.jcom.co.jp/notice/95220.html
    title: NET障害ならびにカスタマーセンターにお電話が繋がらない症状について
    author: organization:JCOM
---

# Executive summary

2026年9月23日8時55分頃から18時頃まで、J:COM NETを中心とするインターネット接続サービスで、利用不能または利用しづらい状態が発生した。最大影響対象は約408万件のJ:COMサービス加入世帯。18時頃に復旧作業が完了し、20時に全サービスの正常提供を最終確認した。[^jcom-release]

JCOMは翌24日、原因について**外部から大量のアクセスがあり、DNSサーバーに高負荷が発生したため**と公表した。[^jcom-release]

ただし公開資料は、この大量アクセスをDDoS攻撃や犯罪行為と明示していない。そのためDenno Watchでは「外部高負荷トラフィックによるサイバー・レジリエンス事案」として記録し、攻撃者や意図を推定しない。

# Observable timeline

| Date / time | Observable event |
| --- | --- |
| 2026-09-23 08:55頃 | インターネット接続サービス等で障害開始。[^jcom-release] |
| 2026-09-23 daytime | J:COM NETを中心に、ネット接続不能・不安定状態が広域で継続。カスタマーセンターもつながりにくい状態が発生。[^jcom-release][^jcom-outage] |
| 2026-09-23 18:00頃 | サービス復旧作業完了。[^jcom-release] |
| 2026-09-23 20:00 | 全サービスが正常提供されていることを最終確認。[^jcom-release] |
| 2026-09-24 | 最大影響約408万件、外部大量アクセスによるDNS高負荷が原因と公表。アクセス集中対策と障害情報提供の改善を再発防止策として表明。[^jcom-release] |

# Impact

## Geographic scope

影響エリアは北海道・九州を除くJ:COM NET提供エリアと、JCOMがインターネットサービスを提供する一部ケーブルテレビ事業者エリア。[^jcom-release]

## Maximum affected population

最大影響対象件数は約408万件の加入世帯。これは実際に同時に通信不能となった端末数ではなく、会社が示した最大影響対象の加入世帯数である。[^jcom-release]

## Services

公表された主な影響対象は以下。[^jcom-release]

- J:COM NETのインターネット接続（一部方式を除く）
- J:COM TVの双方向サービス、ネット動画配信サービス
- J:COM MOBILEのインターネット接続
- パーソナルIDでのログインを要する一部サービス
- JCOMが取引する一部ケーブルテレビ事業者向けインターネットサービス

テレビ放送サービス自体の視聴への影響は確認されていない。[^jcom-release]

# Cause and evidence state

JCOMが確認した直接原因は、外部からの大量アクセスによりDNSサーバーが高負荷となり、インターネット接続時に必要な処理を正常に行えなくなったこと。[^jcom-release]

公開情報からは以下を確認できない。

- 大量アクセスが意図的なDDoS攻撃だったか
- 単一または複数の送信元によるものか
- DNSソフトウェアやネットワーク機器の脆弱性が関与したか
- 権威DNS、キャッシュDNS、加入者向けリゾルバのどの層が主対象だったか
- 攻撃者や帰属

したがって「DDoS攻撃」と断定せず、会社公表どおり外部大量アクセスによるDNS高負荷として保持する。

# Recovery and prognosis

復旧作業は9月23日18時頃に完了し、20時に正常性を確認。JCOMは再発防止としてアクセス集中対策を強化し、障害発生時の情報提供についても改善するとした。[^jcom-release]

公開資料では、具体的な容量増強、DNS冗長化方式、トラフィック制御、外部スクラビング等の技術対策の詳細は示されていない。

# Defensive lessons

- **可用性事案も重大なサイバーインシデントとして記録する。** 情報流出がなくても、DNSのような共通依存点の障害は数百万世帯規模のサービス停止につながる。
- **「攻撃らしさ」と確認済み原因を混同しない。** 外部大量アクセスは確認済みだが、悪意や攻撃者の存在は公表資料から確定できない。
- **顧客向け障害情報もレジリエンスの一部。** 会社自身が再発防止に障害発生時の情報提供改善を含めたため、技術復旧だけでなく通信・案内能力も事後評価に含める。[^jcom-release]
- **最大影響件数と実測停止件数を区別する。** 約408万は最大影響対象の加入世帯数であり、全世帯が同一時間帯に完全断だったことを意味しない。

# Unknowns

- 外部大量アクセスの発生源・意図・持続パターン
- DNS層の具体的な構成とボトルネック
- 実際に完全断となった加入世帯数と時間分布
- 追加の技術的再発防止策

[^jcom-release]: JCOM株式会社、2026年9月24日更新ニュースリリース。
[^jcom-outage]: JCOM株式会社、復旧済み障害案内。
