---
type: Cybersecurity Incident
title: 扶桑電通 — クラウド共有フォルダ認証情報悪用と26,489件の個人情報漏えい可能性
description: 2026年7月のクラウドストレージ共有フォルダ侵害について、認証情報不正利用、26,489件の潜在影響、外部利用者MFA義務化等の再発防止を記録する。
resource: https://www.fusodentsu.co.jp/news/news_cp_20260910/
tags: [japan, cloud-storage, credential-abuse, personal-data, mfa, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T06:23:00+09:00 }
incident:
  organization: 扶桑電通株式会社
  sector: ict-services
  jurisdiction: JP
  incident_status: public_report_closed_monitoring
  attack_type: unauthorized-access-via-credential-misuse
  earliest_known_activity: "2026-07-15"
  detected_at: "2026-07-15"
  first_disclosed_at: "2026-07-22"
  latest_public_update: "2026-09-10"
  public_record_checked_at: "2026-10-04T06:23:00+09:00"
  intrusion_vector: "misuse of authentication credentials; how the credentials were acquired was not identified"
  affected_services: "shared folders in a cloud-storage service used for information exchange with external parties"
  data_exposure: possible
  availability_impact: "affected shared-folder access was stopped as containment; no broader business outage publicly disclosed"
  restoration_state: "investigation completed; access controls and account governance strengthened"
  secondary_abuse: not_observed
  downstream_impact: "26,489 customer/contact records in files stored in the affected shared folder potentially exposed"
  regulatory_response: "initial report to the Personal Information Protection Commission"
  notification_state: "affected customers individually contacted"
  business_continuity: "shared-folder access was suspended while related systems were investigated"
  data_sensitivity: "name, address, telephone number; bank-account and credit-card payment information excluded"
sources:
  - id: fuso-first
    resource: https://www.fusodentsu.co.jp/news/news_cp_20260722.html
    title: 当社が利用するクラウドストレージへの不正アクセスについて（第1報）
    author: organization:扶桑電通株式会社
  - id: fuso-second
    resource: https://www.fusodentsu.co.jp/news/news_cp_20260910/
    title: 当社が利用するクラウドストレージへの不正アクセスについて（第2報）
    author: organization:扶桑電通株式会社
---

# 概要

扶桑電通は2026年7月15日、社外関係者との情報共有に利用していたクラウドストレージの共有フォルダへの第三者不正アクセスを確認した。外部専門会社による調査で、原因は**認証情報の不正利用**と確認されたが、その認証情報が第三者に取得された具体的経路は特定できなかった。[^fuso-first][^fuso-second]

不正アクセスを受けた共有フォルダには、取引先顧客・担当者の氏名、住所、電話番号を含むファイルがあり、**26,489件**に漏えい可能性があるとされた。銀行口座番号やクレジットカード情報等の決済情報は含まれていない。二次被害は公表時点で確認されていない。[^fuso-second]

再発防止策には、クラウドストレージを利用する**外部利用者へのMFA義務化**、パスワードポリシー強化、共有フォルダ管理・定期点検、年2回のアカウント棚卸しが含まれる。[^fuso-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-07-15 | 共有フォルダへの第三者不正アクセスを確認。共有停止、関係システム調査を開始。[^fuso-first] |
| 2026-07-22 | 第一報。個人情報を含むファイルの存在と漏えい可能性、個人情報保護委員会への初報を公表。[^fuso-first] |
| 2026-09-10 | 第二報。認証情報不正利用を原因として確認、26,489件の潜在影響、調査完了、再発防止策を公表。[^fuso-second] |
| 2026-10-04 | 公式お知らせ一覧を再確認。第二報より新しい本件事故公表は確認できず。 |

# 影響

潜在影響は取引先顧客・担当者の氏名、住所、電話番号26,489件。これは「漏えいの可能性がある個人情報」の件数であり、外部取得が個別に確認された人数と読み替えない。[^fuso-second]

決済関連情報は対象外と公表され、二次被害も確認されていない。[^fuso-second]

可用性については、対象共有フォルダの共有停止が封じ込めとして実施されたが、全社業務停止等は公表されていない。

# 技術的に確認できた事項

外部専門会社の調査で第三者による認証情報不正利用が確認された。他の不審活動は確認されず、認証情報が取得された具体的経路は特定されていない。[^fuso-second]

したがって、フィッシング、マルウェア、パスワード再利用、情報窃取型マルウェア等のどれかを原因として推測しない。

# 対応と復旧

- 対象共有フォルダの共有停止。[^fuso-first]
- 関係アカウント削除、アクセスログ調査、緊急対策本部設置。[^fuso-first]
- 外部専門会社によるフォレンジック/原因調査。[^fuso-second]
- 対象顧客への個別連絡。[^fuso-second]
- 外部利用者へのMFA導入・義務化。[^fuso-second]
- パスワード複雑性・変更ルール強化。[^fuso-second]
- 外部共有フォルダの権限管理と定期点検ルール見直し。[^fuso-second]
- 年2回のアカウント棚卸しとセキュリティ教育。[^fuso-second]

# 現在の状況と予後

2026年9月10日時点で同社は調査完了とし、新たな事実は確認されていないと公表した。影響対象者への連絡と再発防止策が進められているため、公的事故調査は成熟しているが、二次被害監視を含む意味で `public_report_closed_monitoring` とする。[^fuso-second]

# 防御上の教訓

- **社外共有クラウドでもMFAを標準にする。** 本件の再発防止策は認証情報単独取得に耐える設計へ直接対応している。
- **共有フォルダは恒久データ置場にしない。** 外部共有領域に個人情報ファイルが残存すると、1アカウントの侵害が長期保存データへ広がる。
- **アカウント棚卸しを定期制御にする。** 不要アカウント・ルール違反を検出する年2回の棚卸しが明示された。
- **「認証情報悪用」と「認証情報取得経路」を分離する。** 前者が確認されても後者が不明なら、原因を過度に具体化しない。

# 不明点・未公表事項

- 認証情報が第三者へ渡った経路
- 利用されたアカウント種別と権限範囲
- 実際に外部取得されたファイルの有無・件数
- クラウドストレージ製品名
- MFA導入以前の外部利用者認証構成

[^fuso-first]: 扶桑電通株式会社「当社が利用するクラウドストレージへの不正アクセスについて（第1報）」2026-07-22.
[^fuso-second]: 扶桑電通株式会社「当社が利用するクラウドストレージへの不正アクセスについて（第2報）」2026-09-10.
