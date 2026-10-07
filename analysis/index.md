# 分析資料

## 全体像

* [Denno Watch 知識基盤マップ](knowledge-base-map-2026-10-04.md) - 個別事例、横断分析、方法論、海外比較ケースを事故の時間軸と目的から辿る入口。
* [ローカルLLM実用化以降の重大インシデント比較](local-llm-era-incident-retrospective-2023-2025-2026-10-05.md) - 2023年7月前後から2025年までの国内26件を、初動、復旧、長期予後、事故前統制、株主・規制資料の軸で比較。
* [事故前に公表されたセキュリティ統制と実侵害のギャップ](pre-incident-control-gap-comparison-2023-2025-2026-10-05.md) - ISO、MFA、EDR、SOC、Zero Trust等の公表・認証と、実際の適用範囲、例外、旧資産、境界機器、資格情報、パッチ、ログ、データ保持等の失敗面を比較。
* [事故前セキュリティ・株主／規制向け資料台帳](pre-incident-security-and-ir-pdf-ledger-2023-2025.md) - 事故前の統合報告・セキュリティ資料、事故調査、株主・財務、規制・第三者認証資料を一つの証拠台帳で対応付ける。
* [AIで攻撃コストが崩れた時代の企業サイバーリスク](executive-ai-amplified-cyber-risk-report-2026-10-04.md) - AIによる攻撃経済性の変化、国内事例、多層防御、防衛判断を統合した経営・実務向け総合レポート。

## 事故発生から復旧・予後まで

* [サイバーインシデントのライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md) - 発生前条件、初期侵入、横展開、被害、検知、封じ込め、根絶、技術復旧、業務復旧、影響確定、通知、長期予後を一つの時間軸で整理。
* [インシデント対応指標と経営判断トリガー](incident-response-metrics-and-decision-triggers-2026-10-04.md) - 最初の60分、重大度、全面停止と部分隔離、復旧開始・完了条件、平時に測る先行指標を整理。
* [バックアップ・復元可能性・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md) - バックアップの存在ではなく、分離、復元試験、復旧点、構成・秘密情報、クリーンな復旧先、業務照合までを復旧能力として評価。
* [再発防止策の実効性と再発追跡](remediation-effectiveness-and-recurrence-tracking-2026-10-04.md) - 対策を予定、実装、試験、独立評価、実運用での効果へ分け、同一組織・共有基盤を長期追跡。
* [インシデント後の長期予後](post-incident-long-tail-prognosis-2026-10-04.md) - 技術復旧後に残る本人保護、規制、契約、訴訟、保険、信用、技術負債、人員負荷を数か月〜数年の時間軸で整理。

## 制度・公表・財務

* [サイバーインシデントの報告・通知・公表マップ](regulatory-reporting-and-disclosure-map-2026-10-04.md) - 個人情報保護、マイナンバー、金融、重要インフラ、共通報告様式、上場会社の市場開示を事故対応の時間軸へ接続。
* [インシデント公表の品質・透明性](incident-disclosure-quality-and-transparency-framework-2026-10-04.md) - 初報速度だけでなく、不確実性、件数単位、訂正、復旧状態、利用者の行動可能性、長期追補まで公表品質を評価。
* [サイバーインシデントの財務・事業影響](incident-financial-and-business-impact-knowledge-base-2026-10-04.md) - 直接対応費、事業中断、顧客支援、法務・規制、保険、再発防止投資等を分離し、会社開示実績と推計を混同せず追跡。
* [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md) - 最新公表日と最終確認日を分離し、活動中事故から長期予後まで情報源を再確認する方法を定義。

## 被害の質・安全

* [データ被害・感度・保持期間の評価](data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md) - 件数だけでなく、変更可能性、悪用可能期間、連結可能性、完全性、回復可能性、保持期間を使って長期リスクを分類。
* [完全性・破壊・不正操作の被害](integrity-and-destructive-impact-knowledge-base-2026-10-04.md) - DB削除、改変、不正送信、設定変更、ログ・復旧基盤破壊など、漏えい件数では測れない被害を独立評価。
* [OT・重要インフラの安全・復旧リスク](ot-critical-infrastructure-safety-and-recovery-2026-10-04.md) - 物理プロセス、安全、遠隔アクセス、制御ロジック、工学バックアップ、縮退運転、相互依存、通常操業までの復旧をIT事故と分けて整理。

## 集中・依存・クラウド・防御統制

* [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md) - 委託先、SaaS、認証情報、共有基盤、データ集中、復旧依存が単一事故を複数組織へ波及させる条件を国内外事例から整理。
* [システム依存・集中リスクのグラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md) - 組織、SaaS、ID、管理面、データ、バックアップ、重要業務をノードと依存関係として記録し、単一点障害と下流波及を比較。
* [クラウド・SaaSの共有責任と証拠境界](cloud-saas-shared-responsibility-and-evidence-boundaries-2026-10-04.md) - 設定・ID・ログ・検知・対応・復旧の責任と、事故時に顧客側が取得できる証拠の限界を分離。
* [失敗モードと防御統制の対応表](control-failure-mode-crosswalk-2026-10-04.md) - 認証、脆弱性、過大権限、共有基盤、ログ、セグメント、バックアップ等の失敗モードを、防御統制へ対応付ける。
* [全業種サイバー侵害・最大被害ストレスマトリクス](sector-worst-case-impact-matrix-2026-10-04.md) - 日本標準産業分類A〜Sを基礎に、情報、金銭、事業継続、安全、社会・サプライチェーンへの最大被害を整理。

## 証拠・根拠・予算

* [デジタル証拠の保全と因果関係の確度](forensic-evidence-preservation-and-causal-confidence-2026-10-04.md) - ログ・端末・クラウド・SaaS等の証拠源、原本性、時刻、保全と、侵入経路・流出・破壊等の結論がどこまで因果を支えるかを整理。
* [2026年 日本の重大サイバーインシデント — 攻撃パターン、現実的対抗策、防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md) - 国内事例を横断し、攻撃・障害パターン、予防・検知・復旧策、想定最大損失、防衛予算の判断材料を整理。
* [AI時代の企業サイバーリスク — 根拠資料台帳](evidence-ledger-ai-cyber-risk-2026-10-04.md) - 総合レポートの主要な主張を一次資料、公的資料、脅威インテリジェンスへ対応付け、観測事実・推論・ストレスシナリオ・不明を分離。

## 比較事例

* [国内インシデントレポート](../incidents/index.md) - 2023〜2026年の国内77件。
* [海外比較インシデント](../incidents/international/index.md) - Change Healthcare、Snowflake顧客アカウント侵害、Caesars Entertainment、MOVEit Transfer等を国内事例集と分離して記録。
