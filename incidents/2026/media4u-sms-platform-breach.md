---
type: Cybersecurity Incident
title: メディア4u — SMS配信基盤侵害・95,412件の管理情報流出と280件の不正SMS送信
description: 2026年6月24日に確認されたSMS配信システム侵害、管理コンソール用アカウント一覧の流出、1社アカウント経由280件の不正SMS送信、OEM・代理店を含む波及を追跡する記録。
resource: https://www.media4u.co.jp/news/3354
tags: [japan, sms, communications-platform, unauthorized-access, data-breach, supply-chain, 2026]
status: draft
stale_after: 2026-10-18T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T06:23:00+09:00 }
incident:
  organization: 株式会社メディア4u
  sector: communications-platform
  jurisdiction: JP
  incident_status: monitoring_and_customer_scope_refinement
  attack_type: unauthorized-access-through-vulnerability
  earliest_known_activity: "2026-06-24"
  detected_at: "2026-06-24"
  first_disclosed_at: "2026-07-14"
  latest_public_update: "2026-07-17"
  public_record_checked_at: "2026-10-04T06:23:00+09:00"
  intrusion_vector: "a vulnerability in the SMS platform; detailed attack method and affected ingress customer withheld"
  affected_services: "SMS distribution platform management/control plane; one client account was used for unauthorized SMS transmission"
  data_exposure: confirmed
  availability_impact: "emergency maintenance performed; service subsequently continued"
  restoration_state: "access route blocked, vulnerability fixed, management credentials invalidated/reissued, monitoring strengthened; service available"
  secondary_abuse: "280 unauthorized SMS messages confirmed through one client account"
  downstream_impact: "all customer account-management records were included in the leaked list; customer-by-customer assessment included OEM and reseller users"
  regulatory_response: "reports/coordination with relevant supervisory authorities and third-party organizations; Personal Information Protection Commission consultation on data classification"
  notification_state: "customer-specific affected fields/counts being individually confirmed and communicated"
  business_continuity: "platform continued service after emergency containment and validation"
  data_sensitivity: "account IDs, organization/site names, contact names and notification email addresses; passwords/hashes/API keys/tokens/payment data excluded"
sources:
  - id: media4u-first
    resource: https://www.media4u.co.jp/news/3351
    title: SMS配信システムへの不正アクセスに関するお知らせとお詫び
    author: organization:Media4u
  - id: media4u-second
    resource: https://www.media4u.co.jp/news/3354
    title: SMS配信システムへの不正アクセスに関するお知らせとお詫び（第2報）
    author: organization:Media4u
---

# Executive summary

メディア4uは2026年6月24日、同社SMS配信システムへの第三者不正アクセスを確認した。外部流出が確認されたのは、同社が顧客企業の管理コンソールアカウントを管理するために保有していた一覧ファイルで、**95,412レコード**。このうち担当者名や個人を識別し得るメールアドレス等を含む可能性がある精査対象は **22,928レコード** と公表された。件数はレコード数であり本人の人数と一致するとは限らない。[^media4u-first][^media4u-second]

さらに、侵入口となった特定1社のクライアントアカウントを通じて**280件の不正SMS送信**が確認された。これは機密性侵害だけでなく、正規通信基盤が第三者メッセージ配信に使われた完全性・信頼性侵害である。[^media4u-first][^media4u-second]

一方、流出確認ファイルにはSMS配信先エンドユーザーの電話番号、氏名、本文、問い合わせ内容は含まれず、同社は配信先リストを恒常保存するアドレス帳機能自体がないと説明した。パスワード、ハッシュ、APIキー、認証トークン、決済・請求情報も当該流出ファイルに含まれない。[^media4u-second]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-06-24 | 不正アクセス確認。経路遮断、緊急メンテナンス、ログ保全、外部専門機関との調査を開始。[^media4u-second] |
| 2026-06-24 – 07-13 | 管理用認証情報を全件無効化・再発行。原因脆弱性を修正し、ログイン監視を強化。[^media4u-second] |
| 2026-07-14 | 第一報。95,412レコードの管理情報流出、22,928レコードの個人情報該当可能性、280件の不正SMS送信を公表。[^media4u-first] |
| 2026-07-14以降 | OEM・販売代理店経由を含む顧客別の該当項目・件数確認、不正送信対象顧客対応、監督官庁等への報告を継続。[^media4u-second] |
| 2026-07-17 | 第二報/FAQ。データ範囲、件数単位、制御、サービス継続状態を詳細化。[^media4u-second] |
| 2026-10-04 | 公開記録を再確認。第二報より新しい主要事故公表は確認できず。 |

# Impact

## Confirmed data leak

流出確認ファイルは顧客企業のアカウント管理一覧で、アカウントID、企業名/営業所名、担当者名、通知用メールアドレス等を含む。総レコード数は95,412件で、22,928件が個人情報に該当し得る情報を含む精査対象とされた。[^media4u-first][^media4u-second]

パスワード、パスワードハッシュ、APIキー、認証トークン、決済・請求情報は当該ファイルに含まれない。[^media4u-second]

## End-user data boundary

SMSの最終受信者について、電話番号、氏名、SMS本文、問い合わせ内容等は流出確認ファイルに含まれず、現時点で流出確認なしとされた。恒常的な配信先リストを持たない設計がblast radiusを抑えた。[^media4u-second]

## Integrity / abuse

特定1社のクライアントアカウントを通じ280件のSMSが不正送信された。他顧客アカウントからの不正送信は公表時点で確認されていない。[^media4u-second]

# Technical findings

メディア4uは「原因となった脆弱性」を修正したと公表しているが、脆弱性識別子や具体的攻撃手法、侵入口となった企業名は保護・調査上の理由から非公表としている。したがってCVEや製品脆弱性を外部推測で補わない。[^media4u-second]

本件では顧客データ面と制御面を分離する必要がある。配信先データの恒常保存は限定されていた一方、管理アカウント一覧と1社の送信権限が悪用された。

# Response and recovery

- 不正アクセス経路を遮断し緊急メンテナンス。[^media4u-second]
- アクセスログを保全し外部専門機関と調査。[^media4u-second]
- 管理用認証情報を全件無効化・再発行。[^media4u-second]
- 原因となった脆弱性を修正。[^media4u-second]
- ログイン監視を強化し、パスワードポリシー強化を予定。[^media4u-second]
- 顧客別の影響情報をOEM・代理店経由利用者を含め順次通知。[^media4u-second]
- 個人情報保護委員会を含む関係機関と情報区分・報告を調整。[^media4u-second]

# Prognosis / current state

2026年7月17日時点で、同社は対策後のサービス継続を可能と判断し提供を継続している。主要な流出ファイルと不正SMS送信数は確定したが、顧客ごとの個人情報該当性や通知整理は継続していたため `monitoring_and_customer_scope_refinement` とする。[^media4u-second]

# Defensive lessons

- **通信プラットフォームでは制御面の侵害を独立評価する。** エンドユーザーデータが漏れていなくても、正規SMS送信権限の悪用は大きな信頼侵害になる。
- **認証情報は全件ローテーション可能にする。** 本件では管理用認証情報の全無効化・再発行が封じ込め手段となった。
- **不要な宛先データを恒常保持しない。** 配信先アドレス帳を持たない設計により、顧客管理一覧漏えいがSMS受信者DB全体の漏えいへ直結しなかった。
- **OEM/代理店経由の所有関係をモデル化する。** 直接契約だけでなく再販経路まで通知・影響判定が必要だった。
- **件数単位を正確に保つ。** 95,412はアカウント管理レコード、22,928は個人情報該当可能性の精査対象であり、人数ではない。

# Unknowns / withheld details

- 原因脆弱性の技術識別子と具体的悪用手順
- 侵入口となった特定1社の名称
- 不正アクセス開始時刻・滞留時間
- 95,412レコードが取得された具体的経路
- 個人情報保護委員会との最終的な個人データ該当整理
- 顧客別通知の最終完了日

[^media4u-first]: 株式会社メディア4u「SMS配信システムへの不正アクセスに関するお知らせとお詫び」2026-07-14.
[^media4u-second]: 株式会社メディア4u「SMS配信システムへの不正アクセスに関するお知らせとお詫び（第2報）」2026-07-17.
