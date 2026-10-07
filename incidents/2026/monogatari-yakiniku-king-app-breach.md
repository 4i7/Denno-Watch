---
type: Cybersecurity Incident
title: 物語コーポレーション / 焼肉きんぐ — 公式アプリ会員管理システム侵害・10,788,963件の個人情報漏えい
description: 2026年10月に焼肉きんぐ公式アプリの会員管理システムが不正アクセスを受け、登録約1,081万件のうち10,788,963件の会員情報漏えいが確認された事案。
resource: https://www.monogatari.co.jp/news/261005_news/
tags: [japan, restaurant, mobile-app, unauthorized-access, personal-data, large-scale, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 株式会社物語コーポレーション
  sector: food-service
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: "2026-10-02"
  detected_at: "2026-10-02"
  first_disclosed_at: "2026-10-05"
  latest_public_update: "2026-10-05"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: "not publicly disclosed; third-party unauthorized access to the Yakiniku King app membership management system confirmed"
  affected_services: "焼肉きんぐ公式アプリ会員管理システム"
  data_exposure: confirmed
  availability_impact: "アプリは防御措置を講じた上で提供継続"
  restoration_state: "通信遮断・防御措置実施済み、原因と侵入経緯を調査中"
  secondary_abuse: not_observed
  downstream_impact: "10,788,963件の会員情報が漏えい"
  regulatory_response: "個人情報保護委員会への報告および警察への被害届提出等を進行"
  notification_state: "公式公表と専用窓口による案内"
  business_continuity: "焼肉きんぐ公式アプリは防御措置後も継続提供、他ブランドアプリでは漏えいを確認せず"
  data_sensitivity: "会員番号、氏名、メールアドレス、電話番号"
sources:
  - id: monogatari-primary
    resource: https://www.monogatari.co.jp/news/261005_news/
    title: 『焼肉きんぐ』公式アプリ 会員管理システムへの第三者からの不正アクセスによる個人情報漏えいに関するお詫び
    author: organization:株式会社物語コーポレーション
---

# 概要

物語コーポレーションは2026年10月2日、「焼肉きんぐ」公式アプリの会員管理システムへの第三者による不正アクセスを確認した。通信遮断と防御措置を実施した後、10月3日に会員情報の漏えいを確認し、10月5日に公表した。[^monogatari-primary]

ユーザー登録10,808,784件のうち、**10,788,963件**について会員番号、氏名、メールアドレス、電話番号が漏えいした。登録母数のほぼ全体が対象となる大規模事案である。一方、ログインパスワード、生年月日、性別、郵便番号、保有ポイントを含む店舗利用履歴は漏えいしておらず、クレジットカード等の決済情報は同社が保持していない。[^monogatari-primary]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-10-02 | 会員管理システムへの不正アクセスを確認。通信遮断と防御措置を実施。[^monogatari-primary] |
| 2026-10-03 | 会員情報の漏えいを確認。[^monogatari-primary] |
| 2026-10-05 | 10,788,963件の漏えい、対象項目、対応状況を公表。[^monogatari-primary] |

# 影響

漏えいが確認されたのは、会員番号、氏名、メールアドレス、電話番号である。公表時点で、漏えい情報が不特定多数に公開された事実や不正利用は確認されていない。[^monogatari-primary]

パスワードや決済情報が対象外でも、氏名・メール・電話番号の組合せは、サービス利用者を装った標的型フィッシングやなりすまし連絡に利用され得るため、同社自身も注意喚起している。[^monogatari-primary]

# 技術的に確認できた事項

公開情報から確認できる原因粒度は「第三者による不正アクセス」までである。侵入口、脆弱性、認証情報悪用の有無、攻撃主体は調査中であり推測しない。[^monogatari-primary]

# 対応と復旧

- 不正アクセス確認後に通信を遮断し、防御措置を実施。[^monogatari-primary]
- 開発会社・関係会社とセキュリティ対策および監視体制を強化。[^monogatari-primary]
- 個人情報保護委員会への報告、警察への被害届提出等を進行。[^monogatari-primary]
- 公式アプリは防御措置を講じた上で提供を継続。[^monogatari-primary]

# 現在の状況と予後

2026年10月5日時点で、漏えい件数と主要な対象項目は確認済みだが、侵入経路と原因は調査中である。二次被害は公表時点で確認されていない。

# 防御上の教訓

- **アプリ会員基盤は大量の連絡先を一括して失う集中点になる。** 認証情報や決済情報が分離されていても、数百万〜千万単位の本人識別・連絡先データが一つの事故で露出し得る。
- **保持しない情報は漏えいしない。** 決済情報を保持していなかったこと、パスワード等が漏えい対象外だったことは、侵害後の被害境界として重要である。
- **「サービス継続」と「原因究明完了」は別状態で記録する。** 本件は防御措置後もアプリ提供を継続しているが、侵入経路は未確定である。

# 不明点・未公表事項

- 初期侵入経路
- 悪用された脆弱性または認証情報の有無
- 攻撃者が取得したデータの具体的な取得方法
- 最終フォレンジック結果
- 二次悪用の長期評価

[^monogatari-primary]: 株式会社物語コーポレーション「『焼肉きんぐ』公式アプリ 会員管理システムへの第三者からの不正アクセスによる個人情報漏えいに関するお詫び」2026-10-05.
