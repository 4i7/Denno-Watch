---
type: Cybersecurity Incident
title: 楽天ドライブ — 管理用アカウント認証情報侵害／保存ファイルを含む最大15,382アカウント
description: 楽天ドライブの一部システムで管理用アカウントの認証情報が不正取得され、アカウント情報・暗号化パスワード関連情報・保存ファイルが取得または閲覧されたことを確認した事案。
resource: https://support.rakuten-drive.com/hc/ja/articles/62934949147929
tags: [japan, cloud-storage, credential-theft, account-takeover, stored-files, personal-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 楽天ドライブ
  sector: cloud-storage
  jurisdiction: JP
  incident_status: contained_and_monitoring
  attack_type: management-account-credential-compromise
  earliest_known_activity: "2026-01-29"
  detected_at: not_publicly_disclosed
  first_disclosed_at: "2026-10-06"
  latest_public_update: "2026-10-06"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: "management account credentials were improperly obtained by a third party; credential acquisition method not publicly disclosed"
  affected_services: "楽天ドライブの一部システム"
  data_exposure: confirmed
  availability_impact: "アプリケーションのダウンロード、新規アカウント発行を制限"
  restoration_state: "不正アクセス経路遮断、監視強化、利用制限、対象者通知を実施"
  secondary_abuse: not_observed
  downstream_impact: "保存写真・文書等を含むデータが15,382アカウントで取得・閲覧されたことを確認"
  regulatory_response: "関係当局へ報告"
  notification_state: "対象者へメール等で個別通知"
  data_sensitivity: "アカウント名、表示名、プロフィール画像URL、暗号化パスワードと付加文字列、保存写真・文書等"
sources:
  - id: rakuten-drive-primary
    resource: https://support.rakuten-drive.com/hc/ja/articles/62934949147929
    title: 【重要】「楽天ドライブ」における不正アクセスの発生について
    author: organization:Rakuten Drive
---

# 概要

楽天ドライブは2026年10月6日、一部システムで第三者による不正アクセスがあったことを公表した。第三者が管理用アカウントの認証情報を不正に取得してシステムへアクセスし、複数種類の情報が取得・閲覧されたことを確認している。[^rakuten-drive-primary]

公表された事象は3つに分かれる。

| 事象 | 時期 | 対象 | 規模 |
| --- | --- | --- | --- |
| ① | 2026-08-27 | アカウント名、表示名、プロフィール画像URL | 687アカウント |
| ② | 2026-08-27 | 上記に加え、暗号化パスワードと暗号化時に加えた文字列 | 313アカウント |
| ③ | 2026-01-29〜09-17 | 楽天ドライブ上に保存された写真・文書等 | 15,382アカウント |

各母集団の重複関係は公表されていないため、件数を単純合算しない。[^rakuten-drive-primary]

# 影響

本件の特徴は、会員属性だけでなく**利用者がクラウドストレージへ保存したファイルそのもの**が取得・閲覧されたことが確認されている点にある。保存データは写真・文書等を含み、内容の感度は利用者ごとに異なり得る。[^rakuten-drive-primary]

313アカウントについては暗号化されたパスワードと暗号化時に加えた文字列も対象となった。公表は復号可能性やハッシュ方式等を示していないため、安全性を独自評価しない。[^rakuten-drive-primary]

公表時点で本件に起因する二次被害は確認されていない。[^rakuten-drive-primary]

# 技術的に確認できた事項

確認されている初期アクセス面は、楽天ドライブが使用する一部システムの**管理用アカウント認証情報の不正取得**である。認証情報がフィッシング、マルウェア、漏えい、設定不備等のどの経路で取得されたかは公表されていない。[^rakuten-drive-primary]

# 対応と復旧

- 不正アクセス経路を遮断。[^rakuten-drive-primary]
- 監視体制を強化。[^rakuten-drive-primary]
- アプリケーションのダウンロード、新規アカウント発行を制限。[^rakuten-drive-primary]
- Webサイトで公表し、対象者へメール等で通知。[^rakuten-drive-primary]
- 関係当局へ報告。[^rakuten-drive-primary]

# 現在の状況と予後

2026年10月6日時点で二次被害は未確認だが、保存ファイルが取得・閲覧されたこと自体は確認済みである。対象ファイルの内容が利用者ごとに異なるため、件数だけでは長期リスクを評価できない。

# 防御上の教訓

- **管理アカウントは「一人分のアカウント」ではなく多数利用者の保存物へ到達できる集中権限として扱う。**
- **クラウドストレージ事故ではメタデータと保存コンテンツを分離して評価する。** 氏名・メール等より少ない件数でも、保存ファイルは高感度になり得る。
- **暗号化済み認証情報の外部取得もローテーション判断の対象にする。**
- **複数事象の母集団を足し算しない。** 687、313、15,382の重複関係は不明である。

# 不明点・未公表事項

- 管理用アカウント認証情報の取得経路
- 管理用アカウントへのMFA有無
- 各事象の対象アカウント間の重複
- 取得・閲覧された保存ファイルの総数・容量・データクラス
- 最終フォレンジック結果

[^rakuten-drive-primary]: Rakuten Drive Support「【重要】『楽天ドライブ』における不正アクセスの発生について」2026-10-06.
