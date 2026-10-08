---
type: Cybersecurity Incident
title: 名鉄協商 — 複数サーバへの不正アクセスと長期Webサービス障害・顧客情報漏えい可能性
description: 2026年6月23日に発生した名鉄協商の広範なWebサービス障害について、第三者不正アクセス、複数サーバへの攻撃、段階復旧、顧客情報漏えい可能性と通知対象拡大を追跡する記録。
resource: https://www.mkyosho.co.jp/news/2026/07/28/13-770/?list=1
tags: [japan, mobility, parking, unauthorized-access, multi-server, availability, personal-data, 2026]
status: draft
stale_after: 2026-10-18T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:54:53Z }
incident:
  organization: 名鉄協商株式会社
  sector: mobility-parking-and-services
  jurisdiction: JP
  incident_status: partial_recovery_investigation_continues
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-06-23 around 08:00 JST"
  first_disclosed_at: "2026-06-23"
  latest_public_update: "2026-09-03"
  public_record_checked_at: "2026-10-04T04:54:53+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "multiple parking, car-sharing, leasing, card, commerce and business Web services"
  data_exposure: possible_not_confirmed
  availability_impact: confirmed_material_and_prolonged
  restoration_state: "partial services resumed from 2026-07-22; some functions such as MKP Point Card remained under long-term staged recovery with a year-end target as of 2026-08-27"
  secondary_abuse: not_observed
sources:
  - id: mky-initial
    resource: https://www.mkyosho.co.jp/news/2026/06/23/14-711/?list=2
    title: 名鉄協商各種Webサイトにおけるシステム障害のお知らせ
    author: organization:Meitetsu Kyosho
  - id: mky-cause
    resource: https://www.mkyosho.co.jp/news/2026/07/02/13-726/?list=1
    title: 不正アクセスによるシステム障害発生に関するお知らせ
    author: organization:Meitetsu Kyosho
  - id: mky-resume
    resource: https://www.mkyosho.co.jp/news/2026/07/22/13-760/?list=1
    title: 各種Webサイトにおける一部サービス再開のお知らせ
    author: organization:Meitetsu Kyosho
  - id: mky-leak-risk
    resource: https://www.mkyosho.co.jp/news/2026/07/28/13-770/?list=1
    title: 不正アクセスに伴うお客様情報漏洩のおそれに関するお知らせ
    author: organization:Meitetsu Kyosho
  - id: mky-notifications
    resource: https://www.mkyosho.co.jp/news/2026/09/03/13-817/?list=1
    title: お客様情報漏えいのおそれに関する個別案内の実施状況につきまして（9月3日時点）
    author: organization:Meitetsu Kyosho
  - id: mkp-recovery
    resource: https://point.mkp.jp/news/2026/08/27/14-813/
    title: システム障害の現状と今後の対応について
    author: organization:Meitetsu Kyosho
  - id: mky-news
    resource: https://www.mkyosho.co.jp/news/
    title: 名鉄協商 新着情報
    author: organization:Meitetsu Kyosho
---

# 概要

2026年6月23日8時頃、名鉄協商の多数のWebサービスでシステム障害が発生した。初期公表では、時間貸し・月ぎめ駐車場、MKPポイントカード、MKPビジネスカード、駐車サービス券販売、カーリース、カーシェア「カリテコ」などで広範な機能停止が確認された。[^mky-initial]

後続公表で原因は同社運用サーバーへの第三者による不正アクセスと説明された。7月28日までの外部専門機関との調査では、**複数サーバーに対する攻撃**が確認され、顧客情報について外部漏えいのおそれを否定できないことが判明した。一方、9月3日時点でも実際の外部流出を示す事実は確認されていない。[^mky-leak-risk][^mky-notifications]

可用性影響は長期化した。7月22日に一部機能が段階的に再開した一方、MKPポイントカードなどはその後も停止・制限が継続し、8月27日時点では年内のサービス再開を目標として復旧作業が進められていた。[^mky-resume][^mkp-recovery]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-06-23 around 08:00 | 多数のWebサービスで障害発生。駐車場検索・各種申請、月ぎめ契約、ポイントカード、ビジネスカード、EC、カーリース、カリテコ等に影響。[^mky-initial] |
| 2026-07-02 | システム障害の原因が第三者による不正アクセスであることを公表。[^mky-cause] |
| 2026-07-22 | カリテコの入会・契約変更、カリテコバイク法人手続、MKPビジネスカードの明細・請求書閲覧など一部機能を再開。代替フォーム等による臨時対応も実施。[^mky-resume] |
| 2026-07-28 | 外部調査で複数サーバへの攻撃を確認。顧客情報の外部漏えい可能性を否定できないと公表。[^mky-leak-risk] |
| 2026-08-27 | MKPポイントカードでは多数機能の停止が継続し、年内再開を目標に段階復旧中と公表。[^mkp-recovery] |
| 2026-09-03 | 漏えいのおそれがある顧客への個別通知対象が多数の事業・サービスへ拡大。外部流出を示す事実はなお未確認。[^mky-notifications] |

# 影響

## 可用性と業務機能

6月23日時点で公表された主な停止・障害範囲には以下が含まれる。[^mky-initial]

- 名鉄協商パーキング時間貸し検索サイト: 料金シミュレーション、Web領収書、長時間駐車・封鎖等の申請、満空情報更新
- 月ぎめ検索サイト: 新規契約を含む手続き全般
- MKPポイントカード: マイページ手続、新規登録、来店ポイント等
- MKPビジネスカード: Web手続き全般
- 駐車サービス券販売サイト: 注文
- カーリース「ビジカーネット」: Webアクセス
- カーシェア「カリテコ」: 新規入会、免許更新、法人運転者管理等
- アワーシリーズ等の一部サービス

障害は数日では解消せず、一部サービスは7月22日から段階再開したが、サービスごとに復旧速度が異なった。MKPポイントカードでは8月27日時点でも重要な会員機能が停止していた。[^mky-resume][^mkp-recovery]

# 機密性への影響

7月28日の調査結果では複数サーバが攻撃され、顧客情報について外部漏えいのおそれを否定できないとされた。ただし、9月3日時点でも顧客情報が外部に流出したことを示す事実は確認されていない。[^mky-leak-risk][^mky-notifications]

したがって `possible_not_confirmed` とし、通知対象者が存在することを「流出確認済み」とは扱わない。

9月3日時点までに漏えいのおそれに関する個別案内が行われた対象には、少なくとも以下が含まれる。[^mky-notifications]

- カーシェア「カリテコ」個人会員・法人会員
- 名鉄協商パーキングのオーナー
- 月ぎめ駐車場利用者
- MKPポイントカード会員
- 駐車サービス券・MKPギフトカード購入者
- 名鉄カナエルショップ利用者
- ゴントランシェリエ オンラインストア利用者
- 旧保険代理店システム登録者
- WEBナビ名鉄のハイキングの賞品引換申込者
- 名鉄ミューズポイントからmanacaチャージ券への交換サービス申込者

会社全体を横断する複数サービスの情報資産が調査対象になったことが分かる一方、公開された一意人数・総件数は確認できないため推定しない。

# 技術的に確認できた事項

公開情報で確認できる技術的事実は次の範囲である。

- 第三者による名鉄協商サーバーへの不正アクセスが障害原因。[^mky-cause]
- 外部専門機関の調査で複数サーバへの攻撃を確認。[^mky-leak-risk]
- 影響は多数の異なるWebサービス・業務機能にまたがった。[^mky-initial]

初期侵入経路、利用された脆弱性、資格情報の悪用有無、マルウェアの有無、侵害開始日時、攻撃主体、サーバ間の横展開経路は公表されていない。

# 対応と復旧

- 原因究明と復旧作業を並行実施し、顧客相談専用窓口を設置。[^mky-cause]
- 外部専門機関と影響範囲を調査。[^mky-leak-risk]
- 7月22日からサービス単位・機能単位で段階的に再開。[^mky-resume]
- 通常サイトが使えない機能では臨時フォームや電話受付など代替手段を導入。[^mky-resume]
- 漏えいのおそれがある顧客をサービス単位で順次特定し個別通知。[^mky-notifications]
- MKPポイントカードでは、障害期間中の利用実績を保存し、復旧後のポイント付与・クーポン補填を計画。[^mkp-recovery]

# 現在の状況と予後

2026年10月4日に名鉄協商の新着情報を再確認した時点では、本件に関する親会社側の最新更新は9月3日の個別案内状況である。[^mky-news]

一部サービスは復旧しているが、少なくとも8月27日時点でMKPポイントカードは年内再開目標の長期復旧状態だった。情報漏えいも「可能性あり・実流出未確認」の状態が続いているため、`partial_recovery_investigation_continues` とする。

なお、8月4日〜10日の「カリテコバイク」全面停止・再開は、株式会社ドコモ・バイクシェア側で8月1日に発生した別のシステム不具合が原因と公表されており、6月23日の本インシデントの復旧タイムラインには統合しない。

# 防御上の教訓

- **単一サービスではなく共有基盤単位で被害範囲を把握する。** 複数サーバと多数の異業種サービスが同時に影響を受けた。
- **復旧状況をサービス単位で持つ。** 「会社として復旧済み」という一値では、7月に再開した機能と8月末でも停止中の機能を区別できない。
- **代替チャネルをBCPへ組み込む。** Web手続が使えない期間に電話・臨時フォームなどを使い業務継続を図った。
- **通知対象と漏えい確定を混同しない。** リスク対象者への個別案内が広範でも、会社は外部流出の事実を確認していない。
- **近接する別障害の因果関係を自動統合しない。** 8月のカリテコバイク停止は別事業者の障害で、本件とは別原因だった。

# 不明点・要追跡事項

- 初期侵入経路・攻撃手法
- 攻撃を受けたサーバ数とシステム構成
- 対象顧客の総件数・一意人数
- 実際の外部データ取得の有無
- 全サービスの完全復旧日時
- 恒久的な再発防止策
- 攻撃主体と侵害滞在期間

[^mky-initial]: 名鉄協商「名鉄協商各種Webサイトにおけるシステム障害のお知らせ」2026-06-23.
[^mky-cause]: 名鉄協商「不正アクセスによるシステム障害発生に関するお知らせ」2026-07-02.
[^mky-resume]: 名鉄協商「各種Webサイトにおける一部サービス再開のお知らせ」2026-07-22.
[^mky-leak-risk]: 名鉄協商「不正アクセスに伴うお客様情報漏洩のおそれに関するお知らせ」2026-07-28.
[^mky-notifications]: 名鉄協商「お客様情報漏えいのおそれに関する個別案内の実施状況につきまして（9月3日時点）」2026-09-03.
[^mkp-recovery]: 名鉄協商 MKPポイントカード「システム障害の現状と今後の対応について」2026-08-27.
[^mky-news]: 名鉄協商「新着情報」一覧。2026-10-04確認。
