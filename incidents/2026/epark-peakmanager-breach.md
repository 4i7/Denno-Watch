---
type: Cybersecurity Incident
title: EPARKリラク＆エステ / PeakManager — 顧客DB外部転送・削除と約2,218万レコード漏えい
description: 初報約3,300万レコードの可能性から、フォレンジックで外部転送を確認し約2,218万レコードへ精査、要配慮個人情報と備考欄内カード情報5件まで判明した事案。
resource: https://www.epark-relax.co.jp/news/231
tags: [japan, saas, reservation, customer-management, data-breach, sensitive-data, free-text, 2026]
status: draft
stale_after: 2026-10-25T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 株式会社EPARKリラク＆エステ
  sector: reservation-and-customer-management-platform
  jurisdiction: JP
  incident_status: forensic_investigation_reported_monitoring_continues
  attack_type: unauthorized-database-access
  earliest_known_activity: unknown
  detected_at: "2026-07-27"
  first_disclosed_at: "2026-07-31"
  latest_public_update: "2026-09-24"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: "withheld by the company to avoid inducing similar attacks"
  affected_services: "PeakManager reservation/customer-management platform database"
  data_exposure: confirmed_external_transfer
  availability_impact: "customer data in the affected database was deleted by the attacker; data later restored"
  restoration_state: "deleted data restored; affected DB/server path rebuilt/migrated and credentials changed; no traces of impact to other company systems found"
  secondary_abuse: not_observed_as_of_2026-09-24
  downstream_impact: "records entered by multiple participating stores; one person may appear in multiple store ledgers"
  regulatory_response: "reported to the Personal Information Protection Commission"
  notification_state: "public notice issued; precise person count cannot be derived from the remaining record set"
  business_continuity: "affected database was stopped, backup/recovery and migration used during response"
  data_sensitivity: "identity/contact data plus free-text treatment notes that may contain health/sensitive personal information; five note entries may contain expired card information"
sources:
  - id: peak-first
    resource: https://www.epark-relax.co.jp/news/225
    title: 不正アクセスによる個人情報漏えいの可能性に関するお知らせ（第一報）
    author: organization:株式会社EPARKリラク＆エステ
  - id: peak-second
    resource: https://www.epark-relax.co.jp/news/231
    title: 不正アクセスと個人情報漏えいに関するお知らせ（第二報）
    author: organization:株式会社EPARKリラク＆エステ
---

# Executive summary

EPARKリラク＆エステは2026年7月27日、予約・顧客管理プラットフォーム「PeakManager」の一部データベースへの不正アクセスと、保存されていた顧客情報の削除を確認した。7月31日の第一報では最大約3,300万レコードが漏えいした可能性を公表した。[^peak-first]

9月24日の第二報で、外部専門機関のフォレンジックにより、第三者がデータベース内の情報を**外部へ転送したこと**、その後データを削除したことが確認された。さらに重複除外・名寄せ等の精査後の対象を**約2,218万レコード**としたが、正確な個人数へ置き換えることは困難と明示している。[^peak-second]

第二報ではデータ種別も更新された。氏名等に加え、店舗が施術申し送り等として入力した備考欄に健康状態等の要配慮個人情報が含まれ得る。また第一報ではカード情報なしとされていたが、備考欄にクレジットカード情報に該当する可能性がある記載が5件見つかった。専用カード項目ではなく、実在/正確性は未確認で、いずれも有効期限は経過している。[^peak-second]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-07-27 | PeakManagerの一部DBへの不正アクセスと顧客情報削除を確認。[^peak-first] |
| 2026-07-30 | 個人情報保護委員会へ報告。[^peak-first] |
| 2026-07-31 | 第一報。最大約3,300万レコードの漏えい可能性を公表。対象DB停止、接続アカウント無効化/認証変更、復旧・移行を実施。[^peak-first] |
| 2026-07 – 09 | 外部専門機関によるデジタルフォレンジックとデータ精査。[^peak-second] |
| 2026-09-24 | 第二報。外部転送を確認。名寄せ後約2,218万レコードへ精査し、要配慮個人情報と備考欄のカード情報候補5件を追加公表。[^peak-second] |

# Impact

## Count semantics: 33M → 22.18M records

第一報の約3,300万は初期対象レコード規模。第二報では電話番号・メールアドレス一致等による名寄せを可能な範囲で行い、約2,218万レコードへ精査した。店舗ごとに独立入力され、同一人物でも表記差があり、連絡先未登録では同一人物判定ができないため、この値を「2,218万人」としてはならない。[^peak-second]

この訂正は過去値の誤りを消すのではなく、**初期最大候補 → 精査後の外部転送確認レコード**という証拠状態の進展として保持する。

## Data categories and free-text risk

漏えい項目には氏名・フリガナ、生年月日、性別、住所、電話番号、メールアドレス、店舗備考欄が含まれる。備考欄には健康状態等の要配慮個人情報が一部含まれる。[^peak-second]

さらに設計上カード情報の入力欄が存在しなくても、自由記述の備考欄へカード情報らしき値が5件入力されていた。データ分類はスキーマだけでなく自由記述を含めて行う必要がある。[^peak-second]

## Integrity / destructive action

攻撃者は外部転送後、DB内データを削除した。削除データは復旧済みで、他システムへの影響痕跡はフォレンジックで確認されていない。[^peak-second]

# Technical findings

会社は侵入経路・手法について、同種攻撃を誘発するおそれを理由に公表を差し控えている。したがって第三者情報から手法を推測・補完しない。[^peak-second]

# Response and recovery

- 対象DB停止、バックアップ/復旧、サーバー・DBの移行。[^peak-first]
- 悪用されたDB接続アカウントを無効化し、認証情報を変更。[^peak-first]
- 外部専門機関によるフォレンジックを実施。[^peak-second]
- 名寄せ・重複除外により対象レコードを再精査し、個人数へ変換不能であることをPPCへ報告。[^peak-second]
- 情報管理体制とセキュリティ対策を見直し・強化。[^peak-second]

# Prognosis / current state

外部転送と対象レコード規模は確認され、削除データは復旧済み。9月24日時点で不正利用、金銭被害その他の二次被害は確認されていない。新事実があれば追加公表するとしているため、公開調査は成熟しているが監視対象として残す。[^peak-second]

# Defensive lessons

- **records ≠ people を機械的に守る。** 約2,218万レコードはユニーク人数ではない。[^peak-second]
- **自由記述欄はスキーマ外の高感度データを吸収する。** 「カード欄なし」でも備考欄にカード情報が混入した。
- **要配慮情報は用途外の備考にも存在し得る。** 健康状態等の入力を最小化・分類・制御する必要がある。
- **外部転送→削除という複合影響を記録する。** 機密性と完全性の両方が侵害された。

# Unknowns / withheld details

- 具体的侵入経路・手法
- 約2,218万レコードに対応するユニーク人数
- データ転送量と転送先
- 5件のカード情報候補の真正性
- 最終的な対象者個別通知範囲

[^peak-first]: 株式会社EPARKリラク＆エステ「不正アクセスによる個人情報漏えいの可能性に関するお知らせ（第一報）」2026-07-31.
[^peak-second]: 株式会社EPARKリラク＆エステ「不正アクセスと個人情報漏えいに関するお知らせ（第二報）」2026-09-24.
