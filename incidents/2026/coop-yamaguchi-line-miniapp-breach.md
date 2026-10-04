---
type: Cybersecurity Incident
title: コープやまぐち — LINEミニアプリDB全削除と21万件超の組合員情報漏えい可能性
description: 2026年8月27日の第三者不正アクセスによるデータベース全削除、同日バックアップ復元、組合員情報・ここカード識別情報の潜在影響を追跡する記録。
resource: https://www.yamaguti-coop.or.jp/line-miniapp-incident-report2/
tags: [japan, cooperative, line-miniapp, unauthorized-access, data-destruction, personal-data, backup, 2026]
status: draft
stale_after: 2026-10-18T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T06:23:00+09:00 }
incident:
  organization: 生活協同組合コープやまぐち
  sector: retail-and-cooperative
  jurisdiction: JP
  incident_status: investigating_after_service_restoration
  attack_type: unauthorized-access
  earliest_known_activity: "2026-08-27"
  detected_at: "2026-08-27"
  first_disclosed_at: "2026-08-28"
  latest_public_update: "2026-09-24 clarification added to primary notices"
  public_record_checked_at: "2026-10-04T06:23:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Co-op Yamaguchi LINE mini-app database operated through an external development/operations provider"
  data_exposure: possible
  availability_impact: "database contents deleted; service restored the same day from backup after access blocking and security measures"
  restoration_state: "service restored; external-exfiltration investigation remains unresolved"
  secondary_abuse: not_observed
  downstream_impact: "member and order/reservation information held in the mini-app database; incident did not involve LINE Yahoo's database"
  regulatory_response: "reported to the Personal Information Protection Commission and consulted/reported to police"
  notification_state: "affected populations identified by category; notices to affected people were being delivered through appropriate channels"
  business_continuity: "database restored from backup on the incident day"
  data_sensitivity: "member identifiers/contact data and, for one population, Koko Card number and PIN; card/payment-account/password/special-care personal data excluded"
sources:
  - id: coop-first
    resource: https://www.yamaguti-coop.or.jp/line-miniapp-incident-report/
    title: コープやまぐちLINEミニアプリへの不正アクセスによる個人情報漏えいのおそれについて（第一報）
    author: organization:生活協同組合コープやまぐち
  - id: coop-second
    resource: https://www.yamaguti-coop.or.jp/line-miniapp-incident-report2/
    title: コープやまぐちLINEミニアプリへの不正アクセスによる個人情報漏えいのおそれについて（第二報）
    author: organization:生活協同組合コープやまぐち
---

# 概要

2026年8月27日、コープやまぐちの「LINEミニアプリ」が利用するデータベースに第三者が不正アクセスし、**データベース内の全データが削除**された。組合は外部アクセスを遮断し、同日中にバックアップからデータを復元して必要なセキュリティ対策を実施した上でサービスを再開した。[^coop-first][^coop-second]

第二報で対象範囲が精査され、主な組合員情報は、電子マネー機能付きここカードを持たない組合員 **69,586件** と、同カードを持つ組合員 **143,126件**。後者にはここカード番号とPIN番号も含まれる。さらに注文・予約利用者の一部では氏名、住所、メールアドレス等が追加で対象となる。これらはレコード/対象件数として記録し、ユニーク人数へ無条件に変換しない。[^coop-second]

外部への持ち出しは2026年10月4日の確認時点で公表上確認されておらず、流出可能性を否定できない状態である。カード番号とPINだけでは残高照会や支払いはできない設計と説明され、不正利用等の二次被害も確認されていない。[^coop-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-08-27 | LINEミニアプリDBへの第三者不正アクセスと全データ削除を確認。外部アクセス遮断、バックアップ復元、対策実施後に同日サービス復旧。[^coop-first][^coop-second] |
| 2026-08-28 | 第一報。外部持ち出しは未確認だが否定できないとして注意喚起。[^coop-first] |
| 2026-09-07 | 第二報。保存内容を精査し、対象範囲・情報項目を確定。[^coop-second] |
| 2026-09-24 | 公表ページに、本件はコープやまぐち管理DBへの侵害でありLINEヤフー管理DBではない旨を追記。[^coop-first][^coop-second] |
| 2026-10-04 | 公開記録を再確認。第二報以降の新たな事故調査結果は確認できず。 |

# 影響

## 完全性と可用性

最も明確な被害は**データベース全削除**である。これは機密性の可能性だけでなく完全性・可用性への実害を伴う。バックアップが機能し、同日復旧できた点は重要な回復証拠である。[^coop-first]

## 影響を受ける可能性のある個人情報

第二報の主要2区分は次の通り。[^coop-second]

- ここカードなし: 69,586件 — 組合員コード、名字、電話番号、郵便番号。
- 電子マネー機能付きここカードあり: 143,126件 — 上記に加え、ここカード番号、PIN番号。

このほか、一部のギフト利用者62件、Web予約利用者102件では、利用状況に応じ氏名、住所、メールアドレス等も対象となる。これらは上記母集団の部分集合として扱い、加算しない。[^coop-second]

クレジットカード情報、銀行口座情報、各種ログインパスワード、要配慮個人情報は対象DBに含まれないと公表された。[^coop-second]

# 技術的に確認できた事項

公開情報から侵入経路、認証突破方法、脆弱性識別子、攻撃主体は判定できない。システムの開発・運用は外部事業者へ委託されていたが、委託先侵害やLINEヤフー側侵害と読み替えない。[^coop-first]

観測可能な技術的事実は、攻撃者が当該DBへ到達して全データを削除できたこと、コープ側が外部アクセスを遮断したこと、バックアップから復旧できたことに限定する。

# 対応と復旧

- 外部からのアクセスを直ちに遮断。[^coop-first]
- 同日中にバックアップからDBを復元し、必要なセキュリティ対策後にサービス復旧。[^coop-second]
- 外部専門家と外部持ち出し有無を継続調査。[^coop-second]
- 個人情報保護委員会への報告と警察への相談・届出を実施。[^coop-second]
- 対象者への通知、ここカード再発行希望者への無償対応を案内。[^coop-second]

# 現在の状況と予後

可用性は事故当日に回復したが、機密性影響は閉じていない。公開情報では外部流出の痕跡は確認されていない一方、否定できないため `investigating_after_service_restoration` とする。二次被害は公表上未観測である。[^coop-second]

# 防御上の教訓

- **バックアップはランサムウェアだけでなく破壊的なDB操作にも効く。** 本件では全削除という完全性障害から同日復旧した。
- **サービス固有DBに不要な会員情報を複製しない。** ミニアプリ利用の有無にかかわらず一部組合員情報が当該DBに存在し、blast radiusを拡大した。[^coop-second]
- **復旧と漏えい判定を分離する。** データが戻ってサービスが動いても、攻撃者による閲覧・取得の有無は別問題である。
- **委託境界を明示する。** 外部委託システムの事故と、プラットフォーム事業者LINEヤフーのDB侵害を混同しない。
- **識別子の組合せリスクを評価する。** 単独では決済不能とされるカード番号/PINでも、再発行経路と二次詐欺への備えが必要になる。

# 不明点・未公表事項

- 初期侵入経路と認証方式
- 利用された脆弱性または認証情報の有無
- データ削除前の閲覧・取得・外部転送の有無
- 委託先を含む責任分界と具体的再発防止策
- 最終的な通知完了状態
- フォレンジック調査の最終終了日

[^coop-first]: 生活協同組合コープやまぐち「コープやまぐちLINEミニアプリへの不正アクセスによる個人情報漏えいのおそれについて（第一報）」2026-08-28（2026-09-24追記）.
[^coop-second]: 生活協同組合コープやまぐち「コープやまぐちLINEミニアプリへの不正アクセスによる個人情報漏えいのおそれについて（第二報）」2026-09-07（2026-09-24追記）.
