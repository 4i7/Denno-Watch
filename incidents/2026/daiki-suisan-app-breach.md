---
type: Cybersecurity Incident
title: 大起水産 — 公式アプリ不正アクセス／174,933人の個人情報に漏えい可能性
description: 大起水産公式アプリで不正アクセスが確認され、2024年11月から2026年9月までの登録者174,933人について個人情報漏えいの可能性を否定できないと公表された事案。
resource: https://www.daiki-suisan.co.jp/files/optionallink/00000164_file.pdf
tags: [japan, restaurant, mobile-app, unauthorized-access, personal-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 大起水産株式会社
  sector: food-service
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-15"
  first_disclosed_at: "2026-10-05"
  latest_public_update: "2026-10-06"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "大起水産公式アプリ"
  data_exposure: possible
  availability_impact: "アプリは通常利用可能"
  restoration_state: "不正アクセス防止策、セキュリティ・監視強化を実施し、外部専門会社が調査継続"
  secondary_abuse: not_observed
  downstream_impact: "174,933人（退会者を含む）が漏えい可能性の対象"
  regulatory_response: "個人情報保護委員会へ報告・相談"
  notification_state: "対象者へ登録メールアドレス宛に順次案内"
  data_sensitivity: "氏名、電話番号、メールアドレス、性別、郵便番号、住所、生年月日。パスワードは別サーバー管理で対象外"
sources:
  - id: daiki-primary
    resource: https://www.daiki-suisan.co.jp/files/optionallink/00000164_file.pdf
    title: 不正アクセスによる個人情報漏えいのおそれに関するお詫びとお知らせ
    author: organization:大起水産株式会社
---

# 概要

大起水産は、公式アプリのシステムが第三者から不正アクセスを受けたことを2026年9月15日に確認し、10月5日に公表した。公表時点で個人情報が実際に外部へ漏えいした事実や不正利用は確認されていないが、漏えい可能性を否定できないとしている。[^daiki-primary]

対象は2024年11月1日から2026年9月15日までの公式アプリ登録者**174,933人**で、退会者を含む。対象となり得る情報は氏名、電話番号、メールアドレス、性別、郵便番号、住所、生年月日である。住所と生年月日は任意登録であり、全員が保持されているわけではない。パスワードは別サーバーで管理され、本件の対象外とされる。[^daiki-primary]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-15 | 不正アクセスを確認し、外部からの不正アクセス防止策、セキュリティ・監視強化を実施。[^daiki-primary] |
| 2026-10-05 | 174,933人を対象とする漏えい可能性を公表。[^daiki-primary] |
| 2026-10-06 | 公表資料が更新。[^daiki-primary] |

# 影響

本件は「実流出確認」ではなく、外部漏えいの可能性を否定できない状態である。この証拠状態を、同時期の焼肉きんぐやinfoQのような確認済み持ち出しと混同しない。[^daiki-primary]

# 技術的に確認できた事項

第三者による不正アクセスが確認されたこと以外、侵入口、脆弱性、認証情報悪用、外部取得の痕跡等の詳細は公表されていない。[^daiki-primary]

# 対応と復旧

- 2026年9月15日の確認後、不正アクセス防止策を実施。[^daiki-primary]
- システムのセキュリティ対策と監視体制を強化。[^daiki-primary]
- 外部専門調査会社による調査を継続。[^daiki-primary]
- 個人情報保護委員会へ報告・相談。[^daiki-primary]
- 対象者へ登録メールアドレス宛に順次案内。[^daiki-primary]
- 公式アプリは通常どおり利用可能。[^daiki-primary]

# 現在の状況と予後

2026年10月6日時点で、外部流出の有無そのものが調査継続中である。したがって data_exposure は possible を維持し、後続調査で確認・否定された場合に更新する。

# 防御上の教訓

- **「漏えい可能性」と「確認済み漏えい」を同じ件数表現で扱わない。**
- **退会後データも影響母集団になり得る。** アカウント削除・退会と個人データ削除の完了を別々に監査する必要がある。
- **パスワードの別サーバー管理は侵害時の被害境界になり得る。**

# 不明点・未公表事項

- 初期侵入経路
- 不正アクセスの開始時刻と滞留期間
- 外部取得の有無と取得量
- 退会者データの保持期間・削除条件
- 最終調査結果

[^daiki-primary]: 大起水産株式会社「不正アクセスによる個人情報漏えいのおそれに関するお詫びとお知らせ」2026-10-05、2026-10-06更新.
