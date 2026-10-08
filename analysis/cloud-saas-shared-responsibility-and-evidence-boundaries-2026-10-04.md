---
type: Analysis Log
title: クラウド・SaaSの共有責任と証拠境界 — 防御責任だけでなく調査可能性を設計する
description: SaaS・クラウドで利用組織と提供者が分担する設定、ID、ログ、検知、対応、データ、復旧の責任と、事故時に利用組織が取得できる証拠の境界を整理する。
tags: [analysis, cloud, saas, shared-responsibility, evidence, logging, incident-response, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T21:40:00+09:00 }
sources:
  - id: cisa-scuba
    resource: https://www.cisa.gov/sites/default/files/2022-12/SCuBA_TRA_RFC_EG_508c.pdf
    title: Secure Cloud Business Applications Technical Reference Architecture
    author: organization:CISA
  - id: cisa-cloud-tra
    resource: https://www.cisa.gov/sites/default/files/publications/CISA%20Cloud%20Security%20Technical%20Reference%20Architecture_Version%201.pdf
    title: Cloud Security Technical Reference Architecture
    author: organization:CISA
  - id: nist-cloud
    resource: https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-146.pdf
    title: Cloud Computing Synopsis and Recommendations
    author: organization:NIST
---

# 目的

「クラウド事業者が安全にする部分」と「利用企業が設定する部分」を分ける共有責任モデルは広く知られている。しかし、事故対応ではもう一つ重要な境界がある。

**事故時に誰が、どのログ・管理履歴・データアクセス証跡を取得できるか。**

SaaSでは、利用組織がサーバーやネットワークを直接管理しないため、提供者が公開する監査ログ・API・管理画面以上の証拠を自力で取得できない場合がある。CISAはSCuBAで、利用組織がクラウド業務アプリの適切な構成や一次対応を担い、提供者は基盤を保護し必要なセキュリティ機能を提供するという共有責任を示している。また可視性・検知・対応も複数主体の共有責任としている。[^cisa-scuba]

本資料は、契約・設定・ログ・事故対応の設計時に、**責任境界と証拠境界を同時に確認する**ための共通枠組みを定義する。

# 共有責任を八つの能力へ分解する

| 能力 | 主な確認事項 |
| --- | --- |
| 基盤保護 | SaaS基盤、ホスト、ネットワーク、基盤パッチ等を誰が保護するか |
| テナント設定 | MFA、外部共有、アクセス制御、保持設定等を誰が設定するか |
| ID・権限 | アカウント発行、SSO、特権、退職者処理、API資格情報を誰が管理するか |
| データ管理 | 何を保存し、どこまで削除・暗号化・分離できるか |
| ログ・可視性 | 誰がどのイベントを生成・取得・保持できるか |
| 検知・対応 | 誰が一次トリアージし、誰が提供者側調査を行うか |
| 復旧 | データ復元、設定復元、代替サービス、エクスポートを誰が担うか |
| 通知・法務 | 顧客、本人、委託元、規制当局への通知を誰が行うか |

「提供者が責任を持つ」と「利用者が何もしなくてよい」は同義ではない。

# 三つの責任状態

各能力について、単純な二者択一ではなく次の三状態で考える。

## 利用組織責任

例:

- 自社ユーザーのアカウントライフサイクル。
- SaaS側で提供されるMFA・SSO・共有設定の有効化。
- 自社が投入するデータの最小化。
- 自社保有ログとの相関分析。

## 提供者責任

例:

- SaaS基盤のホスト・サービス実装。
- テナント境界を成立させる基盤機能。
- 利用者が直接管理できない基盤ログ。
- サービス全体の脆弱性修正。

## 共有責任

例:

- 異常検知。
- ログ・テレメトリーの組み合わせ。
- インシデント調査。
- 設定変更と製品側制御の組み合わせ。
- 大規模事故時の顧客通知。

CISAのSCuBAは、保護統制だけでなく可視性・検知・対応についても利用組織、CISA、提供者の役割を分けている。[^cisa-scuba]

# 証拠境界

事故時に重要なのは、「ログが存在するか」ではなく次である。

```text
生成されるか
    ↓
利用組織が取得できるか
    ↓
事故後も遡れる期間だけ保持されるか
    ↓
提供者障害・契約停止中もアクセスできるか
    ↓
改ざんされにくい場所へ独立保管できるか
```

CISAのCloud Security Technical Reference Architectureは、SaaSのログがAPI、管理画面、エクスポート等を介して提供される一方、テナントは提供者が用意する以上のログを追加取得できない場合があると説明している。またSaaS自身が別クラウド上に構築され、SaaS提供者自身の可視性が制限される場合もある。[^cisa-cloud-tra]

# ログの可視性を四層に分ける

## 1. テナント監査ログ

利用者が比較的取得しやすい。

- ログイン。
- 管理者操作。
- 権限変更。
- 共有設定。
- データエクスポート。
- API利用。

## 2. アプリケーション内部ログ

一部は利用者へ公開されるが、全量ではない場合がある。

- バックエンド処理。
- 内部エラー。
- 内部API。
- データ処理履歴。

## 3. 基盤ログ

通常は提供者しか取得できない。

- ホスト・コンテナ。
- 基盤ネットワーク。
- 管理プレーン内部。
- テナント分離機構。

## 4. 下位クラウド・外部依存ログ

SaaS提供者自身がIaaS/PaaS等へ依存している場合、その下位層の証拠はさらに別主体へ依存する。

この層構造は、原因確定の限界を理解するために重要である。

# 「ログ保持期間」を契約・設計要件にする

侵入から検知まで数か月ある場合、30日しかログが残らなければ侵入初期を再構成できない。

確認する項目:

- 標準プランでの保持期間。
- 上位プランでのみ得られる監査ログがあるか。
- APIで外部SIEM等へ常時エクスポートできるか。
- 契約終了後にログへアクセスできる期間。
- 事故時に提供者へ追加ログを要求できるか。
- 提供者側での保全・法的ホールド手続。

セキュリティ監査ログが高額プランに限定されている場合、その費用は単なる運用機能ではなく**インシデント調査可能性の費用**でもある。

# IDとSaaSの責任境界

SaaS事故で特に重要なのは、提供者基盤の侵害と顧客資格情報の悪用を区別することである。

確認する。

- ローカルアカウントとSSOの併存。
- MFAの強制範囲。
- サービスアカウント・APIキー。
- OAuth・連携アプリ。
- 回復コード・緊急管理者。
- セッション失効。
- 退職者・委託終了者の権限。

顧客資格情報を使った正規ログイン形式の操作では、提供者側から異常と判定しにくいことがある。逆にSaaS基盤側の脆弱性は顧客設定だけでは防げない。

# データ責任境界

「SaaSへ預けたからデータ管理責任も移転した」とは限らない。

利用組織が設計すべきもの:

- そもそも投入する必要のないデータを送らない。
- 高感度データを一般データと分離できるか。
- 契約終了後の削除。
- バックアップ・分析複製を含む削除範囲。
- 顧客単位・用途単位の分離。
- エクスポート権限の最小化。

提供者側に確認するもの:

- テナント分離方式の保証範囲。
- 提供者従業員のアクセス統制。
- サポートアクセスの監査。
- 下請け・サブプロセッサー。
- バックアップ保持・削除。

# 復旧境界

SaaSでは、自社でVMを復元するような復旧ができない場合がある。

確認する。

- 誤削除からどこまで戻せるか。
- 提供者障害時の復旧目標。
- テナント単位の復元が可能か。
- 設定・権限も復元できるか。
- 定期的なデータエクスポートが可能か。
- 他サービスへ移行するための形式・APIがあるか。
- SaaS停止中に最低限の業務を継続できるか。

「高可用なSaaS」と「自社が事故から独立して復旧できる」は別の性質である。

# 契約時に確認すべき事故対応能力

価格・機能比較だけでなく、次を調達要件に含める価値が高い。

1. 事故通知の条件と期限。
2. 取得可能な監査ログ。
3. ログ保持期間。
4. 事故時の追加ログ提供手続。
5. テナント単位の影響切り分け能力。
6. データ削除・復元能力。
7. サブプロセッサー一覧と変更通知。
8. 提供者側インシデント時の連絡経路。
9. 契約終了時のデータ・ログ取得。
10. 規制・本人通知に必要な情報提供。

# 事故調査時の証拠マトリクス

| 質問 | 自社だけで確認 | 提供者協力が必要 | 下位クラウド等も必要 |
| --- | --- | --- | --- |
| 誰がログインしたか | 場合により可能 | 場合により必要 | 通常不要 |
| 誰が大量データを取得したか | SaaS監査ログ次第 | 多くの場合必要 | 場合により必要 |
| テナント境界を越えたか | 通常困難 | 必要 | 場合により必要 |
| SaaS基盤の脆弱性が悪用されたか | 困難 | 必要 | 場合により必要 |
| 下位クラウドで障害・侵害があったか | 困難 | 必要 | 必要 |
| 利用者設定が原因だったか | 多くは可能 | 補助が有用 | 通常不要 |

この表を契約前に考えると、事故後に初めて「そのログは提供されない」と判明するリスクを下げられる。

# 機械可読モデル候補

```yaml
shared_responsibility:
  identity:
    customer: [account_lifecycle, sso_configuration]
    provider: [platform_identity_controls]
    shared: [anomaly_detection]
  logging:
    customer_accessible_events: []
    provider_only_events: []
    retention_days: unknown
    external_export: unknown
  incident_response:
    customer_first_line: unknown
    provider_escalation: unknown
    evidence_request_process: unknown
  recovery:
    tenant_restore: unknown
    export_available: unknown
    alternate_operation: unknown
```

# 依存グラフとの接続

[システム依存・集中リスクのグラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md)では、組織とSaaSの関係を `stores_data_at`、`authenticates_via`、`depends_on_for_operation` 等で表す。

本資料は、その辺についてさらに次を説明する。

- 誰が保護統制を実施するか。
- 誰が証拠を持つか。
- 誰が事故対応を開始できるか。
- 利用者が提供者なしでどこまで復旧・調査できるか。

つまり、依存グラフが「どこへ依存するか」、本資料が「その依存の中で何を誰が担うか」を扱う。

# Snowflake型事例との接続

[Snowflake顧客アカウント侵害](../incidents/international/snowflake-unc5537-2024.md)のように、クラウド/SaaS基盤自体の侵害と、顧客側の認証情報悪用を分けて理解する必要がある事例は、共有責任を検討する比較ケースとして有用である。

重要なのは「クラウドは安全／危険」という二択ではなく、**どの責任・証拠・設定がどちら側にあったか**を個別に確認すること。

# 防御上の指標

- 重要SaaSでMFA/SSOを強制できている割合。
- 重要SaaSの監査ログを外部へ連続取得している割合。
- 潜在侵入期間より長くログを保持できるサービス割合。
- 提供者側事故時の連絡SLAを契約で確認している割合。
- テナント単位でデータエクスポート・復元可能な割合。
- 契約終了時のデータ削除証跡を取得できる割合。
- 提供者なしで最低限の業務を継続できる重要SaaS割合。

# 関連資料

- [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md)
- [システム依存・集中リスクのグラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md)
- [失敗モードと防御統制](control-failure-mode-crosswalk-2026-10-04.md)
- [バックアップ・復元可能性・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md)
- [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md)

[^cisa-scuba]: CISA, “Secure Cloud Business Applications Technical Reference Architecture”, shared responsibility for protective controls and visibility/detection/response. https://www.cisa.gov/sites/default/files/2022-12/SCuBA_TRA_RFC_EG_508c.pdf
[^cisa-cloud-tra]: CISA, “Cloud Security Technical Reference Architecture”, SaaS logging and tenant visibility considerations. https://www.cisa.gov/sites/default/files/publications/CISA%20Cloud%20Security%20Technical%20Reference%20Architecture_Version%201.pdf
