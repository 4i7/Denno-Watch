---
type: Cybersecurity Incident
title: "ソースネクスト — 会員取得API不正利用で最大22,519,960件流出・パスワードを含む"
description: "2026年10月9日以降の会員取得API不正利用を発見し、10月13日に封じ込め、15日に最大22,519,960件の情報流出を公表した事案。"
resource: https://www.sourcenext.com/support/i/2026/1015_info/
tags: [japan, 2026, ecommerce, api, credentials, authentication, large-scale]
status: draft
stale_after: 2026-10-26T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:43:16.292+00:00 }
incident:
  organization: "ソースネクスト株式会社"
  sector: "software-ecommerce"
  jurisdiction: "JP"
  incident_status: "contained_investigating_and_notification"
  attack_type: "unauthorized-data-acquisition-via-API"
  earliest_known_activity: "2026-10-09 10:00 JST"
  detected_at: "2026-10-13 09:00 JST"
  first_disclosed_at: "2026-10-15"
  latest_public_update: "2026-10-15"
  intrusion_vector: "会員情報取得APIの不正利用を会社が確認。具体的な認可問題・CVEは未公表"
  affected_services: "会員情報管理システム・会員情報取得API"
  data_exposure: "confirmed"
  availability_impact: "不正通信を遮断、Webサイトの全面停止は未公表"
  restoration_state: "2026-10-13 13:36 JSTまでに封じ込め。第三者調査と全システム点検は継続"
  secondary_abuse: "他サービスへの認証情報再利用が懸念されるが確定した二次不正ログイン件数未公表"
  notification_state: "対象登録メールへ順次通知。ログイン時パスワード再設定措置"
  regulatory_response: "PPC 2026-10-15報告完了、翌16日警察被害申告を予定と発表"
  data_sensitivity: "メール、パスワード、氏名、住所、連絡先、生年月日、会社・部署、契約サービスやログイン日など。クレジットカードは保存なし"
  public_record_checked_at: "2026-10-23T09:43:16.292+00:00"
sources:
  - id: primary
    resource: https://www.sourcenext.com/support/i/2026/1015_info/
    title: "当社サイトへの不正アクセスによるお客様情報流出のお詫びとお知らせ"
    author: "organization:ソースネクスト株式会社"
---

# ソースネクスト — 会員取得API不正利用で最大22,519,960件流出・パスワードを含む

## 具体的な侵害操作

ソースネクストは10月13日午前9時頃、会員情報管理システムへの不正アクセスを検知した。フォレンジックにより**10月9日10時頃から会員情報取得APIを第三者が不正利用し、会員情報を取得**していたことが判明。10月13日13時36分までに外部からの不正アクセスを封じ込めた。[^primary]

| 節目 | 日時 | 意味 |
| --- | --- | --- |
| 確認できた不正API利用開始 | 10月9日10時頃 | 侵入活動の観測。初期侵入時刻とは断定しない |
| 検知 | 10月13日09時頃 | 不正取得から約4日後に把握 |
| 封じ込め | 10月13日13時36分 | **検知から約4時間36分**。全調査終了ではない |
| 公表・PPC報告 | 10月15日 | 件数上限と情報種別の説明 |

## データの意味とパスワードの不確実性

**22,519,960件**は会社公表の影響対象レコード数。氏名・カナ、メール、パスワード、住所、性別、電話、FAX、生年月日、会社名・部署・役職、サービス登録日やログイン日などの識別情報が含まれ得る。顧客の登録状況によって対象項目は異なり、**全件・全項目が同一とは限らない**。対象レコード数を一意の人物数として扱わない。カード情報は対象システムに保管しないため今回の漏えい対象外。[^primary]

**パスワードが保存された形態（平文・ハッシュ・暗号化）は初報では明示されていない**。平文流出を勝手に断定せず、パスワード関連データの外部取得可能性を過小評価もしない。これが必要な理由は、他サービスで同一組合せを使っていた場合、当該他サービス側の変更も必要になるためである。[^primary]

## 初動・本人保護・規制

会員ログイン時のパスワード再設定を要求し、同一パスワードを使う他サービスの変更とフィッシングへの警戒を呼びかける。対象顧客には登録メールへ順次連絡。10月15日にPPCへ報告済みで、警察への申告は翌16日の**予定**として記されている。公表だけでは警察申告完了日や全対象への通知完了を認定しない。[^primary]

## 防御面の検証

APIごとの認可境界、異常な大量取得の検知、会員単位のレート制限、アクセス元・認証情報の利用状況、第三者に取得された実データ量の確定、本人通知と再設定完了率。初期侵入ベクトルや特定CVE、二次被害の有無、財務損失は未確定。

[^primary]: ソースネクスト株式会社「当社サイトへの不正アクセスによるお客様情報流出のお詫びとお知らせ」. https://www.sourcenext.com/support/i/2026/1015_info/
