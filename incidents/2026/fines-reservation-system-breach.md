---
type: Cybersecurity Incident
title: ファインズ — 予約システム不正アクセスによる153万6322件の情報漏えい
description: 2026年9月に株式会社ファインズの予約システムで確認された不正アクセスと大規模な予約者情報漏えいを追跡する速報記録。
resource: https://e-tenki.co.jp/news/%E5%BC%8A%E7%A4%BE%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84/
tags: [japan, reservation-system, unauthorized-access, data-breach, personal-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T14:50:00Z }
incident:
  organization: 株式会社ファインズ
  sector: digital-services
  jurisdiction: JP
  incident_status: investigating
  earliest_known_activity: unknown
  detected_at: "2026-09-22"
  first_disclosed_at: "2026-09-25"
  latest_public_update: "2026-09-25"
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
---

# Executive summary

株式会社ファインズは2026年9月22日、同社が提供する予約システムの異常を検知し、調査の結果、第三者による不正アクセスを確認した。直ちにアクセス遮断等の緊急措置を実施し、9月25日に速報を公表した。[^fines-primary]

公表時点の影響範囲は **1,536,322件**。予約者の氏名、電話番号、メールアドレス、予約店舗、予約メニュー、予約日時等が対象とされている。[^fines-primary]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-09-22 | システム異常を検知。調査で第三者による不正アクセスを確認し、アクセス遮断等の緊急措置を実施。[^fines-primary] |
| 2026-09-25 | 速報を公表。対象1,536,322件と対象情報を開示。関係機関への報告と詳細調査の継続を表明。[^fines-primary] |

# Impact

公表された対象件数は1,536,322件。対象データには以下が含まれる。[^fines-primary]

- 氏名
- 電話番号
- メールアドレス
- 予約店舗
- 予約メニュー
- 予約日時
- その他、予約者情報として管理されていた項目

予約履歴は単純な連絡先情報とは異なり、利用した店舗・サービス・時刻の組み合わせによって行動履歴や生活パターンを推測できる可能性がある。この点は公表された被害事実と分け、二次利用リスクとして扱う。

# Response

9月25日の速報時点で確認できる対応は以下。[^fines-primary]

- 不正アクセス確認後のアクセス遮断等の緊急措置
- 弁護士と連携した詳細調査
- 個人情報保護委員会等の関係機関への報告
- 影響範囲の特定
- セキュリティ強化
- 新たな事実判明時の続報公表

# Defensive observations

- 予約システムは氏名・連絡先だけでなく、店舗・メニュー・日時という行動情報を集約するため、漏えい時の意味を項目数だけで評価しない方がよい。
- 速報段階では件数が示されても、実際に外部取得された範囲、侵入開始時刻、侵入経路、認証情報や決済情報への影響がまだ未確定である。速報値と確定値を分離して追跡する必要がある。

# Unknowns / open questions

2026-10-03時点で公表情報から確定できない事項:

- 不正アクセスの開始日時と継続期間
- 初期侵入経路
- 悪用された脆弱性・認証情報の有無
- 1,536,322件の全てが実際に外部取得されたのか、調査対象母数を含むのか
- パスワード、決済関連情報等への影響
- サービス停止・復旧の詳細
- 二次被害の有無
- 外部専門機関による調査結果

速報段階のため、上記は未公表であり否定事実としては扱わない。

[^fines-primary]: 株式会社ファインズ「弊社システムへの不正アクセスによる情報漏えいについてのお詫びとお知らせ【速報】」（2026-09-25）
