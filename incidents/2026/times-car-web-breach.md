---
type: Cybersecurity Incident
title: タイムズカー — Webシステム不正アクセスによる約660万アカウント情報流出
description: 2026年9月に発生したタイムズカーWebシステムへの不正アクセスと、本人確認書類約160万件を含む大規模な会員情報流出を追跡する記録。
resource: https://www.park24.co.jp/news/2026/09/20260929-1.html
tags: [japan, mobility, unauthorized-access, identity-documents, personal-data, credentials, 2026]
status: draft
stale_after: 2026-10-13T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:46:31Z }
incident:
  organization: タイムズモビリティ株式会社 / パーク２４株式会社
  sector: mobility-and-car-sharing
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-25 09:07 JST"
  first_disclosed_at: "2026-09-25"
  latest_public_update: "2026-09-29"
  public_record_checked_at: "2026-10-04T04:46:31+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Times Car Web system"
  data_exposure: confirmed
  availability_impact: not_observed
  restoration_state: "access path and attacker communications blocked by 2026-09-26 07:25; services continued normally"
  secondary_abuse: not_observed
sources:
  - id: times-first
    resource: https://www.park24.co.jp/news/2026/09/web1.html
    title: タイムズカーWebサイトへの不正アクセスによる個人情報漏えいの可能性について（第1報）
  - id: times-second
    resource: https://www.park24.co.jp/news/2026/09/20260928-1.html
    title: タイムズカーWebシステムへの不正アクセスに関する調査結果および今後の対応について（第2報）
  - id: times-third
    resource: https://www.park24.co.jp/news/2026/09/20260929-1.html
    title: タイムズカーWebシステムへの不正アクセスに関する調査結果および今後の対応について（第3報）
  - id: park24-home
    resource: https://www.park24.co.jp/
    title: パーク２４株式会社
---

# Executive summary

タイムズモビリティが運営するタイムズカーWebシステムで、2026年9月25日9時07分に外部からの不正アクセスを検知した。9月26日7時25分までに侵入経路と攻撃元通信を遮断し、遮断後に再アクセスできないことを確認した。[^times-first][^times-second]

外部専門機関との調査で、第三者がシステムに保存されていた会員情報を実際に取得していたことを確認。漏えいしたアカウントは約660万件で、氏名、住所、生年月日、電話番号、メールアドレス、運転免許情報、本人確認書類情報、復元不能形式で保存されたパスワード、外部連携サービスID等が対象となる。[^times-second]

9月29日の第3報では、このうち運転免許証画像、現住所確認書類画像、学生証画像、家族確認書類画像など**本人確認書類が漏えいしたアカウントが約160万件**と確定した。[^times-third]

クレジットカード情報は漏えいしておらず、サービス提供への影響も確認されていない。9月28日時点で情報の不特定多数への公開や本件起因の不正利用も確認されていなかった。[^times-second]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-09-25 09:07 | タイムズカーWebシステムで不正アクセスを検知し調査開始。[^times-first][^times-second] |
| 2026-09-25 | 第一報。会員個人情報の漏えい可能性を公表。[^times-first] |
| 2026-09-26 07:25まで | 不正アクセス経路の遮断、攻撃元との通信遮断、遮断後のアクセス不能確認を完了。[^times-first][^times-second] |
| 2026-09-28 | 第2報。約660万アカウント分の情報が第三者に取得されたことを確認。外部専門機関によるフォレンジック継続。[^times-second] |
| 2026-09-29 | 第3報。約160万アカウントで本人確認書類情報の漏えいを確認。対象者への個別案内開始。[^times-third] |

# Impact

## Scale

漏えいしたアカウント数は約660万件。対象には現会員だけでなく退会済み顧客、入会申込みをしたものの完了していない人、タイムズビジネスサービス会員・退会者も含まれる。[^times-second]

## Identity documents

約160万アカウントで本人確認書類の漏えいを確認。対象として以下が公表されている。[^times-third]

- 運転免許証画像
- 現住所確認書類画像（公共料金の請求書等）
- 学生証画像
- 家族確認書類画像

本人確認書類は氏名・住所等のテキストデータよりも、なりすましや本人確認プロセス悪用に利用され得る高感度データである。ただし実際の不正利用件数は確認されていないため、リスクと観測被害を分ける。

## Other personal and account data

対象者によって異なるが、氏名、法人会員の所属部署、住所、生年月日、電話番号、メールアドレス、運転免許情報、パスワード、連携サービスID等が漏えいした。[^times-second]

パスワードは復元できない形式で保存されており、パーク２４は当該情報だけから顧客アカウントを不正利用するおそれはないと説明している。[^times-second]

## Payment data and availability

クレジットカード情報の漏えいは確認されていない。サービス提供への影響も確認されず、各種サービスは通常どおり継続した。[^times-second]

## Secondary abuse

9月28日時点で、漏えい情報が不特定多数に公開された事実、本件に起因する個人情報の不正利用は確認されていない。[^times-second]

# Technical findings

公表情報は第三者によるWebシステムへの不正アクセスと情報取得を確認しているが、初期侵入経路、脆弱性、認証情報の悪用有無、攻撃元インフラ、侵害開始時刻、データ取得手法はまだ公表していない。[^times-second]

防御側にとって重要なのは、検知から約22時間以内に侵入経路と攻撃元通信の遮断・再アクセス不能確認まで進めた一方、データ影響の全容確定はその後も継続した点である。封じ込め完了と情報影響確定は別のマイルストーンとして扱う。[^times-first][^times-second][^times-third]

# Response and recovery

- 検知直後に調査・対応開始。[^times-first]
- 9月26日7時25分までに侵入経路・攻撃元通信を遮断し、再アクセス不能を確認。[^times-second]
- 外部専門機関によるフォレンジックを実施。[^times-second]
- 個人情報保護委員会・警察へ報告。[^times-second]
- 約660万アカウント対象者へ順次個別案内。[^times-second]
- 本人確認書類漏えい対象約160万アカウントへ9月29日から個別メール案内。[^times-third]
- 再発防止策は実施済み対策、中長期策、実施予定時期を整理して続報予定。[^times-second]

# Prognosis / current state

侵入経路は遮断済みで、新たな不正アクセスは9月28日時点で確認されていない。一方、個々の漏えい内容、原因、最終影響範囲、再発防止策は追加調査・通知中である。[^times-second][^times-third]

2026年10月4日にパーク２４の最新情報を再確認した時点でも、本件の最新一次公表は9月29日の第3報であり、第4報以降は確認できていない。[^park24-home]

本人確認書類という高感度データを約160万件含むため、後続の不正利用監視・本人保護措置と最終報を追跡する必要があり、`investigating` とする。

# Defensive lessons

- **本人確認書類を通常PIIと同じ保持ポリシーにしない。** 退会者・未入会完了者を含む大規模な履歴データが影響対象になったため、本人確認完了後の画像保持期間、必要性、分離保管、アクセス権を明示的に設計する必要がある。[^times-second][^times-third]
- **封じ込めSLAと影響調査SLAを分ける。** ネットワーク遮断は約1日で進められても、誰のどの項目が取得されたかの確定には追加日数を要した。[^times-second][^times-third]
- **退会者データもblast radiusへ含める。** アクティブ会員だけを対象にした資産台帳では事故時の影響人数を過小評価する。[^times-second]
- **復元不能パスワードと本人確認書類を同列に扱わない。** 侵害後に必要な顧客保護策はデータ種別ごとに異なる。[^times-second][^times-third]

# Unknowns / withheld details

- 初期侵入経路、利用された脆弱性・資格情報
- 侵害開始日時と滞在期間
- 取得に使われた技術・クエリ・API
- 約660万のうち各データ項目別の詳細件数（本人確認書類以外）
- 本人確認書類の種別別件数
- 後続の不正利用・なりすまし被害
- 最終再発防止策

[^times-first]: パーク２４「タイムズカーWebサイトへの不正アクセスによる個人情報漏えいの可能性について（第1報）」2026-09-25、9月26日追記.
[^times-second]: パーク２４「タイムズカーWebシステムへの不正アクセスに関する調査結果および今後の対応について（第2報）」2026-09-28.
[^times-third]: パーク２４「タイムズカーWebシステムへの不正アクセスに関する調査結果および今後の対応について（第3報）」2026-09-29.
[^park24-home]: パーク２４株式会社トップページ。2026-10-04確認。
