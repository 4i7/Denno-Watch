---
type: Cybersecurity Incident
title: ファインズ — 予約システム不正アクセスによる153万6322件の情報漏えい
description: 2026年9月に株式会社ファインズの予約システムで確認された不正アクセスと大規模な予約者情報漏えいを追跡する速報記録。
resource: https://e-tenki.co.jp/news/%E5%BC%8A%E7%A4%BE%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84/
tags: [japan, reservation-system, unauthorized-access, data-breach, personal-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:46:31Z }
incident:
  organization: 株式会社ファインズ
  sector: digital-services
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-22"
  first_disclosed_at: "2026-09-25"
  latest_public_update: "2026-09-25"
  public_record_checked_at: "2026-10-04T04:46:31+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "company-provided reservation system"
  data_exposure: confirmed_by_company_announcement
  availability_impact: not_publicly_disclosed
  restoration_state: "emergency access blocking implemented; detailed investigation ongoing"
  secondary_abuse: unknown
sources:
  - id: fines-primary
    resource: https://e-tenki.co.jp/news/%E5%BC%8A%E7%A4%BE%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84/
    title: 弊社システムへの不正アクセスによる情報漏えいについてのお詫びとお知らせ【速報】
    author: organization:Fines
    last_modified: 2026-09-25T00:00:00+09:00
  - id: fines-news-index
    resource: https://e-tenki.co.jp/news/
    title: 株式会社ファインズ ニュース一覧
    author: organization:Fines
---

# 概要

株式会社ファインズは2026年9月22日、同社が提供する予約システムの異常を検知し、調査の結果、第三者による不正アクセスを確認した。直ちにアクセス遮断等の緊急措置を実施し、9月25日に速報を公表した。[^fines-primary]

公表時点の影響範囲は **1,536,322件**。予約者の氏名、電話番号、メールアドレス、予約店舗、予約メニュー、予約日時等が対象とされている。[^fines-primary]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-22 | システム異常を検知。調査で第三者による不正アクセスを確認し、アクセス遮断等の緊急措置を実施。[^fines-primary] |
| 2026-09-25 | 速報を公表。対象1,536,322件と対象情報を開示。関係機関への報告と詳細調査の継続を表明。[^fines-primary] |

# 影響

公表された対象件数は1,536,322件。会社は「情報漏えい」として公表しているが、この数字が実際に第三者取得を個々に確認した件数なのか、調査で影響対象とした母数なのかは速報本文だけでは判別できない。したがって件数の単位と確度をそのまま保持する。[^fines-primary]

対象データには以下が含まれる。[^fines-primary]

- 氏名
- 電話番号
- メールアドレス
- 予約店舗
- 予約メニュー
- 予約日時
- その他、予約者情報として管理されていた項目

予約履歴は単純な連絡先情報とは異なり、利用した店舗・サービス・時刻の組み合わせによって行動履歴や生活パターンを推測できる可能性がある。この点は公表された被害事実と分け、二次利用リスクとして扱う。

# 技術的に確認できた事項

公開情報で確認できる技術的事実は、予約システムへの第三者による不正アクセスと、9月22日にシステム異常を検知したことまでである。初期侵入経路、悪用された脆弱性、認証情報の悪用有無、侵害開始日時、外部取得の手法は公表されていない。[^fines-primary]

# 対応と復旧

9月25日の速報時点で確認できる対応は以下。[^fines-primary]

- 不正アクセス確認後のアクセス遮断等の緊急措置
- 弁護士と連携した詳細調査
- 個人情報保護委員会等の関係機関への報告
- 影響範囲の特定
- セキュリティ強化
- 新たな事実判明時の続報公表

公開情報からは、サービス停止の有無、通常運用への復旧日時、フォレンジック完了時期、恒久対策の完了状態までは確認できない。

# 現在の状況と予後

2026年10月4日にファインズのニュース一覧を再確認した時点でも、本件に関する後続の公式報告は確認できず、9月25日の速報が最新の公開記録である。[^fines-news-index]

したがって `investigating` を維持する。速報段階で示された1,536,322件を最終確定値とみなさず、侵入経路、取得確認範囲、通知対象、復旧状態、再発防止策の後続公表を追跡する。

# 防御上の観察事項

- **予約データを単なる連絡先データとして扱わない。** 店舗・メニュー・日時の組み合わせは利用者の行動情報を含む。
- **速報値と確定値を分離する。** 大きな対象件数が早期に示されても、取得確認件数・調査母数・通知対象が同一とは限らない。
- **封じ込めと調査完了を分離する。** アクセス遮断は実施済みでも、公開記録上は原因・影響範囲・復旧状態の確定が残っている。

# 不明点・未解決事項

2026-10-04時点で公表情報から確定できない事項:

- 不正アクセスの開始日時と継続期間
- 初期侵入経路
- 悪用された脆弱性・認証情報の有無
- 1,536,322件の全てが実際に外部取得されたのか、調査対象母数を含むのか
- パスワード、決済関連情報等への影響
- サービス停止・復旧の詳細
- 二次被害の有無
- 外部専門機関等による最終調査結果
- 最終的な再発防止策

未公表事項は否定事実として扱わない。

[^fines-primary]: 株式会社ファインズ「弊社システムへの不正アクセスによる情報漏えいについてのお詫びとお知らせ【速報】」（2026-09-25）
[^fines-news-index]: 株式会社ファインズ「ニュース」一覧。2026-10-04確認。
