---
type: Cybersecurity Incident
title: イエローハット — Web作業予約システム不正アクセスと最大180万1499名分の個人情報漏えい可能性
description: 2026年8月に検知されたイエローハットWeb作業予約システムへの不正アクセスと、最大1,801,499名分の会員情報漏えい可能性を追跡する記録。
resource: https://assets.minkabu.jp/news/article_media_content/urn%3Anewsml%3Atdnet.info%3A20260828527904/140120260828527904.pdf
tags: [japan, retail, automotive, unauthorized-access, reservation-system, personal-data, 2026]
status: draft
stale_after: 2026-10-18T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:35:00Z }
incident:
  organization: 株式会社イエローハット
  sector: automotive-retail
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-08-18 morning JST"
  first_disclosed_at: "2026-08-28"
  latest_public_update: "2026-08-28"
  intrusion_vector: not_publicly_disclosed
  affected_services: "イエローハットWEB作業予約システム"
  data_exposure: possible_not_yet_confirmed_in_public_report
  availability_impact: "system stopped as part of containment"
  restoration_state: "company stated necessary security measures were completed by first disclosure; exact restart state not specified"
  secondary_abuse: not_publicly_confirmed
sources:
  - id: yh-tdnet
    resource: https://assets.minkabu.jp/news/article_media_content/urn%3Anewsml%3Atdnet.info%3A20260828527904/140120260828527904.pdf
    title: イエローハットにおける不正アクセスによる個人情報漏えいの可能性に関するお詫びとお知らせ
    author: organization:Yellow Hat Ltd.
  - id: yh-disclosure-index
    resource: https://finance.yahoo.co.jp/quote/9882.T/disclosure
    title: イエローハット適時開示一覧
---

# 概要

2026年8月18日朝、イエローハットは「イエローハットWEB作業予約システム」への不正アクセスを検知し、外部接続の遮断とシステム停止を含む緊急措置を実施した。調査の過程で、同システムに保管されていた会員情報の一部が外部へ漏えいした可能性が判明し、8月28日に公表した。[^yh-tdnet]

公表時点の対象は最大**1,801,499名分**。対象項目は氏名、電話番号、メールアドレス、会員番号。クレジットカード情報、パスワード、車両情報は当該システムに保持していないため、漏えいしていないと説明している。[^yh-tdnet]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-08-18 morning | 不正アクセスを検知。外部接続遮断、システム停止等の緊急措置を実施。[^yh-tdnet] |
| 2026-08-18 onward | 影響範囲調査とセキュリティ強化を実施。[^yh-tdnet] |
| 2026-08-28 | 最大1,801,499名分の会員情報漏えい可能性を公表。個人情報保護委員会への報告、警察への相談も公表。[^yh-tdnet] |
| 2026-08-28 | 会社は詳細調査と必要なセキュリティ対策を既に完了したと説明。対象候補者へのメール、SMS、電話、書面による通知を予定。[^yh-tdnet] |

# 影響

## 影響を受けた可能性のある対象者

最大1,801,499名分。公開資料は「漏えいした可能性」としており、取得が確認された確定件数ではない。[^yh-tdnet]

対象候補の情報は以下。[^yh-tdnet]

- 氏名
- 電話番号
- メールアドレス
- 会員番号

## 影響を受けたシステムに含まれないデータ

以下は当該システムで保持していなかったため、本件による漏えいはないと公表された。[^yh-tdnet]

- クレジットカード情報
- パスワード
- 車両情報

また、Web作業予約システムはグループ他社の予約システムとは異なる管理システムを採用しており、他ブランド顧客への影響はないとされた。[^yh-tdnet]

# 技術的に確認できた事項

公開資料が示す攻撃の説明は「不正プログラムによる攻撃」「不正アクセス」までで、具体的な侵入経路、脆弱性、認証情報悪用の有無、侵害開始日時、データ取得の成否は公表されていない。[^yh-tdnet]

したがって、最大1,801,499名という数字は**潜在的影響範囲**として扱い、確定漏えい件数とは区別する。

# 復旧と予後

8月28日の第一報時点で、会社はシステム停止を含む封じ込め、詳細調査、セキュリティ強化を進め「必要な対策を完了」したと説明している。一方、システムの具体的な再開日時、最終フォレンジック結果、確定漏えい件数、再発防止策の詳細は同資料では公表していない。[^yh-tdnet]

個人情報保護委員会への報告と警察への相談を実施し、対象となる可能性のある顧客に対して複数チャネルで通知するとした。[^yh-tdnet]

# 先行する2りんかん事案との関係

本件は、同じイエローハットグループで2026年4月に検知された[２りんかん会員サーバー事案](yellowhat-2rinkan-breach.md)とは別のシステム・別の事故として扱う。

２りんかん事案では最終報告で3,179,454名分のデータ取得が確認され、APIの仕組みの悪用が公表された。対して本件はイエローハット本体のWeb作業予約システムで、8月28日時点では侵入経路も漏えい確定件数も未公表である。

この二件を混同すると、原因・対象者・影響範囲・確度が誤って統合されるため、Denno Watchでは別レコードとして保持する。

# 防御上の教訓

- **データ最小化・分離が影響範囲を限定した。** 決済情報、パスワード、車両情報を作業予約システムに保持していなかったことが、漏えい候補項目を限定した。[^yh-tdnet]
- **グループ内システム分離は被害範囲を限定する。** 他社・他ブランドの予約システムを別管理にしていたため、本件の影響は他ブランドへ及ばないとされた。[^yh-tdnet]
- **同一企業グループ内の再発は、局所対策と全体対策を分けて評価すべきである。** 4月の２りんかん事案と8月の本件は別システムで発生しており、一つのシステム修復だけでは組織全体のリスク低減を保証しない。
- **「可能性」と「確認済み」を分離する。** 現時点では1,801,499名を確定漏えい件数として扱わない。

# 不明点・要追跡事項

- 不正アクセスの開始時刻と滞在期間
- 初期侵入経路または悪用された弱点
- 実際に外部取得されたデータの有無と確定件数
- Web作業予約システムの停止・再開日時
- 最終フォレンジック調査結果
- 追加の個人情報保護委員会対応
- 情報の二次利用・公開の有無

後続の公式発表が確認できるまで、このレコードは `draft` とする。

[^yh-tdnet]: イエローハット、2026年8月28日適時開示。
[^yh-disclosure-index]: イエローハット適時開示一覧。
