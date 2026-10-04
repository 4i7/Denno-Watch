---
type: Reference
title: Denno Watch インシデント記録基準
description: 公開インシデント記録の証拠評価、出典管理、ライフサイクル、各フィールドの意味を定義する。
tags: [methodology, incident-response, provenance, okf]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T06:23:00+09:00 }
sources:
  - id: okf-v02
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format v0.2 specification, pinned revision ad30107c
    author: team:GoogleCloudPlatform
---

# 目的

Denno Watch は、日本の組織に影響する重大なサイバーインシデントについて、公開根拠から確認できる事実を記録する。後の防御に利用できるよう、何が起きたか、何が影響を受けたか、対応と復旧がどう進んだか、何が不明のまま残ったか、公開事実からどのような防御上の教訓を得られるかを整理する。

ナレッジベースは OKF v0.2 に従う。各概念文書は YAML フロントマター付き Markdown とし、出典情報を `sources` に保持する。個別の主張は対応する脚注 ID で根拠へ結び付ける。機械生成と独立検証は別の状態として扱う。[^okf-v02]

上流の OKF v0.2 は同じ版番号を維持したまま本文が更新されているため、ルートの `index.md` には `okf_version` に加え、Denno Watch が参照した正確な `okf_spec_revision` と `okf_spec_resource` を記録する。これらは生成側が追加するメタデータであり、標準の `okf_version` を置き換えるものではない。

# 収録基準

公開根拠から、少なくとも次のいずれかが確認できる事例を収録対象とする。

- 事業または顧客向けサービスに重大な停止・制限が生じた。
- 大規模、機微、または認証に関わる情報の流出・取得・曝露が確認された、または否定できない。
- データ・設定・正規機能・復旧基盤等の完全性に重大な侵害が生じた。
- 顧客、委託先、インフラ、複数組織へ意味のある波及が生じた。
- 物理プロセス、安全、重要供給へ意味のある影響が生じた。
- 被害組織の公表が十分に具体的で、他組織でも再利用できる防御上の教訓が得られる。

収録は深刻度ランキングではない。Denno Watch は企業へ点数を付けず、公表されていない事業損失、侵入経路、欠落統制を推定値として断定しない。

# 根拠資料の優先順位

利用可能な場合は、原則として次の順で根拠を優先する。

1. 被害組織、親会社・子会社、または当該サービスを直接運営する事業者。
2. 規制当局、捜査機関、その他の権限ある公的機関。
3. 直接影響を受けた取引先・顧客組織。
4. 独立して観測可能な事実を追加する、信頼性の高い二次報道・研究。

二次報道を、後から公表された一次情報による訂正より優先してはならない。匿名の攻撃者主張、リークサイト上の主張、SNS投稿は、独立した裏付けがある場合、または「その主張・掲載自体が存在した」ことを記録する場合に限って扱う。

情報源の再確認、更新検知、置換・撤回、長期追跡は [情報源の監視・鮮度・再確認基準](source-monitoring-and-freshness-standard.md) に従う。

# 事実状態

「証拠が見つからない」ことを「発生していない」と読み替えない。

| 状態 | 意味 |
| --- | --- |
| `confirmed` | 引用した根拠が明示的に事実として確認している。 |
| `possible` | 根拠が、影響・流出等を否定できない、または発生した可能性があるとしている。 |
| `not_observed` | 調査で該当事象を示す証拠が確認されなかった。発生しなかったことの証明ではない。 |
| `not_publicly_disclosed` | 組織が詳細を公表していない、または非公表としている。 |
| `unknown` | 公開根拠だけでは判断できない。 |
| `not_applicable` | 当該フィールドがその事例には適用されない。 |

# 標準インシデントメタデータ

各インシデントは `type: Cybersecurity Incident` と、Denno Watch が追加する `incident` マッピングを用いる。公開記録を正確に表現するために必要であればフィールドを追加できる。

| フィールド | 意味 |
| --- | --- |
| `organization` | 主な被害組織。 |
| `sector` | 大まかな業種。 |
| `jurisdiction` | 主な法域。本事例集では現在 `JP`。 |
| `incident_status` | `investigating`、`recovering`、`monitoring`、`public_report_closed` など、公表上のライフサイクル状態。 |
| `attack_type` | 公開根拠で確認された攻撃・事故類型。症状だけから推定しない。 |
| `earliest_known_activity` | 公開調査が本件と結び付けた最も早い活動時点。 |
| `detected_at` | 公表されている場合の検知日時。 |
| `first_disclosed_at` | 最初の公表日。 |
| `latest_public_update` | 記録へ反映した最新の一次公表日。再確認日ではない。 |
| `public_record_checked_at` | より新しい公表がないか最後に能動確認した時刻。UTC オフセット付き ISO 8601 を用いる。 |
| `intrusion_vector` | 確認済みの侵入経路、または明示的な不明・非公表状態。 |
| `affected_services` | 影響を受けたと公表された重要システム・サービス。 |
| `data_exposure` | `confirmed`、`possible`、`not_observed`、`unknown`、またはこの区別を保つさらに精密な状態。 |
| `availability_impact` | 業務・サービス停止の有無と内容。 |
| `restoration_state` | 最新の公開情報から確認できる復旧状態。封じ込め、サービス復旧、調査完了を分離する。 |
| `secondary_abuse` | 本件後に公表された二次悪用。 |
| `downstream_impact` | 主被害組織を越えて、顧客、委託元、取引先、データ所有者等へ生じた観測可能な影響。 |
| `regulatory_response` | 規制当局、警察等への報告、調査、連携など公表された対応。 |
| `notification_state` | 影響対象の特定・通知が継続中か、完了したか、または非公表か。 |
| `business_continuity` | 影響システムを制限している間も業務継続に寄与した代替経路、手作業、非影響サービス等。 |
| `data_sensitivity` | 認証情報、本人確認書類、雇用、健康、金融など、防御上の重要性を左右するデータの性質。 |

末尾6項目は、公開記録に根拠がある場合に使う Denno Watch 独自の追加メタデータである。主な影響フィールドとは分離し、「サービス提供事業者の侵害」と「顧客側のデータ影響」、「サービス復旧」と「代替経路による業務継続」などを区別する。

`incident` 内の日付は公表された精度をそのまま使い、時刻が公表されていない場合は作らない。`public_record_checked_at`、`generated.at`、`verified[].at`、`stale_after` などの時刻値は、UTC オフセット付き ISO 8601 を使う。[^okf-v02]

後日の確認で新しい公表がなかっただけなら、`latest_public_update` を更新してはならない。その確認日時は `public_record_checked_at` に記録する。

# 条件付きで追加する横断メタデータ

以下はすべての事例で必須ではない。既存レコードへ空欄を機械的に追加せず、公開根拠があり、横断比較へ意味がある場合だけ追加する。

## 報告・通知・公表

詳細は [サイバーインシデントの報告・通知・公表マップ](../analysis/regulatory-reporting-and-disclosure-map-2026-10-04.md) に従う。

| フィールド | 意味 |
| --- | --- |
| `incident_known_at` | 組織が報告対象となり得る事故として認識した日時・日付。検知時刻と同一とは限らない。 |
| `regulatory_initial_reported_at` | 公表資料で確認できる速報・初回報告日。 |
| `regulatory_final_reported_at` | 公表資料で確認できる確報・最終報告日。 |
| `regulatory_channels` | 公表された報告先。個人情報保護委員会、所管省庁、監督当局等。 |
| `law_enforcement_contact` | 警察等への相談・届出・連携。 |
| `market_disclosure` | TDnet等の市場向け開示。 |
| `contractual_notifications` | 委託元、顧客、取引先等への契約上又は業務上の通知。 |
| `notification_started_at` | 本人・顧客等への通知開始。 |
| `notification_completed_at` | 通知完了が明示された場合のみ。 |
| `disclosure_corrections` | 件数、影響、原因等の重要な訂正履歴。 |

報告先が公表されていない場合、報告していないと推定しない。

## 公表品質

詳細は [インシデント公表の品質・透明性](../analysis/incident-disclosure-quality-and-transparency-framework-2026-10-04.md) を参照する。

```yaml
disclosure_quality:
  initial_disclosure_at: null
  next_update_commitment: unknown
  uncertainty_explicit: unknown
  count_units_clear: unknown
  restoration_distinguished: unknown
  correction_history_preserved: unknown
  user_actions_provided: unknown
  regulatory_channels_disclosed: unknown
  market_disclosure_present: unknown
  long_tail_updates_present: unknown
```

数値ランキングへ機械的に合算しない。適用しない項目は `not_applicable` とする。

## データ被害プロファイル

高感度又は長期悪用可能なデータを含む場合は、[データ被害・感度・保持期間の評価](../analysis/data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md) を用いる。

```yaml
data_harm_profile:
  data_classes: []
  revocability: unknown
  expected_value_lifetime: unknown
  linkability: unknown
  integrity_impact: unknown
  retention_amplifier: unknown
  secondary_abuse: unknown
```

これは法的評価や数値スコアではない。

## 完全性・破壊・正規機能の悪用

削除、改変、不正送信、設定変更、ログ・復旧基盤破壊等が重要な場合は、[完全性・破壊・不正操作の被害](../analysis/integrity-and-destructive-impact-knowledge-base-2026-10-04.md) に従う。

```yaml
integrity_impact:
  status: unknown
  destructive_actions: []
  unauthorized_modifications: []
  trusted_channel_abuse: []
  evidence_destruction: unknown
  recovery_assets_targeted: unknown
  last_known_good_state: null
  restoration_completed_at: null
  reconciliation_completed_at: null
```

データ削除の確認だけから外部持ち出しを確定してはならない。逆に漏えいが確認されていなくても、完全性被害は独立して成立する。

## バックアップ・復元可能性

バックアップや再構築が復旧上重要な場合は、[バックアップ・復元可能性・クリーン復旧](../analysis/backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md) を用いる。

```yaml
recoverability:
  backup_available: unknown
  backup_isolation: unknown
  immutable_or_delete_protected: unknown
  restore_tested_before_incident: unknown
  recovery_point: null
  estimated_data_loss_window: unknown
  clean_environment_used: unknown
  configuration_rebuilt: unknown
  credentials_rotated: unknown
  business_reconciliation_completed_at: null
  measured_rto: null
  measured_rpo: null
```

「バックアップあり」を「安全に復旧可能」と読み替えない。

## 財務・事業影響

会社が事故関連費用・業績影響・保険等を開示している場合は、[サイバーインシデントの財務・事業影響](../analysis/incident-financial-and-business-impact-knowledge-base-2026-10-04.md) に従う。

```yaml
financial_impact:
  status: unknown
  currency: null
  direct_response_costs: []
  business_interruption: []
  customer_support: []
  legal_regulatory: []
  remediation_investment: []
  insurance_recoveries: []
  contingent_losses: []
  latest_financial_update: null
```

実績、会社見積、外部推計、保険控除前後を混同しない。会社が金額を公表していない場合、独自推計で埋めない。

## 統制に関する証拠

事故前後の統制が組織自身の公表等から確認できる場合は、[失敗モードと防御統制の対応表](../analysis/control-failure-mode-crosswalk-2026-10-04.md) に従う。

```yaml
control_evidence:
  confirmed_existing: []
  confirmed_gap: []
  post_incident_changes: []
  defensive_inference: []
```

事故が起きたことだけから「MFAがなかった」「EDRがなかった」等を `confirmed_gap` へ入れてはならない。

## 依存・集中関係

複数組織・複数サービスへの波及、共有基盤、認証・管理・データ・復旧集中が重要な場合は、[システム依存・集中リスクのグラフモデル](../analysis/systemic-dependency-and-concentration-graph-model-2026-10-04.md) を使う。

```yaml
dependency_evidence:
  nodes: []
  edges: []
```

公開情報で確認できる能力単位の依存だけを記録し、未公表の内部ネットワークやアクセス経路を推定しない。

## OT・重要インフラ

物理プロセス、制御系、安全又は重要インフラの操業へ意味のある影響が確認される場合は、[OT・重要インフラの安全・復旧リスク](../analysis/ot-critical-infrastructure-safety-and-recovery-2026-10-04.md) を用いる。

```yaml
ot_impact:
  physical_process_affected: unknown
  safety_impact: unknown
  control_integrity: unknown
  remote_access_involved: unknown
  manual_operation_available: unknown
  degraded_operation_used: unknown
  engineering_backups_available: unknown
  safety_validation_completed_at: null
  normal_operations_restored_at: null
  cross_infrastructure_dependency: []
```

鉄道、物流、医薬、データセンター等の社会的重要性だけを理由に、制御系が侵害されたと推定してはならない。

# 必須レポート構成

各レポートは原則として次を含む。

1. **概要** - インシデントを正確に把握できる最小限の要約。
2. **公開情報で確認できる時系列** - 活動、検知、公表、対応、復旧、後続調査を時系列で記録する。
3. **影響** - 可用性、機密性、完全性、顧客・従業員・取引先、下流への影響。
4. **技術的に確認できた事項** - アクセス、マルウェア、認証情報、インフラ、侵入経路について公開根拠で確認できる範囲だけを記載する。
5. **対応と復旧** - 封じ込め、調査、通知、再構築、再発防止策。
6. **現在の状況と予後** - 推測による将来予測ではなく、最新の運用・調査状態。
7. **防御上の教訓** - 公開事実から直接支えられる範囲に限定した教訓。
8. **不明点・未公表事項** - 公表されていない重要事項を明示し、沈黙を確定事実と誤読させない。

次は条件付きで独立節を追加する。

- **報告・通知・公表** - 複数の規制・契約・市場開示経路が重要な場合。
- **公表品質** - 初報、訂正、利用者行動、長期追補の構造が重要な場合。
- **データ被害の性質** - 本人確認、認証、医療、金融、長期保持等が重要な場合。
- **完全性・破壊** - 削除、改変、不正操作、正規機能の悪用がある場合。
- **復元可能性** - バックアップ、再構築、クリーン復旧が事故結果を左右した場合。
- **財務・事業影響** - 会社が業績・費用・保険等を開示した場合。
- **依存関係** - 共有基盤・第三者・認証等から複数組織へ波及した場合。
- **安全・操業** - OT、重要インフラ、物理プロセスへ影響する場合。
- **事故前後の統制** - 事故前の統制又は事故後の具体的対策が一次資料から確認できる場合。

# 件数と訂正

情報源が用いた単位を保持する。人数、アカウント数、レコード数、店舗数、システム数、世帯数、ファイル数などを勝手に変換しない。情報源が明示しない限り、レコード数をユニーク人数として表現してはならない。

重要な件数は、次のように証拠状態も保持する。

- **最大値／影響可能性のある対象数**: 流出・影響した可能性のある上限または母集団。
- **確認済みの流出・取得数**: アクセス、取得、流出が確認された数。
- **通知対象数**: 連絡・通知した人数またはアカウント数。確認済み流出数とは一致しない場合がある。
- **ユニーク人数**: 情報源が重複排除を明示した場合だけ使用する。
- **レコード／アカウント／項目数**: 根拠なく人数へ変換しない。

組織が件数を訂正した場合、訂正後の値を現在値とし、訂正前の値も「当時の公表値」として時系列に残す。重複する可能性のある母集団は、互いに排他的であることが根拠から確認できない限り合算しない。

# 復旧状態の定義

復旧を単一の真偽値へまとめない。公開根拠がある場合は、次の節目を分けて記録する。

1. **封じ込め** - 不正アクセス・通信を遮断した、または影響資産を隔離した。
2. **サービス復旧** - 利用者が再びサービスを利用できる。
3. **安全な運用状態への復旧** - 一時的な安全設定・制限を解除できる状態へ戻った。
4. **データ・業務整合性の確認** - 復元後のデータ、取引、外部連携が正しいことを必要な範囲で確認した。
5. **データ影響範囲の確定** - 公表に必要な程度まで流出・取得範囲が判明した。
6. **調査完了** - 組織が調査または公表上の対応完了を明示した。
7. **長期的な再発防止** - 中長期対策が「予定」ではなく実施済みになった。
8. **サービス廃止** - 影響サービスを復旧せず、恒久終了または別サービスへ置換した。

サービスが稼働していてもインシデント全体は `investigating` のままの場合がある。OT・重要インフラでは、サービスや通信の再開と、制御系・安全確認・通常操業の復旧を分離する。

# 鮮度とレビュー

機械生成レポートには `generated` を付け、独立確認されるまで `status: draft` を維持する。同じ生成主体が情報源を再読しただけで `verified` を追加してはならない。OKF の `verified` は生成とは別の実際の確認事象を表す。[^okf-v02]

進行中の事例は `stale_after` を使い、再確認が必要な時期を機械的に判定できるようにする。終結・成熟したレポートでは省略してよいが、`latest_public_update` は保持し、能動的な後続確認を行った場合は `public_record_checked_at` も記録することが望ましい。

後続確認で新しい一次公表がなかった場合は次のように扱う。

- 時系列へ架空の新規イベントを追加しない。
- `public_record_checked_at` を更新する。
- `latest_public_update` は変更しない。
- 継続監視に意味がある場合だけ `stale_after` を先へ進める。
- 「新情報なし」という確認自体が現在状態の理解に重要な場合だけ、本文にも記録する。

再確認の優先順位、情報源の状態、長期追跡、差分更新の条件は [情報源の監視・鮮度・再確認基準](source-monitoring-and-freshness-standard.md) を参照する。

# 言語・専門用語の基準

人が読む本文、見出し、表の説明、索引、更新履歴は**日本語を既定**とする。英単語を混在させるのは、一般的な AI・IT・サイバーセキュリティ分野でその表記自体が定着している場合、固有名詞、規格名、製品名、または原文の正式名称を保持する必要がある場合に限る。

次は原則として英字表記を許容する例である: `AI`、`LLM`、`API`、`GPU`、`SaaS`、`VPN`、`MFA`、`FIDO2`、`EDR`、`SOC`、`SIEM`、`WAF`、`DNS`、`HTTP`、`CVE`、`CVSS`、`KPI`、`GitHub`、`MITRE ATT&CK`。

一方、`account`、`record`、`incident corpus`、`risk`、`provider`、`recovery`、`identity document`、`blast radius`、`control-plane abuse`、`standing privilege` など、日本語で意味を失わず表現できる一般語・内部用語は、本文中でそのまま英語にしない。「アカウント」「レコード」「インシデント事例集」「リスク」「提供事業者」「復旧」「本人確認書類」「被害範囲」「制御プレーンの悪用」「常設権限」など、読者が自然に理解できる日本語へ直す。

機械可読性を保つため、YAML のフィールド名、列挙値、ファイル名、URL、コード識別子は翻訳しない。出典の正式な英語タイトルも原題を保持してよい。新しい略語・造語・本資料だけで通じる内部用語を導入する場合は避けることを優先し、必要不可欠なら初出時に日本語で定義する。

# 安全性と公開範囲

本事例集は防御目的かつ公開情報のみを対象とする。公表済みの侵入経路や統制上の失敗は記録できるが、未公表の攻撃手順、シークレット、認証情報、個人情報の実例、その他悪用を容易にするだけの運用詳細を追加しない。

# 関連資料

- [情報源の監視・鮮度・再確認基準](source-monitoring-and-freshness-standard.md)
- [海外比較ケース記録基準](international-comparative-case-standard.md)
- [サイバーインシデントの報告・通知・公表マップ](../analysis/regulatory-reporting-and-disclosure-map-2026-10-04.md)
- [インシデント公表の品質・透明性](../analysis/incident-disclosure-quality-and-transparency-framework-2026-10-04.md)
- [データ被害・感度・保持期間の評価](../analysis/data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md)
- [完全性・破壊・不正操作の被害](../analysis/integrity-and-destructive-impact-knowledge-base-2026-10-04.md)
- [バックアップ・復元可能性・クリーン復旧](../analysis/backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md)
- [サイバーインシデントの財務・事業影響](../analysis/incident-financial-and-business-impact-knowledge-base-2026-10-04.md)
- [システム依存・集中リスクのグラフモデル](../analysis/systemic-dependency-and-concentration-graph-model-2026-10-04.md)
- [失敗モードと防御統制の対応表](../analysis/control-failure-mode-crosswalk-2026-10-04.md)
- [OT・重要インフラの安全・復旧リスク](../analysis/ot-critical-infrastructure-safety-and-recovery-2026-10-04.md)

[^okf-v02]: Open Knowledge Format v0.2 specification. Denno Watch では本ナレッジベースの参照版を `ad30107c31c06aec8a7d5636e0d1058118604e6f` に固定している。