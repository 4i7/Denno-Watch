---
type: Analysis Log
title: システム依存・集中リスクのグラフモデル — 単一障害点と下流波及を関係として記録する
description: 組織、SaaS、共有基盤、認証、管理面、データ保管、バックアップ、重要業務の依存関係をグラフとして記録し、単一点障害、制御集中、データ集中、復旧依存を比較するためのモデル。
tags: [analysis, dependency-graph, concentration-risk, third-party, supply-chain, resilience, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T21:20:00+09:00 }
sources:
  - id: kddi-final
    resource: https://newsroom.kddi.com/news/assets/2026/kddi_nr_s-73_4619/kddi_nr_s-73_4619_pdf_01.pdf
    title: ISP事業者向けメールシステムに対する不正アクセスについてのお詫びとご報告
    author: organization:KDDI株式会社
  - id: applynow-primary
    resource: https://applynow.co.jp/news/20260909
    title: 採用管理プラットフォームへの不正アクセスに関するお知らせ
    author: organization:株式会社ApplyNow
  - id: tokorozawa
    resource: https://www.city.tokorozawa.saitama.jp/tokoronews/press/r8/9gatu/kojinjyohou.html
    title: 職員採用試験動画投稿型面接システム事業者における個人情報の漏えいについて
    author: organization:所沢市
  - id: nist-csf
    resource: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1299.pdf
    title: NIST Cybersecurity Framework 2.0 Resource & Overview Guide
    author: organization:NIST
---

# 目的

第三者リスクを「ベンダー一覧」だけで管理すると、同じ提供事業者でも何に依存しているかが見えない。

たとえば一社のSaaSに依存していても、単なる社内掲示板なら停止影響は小さいかもしれない。一方、同じ提供事業者へ認証、管理、データ保管、バックアップ、顧客通知まで集中していれば、一つの侵害が複数の防御・復旧機能を同時に失わせる。

本資料は、**誰が誰へ依存しているかではなく、何の能力を何へ依存しているか**をグラフとして記録するための共通モデルを定義する。

# 基本モデル

```text
[組織]
  │
  ├─ authenticates_via ─→ [ID基盤]
  ├─ stores_data_at ────→ [SaaS / クラウド]
  ├─ administered_by ───→ [MSP / 管理サービス]
  ├─ backs_up_to ───────→ [バックアップ基盤]
  ├─ depends_on_for_operation → [通信 / 決済 / 物流 / BPO]
  └─ notifies_through ──→ [メール / SMS / 顧客ポータル]
```

事故時に重要なのは、複数の辺が同じノードへ集中しているかである。

# ノード種別

| ノード | 意味 |
| --- | --- |
| `organization` | 被害組織、顧客組織、委託元等 |
| `service` | 顧客向け・社内向けサービス |
| `saas` | SaaS・業務プラットフォーム |
| `cloud` | クラウド基盤・ホスティング |
| `identity_provider` | 認証・SSO・ディレクトリ |
| `control_plane` | 管理コンソール、管理API等 |
| `data_store` | DB、オブジェクトストレージ等 |
| `analytics_platform` | BI・分析・データ集約環境 |
| `backup_platform` | バックアップ・復旧基盤 |
| `msp_bpo` | MSP、BPO、運用委託先 |
| `communications_provider` | ISP、メール、SMS等 |
| `payment_provider` | 決済・請求・与信 |
| `logistics_provider` | 物流・配送 |
| `critical_process` | 組織が継続すべき重要業務 |
| `physical_infrastructure` | OT・設備・重要インフラ |

同一企業が複数種別を提供する場合でも、機能上のノードは分離する。企業名だけを一つの巨大ノードにすると、どの能力が集中していたのか分からないためである。

# エッジ種別

| エッジ | 意味 |
| --- | --- |
| `authenticates_via` | 認証を依存する |
| `administered_by` | 管理権限・運用を依存する |
| `stores_data_at` | データを保存する |
| `processes_data_at` | データ処理を依存する |
| `connects_through` | 通信・接続を依存する |
| `backs_up_to` | 復旧データを依存する |
| `depends_on_for_operation` | 重要業務の継続を依存する |
| `notifies_through` | 顧客・本人への通知を依存する |
| `receives_from` | 下流データ・業務を受ける |
| `supplies_to` | 他組織・業務へ供給する |
| `shares_control_plane_with` | 管理面を共有する |
| `shares_data_plane_with` | データ処理基盤を共有する |
| `failover_to` | 代替・切替先がある |

「契約している」という関係だけでは、実際の被害範囲を説明できない。可能な限り能力単位の辺へ分解する。

# エッジ属性

```yaml
edge:
  relation: stores_data_at
  criticality: high
  failover: none_confirmed
  tenant_isolation: unknown
  shared_credentials: unknown
  data_sensitivity: employment
  recovery_dependency: high
  source_id: applynow-primary
```

主な属性:

- `criticality`: その依存が停止・侵害した場合の業務重要度。
- `failover`: 公表済みの代替経路があるか。
- `tenant_isolation`: 顧客・組織単位の分離が確認できるか。
- `shared_credentials`: 共通資格情報・管理権限の共有が確認されるか。
- `data_sensitivity`: 認証、本人確認、雇用、金融等。
- `recovery_dependency`: 復旧にも同じ提供者が必要か。
- `source_id`: 関係を裏付ける公開資料。

公開情報で分からない属性を `false` にしてはならず、`unknown` とする。

# 集中リスクを五つへ分ける

## 1. 認証集中

一つのIdP・ディレクトリが多数サービスの認証を担う。

利点:

- 統一したMFA・失効・監査。

リスク:

- IdP侵害・停止が多数サービスへ同時波及。
- 復旧用管理アカウントまで同じIdPに依存すると、復旧能力も失う。

## 2. 制御面集中

一つの管理コンソール・API・MSPから複数顧客や複数システムを操作できる。

見るべき点:

- 一つの管理者で到達できるテナント数。
- 顧客ごとの権限・鍵分離。
- 管理操作ログ。
- 緊急失効能力。

## 3. データ集中

分析基盤、DWH、採用SaaS、顧客管理等へ複数組織・長期間のデータが集まる。

データ量だけでなく、次を確認する。

- 保持期間。
- 顧客横断性。
- 高感度データの混在。
- 本番から分析環境への複製。
- 契約終了後の削除状態。

## 4. 業務集中

一つの通信・決済・物流・BPO等が止まると、多数の組織が同時に業務停止する。

ここでは情報漏えいがなくても、可用性だけで大きな下流影響が生じる。

## 5. 復旧集中

平時サービスと復旧手段が同じ基盤へ依存する。

例:

- 本番とバックアップが同じ管理アカウント。
- 事故連絡網が侵害されたメール基盤だけに存在。
- 緊急管理アカウントが停止したIdPでしか認証できない。
- SaaS停止時にデータエクスポート手段も同じSaaS内にしかない。

これは通常のベンダー台帳では見落としやすい。

# 国内例1: KDDIの共有ISPメール基盤

KDDIは6社のISP向けに共通メール基盤を提供しており、第三者製ソフトウェアの当時ベンダー未認知だった脆弱性が悪用された結果、複数ISPへ同時に影響した。最終公表ではメールアドレス12,231,954名分、その内数としてパスワード7,616,173名分の漏えいが確認された。[^kddi-final]

グラフとしては、各ISPブランドを個別ノードにした上で、共通メール基盤へ `depends_on_for_operation`、`stores_data_at` 又は `authenticates_via` に相当する関係を、公開範囲で記録する。

```text
[ISP A] ─┐
[ISP B] ─┤
[ISP C] ─┼──→ [KDDI shared mail platform]
[ISP D] ─┤
[ISP E] ─┤
[ISP F] ─┘
```

事故件数の大きさだけでなく、**一つの共有基盤が六つの提供主体へ波及した構造**が再利用可能な知見になる。

# 国内例2: ApplyNowの分析環境

ApplyNowでは、採用管理基盤で利用していたデータ分析ツールへの不正アクセスが、複数顧客の採用・雇用関連データへ波及した。所沢市は2022〜2025年度の受験者1,701件について漏えいを公表し、動画データは別保管領域で対象外だった。[^applynow-primary][^tokorozawa]

ここでは次の二つを同時に表現できる。

1. 複数顧客 → 同じSaaS/分析環境への集中。
2. 動画・画像の別領域 → 被害範囲を抑えた分離境界。

```text
[顧客A] ─┐
[顧客B] ─┼─ stores_data_at → [ApplyNow analytics environment]
[顧客C] ─┘

[video/media data] ─ stores_data_at → [separate storage]
```

「同じベンダーを使っていた」だけでなく、**どのデータ面が共有され、どこが分離されていたか**を記録できる。

# 被害範囲の指標候補

単一のリスク点数へ畳み込まず、次を個別指標として持つ。

## 到達組織数

一つのノード又は制御面の侵害から、直接到達可能な組織・テナント数。

## 重要業務到達数

依存先停止で止まる重要業務数。

## 高感度データ集中度

一つのデータ面へ集約されるデータ種別・保持期間・顧客数。

## 制御面集中度

一つの管理資格情報・コンソールで操作できるサービス・顧客範囲。

## 復旧依存度

事故時の復旧、通知、バックアップ、管理アクセスが同じ障害ノードへ依存する割合。

## 代替経路率

重要な依存に対し、実際に利用可能な代替経路が確認されている割合。

公開事例の比較では、値が非公表なら無理に算出しない。

# 「単一障害点」を二種類に分ける

## 技術的単一障害点

一つのシステム・基盤停止が直接サービス停止を起こす。

## 組織的単一障害点

技術基盤は分散していても、一つの運用会社・管理チーム・契約・認証・知識へ依存するため復旧できない。

クラウドのリージョン冗長化があっても、管理アカウントを一つしか持たなければ組織的単一障害点が残る。

# グラフに含めないもの

公開ナレッジベースで内部ネットワーク構成を詳細に再現する必要はない。

含めない:

- 未公表の内部IP・ホスト名。
- 防火壁ルールの詳細。
- 有効なアカウント名・秘密情報。
- 攻撃者が再現に利用できる内部経路。

必要なのは「どの能力がどこへ依存するか」という抽象化された関係である。

# 機械可読モデル例

```yaml
nodes:
  - id: provider-mail-platform
    type: communications_provider
    label: Shared ISP mail platform
  - id: isp-a
    type: organization
    label: ISP A

edges:
  - from: isp-a
    to: provider-mail-platform
    relation: depends_on_for_operation
    criticality: high
    failover: unknown
    evidence_state: confirmed
    source_id: primary-report
```

実際のレコードでは、公開された固有名詞を使ってよい。ここではモデル説明のため一般化している。

# インシデント後にグラフを更新する

事故後は、依存関係そのものが変わる場合がある。

- 代替サービス追加。
- テナント分離。
- バックアップの別管理面化。
- ID基盤の分離。
- 委託終了・内製化。
- 通知経路の冗長化。

再発防止策を文章で保存するだけでなく、グラフの辺がどう変化したかを比較すると、**集中リスクが本当に減ったか**を追跡しやすい。

# 調査時の質問

- この事故で実際に止まった／漏れた主体は誰か。
- それらはどの共通サービスへ依存していたか。
- 共通なのはデータ面、制御面、認証面、業務面のどれか。
- 一つの資格情報で複数顧客へ到達できた証拠があるか。
- 顧客ごとに分離されていた領域は何か。
- 代替経路は存在したか、実際に使われたか。
- 復旧も同じ提供者・認証・管理面へ依存していなかったか。
- 事故後に依存関係が変更されたか。

# 既存資料との接続

- [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md): 集中リスクの意味と国内外事例。
- [失敗モードと防御統制](control-failure-mode-crosswalk-2026-10-04.md): 集中を抑える統制。
- [バックアップ・復元可能性・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md): 復旧依存と管理分離。
- [データ被害・感度・保持期間](data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md): データ集中の質。
- [OT・重要インフラの安全・復旧リスク](ot-critical-infrastructure-safety-and-recovery-2026-10-04.md): デジタル依存だけでなく物理供給依存。

# 今後の発展

1. 国内42件から、公開情報で確認できる依存関係だけを抽出する。
2. サービス名ではなく、認証・データ・管理・業務・復旧のどの辺かを分類する。
3. KDDI、ApplyNow、両毛システムズ、日本テレネット、メディア4u等から小規模な実例グラフを作る。
4. 海外比較ケースから、Change Healthcareのような大規模下流依存を追加する。
5. 2027年以降、事故後の分離・代替追加でグラフがどう変わったか追跡する。

[^kddi-final]: KDDI株式会社「ISP事業者向けメールシステムに対する不正アクセスについてのお詫びとご報告」2026年7月（7月21日訂正）.
[^applynow-primary]: 株式会社ApplyNow「採用管理プラットフォームへの不正アクセスに関するお知らせ」2026-09-09.
[^tokorozawa]: 所沢市「職員採用試験動画投稿型面接システム事業者における個人情報の漏えいについて」2026-09-19.
