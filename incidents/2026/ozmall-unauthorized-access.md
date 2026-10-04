---
type: Cybersecurity Incident
title: OZmall / スターツ出版 — 不正アクセスと最大44万2779名分の個人情報閲覧可能性
description: 2026年9月のOZmall不正アクセスについて、初報最大447,610名から第2報442,779名への訂正、退会者を含む影響範囲、封じ込め・サービス再開・再発防止を追跡する記録。
resource: https://starts-pub.jp/info20261001
tags: [japan, media, reservation-service, unauthorized-access, personal-data, data-minimization, 2026]
status: draft
stale_after: 2026-10-15T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:54:53Z }
incident:
  organization: スターツ出版株式会社 / OZmall
  sector: media-and-reservation-services
  jurisdiction: JP
  incident_status: service_restored_monitoring
  attack_type: unauthorized-access
  earliest_known_activity: "2026-09-26"
  detected_at: "2026-09-26"
  first_disclosed_at: "2026-09-27"
  latest_public_update: "2026-10-01"
  public_record_checked_at: "2026-10-04T04:54:53+09:00"
  intrusion_vector: "vulnerability in the affected site; technical identifier not publicly disclosed"
  affected_services: OZmall
  data_exposure: possible_viewing
  availability_impact: "affected page temporarily stopped; service subsequently resumed"
  restoration_state: "cause identified, blocking fix implemented, service resumed; monitoring and external-specialist hardening continue"
  secondary_abuse: not_observed
sources:
  - id: oz-first
    resource: https://starts-pub.jp/info20260927
    title: 当社への不正アクセスによる個人情報流出の可能性に関するお知らせ
    author: organization:Starts Publishing
  - id: oz-second
    resource: https://starts-pub.jp/info20261001
    title: 当社への不正アクセスによる個人情報流出の可能性に関するお知らせ（第2報）
    author: organization:Starts Publishing
  - id: oz-index
    resource: https://starts-pub.jp/news_category/topic_ozmall
    title: スターツ出版 OZmall お知らせ一覧
    author: organization:Starts Publishing
---

# 概要

2026年9月26日、スターツ出版が運営するOZmallで海外からの大量の不正アクセスをシステム部門が検知した。同社は該当ページへのアクセスを一時停止し、原因を特定して不正アクセス遮断のためのシステム修正を実施した。調査の結果、会員の個人情報が閲覧された可能性が判明した。[^oz-first][^oz-second]

9月27日の第一報では漏えい可能性のある対象を最大447,610名分としていたが、10月1日の第2報で精査後の最大値を**442,779名分**へ訂正し、対象にはOZmall会員だけでなく一部退会者も含まれることを明示した。[^oz-first][^oz-second]

対象情報はメールアドレス、および一部利用者の氏名と住所（都道府県まで）。電話番号や番地を含む詳細住所は閲覧形跡が確認されておらず、クレジットカード情報は外部決済システムを利用しているため漏えい可能性がないとされた。[^oz-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-26 | 海外から大量の不正アクセスを検知。該当ページを一時停止し、原因特定と遮断措置のシステム修正を実施。[^oz-first][^oz-second] |
| 2026-09-27 | 第一報。メールアドレス最大447,610名分と、一部の氏名・都道府県までの住所に閲覧可能性を公表。サービスは対策後に再開。[^oz-first] |
| 2026-09-28 | 個人情報保護委員会へ報告。[^oz-second] |
| 2026-10-01 | 第2報。対象最大値を442,779名へ訂正し、一部退会者を含むことを明示。再発防止策と通知状況を更新。[^oz-second] |

# 影響

## 影響を受けた可能性のある対象者

最新の公開最大値は **442,779名分**。9月27日の447,610名分から減少しているため、Denno Watchでは442,779をcanonicalな最大値とし、旧値は訂正履歴としてタイムラインに残す。[^oz-first][^oz-second]

第2報では対象に「OZmall会員および一部の退会者」が含まれる。退会者情報は取引上の履歴管理として一定期間保存していた情報と説明されている。[^oz-second]

## データ項目

漏えい可能性がある情報は以下。[^oz-second]

- メールアドレス
- 一部利用者の氏名
- 一部利用者の住所（都道府県まで）

現時点の調査では以下の閲覧形跡は確認されていない。[^oz-second]

- 電話番号
- 番地を含む詳細住所

クレジットカード情報は外部決済システムを利用しているため、OZmall側の本件対象には含まれない。[^oz-first][^oz-second]

## 可用性と完全性

検知後、該当ページへのアクセスを一時停止した。原因特定と遮断対策後、プログラム改ざん等の被害が発生していないことを確認したうえでサービスを再開した。[^oz-second]

# 技術的に確認できた事項

第2報は「不正アクセスの原因を特定し、当該脆弱性への対策を実施」としているが、脆弱性の技術的内容・識別子・対象コンポーネントは公開していない。[^oz-second]

公表範囲から確定できるのは以下までである。

- 9月26日に海外から大量の不正アクセスを検知。
- 個人情報の閲覧可能性を確認。
- 原因となる脆弱性を特定し対策。
- 影響を受けなかったサーバにも不正アクセス痕跡がないことを確認し、追加対策を実施。[^oz-second]

具体的な攻撃手法や攻撃主体は推測しない。

# 対応と復旧

- 該当ページへのアクセスを一時停止。[^oz-first]
- 原因を特定し、不正アクセスを遮断するシステム修正を実施。[^oz-first][^oz-second]
- 対策後、プログラム改ざん等がないことを確認してサービス再開。[^oz-second]
- 対策本部を設置し影響範囲調査。[^oz-second]
- 9月28日に個人情報保護委員会へ報告。[^oz-second]
- 対象となる可能性のある利用者へ登録メールアドレスで順次通知。[^oz-second]
- 他サーバの不正アクセス痕跡確認と追加セキュリティ対策を実施。[^oz-second]
- 外部専門機関とセキュリティ対策・監視体制の強化を継続。[^oz-second]

# 現在の状況と予後

2026年10月4日にOZmall関連のお知らせ一覧を確認した時点で、本件の最新一次公表は10月1日の第2報である。[^oz-index]

サービスは再開しており、二次被害も確認されていない。一方、会社は新たな事実が判明した場合の追加公表と監視・対策強化を継続するとしているため、`service_restored_monitoring` とする。

# 防御上の教訓

- **速報値を確定値扱いしない。** 第一報447,610名から第二報442,779名へ対象最大値が訂正された。
- **退会者データの保持根拠と期間を資産台帳に含める。** 退会後も取引履歴として保存された情報が影響対象になった。[^oz-second]
- **決済情報を分離する。** 外部決済システム利用によりカード情報は本件の被害範囲外だった。[^oz-second]
- **封じ込め後に整合性確認してから再開する。** 遮断修正だけでなく、プログラム改ざんがないことを確認後にサービスを再開した。
- **被害を受けなかったサーバも横断確認する。** 影響範囲外と考えたサーバにも痕跡確認と追加対策を実施した。[^oz-second]

# 不明点・要追跡事項

- 脆弱性の具体的種類・識別子
- 不正アクセスの正確な開始時刻・継続時間
- 442,779名のうち実際に閲覧されたことを個別に確認できた人数
- 項目別の影響人数
- 攻撃主体・攻撃元インフラ
- 恒久対策の具体的技術構成

[^oz-first]: スターツ出版「当社への不正アクセスによる個人情報流出の可能性に関するお知らせ」2026-09-27.
[^oz-second]: スターツ出版「当社への不正アクセスによる個人情報流出の可能性に関するお知らせ（第2報）」2026-10-01.
[^oz-index]: スターツ出版 OZmall お知らせ一覧。2026-10-04確認。
