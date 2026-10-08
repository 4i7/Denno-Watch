---
type: Cybersecurity Incident
title: スカラコミュニケーションズ / i-ask — 管理サイト不正ログイン・不正プログラム設置／最大5社・713,126件の問い合わせ情報
description: FAQシステムi-askの管理サイトへ不正ログインされ、同一サーバー上の最大5社の環境へ波及し、最大713,126件の問い合わせ情報が取得された可能性がある供給者側インシデント。
resource: https://scala-com.jp/news/2026/10-1/
tags: [japan, saas, faq, supply-chain, credential-abuse, malware, personal-data, shared-hosting, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 株式会社スカラコミュニケーションズ
  sector: software-as-a-service
  jurisdiction: JP
  incident_status: investigating_and_downstream_notification
  attack_type: unauthorized-login-and-malicious-program
  earliest_known_activity: "2026-10-02 20:30 JST"
  detected_at: "2026-10-03 morning"
  first_disclosed_at: "2026-10-06"
  latest_public_update: "2026-10-07"
  public_record_checked_at: "2026-10-08T14:54:00+09:00"
  intrusion_vector: "unauthorized login to the i-ask administration site; exact credential acquisition route not publicly disclosed"
  affected_services: "FAQシステム i-ask の同一サーバー上にある最大5社の利用環境"
  data_exposure: possible
  availability_impact: "不正アクセス遮断と環境保全を実施、顧客別サービス影響は公開情報上で一様ではない"
  restoration_state: "不正ログインアカウント変更、IP遮断、不正プログラム隔離、管理者パスワード全変更、実行制御変更、フォレンジック継続"
  secondary_abuse: not_observed
  downstream_impact: "最大5社・問い合わせ最大713,126件（供給者母数）。シチズン約10万人、大和証券約11万人、損保ジャパン約6万問い合わせ（合算禁止）"
  regulatory_response: "個人情報保護委員会へ報告、警察へ相談"
  notification_state: "利用企業と連携して対象者対応中"
  data_sensitivity: "氏名、メールアドレス、問い合わせ内容等。利用企業により項目が異なり、自由記述に追加情報が含まれる場合がある"
sources:
  - id: scala-primary
    resource: https://scala-com.jp/news/2026/10-1/
    title: FAQシステム「i-ask」への不正アクセスによる個人情報漏えいに関するお詫びとお知らせ
    author: organization:株式会社スカラコミュニケーションズ
  - id: citizen-downstream
    resource: https://www.citizen.co.jp/release/news/detail/2026/20261006.html
    title: 委託先事業者に対する不正アクセスによるお客様情報の漏えいの可能性について
    author: organization:シチズン時計株式会社
  - id: daiwa-home
    resource: https://www.daiwa.jp/
    title: 外部委託先への不正アクセスによるお客さま情報の漏洩の可能性について
    author: organization:大和証券株式会社
  - id: sompo-downstream
    resource: https://www.sompo-japan.co.jp/-/media/SJNK/files/news/2026/20261007_1.pdf?la=ja-JP
    title: 事業者向け通信機能付きドライブレコーダーの委託先不正アクセスによる漏えい可能性について
    author: organization:損害保険ジャパン株式会社
  - id: shikoku-daiwa-downstream
    resource: https://www.shikokubank.co.jp/info/post_195.html
    title: 大和証券の外部委託先への不正アクセスによるお客さま情報の漏洩の可能性について
    author: organization:四国銀行
---

# 概要

スカラコミュニケーションズは、FAQシステム「i-ask」の管理サイトへ第三者が不正ログインし、不正プログラムを設置したことで、同一サーバー上で稼働していた最大5社の利用環境に保存された問い合わせ情報が外部へ漏えいした可能性があると公表した。[^scala-primary]

不正アクセスは2026年10月2日20時30分頃から10月3日8時頃にかけて発生した。10月3日朝、データベース監視アラートを契機に調査を開始し、8時頃に遮断した。対象は問い合わせ単位で最大**713,126件**で、重複を含むため人数とは一致しない。[^scala-primary]

# 公開情報で確認できる時系列

| 日付・時刻 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-10-02 20:30頃 | i-ask管理サイトへの不正ログインが始まったと確認。[^scala-primary] |
| 2026-10-03 朝 | DB監視アラートを契機に調査開始。[^scala-primary] |
| 2026-10-03 08:00頃 | 不正アクセスを遮断。該当利用企業へ同日中に報告。[^scala-primary] |
| 2026-10-06 | 供給者側とシチズン時計等が影響を公表。[^scala-primary][^citizen-downstream] |
| 2026-10-07 | 損保ジャパンがSMILING ROADの下流影響を公式PDFで追加公表。[^sompo-downstream] |

# 影響

## 供給者側の最大範囲

同一サーバー上の最大5社が対象となり、氏名、メールアドレス、問い合わせ内容等を含む最大713,126件の問い合わせ情報が対象となる。件数は問い合わせ単位の延べ数で、同一人物による複数回問い合わせを含む。実人数は名寄せ中である。[^scala-primary]

## シチズン時計

シチズン時計は、自社システムへの侵入ではなく委託先i-askの侵害であると明示し、約10万人分の氏名、住所、電話番号、メールアドレス等が対象となる可能性を公表した。自由記述の問い合わせ内容に銀行口座情報やクレジットカード情報を記載していた場合、それらも対象となる可能性がある。[^citizen-downstream]

シチズンのEC、会員制サービス、生産システム、社内ネットワークへのアクセスは確認されておらず、漏えい可能性情報だけではそれらへログインできないとしている。[^citizen-downstream]

## 損保ジャパン（10月7日新たな下流影響）

損保ジャパンは事業者向け通信機能付きドライブレコーダー「SMILING ROAD」のFAQ・お問い合わせサービスをi-askで提供していたと公表。**約6万件の問い合わせ**が漏えいした可能性がある。これは同一顧客の重複を含む延べ件数であり、**実人数ではない**。氏名、住所、電話番号、メールアドレス、勤務先、ドライバーID、運転アラート、機器シリアル番号、申込番号、問い合わせ本文等が対象となり得る。金融口座・クレジットカード・マイナンバーカード情報は含まれない。[^sompo-downstream]

同社は10月3日に委託先から連絡を受け、同社自体のシステムへの侵害は確認していないと説明。対象顧客に原則個別連絡し、原因究明、委託先管理の検証と強化策の策定を進める。実際の情報不正利用・インターネット公開は未確認。供給者側の最大713,126件に新たな約6万件を**加算しない**。[^sompo-downstream]

## 大和証券

大和証券は公式サイトで外部委託先への不正アクセスによる顧客情報漏えい可能性を案内している。提携先の四国銀行も、大和証券が問い合わせ管理等に利用する外部委託会社で不正アクセスが発生し、インターネット経由の問い合わせ情報等が対象になったと案内している。[^daiwa-home][^shikoku-daiwa-downstream]

供給者側の最大713,126件と、各利用企業が示す人数・問い合わせ件数は単位や重複関係が異なるため、単純合算しない。

# 技術的に確認できた事項

確認済みの流れは、管理サイトへの不正ログイン、不正プログラム設置、同一サーバー上の利用企業環境のDBから問い合わせ情報が取得された可能性、というもの。認証情報がどのように取得されたかは公表されていない。[^scala-primary]

# 対応と復旧

- 不正ログインに使われたアカウントのパスワード変更。[^scala-primary]
- 攻撃元IPアドレスを遮断。[^scala-primary]
- 設置された不正プログラムを隔離。[^scala-primary]
- 全環境の管理者アカウントのパスワードを変更。[^scala-primary]
- アップロードファイルをプログラムとして実行できない設定へ変更。[^scala-primary]
- 外部専門機関によるフォレンジック調査を継続。[^scala-primary]
- MFA、環境間分離、監視強化、第三者脆弱性診断を再発防止策として予定。[^scala-primary]

# 現在の状況と予後

2026年10月6日時点で、供給者横断の実人数と最終影響範囲は未確定である。二次被害は公表時点で確認されていない。複数顧客の通知が並行して進む供給者事故として追跡する。

# 防御上の教訓

- **同一サーバー上の論理分離は、管理面が侵害されれば複数顧客へ同時波及し得る。**
- **問い合わせ自由記述は高感度データの非構造化保管場所になり得る。** 定型項目だけでデータ感度を判断しない。
- **供給者のレコード数と顧客側の人数を合算しない。** 重複、別単位、顧客別保持範囲を分離する。
- **アップロード領域の実行禁止、MFA、環境分離は別レイヤーの統制として扱う。** 本件の再発防止策は侵入・実行・横断波及それぞれを抑える設計になっている。

# 不明点・未公表事項

- 不正ログインに使用された認証情報の取得経路
- 最大5社すべての組織名と各社影響
- 実際のユニーク対象人数
- 外部取得が確定したデータ量
- 最終フォレンジック結果

[^scala-primary]: 株式会社スカラコミュニケーションズ「FAQシステム『i-ask』への不正アクセスによる個人情報漏えいに関するお詫びとお知らせ」2026-10-06.
[^citizen-downstream]: シチズン時計株式会社「委託先事業者に対する不正アクセスによるお客様情報の漏えいの可能性について」2026-10-06.
[^daiwa-home]: 大和証券株式会社公式サイト「外部委託先への不正アクセスによるお客さま情報の漏洩の可能性について」2026-10-05確認.
[^sompo-downstream]: 損害保険ジャパン株式会社「当社事業者向けサービスで使用する外部委託先システムへの不正アクセスによるお客さま情報漏えいの可能性について」2026-10-07、公式2頁PDF。
[^shikoku-daiwa-downstream]: 四国銀行「大和証券の外部委託先への不正アクセスによるお客さま情報の漏洩の可能性について」2026-10-05.
