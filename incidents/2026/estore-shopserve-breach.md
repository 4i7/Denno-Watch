---
type: Cybersecurity Incident
title: Ｅストアー / ショップサーブ — 不正プログラムによる購入者・会員・店舗情報の外部送信
description: 2026年5月から8月にかけて確認されたショップサーブへの不正アクセスと最大延べ8,853,839件の漏えい対象情報に関する公開記録。
resource: https://estore.jp/press/20260802/
tags: [japan, ecommerce, unauthorized-access, data-exfiltration, credentials, payment-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: 株式会社Ｅストアー
  sector: ecommerce-platform
  jurisdiction: JP
  incident_status: investigating
  attack_type: "unauthorized access with malicious program execution and data exfiltration"
  earliest_known_activity: "2026-05-21"
  detected_at: "2026-08-01"
  first_disclosed_at: "2026-08-01"
  latest_public_update: "2026-08-02"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Shopserve server and data handled for purchasers, members and merchant stores"
  data_exposure: confirmed
  availability_impact: not_publicly_quantified
  restoration_state: "attacker communications blocked; scope and cause investigation ongoing in latest incident-specific report"
  secondary_abuse: not_observed
sources:
  - id: estore-first
    resource: https://estore.jp/press/20260801/
    title: 不正アクセスによる個人情報漏えいに関するお詫びとお知らせについて
  - id: estore-second
    resource: https://estore.jp/press/20260802/
    title: 不正アクセスによる個人情報漏えいに関するお知らせ（第2報）
  - id: shopserve-home
    resource: https://shopserve.estore.jp/
    title: ショップサーブ公式サイト
---

# 概要

Ｅストアーは2026年8月1日、EC基盤「ショップサーブ」のサーバーに外部から不正アクセスがあり、第三者がサーバー上で不正なプログラムを実行して購入者情報を外部送信したことを確認・公表した。初報では当日の9:09〜11:06頃の外部送信を説明したが、翌8月2日の第2報で、確認できた発生期間を2026年5月21日から8月1日までに拡大した。[^estore-first][^estore-second]

公表件数は最大延べ8,853,839件。ただし同一人物の複数登録を含み得るため、固有の被害者人数ではない。対象には購入者・配送先情報、会員情報、会員IDとパスワード、カード名義・カード番号の一部・有効期限、さらに店舗側の管理画面/メール/FTPの認証情報や振込先口座情報が含まれる。[^estore-second]

8月2日時点で具体的な二次被害は確認されておらず、侵入の詳細と最終範囲は調査継続中だった。[^estore-second]

# 公開情報で確認できる時系列

| Date / period | Observable event |
| --- | --- |
| 2026-05-21 onward | 第2報で、第三者がサーバー上で不正プログラムを実行し購入者情報を外部送信していたことを確認できる期間の始点として公表。[^estore-second] |
| 2026-08-01 09:09–11:06頃 | 初報で具体的な外部送信時間帯として公表。[^estore-first] |
| 2026-08-01 | 漏えいを確認し初報。攻撃元からの通信を遮断し、遮断後にアクセス不能であることを確認。[^estore-first] |
| 2026-08-02 14:00時点 | 第2報。活動期間、会員・カード・店舗認証情報など追加の漏えい対象を公表。調査継続。[^estore-second] |
| 2026-10-03 review | 公式プレス上で、第2報より後のインシデント固有の確定報はDenno Watchの公開情報調査では確認できていない。ショップサーブ側には8月6日の認証システム変更告知が存在するが、因果関係が明記されない事項は本レポートの確定事実へ自動統合しない。[^shopserve-home] |

# 影響

## 規模

最大延べ8,853,839件という値は「レコード件数」であり、ユニークな顧客人数ではない。同一顧客の複数登録を含む可能性があることをＥストアー自身が明示している。[^estore-second]

## 購入者・会員情報

公開された漏えい対象には以下が含まれる。[^estore-second]

- 購入者・配送先の氏名、住所、電話番号、FAX番号、メールアドレス、勤務先、任意入力情報
- 会員情報（メールマガジン会員を含む）
- 会員ID・パスワード

会員ID・パスワードは暗号化された状態で管理されていたとされ、Ｅストアーは悪用可能性を低いと判断しつつも、不正ログインのおそれがあるとしてパスワード変更を要請した。[^estore-second]

## 決済カード情報

対象にはカード名義、カード番号の一部（先頭6桁・下4桁）、有効期限が含まれる。セキュリティコード（CVV/CVC）は保持しておらず、漏えい対象外と公表された。[^estore-second]

「カード番号の一部」であり完全なカード番号と同一視しない。一方で、氏名・住所・メール・購入関連情報との組み合わせは、なりすましやフィッシングの材料になり得るため、同社も不審連絡への注意を呼びかけている。[^estore-first][^estore-second]

## 加盟店情報

第2報で新たに、ショップサーブ管理画面のログインID・パスワード、店舗メールシステムのID・パスワード、FTPのID・パスワード、振込先口座情報が漏えい対象として公表された。[^estore-second]

この点は購入者個人情報だけでなく、加盟店舗側アカウントへの二次侵入リスクを持つため重要である。同社は店舗へパスワード変更と、必要に応じた二段階認証利用を推奨した。[^estore-second]

## 二次被害

8月2日時点では、本件に起因する具体的な二次被害報告は確認されていなかった。[^estore-second]

# 技術的に確認できた事項

確認された事実は、外部第三者がショップサーブのサーバーへ不正アクセスし、サーバー上で不正プログラムを実行して情報を外部送信したことである。[^estore-second]

一方、初期侵入の脆弱性・認証経路、攻撃者の権限、マルウェア/プログラムの性質、外部送信先、侵入開始を5月21日と特定した証拠の種類は公表されていない。第2報時点で原因の詳細は調査中である。[^estore-second]

# 対応と復旧

- 攻撃元からの通信を遮断し、遮断後にアクセス不能を確認。[^estore-first]
- 購入者へフィッシング・再決済詐欺・アカウント確認を装う連絡への注意を要請。[^estore-first]
- 会員ID/パスワード漏えい判明後、会員へパスワード変更と他サービスでの使い回し解消、多要素認証利用を推奨。[^estore-second]
- 店舗へ管理画面、メール、FTP認証情報の変更を要請し、管理画面の二段階認証を推奨。[^estore-second]
- 個人情報保護委員会への報告を表明し、原因・対象範囲・再発防止策の調査/策定を継続。[^estore-first][^estore-second]

# 現在の状況と予後

最新のインシデント固有一次報として確認できた8月2日時点では、活動期間・漏えい対象が拡大した一方、初期侵入原因、最終対象件数、再発防止策、二次被害の最終評価が未確定である。このため `investigating` とする。

# 防御上の教訓

- **侵害調査では最初に見えた時間帯を全期間とみなさない。** 初報の8月1日数時間から、翌日の調査で少なくとも5月21日まで活動期間が遡った。[^estore-first][^estore-second]
- **SaaS事業者の侵害は顧客とテナント運営者の両方に資格情報リスクを波及させる。** 購入者会員だけでなく、店舗管理、メール、FTPの資格情報が対象になった。[^estore-second]
- **件数の単位を保持する。** 8,853,839は延べレコード数であり、人数への変換はできない。[^estore-second]
- **部分カード情報でも周辺PIIと合わせた詐欺リスクを評価する。** 完全カード番号やCVVが漏れていないことだけで二次被害リスクをゼロ扱いしない。[^estore-second]

# 不明点・未公表事項

- 初期侵入経路と利用された脆弱性/認証情報
- 5月21日より前の侵害有無
- 最終的なユニーク対象人数とレコード数
- 漏えいした各データ項目の実件数
- 攻撃プログラム、外部送信先、攻撃主体
- 最終的な再発防止策と規制当局対応
- 8月2日以降の二次被害有無

[^estore-first]: Ｅストアー「不正アクセスによる個人情報漏えいに関するお詫びとお知らせについて」2026-08-01.
[^estore-second]: Ｅストアー「不正アクセスによる個人情報漏えいに関するお知らせ（第2報）」2026-08-02.
[^shopserve-home]: ショップサーブ公式サイト。2026-10-03確認。
