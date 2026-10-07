---
type: Cybersecurity Incident
title: GMOリサーチ&AI / infoQ — ソフトウェア脆弱性悪用・最大948,498件の個人情報持ち出しとポイント不正交換
description: アンケートサイトinfoQで使用していたソフトウェアの脆弱性が悪用され、最大948,498件の個人情報持ち出しと611件・2,869,500円相当のポイント不正交換が確認された事案。
resource: https://gmo-research.ai/pressroom/notice/notice-20261005
tags: [japan, survey, web-application, vulnerability, data-breach, credential-data, financial-abuse, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: GMOリサーチ&AI株式会社
  sector: online-research
  jurisdiction: JP
  incident_status: service_suspended_and_investigating
  attack_type: vulnerability-exploitation
  earliest_known_activity: "2026-10-02"
  detected_at: "2026-10-03"
  first_disclosed_at: "2026-10-05"
  latest_public_update: "2026-10-05"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: "vulnerability in software used by the infoQ site"
  affected_services: "infoQ"
  data_exposure: confirmed
  availability_impact: "infoQを2026-10-03から停止、一部取引先調査にも影響"
  restoration_state: "攻撃経路遮断・外部アクセス停止、専門会社と調査中、安全確認後に再開予定"
  secondary_abuse: "611件・2,869,500円相当のポイントが本人意思によらずAmazonギフトコードへ交換"
  downstream_impact: "infoQ停止により一部取引先の調査業務に影響、取引先情報自体は本件対象外"
  regulatory_response: "2026-10-05に個人情報保護委員会へ報告"
  notification_state: "2026-10-05から対象会員へ順次メール通知"
  business_continuity: "infoQ以外の同社サービスへの不正アクセスは公表時点で未確認"
  data_sensitivity: "氏名、住所、電話、生年月日、メール、暗号化パスワード、会員ID、ポイント残高・利用状況"
sources:
  - id: gmo-infoq-primary
    resource: https://gmo-research.ai/pressroom/notice/notice-20261005
    title: 当社が運営するアンケートサイト「infoQ」への不正アクセスによる個人情報漏えいに関するお詫びとお知らせ
    author: organization:GMOリサーチ&AI株式会社
---

# 概要

GMOリサーチ&AIは2026年10月3日、アンケートサイト「infoQ」への不正アクセスを確認し、同日サービスを停止した。後の調査で、10月2日以降に第三者が同サイトで使用していたソフトウェアの脆弱性を悪用して侵入し、会員の個人情報を外部へ持ち出していたことが確認された。[^gmo-infoq-primary]

対象は最大**948,498件**で、10月5日時点で同社が保有する個人情報の全件を上限としている。加えて、**611件・2,869,500円相当**のポイントが本人の意思によらずAmazonギフトコードへ交換されており、機密性侵害だけでなく実際の価値移転まで確認された。[^gmo-infoq-primary]

# 公開情報で確認できる時系列

| 日付・時刻 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-10-02以降 | 後の調査で第三者による不正アクセスを確認。[^gmo-infoq-primary] |
| 2026-10-03 午前 | 会員からの問い合わせを契機に調査し、不正アクセスを確認。[^gmo-infoq-primary] |
| 2026-10-03 11:24 | Amazonギフトコード、GMOポイントへの交換を停止。[^gmo-infoq-primary] |
| 2026-10-03 14:15 | 攻撃経路を遮断。[^gmo-infoq-primary] |
| 2026-10-03 15:00 | 外部からinfoQへのアクセスを遮断し、サービス停止。[^gmo-infoq-primary] |
| 2026-10-05 | 個人情報保護委員会へ報告し、対象会員への順次通知を開始。[^gmo-infoq-primary] |

# 影響

## 個人情報

最大948,498件について、氏名、フリガナ、性別、生年月日、メールアドレス、住所、電話番号、暗号化されたパスワード、会員ID、ニックネーム、保有ポイント数、最終回答日等が対象となる。クレジットカード情報とマイナンバーは同社が保有していない。[^gmo-infoq-primary]

## 実際の不正利用

611件、合計2,869,500円相当のポイントがAmazonギフトコードへ不正交換された。同社は不正交換分を全額補填するとしている。[^gmo-infoq-primary]

このため、本件では「漏えいした可能性」ではなく、個人情報の持ち出しと一部アカウント価値の不正利用が双方とも確認済みである。

# 技術的に確認できた事項

同社は、infoQサイトで使用していたソフトウェアの脆弱性を第三者が悪用して侵入したことを確認している。製品名、CVE、具体的な悪用手順は公表されていないため補わない。[^gmo-infoq-primary]

# 対応と復旧

- ポイント交換機能を停止。[^gmo-infoq-primary]
- 攻撃経路を遮断し、infoQ全体を外部からアクセス不能にした。[^gmo-infoq-primary]
- セキュリティ専門会社と調査を継続。[^gmo-infoq-primary]
- 個人情報保護委員会へ報告。[^gmo-infoq-primary]
- 対象会員へ個別通知を開始。[^gmo-infoq-primary]
- 安全性確認と再発防止策実施後にサービス再開予定。[^gmo-infoq-primary]

# 現在の状況と予後

2026年10月5日時点でinfoQは停止中で、最終調査結果と再発防止策は後日公表予定である。取引先情報は本件対象外とされる一方、infoQ停止により一部の依頼調査に業務影響が生じている。[^gmo-infoq-primary]

# 防御上の教訓

- **ポイント等の換価可能資産は個人情報とは別の完全性・金銭被害面として監視する。**
- **大量会員データと換価機能が同じサービス境界にある場合、侵入後の被害が「閲覧」から「価値移転」へ進み得る。**
- **暗号化パスワードも漏えい対象として扱う。** 平文でないことは重要だが、使い回し対策や認証情報ローテーションの必要性を消さない。
- **サービス停止は業務上の下流影響を生む。** 顧客データが漏れていなくても、調査プラットフォーム停止が取引先の業務へ波及した。

# 不明点・未公表事項

- 脆弱性が存在したソフトウェア名とCVE
- 実際に持ち出されたユニーク人数の最終確定値
- 攻撃者がポイント交換まで到達した権限経路
- サービス再開日
- 最終再発防止策

[^gmo-infoq-primary]: GMOリサーチ&AI株式会社「当社が運営するアンケートサイト『infoQ』への不正アクセスによる個人情報漏えいに関するお詫びとお知らせ」2026-10-05.
