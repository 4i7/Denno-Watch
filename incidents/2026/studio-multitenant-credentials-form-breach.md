---
type: Cybersecurity Incident
title: "Studio — クラウドの脆弱性悪用・暗号鍵/フォーム/API認証情報とデジタル庁への波及"
description: "Studioのクラウドへ不正アクセス。フォーム内容、APIキー、暗号鍵にアクセス可能な状態となり、多数の顧客の追加対応が必要となったSaaS供給者事故。"
resource: https://studio.design/ja/whats-new/unauthorized-access-2026-10
tags: [japan, 2026, saas, supply-chain, encryption-keys, api-credentials, forms, cloud]
status: draft
stale_after: 2026-10-26T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:42:15.916+00:00 }
incident:
  organization: "Studio株式会社"
  sector: "web-design-software-as-a-service"
  jurisdiction: "JP"
  incident_status: "contained_forensic_and_notification_ongoing"
  attack_type: "vulnerability-exploitation-to-cloud-data-exposure"
  earliest_known_activity: "2026-09-30 to 2026-10-01 JST"
  detected_at: "2026-10-13"
  first_disclosed_at: "2026-10-16"
  latest_public_update: "2026-10-20 FAQ update; 2026-10-22 downstream Digital Agency"
  intrusion_vector: "Studio一部機能の脆弱性を第三者が悪用。製品名・CVEは未公表"
  affected_services: "Studioアカウント、デザイン/CMS、フォーム、API連携、プレビュー、Google Sheets、Webhook、カスタムプロキシ"
  data_exposure: "possible"
  availability_impact: "2026-10-14 02:30頃、全ユーザーの一括ログアウト。全面的なサイト停止とは別"
  restoration_state: "侵入経路修正は10月13〜14日。サービス側暗号鍵切替10月17日、旧保存データの再暗号化は継続"
  secondary_abuse: "情報の改ざん・削除は公表時点で未確認。外部に取得された実件数は不明"
  downstream_impact: "デジタル庁が過去フォーム回答最大13,323件と管理アカウント35件の可能性を公表"
  regulatory_response: "PPCとの協議によりフォーム利用組織の個別報告またはStudioとの連名報告を選択可能と10月20日公表"
  notification_state: "Studioが影響機能別にプロジェクトオーナーへ個別通知"
  data_sensitivity: "ハッシュ化パスワード、フォーム自由記述、API秘密キー・トークン、Google Sheets連携、暗号鍵、Webhook URL、未公開ライブプレビューURL"
  public_record_checked_at: "2026-10-23T09:42:15.916+00:00"
sources:
  - id: studio
    resource: https://studio.design/ja/whats-new/unauthorized-access-2026-10
    title: "不正アクセスによる情報流出に関するお詫びとお願い（第一報）"
    author: "organization:Studio株式会社"
  - id: faq
    resource: https://studio.design/ja/security/notice/2026-10-incident
    title: "Studioにおける不正アクセスに関するご案内（10月20日更新）"
    author: "organization:Studio株式会社"
  - id: report
    resource: https://studio.design/ja/whats-new/unauthorized-access-2026-10-form
    title: "フォーム機能利用者向け個人情報保護委員会報告案内"
    author: "organization:Studio株式会社"
  - id: agency
    resource: https://www.digital.go.jp/press/a0a8f66c-b32d-4695-9372-bcd5d4280f22
    title: "Studio社における不正アクセスによる個人情報の漏えいの可能性"
    author: "organization:デジタル庁"
---

# Studio — クラウドの脆弱性悪用・暗号鍵/フォーム/API認証情報とデジタル庁への波及

## 調査上の最重要事実

第三者がStudioの一部機能の脆弱性を悪用し、クラウド環境へ不正アクセス。**9月30日〜10月1日に攻撃活動が確認され、データが外部から取得可能な状態は10月14日の対処まで続いた**。10月13日に社内で検知、13〜14日に入口を遮断した。外部取得可能だったことは確認されたが、**実際にどのデータが何件取得されたかは確認できない**。会社は流出したものとみなして対応する。[^studio]

## 盗難可能なデータと暗号化の限界

| カテゴリー | 対象に含まれ得るもの | 重要な証拠境界 |
| --- | --- | --- |
| ユーザー認証 | ユーザー名、メール、ハッシュ化パスワード | 平文パスワード流出とは断定しない |
| サイト制作 | CMS・エディタ内容、未公開プレビューURL | 未公開情報も影響し得る |
| フォーム | サイト訪問者から送信された回答・自由記述 | 顧客と顧客のサイト訪問者の双方に波及 |
| 外部連携の認証情報 | APIキー・トークン、Google Sheets連携資格情報、パスワード保護ページ | 第三者が別サービスへ到達する恐れ。実侵害は未確認 |
| 外部通知 | Webhook URL、カスタムプロキシキー | 顧客側の失効・再発行が不可欠 |

**暗号化データだけでなく、復号に必要な鍵も同じ不正アクセスで読み出せた**ため、「DBは暗号化していた」という理由だけでは機密性が保護されない。Studioはサービス側の鍵や認証情報を切り替えたが、顧客が発行元の他サービスで使うAPIキーを代わりに無効化することはできない。[^studio][^faq]

## 封じ込め・復旧の段階

- 10月13〜14日：脆弱性修正、既知侵入口の閉鎖。
- 10月14日02:30頃：全顧客を一括ログアウトして再認証を要請。
- 10月16日：利用機能別にオーナーへメール通知。API、フォーム、Webhook、パスワード保護、Google Sheets、カスタムプロキシの対応は別。
- 10月17日：**新規データ用暗号鍵は更新済み**。既存データの再暗号化・旧鍵廃止は作業中。
- 10月20日：FAQとPPC報告方法を更新。プロキシキー等、古い鍵は顧客作業が完了しない限り使用可能なケースがある。[^faq]

## デジタル庁の具体的な下流影響

デジタル庁は10月22日、2021年5月〜2023年3月にフォームへ送信された回答の一部について漏えいの**可能性**を公表。[^agency]

| 問い合わせ種別 | 最大件数 |
| --- | ---: |
| 意見・要望 | 8,833 |
| 採用 | 250 |
| 接種証明書アプリ | 3,661 |
| 着ぐるみ借用 | 117 |
| ワークショップ等 | 462 |
| **フォーム5種合計** | **13,323件** |
| Studioアカウント（別母集団） | **35件** |

これらは回答件数で、本人のユニーク人数でも取得確定件数でもない。管理アカウント35件をフォーム送信数へ無条件に加算して「被害人数」としない。デジタル庁は現時点で悪用・二次被害未確認と公表。[^agency]

## 法定報告の運用と顧客側責任

StudioはPPCと協議し、フォーム利用組織による**個別報告**か**Studioとの連名報告**を選択できると発表した。所定の連名報告なら本件に限り速報の目安を過ぎても報告遅延と扱わないという説明で、一般的な法定期限の改正ではない。[^report]

## 防御と監査の検証質問

暗号鍵と暗号文の権限分離、旧鍵廃止・再暗号化の監査証跡、外部APIキーの顧客別失効、フォーム回答の保持期間と削除証跡、Webhook更新後の旧URL失効、顧客ごとのPPC・本人通知義務の把握。**欠落統制の確認**ではなく、今後調べるべきチェック項目である。

未確定：全顧客の影響人数、CVE、実外部取得量、全鍵の失効、第三者フォレンジック完了、財務・法的影響。

[^studio]: Studio株式会社「不正アクセスによる情報流出に関するお詫びとお願い（第一報）」. https://studio.design/ja/whats-new/unauthorized-access-2026-10
[^faq]: Studio株式会社「Studioにおける不正アクセスに関するご案内（10月20日更新）」. https://studio.design/ja/security/notice/2026-10-incident
[^report]: Studio株式会社「フォーム機能利用者向け個人情報保護委員会報告案内」. https://studio.design/ja/whats-new/unauthorized-access-2026-10-form
[^agency]: デジタル庁「Studio社における不正アクセスによる個人情報の漏えいの可能性」. https://www.digital.go.jp/press/a0a8f66c-b32d-4695-9372-bcd5d4280f22
