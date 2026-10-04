---
type: Cybersecurity Incident
title: セイコーマート — アプリ経由の不正アクセスと57万2022人分の会員情報閲覧
description: 2026年9月にセイコーマートアプリを経由して発生した不正アクセス、572,022人分の会員情報閲覧、会員系Web機能の停止と段階復旧を追跡する記録。
resource: https://online.seicomart.co.jp/delivery/cms/preview.php?disp_flg=pc&pre_no=121
tags: [japan, retail, mobile-app, unauthorized-access, personal-data, availability, 2026]
status: draft
stale_after: 2026-10-14T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:49:29Z }
incident:
  organization: 株式会社セイコーマート
  sector: convenience-retail
  jurisdiction: JP
  incident_status: recovering_investigation_continues
  attack_type: unauthorized-access
  earliest_known_activity: "2026-09-24 22:00-23:00 JST (observable unauthorized account withdrawal event)"
  detected_at: "2026-09-28 after 17:00 JST"
  first_disclosed_at: "2026-09-29"
  latest_public_update: "2026-09-30"
  public_record_checked_at: "2026-10-04T04:49:29+09:00"
  intrusion_vector: "access through the Seicomart app server to a server holding membership data; detailed method withheld"
  affected_services: "Seicomart app and membership-related Web functions; official online shop/login-related functions were also temporarily restricted"
  data_exposure: confirmed_viewing
  availability_impact: confirmed_limited
  restoration_state: "core payment/points/coupon functions available; app/Web enrollment and account-maintenance functions remained restricted as of 2026-09-30"
  secondary_abuse: "Pecoma Money unauthorized use not observed in first disclosure"
sources:
  - id: seico-first
    resource: https://online.seicomart.co.jp/delivery/cms/preview.php?pre_no=119
    title: 「セイコーマートアプリ」への不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ
    author: organization:Seicomart
  - id: seico-second
    resource: https://online.seicomart.co.jp/delivery/cms/preview.php?pre_no=120
    title: 「セイコーマートアプリ」への不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ（第二報）
    author: organization:Seicomart
  - id: seico-third
    resource: https://online.seicomart.co.jp/delivery/cms/preview.php?disp_flg=pc&pre_no=121
    title: 「セイコーマートアプリ」への不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ（第三報）
    author: organization:Seicomart
  - id: seico-news
    resource: https://online.seicomart.co.jp/delivery/news/
    title: セイコーマート公式通販 NEWS一覧
    author: organization:Seicomart
---

# 概要

セイコーマートは2026年9月28日夕方、会員情報を保有するサーバーへの不正アクセスの可能性を把握し、同日20時に当該サーバーへの接続を停止した。調査の起点は、9月24日22時〜23時の間に1アカウントで不正なクラブカード退会処理が行われていた事実だった。[^seico-first]

9月29日の初報では約57万アカウントに情報漏えいの可能性があると公表したが、9月30日の第三報で、**セイコーマートアプリに登録したことがある会員572,022人分の情報が不正アクセスにより閲覧されたことを確認**した。これはアプリ会員の49%に相当する。[^seico-first][^seico-third]

パスワード情報は漏えいしておらず、クレジットカード情報は保有していない。購買履歴も漏えいしていないと公表された。[^seico-first][^seico-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-24 22:00-23:00 | 1アカウントで不正なクラブカード退会処理が発生。後の調査起点となる。[^seico-first] |
| 2026-09-28 after 17:00 | 会員サーバーへの不正アクセス可能性を把握。[^seico-first] |
| 2026-09-28 20:00 | 当該サーバーへの接続を停止。新規入会、会員情報変更、登録カード変更、退会、マイページログイン等を停止。[^seico-first] |
| 2026-09-29 | 初報。約57万アカウントに漏えい可能性を公表。[^seico-first] |
| 2026-09-29 | 第二報。購買履歴は漏えいしていないと公表し、公式通販等の会員ログインも安全性検証のため一時停止。[^seico-second] |
| 2026-09-30 | 第三報。572,022人分の情報について不正閲覧を確認。アプリ会員の49%と公表。[^seico-third] |

# 影響

## 確認済みの対象者数

第三報で閲覧が確認された対象は **572,022人分**。対象はセイコーマートアプリに登録したことがある会員であり、アプリ会員全体の49%とされた。アプリ未登録者は対象外。[^seico-third]

## データ項目

初報で第三者に閲覧された可能性があるとされた項目は以下。[^seico-first]

- 姓名
- 性別
- 生年月日
- 住所
- 電話番号
- メールアドレス
- クラブカード入会年月日
- 退会年月日

パスワード情報は漏えいしていない。クレジットカード情報は保有していない。第二報では購買履歴も漏えいしていないと明示された。[^seico-first][^seico-second]

## 業務への影響

接続停止に伴い、アプリやWebでの新規入会、会員情報変更、登録カード変更、退会、マイページログイン、公式通販等の一部機能が停止した。[^seico-first][^seico-second]

一方、9月30日時点でも以下は利用可能とされた。[^seico-third]

- ペコママネー利用・チャージ
- ポイント付与
- 会員価格での購入
- クーポン・キャンペーン利用
- 店頭での新規入会・会員情報変更

このため、会員基盤全体を止めたのではなく、リスクの高いオンライン管理経路を制限しながら店頭・決済系の一部を維持した段階的な事業継続として記録する。

# 技術的に確認できた事項

公表情報から確認できる経路は、セイコーマートアプリのサーバーを経由して会員情報保有サーバーへ第三者が不正アクセスしたことまでである。[^seico-first]

具体的な脆弱性、認証情報の悪用有無、攻撃元、操作手順、侵害開始時刻、閲覧方法については、警察・関係機関と対応中であることを理由に第三報で非公表とされた。[^seico-third]

# 対応と復旧

- 9月28日20時に当該サーバー接続を停止。[^seico-first]
- 外部調査会社、警察、関係機関と調査・安全対策を実施。[^seico-third]
- 個人情報保護法に基づき行政当局へ報告。[^seico-third]
- 公式通販・予約系を含む会員ログイン経路を追加停止し、安全性を検証。[^seico-second]
- 9月末失効予定ポイントを1か月延長。[^seico-second]
- 店頭受付・決済・ポイント等の一部機能を維持しつつ、オンライン会員管理機能の復旧を継続。[^seico-third]

# 現在の状況と予後

2026年10月4日に公式NEWS一覧を確認した時点で、本件の最新一次公表は9月30日の第三報である。[^seico-news]

第三報時点では原因調査と安全対策が継続中で、アプリでの新規入会・登録カード変更、マイページでの会員情報変更・退会、公式通販サイト等の再開時期は未確定だった。よって `recovering_investigation_continues` とする。

# 防御上の教訓

- **異常な業務イベントをセキュリティシグナルとして扱う。** 今回は1件の不正な退会処理が、より広い不正アクセス調査の起点になった。[^seico-first]
- **速報の最大影響範囲と確認済み閲覧範囲を更新する。** 約57万という初期値は、第三報で572,022人分の閲覧確認へ精緻化された。[^seico-third]
- **認証・会員管理経路と決済・店頭機能を分離する。** 全サービス停止ではなく、オンライン会員管理を止めつつ決済・ポイント等を継続できた。
- **不要な高感度情報を保持しないことが被害範囲を限定する。** カード情報非保持、購買履歴非漏えい、パスワード非漏えいは侵害後の追加リスクを限定した。[^seico-first][^seico-second]

# 不明点・要追跡事項

- 具体的な初期侵入経路と悪用された弱点
- 572,022人について項目別に実際に閲覧された範囲
- 不正アクセスの全活動期間
- オンライン会員管理・公式通販等の全面復旧日時
- 恒久的な再発防止策
- 本件に起因する二次被害の有無

[^seico-first]: セイコーマート「『セイコーマートアプリ』への不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ」2026-09-29.
[^seico-second]: セイコーマート「同（第二報）」2026-09-29.
[^seico-third]: セイコーマート「同（第三報）」2026-09-30.
[^seico-news]: セイコーマート公式通販 NEWS一覧。2026-10-04確認。
