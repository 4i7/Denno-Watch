---
type: Cybersecurity Incident
title: ニチレイ — サイバー攻撃による低温物流・冷凍食品出荷停止と個人情報漏えい
description: 2026年7月のニチレイグループへのサイバー攻撃、冷蔵倉庫入出庫・冷凍食品出荷への事業影響、7月24日の全面復旧、9月の個人情報漏えい確定までを追跡する記録。
resource: https://www.nichirei.co.jp/news/2026/524.html
tags: [japan, food, logistics, cyberattack, availability, personal-data, supply-chain, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:49:29Z }
incident:
  organization: 株式会社ニチレイ / ニチレイグループ
  sector: food-and-cold-chain-logistics
  jurisdiction: JP
  incident_status: operations_restored_investigation_continues
  attack_type: cyberattack
  earliest_known_activity: unknown
  detected_at: "2026-07-13"
  first_disclosed_at: "2026-07-13"
  latest_public_update: "2026-09-18"
  public_record_checked_at: "2026-10-04T04:49:29+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Nichirei Logi Group refrigerated-warehouse inbound/outbound operations and Nichirei Foods frozen-food shipment operations"
  data_exposure: confirmed
  availability_impact: confirmed_material
  restoration_state: "partial operations resumed 2026-07-17; all affected sites returned to normal operation 2026-07-24"
  secondary_abuse: "not observed as of 2026-09-18"
sources:
  - id: nichirei-1
    resource: https://www.nichirei.co.jp/news/2026/512.html
    title: 当社グループでのシステム障害発生について（第1報）
    author: organization:Nichirei
  - id: nichirei-2
    resource: https://www.nichirei.co.jp/news/2026/513.html
    title: 当社グループでのシステム障害発生について（第2報）
    author: organization:Nichirei
  - id: nichirei-3
    resource: https://www.nichirei.co.jp/news/2026/514.html
    title: 当社グループでのシステム障害発生について（第3報）
    author: organization:Nichirei
  - id: nichirei-4
    resource: https://www.nichirei.co.jp/news/2026/515.html
    title: 当社グループでのシステム障害発生について（第4報）
    author: organization:Nichirei
  - id: nichirei-5
    resource: https://www.nichirei.co.jp/news/2026/517.html
    title: 当社グループでのシステム障害発生について（第5報）
    author: organization:Nichirei
  - id: nichirei-6
    resource: https://www.nichirei.co.jp/news/2026/530.html
    title: 当社グループでのシステム障害発生について（第6報）
    author: organization:Nichirei
  - id: nichirei-7
    resource: https://www.nichirei.co.jp/news/2026/524.html
    title: 当社グループでのシステム障害発生について（第7報）
    author: organization:Nichirei
  - id: nichirei-index
    resource: https://www.nichirei.co.jp/news/2026
    title: ニチレイ プレスリリース2026年
    author: organization:Nichirei
---

# Executive summary

2026年7月13日、ニチレイグループで不正アクセスに起因するシステム障害が発生した。ニチレイは被害拡大防止のためグループで使用するシステムを遮断し、緊急対策本部を設置した。これにより、ニチレイロジグループ各社の冷蔵倉庫入出庫業務とニチレイフーズの冷凍食品出荷業務に実害が発生した。[^nichirei-1][^nichirei-2]

7月17日から一部制限下で冷蔵倉庫・食品工場の稼働を順次再開し、7月24日に受発注制限を解除して全拠点が平常時の通常稼働へ移行した。[^nichirei-3][^nichirei-5]

一方、機密性影響の調査は復旧後も継続した。8月14日には従業員情報の漏えい可能性を公表し、9月18日の第7報で、配送先、取引先役職員、従業員・家族・退職者・求職者に関する個人情報の**漏えいを確認**した。[^nichirei-6][^nichirei-7]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-07-13 | システム障害を確認。直ちにシステム遮断、緊急対策本部設置、外部専門会社を交えた調査開始。冷蔵倉庫入出庫と冷凍食品出荷に影響。[^nichirei-1][^nichirei-2] |
| 2026-07-15 | サーバがサイバー攻撃を受けたことを確認。被害サーバに個人情報が保管されていたため、漏えい可能性事案として個人情報保護委員会へ第一報。[^nichirei-2] |
| 2026-07-17 | 冷蔵倉庫全拠点の入出庫業務と冷凍食品出荷業務を、一部受発注制限付きで順次再開。[^nichirei-3] |
| 2026-07-22 | 被害サーバの一部に個人情報が保管されていたことを再公表し、対象者への通知を開始。全拠点通常稼働への移行予定を公表。[^nichirei-4] |
| 2026-07-24 | 受発注制限を解除し、全拠点で平常時の通常稼働へ移行。[^nichirei-5] |
| 2026-08-14 | 国内グループ従業員情報の一部に漏えいのおそれを確認。調査継続と監視強化を公表。[^nichirei-6] |
| 2026-09-11 | 被害サーバ上の個人情報について個人情報保護委員会へ報告。[^nichirei-7] |
| 2026-09-18 | 第7報。複数区分の個人情報漏えいを確認し、件数と項目を公表。[^nichirei-7] |

# Impact

## Business and availability impact

影響した主要業務は以下。[^nichirei-1]

- ニチレイロジグループ各社の冷蔵倉庫入出庫業務
- ニチレイフーズの冷凍食品出荷業務

7月17日から部分稼働、7月24日に通常稼働へ戻った。したがって、最初の公表から全拠点通常稼働まで11日間を要した。[^nichirei-3][^nichirei-5]

これは単なる社内IT停止ではなく、低温物流・食品出荷という物理サプライチェーンへ波及した事案として扱う。

## Confirmed personal-data exposure

9月18日時点で漏えいが確認された区分は以下。[^nichirei-7]

| Population | Data | Count |
| --- | --- | ---: |
| ニチレイグループ各社が受託した配送業務の配送先顧客 | 氏名、住所、電話番号 | 3,308件 |
| 取引先の役職員 | 会社名、所属、役職、氏名、住所、電話番号、メールアドレス | 6,849件 |
| グループ従業員（2021年以降の退職者含む）・家族・求職者 | 氏名、生年月日、性別、住所、電話番号、メールアドレス、従業員番号、給与賞与、在留資格、人事情報等 | 43,709件 |

表の件数を単純合計すると53,866件だが、Denno Watchではこれを「53,866人」とは表現しない。会社は区分別件数を示しているが、全区分横断の一意人数を公表していないためである。

クレジットカード情報は含まれていない。個々のレコードに表記された全項目が含まれるわけでもない。[^nichirei-7]

## Secondary abuse

9月18日時点で不正利用等の二次被害は確認されていない。対象者には順次個別通知が行われた。[^nichirei-7]

# Technical findings

公開情報で確認できるのは、ニチレイのサーバの一部がサイバー攻撃を受けたことまでである。攻撃の詳細は、さらなる被害拡大防止と警察・関係機関との連携を理由に非公表とされた。[^nichirei-2][^nichirei-4]

そのため以下は公開情報から確定できない。

- ランサムウェアかどうか
- 初期侵入経路
- 悪用された脆弱性・認証情報
- 侵害開始日時と滞在期間
- データ外部送信の具体的手法
- 攻撃主体

症状や事業停止だけから攻撃種別を推定しない。

# Response and recovery

- 発生日にグループシステムを遮断し、緊急対策本部を設置。[^nichirei-2]
- 外部セキュリティ専門会社の支援下で安全確認・復旧を実施。[^nichirei-2][^nichirei-3]
- 警察・関係機関と連携。[^nichirei-4]
- 7月17日から段階復旧し、7月24日に全拠点通常稼働。[^nichirei-3][^nichirei-5]
- 個人情報影響の調査は業務復旧後も継続し、9月に漏えいを確定。[^nichirei-7]
- システムセキュリティ、監視体制、グループ全体のセキュリティ水準、BCPの見直しを継続。[^nichirei-7]

# Prognosis / current state

2026年10月4日にニチレイの2026年プレスリリース一覧を確認した時点で、本件の最新一次公表は9月18日の第7報である。[^nichirei-index]

業務可用性は7月24日に通常状態へ復旧しているが、9月18日時点でも原因分析・影響範囲調査とセキュリティ・監視強化は継続中だった。よって `operations_restored_investigation_continues` とする。

# Defensive lessons

- **業務復旧と情報漏えい調査を別のクロックで管理する。** 可用性は11日で平常化したが、個人情報漏えいの確定公表は約2か月後だった。
- **IT遮断が物理サプライチェーンへどう波及するかをBCPで扱う。** 冷蔵倉庫・冷凍食品出荷への影響は、サイバーインシデントが物流能力へ直結する例である。
- **安全確認後に段階復旧する。** 一部受発注制限下で再開し、その後に全拠点通常稼働へ移行した。[^nichirei-3][^nichirei-5]
- **退職者・家族・求職者をデータ資産台帳へ含める。** 現役従業員だけでは影響範囲を把握できない。[^nichirei-7]
- **公表単位を維持する。** 区分別件数を単純合計して一意被害者数へ変換しない。

# Unknowns / withheld details

- 攻撃手法・初期侵入経路
- 侵害開始日時
- 外部送信されたデータの具体的範囲と取得経路
- 攻撃主体
- 調査の最終完了時期
- 恒久対策の具体的構成

[^nichirei-1]: ニチレイ「当社グループでのシステム障害発生について（第1報）」2026-07-13.
[^nichirei-2]: ニチレイ「同（第2報）」2026-07-15.
[^nichirei-3]: ニチレイ「同（第3報）」2026-07-17.
[^nichirei-4]: ニチレイ「同（第4報）」2026-07-22.
[^nichirei-5]: ニチレイ「同（第5報）」2026-07-24.
[^nichirei-6]: ニチレイ「同（第6報）」2026-08-14.
[^nichirei-7]: ニチレイ「同（第7報）」2026-09-18.
[^nichirei-index]: ニチレイ「プレスリリース2026年」一覧。2026-10-04確認。
