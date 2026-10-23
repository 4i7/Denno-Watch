---
type: Cybersecurity Incident
title: "PingCAP / TiDB — 社内認証情報侵害・国内約5万件・SQL履歴とAPI公開鍵部分の流出"
description: "盗まれた認証情報でPingCAPの社内システムからデータを複製。TiDB Cloud本体侵害は未観測だが顧客アカウントとSQL履歴、サポート、契約・APIキー関連情報が対象。"
resource: https://pingcap.co.jp/trust-hub/security/security-update-october-2026/
tags: [japan, 2026, database, cloud, identity, api, supply-chain, credentials]
status: draft
stale_after: 2026-10-27T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:44:16.131+00:00 }
incident:
  organization: "PingCAP株式会社／PingCAP Inc."
  sector: "database-cloud-SaaS"
  jurisdiction: "JP"
  incident_status: "contained_investigation_ongoing"
  attack_type: "stolen-credentials-internal-system-data-copy"
  earliest_known_activity: "2026-09-09 US time"
  detected_at: "2026-10-07"
  first_disclosed_at: "2026-10-21 Japan (English notice 2026-10-19)"
  latest_public_update: "2026-10-21 13:05 JST addendum"
  intrusion_vector: "第三者が不正取得したアカウント資格情報でPingCAP社内システムへアクセス"
  affected_services: "社内システムの顧客・アカウント・契約・サポート関連情報。TiDB Cloud本体への侵入は未観測"
  data_exposure: "confirmed"
  availability_impact: "TiDB Cloudの全面停止は公表なし"
  restoration_state: "盗難認証情報を全失効、既知入口遮断、アクセス権とネットワーク管理改善、調査継続"
  secondary_abuse: "顧客TiDB Cloudへの不正アクセス・カード情報流出は調査上未観測"
  downstream_impact: "日本国内最大約50,000件の個人情報、販売パートナーのクラスメソッドが注意案内"
  regulatory_response: "法執行機関と関係国監督当局に報告"
  notification_state: "顧客へアクセスログ点検・APIキーのローテーションを案内"
  data_sensitivity: "ユーザー名、メール、組織・プロジェクト紐付け、SQLエディタ実行履歴・エラー、サポートチケット、契約条件、暗号化APIキー公開部分"
  public_record_checked_at: "2026-10-23T09:44:16.131+00:00"
sources:
  - id: pingcap
    resource: https://pingcap.co.jp/trust-hub/security/security-update-october-2026/
    title: "不正アクセスによる情報漏洩に関するお詫びとご報告"
    author: "organization:PingCAP株式会社"
  - id: class
    resource: https://classmethod.jp/news/261021-pingcap/
    title: "PingCAP社（TiDB Cloud提供元）の不正アクセスについて"
    author: "organization:クラスメソッド株式会社"
---

# PingCAP / TiDB — 社内認証情報侵害・国内約5万件・SQL履歴とAPI公開鍵部分の流出

## 確認された侵入・情報取得

9月9日〜10月7日（米国時間）、第三者が不正に取得した資格情報を使ってPingCAP**社内システム**にアクセスし、データの複製を取得。10月7日に把握し、盗まれた認証情報の無効化を開始した。日本国内の個人情報は**最大約5万件**。これはアカウント件数・SQL操作数を無条件に同じ人数へ変換できない。[^pingcap]

## 診断上の最重要境界：DBサービス本体は未侵害

会社と外部調査機関は**TiDB Cloudサービス本体への不正アクセスは確認していない**。クレジットカード情報の流出も未確認。一方、社内システムのコピーに含まれた情報は、顧客の環境を推測する材料になり得るため、情報を単なる「名簿」に矮小化しない。[^pingcap]

| 情報 | 外部取得対象になったと会社が説明 | 制限 |
| --- | --- | --- |
| アカウント | ユーザー名、メール、組織・プロジェクト対応関係 | 全顧客で全項目が同時流出したわけではない |
| 操作記録 | **SQLエディタの実行履歴・エラー**、組織・クラスタID | SQL本文に秘密情報が含まれていたかは未確定 |
| 問合せ | **サポートチケット**（10月21日13:05追記） | 各案件の入力内容・機密性は個別照合が必要 |
| 取引 | 連絡先、契約内容、請求・支払条件 | 実決済カード情報の流出は未観測 |
| APIキー | **暗号化したPublic Key部分** | Private Key部分は対象外。公開部分単独でサービスを操作できないと説明 |

## 事後対策と顧客側の判断

不正取得された資格情報は無効化済み。重要キーの更新、権限管理の厳格化、ネットワーク管理の見直し、新しい検知仕組みの導入、法執行機関・監督当局への報告を公表した。顧客に対しても、Cloudと関連アカウントのアクセスログ点検、ロール権限の棚卸し、必要ならAPIキーの更新を要請。販売パートナーのクラスメソッドは自社への侵害を未観測と別途案内した。[^pingcap][^class]

## 既存の公開統制と後続の証拠

外部公開されたTrust Hubやクラウドセキュリティ体制の説明は、事故時点の社内システム資格情報管理が全資産で有効だったという証明ではない。**認証情報の取得元・権限範囲・滞留期間・実コピー**を調査報告で確認する。未確定：取得された資格情報の入手元、全件ユニーク人数、SQL履歴の機微性、二次侵入の有無、最終通知、損害額。

[^pingcap]: PingCAP株式会社「不正アクセスによる情報漏洩に関するお詫びとご報告」. https://pingcap.co.jp/trust-hub/security/security-update-october-2026/
[^class]: クラスメソッド株式会社「PingCAP社（TiDB Cloud提供元）の不正アクセスについて」. https://classmethod.jp/news/261021-pingcap/
