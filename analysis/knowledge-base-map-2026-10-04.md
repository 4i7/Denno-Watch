---
type: Analysis
title: Denno Watch 知識基盤マップ — 事故発生から長期予後まで何をどこで調べるか
description: 個別インシデント、横断分析、方法論、海外比較ケースを、事故の時間軸と調査目的から辿るための案内。
tags: [analysis, knowledge-map, incident-response, resilience, evidence, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T14:22:00+09:00 }
---

# 目的

Denno Watchは、国内個別事例、海外比較ケース、AI時代の脅威、防衛予算、業種別最大被害、制度、復旧、財務、完全性、OT、安全、依存関係、クラウド共有責任、デジタル証拠を分離して記録する。

本資料は、事故を**発生前条件 → 初期侵入 → 拡大 → 被害 → 検知 → 封じ込め → 根絶 → 技術復旧 → 業務復旧 → 安全確認 → 影響範囲確定 → 報告・通知・公表 → 財務・長期予後 → 再発防止 → 再確認 → 再発追跡**まで辿るための入口である。

# 知りたいことから辿る

| 知りたいこと | 主資料 | 補助資料 |
| --- | --- | --- |
| 2023〜2026年に日本で何が起きたか | [国内インシデント事例集](../incidents/index.md) | [インシデント記録基準](../methodology/reporting-standard.md) |
| ローカルLLMが現実的になった時代から何が変わったか | [ローカルLLM実用化以降の重大インシデント比較](local-llm-era-incident-retrospective-2023-2025-2026-10-05.md) | [対象期間と評価基準](../methodology/local-llm-era-corpus-scope-2026-10-05.md) |
| 事故前に対策を公表していた企業で何が破られたか | [事故前統制と実侵害のギャップ](pre-incident-control-gap-comparison-2023-2025-2026-10-05.md) | [事故前セキュリティ・株主／規制向け資料台帳](pre-incident-security-and-ir-pdf-ledger-2023-2025.md) |
| 事故を発生から予後までどう分解するか | [ライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md) | [インシデント記録基準](../methodology/reporting-standard.md) |
| その結論をどの証拠が支えているか | [デジタル証拠の保全と因果関係の確度](forensic-evidence-preservation-and-causal-confidence-2026-10-04.md) | [証拠資料台帳](pre-incident-security-and-ir-pdf-ledger-2023-2025.md) |
| 最初の数十分〜数時間で何を測り、何を止めるか | [対応指標と経営判断トリガー](incident-response-metrics-and-decision-triggers-2026-10-04.md) | [失敗モードと防御統制](control-failure-mode-crosswalk-2026-10-04.md) |
| 委託先・SaaS・認証情報がどう被害を増幅するか | [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md) | [依存・集中グラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md) |
| SaaS事故で誰が何を守り、誰が証拠を持つか | [クラウド・SaaSの共有責任と証拠境界](cloud-saas-shared-responsibility-and-evidence-boundaries-2026-10-04.md) | [依存・集中グラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md) |
| どの失敗モードをどの統制で下げるか | [失敗モードと防御統制](control-failure-mode-crosswalk-2026-10-04.md) | [防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md) |
| 件数以外にデータ被害の深刻さをどう見るか | [データ被害・感度・保持期間](data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md) | [長期予後](post-incident-long-tail-prognosis-2026-10-04.md) |
| 削除・改変・不正送信をどう評価するか | [完全性・破壊・不正操作](integrity-and-destructive-impact-knowledge-base-2026-10-04.md) | [バックアップ・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md) |
| バックアップから安全に戻せるか | [バックアップ・復元可能性・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md) | [ライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md) |
| OT・重要インフラでは何を復旧とみなすか | [OT・重要インフラの安全・復旧リスク](ot-critical-infrastructure-safety-and-recovery-2026-10-04.md) | [バックアップ・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md) |
| 誰へ何を報告・通知・開示するか | [報告・通知・公表マップ](regulatory-reporting-and-disclosure-map-2026-10-04.md) | [インシデント記録基準](../methodology/reporting-standard.md) |
| 公表の品質をどう見るか | [公表の品質・透明性](incident-disclosure-quality-and-transparency-framework-2026-10-04.md) | [報告・通知・公表マップ](regulatory-reporting-and-disclosure-map-2026-10-04.md) |
| 事故はいくらかかり、何年費用が残るか | [財務・事業影響](incident-financial-and-business-impact-knowledge-base-2026-10-04.md) | [長期予後](post-incident-long-tail-prognosis-2026-10-04.md) |
| 再発防止策は実装・検証されたか | [再発防止策の実効性と再発追跡](remediation-effectiveness-and-recurrence-tracking-2026-10-04.md) | [失敗モードと防御統制](control-failure-mode-crosswalk-2026-10-04.md) |
| 情報が古くなっていないか | [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md) | 個別事例の `latest_public_update` / `public_record_checked_at` |
| AIで攻撃側の経済性がどう変わるか | [AIで攻撃コストが崩れた時代の企業サイバーリスク](executive-ai-amplified-cyber-risk-report-2026-10-04.md) | [根拠資料台帳](evidence-ledger-ai-cyber-risk-2026-10-04.md) |
| 業種ごとの最大被害をどう見るか | [全業種最大被害ストレスマトリクス](sector-worst-case-impact-matrix-2026-10-04.md) | [防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md) |

# 事故の時間軸と対応資料

| 段階 | 主な質問 | Denno Watchで見る場所 |
| --- | --- | --- |
| 発生前 | 何が外部公開され、誰がどこへ到達でき、どの能力が集中していたか | 個別事例、事故前統制比較、第三者・認証・集中リスク、依存グラフ、共有責任 |
| 初期侵入 | 脆弱性、認証情報、委託先、正規機能のどれが入口だったか | 個別事例、ライフサイクル、デジタル証拠・因果確度 |
| 足場確立 | どの権限・認証・管理面が奪われたか | 個別事例、第三者・認証・集中リスク、証拠・因果確度 |
| 横展開 | 何の分離境界を越えたか | 個別事例、依存グラフ、失敗モードと防御統制 |
| 被害 | 機密性、完全性、可用性、本人被害、安全のどれが壊れたか | 個別事例、データ被害、完全性、OT安全 |
| 検知 | 何が最初の兆候だったか、侵入から何時間経過していたか | 対応指標、ライフサイクル、証拠・因果確度 |
| 封じ込め | 何を止め、どの証拠を残したか | 個別事例、対応指標、ライフサイクル、証拠・因果確度 |
| 根絶 | 再侵入条件、資格情報、永続化を除去できたか | 個別事例、ライフサイクル、失敗モードと防御統制 |
| 技術復旧 | クリーンな復旧元・復旧先を使えたか | バックアップ・クリーン復旧、ライフサイクル |
| 業務照合 | 復元したデータ・取引・外部連携が正しいか | 完全性、バックアップ・クリーン復旧 |
| 安全確認 | OT・重要インフラで物理プロセスを安全に戻せるか | OT・重要インフラの安全・復旧リスク |
| 業務復旧 | 顧客、物流、決済等が許容水準へ戻ったか | 個別事例、対応指標 |
| 影響確定 | 最大対象、確認済み取得、通知対象、証拠限界、データ感度を分けられるか | 記録基準、データ被害、証拠・因果確度 |
| 報告・通知 | 本人、委託元、当局、警察等への対応がどう進んだか | 個別事例、報告・通知・公表マップ、証拠資料台帳 |
| 公表・訂正 | 不明点、件数訂正、復旧状態、利用者行動を適切に示したか | 公表の品質・透明性 |
| 市場・財務 | 業績影響、費用、保険、重要性判断がどう更新されたか | 財務・事業影響、証拠資料台帳 |
| 再発防止 | 対策は発表、実装、試験、独立評価のどこまで進んだか | 再発防止策の実効性、事故前統制比較、失敗モードと防御統制 |
| 長期予後 | 二次悪用、訴訟、保険、信用、技術負債、事業撤退等が残っているか | 長期予後、個別事例、海外比較ケース |
| 再確認 | 新公表、訂正、決算、当局更新が出ていないか | 情報源の監視・鮮度・再確認基準 |
| 再発追跡 | 過去対策が同型事故の被害範囲・検知・復旧を改善したか | 再発防止策の実効性、個別事例 |

# 具体的な被害類型から事例を選ぶ

個別事例は「漏えい人数の大小」だけで選ばない。次のように、読者の調査目的に合う実際の侵害境界から辿る。

| 読者が比較したい問題 | まず見る国内事例 | 事故のどの事実を検証するか |
| --- | --- | --- |
| 個人データの流出確定と可能性を区別したい | [JAEA研究支援サイト](../incidents/2026/jaea-jrr3-research-portal-exfiltration.md)、[関西国際大学](../incidents/2026/kansai-university-international-eportfolio-breach.md) | 実ファイル外部取得、文章の本人識別可能性、健康・身分証の情報感度 |
| 既知の金銭的二次不正と偽装メールの兆候を比較したい | [infoQ](../incidents/2026/gmo-infoq-breach-point-theft.md)、[ABAHOUSE](../incidents/2026/abahouse-international-order-data-breach.md) | 既遂のポイント不正換金額と、取引内容が一致する不審メールの因果が未確定な状態 |
| データ漏えいがなくても改ざん・破壊が重大な場合 | [くふう Zaim](../incidents/2026/kufu-zaim-integrity-write-incident.md)、[埼玉県 渋沢MIX](../incidents/2026/saitama-shibusawa-mix-integrity-breach.md) | 14人分の不正書換え、情報閲覧とメール送信、復元・通知の別工程 |
| クラウド・SaaSの供給者事故による下流影響 | [IDCフロンティア](../incidents/2026/idc-frontier-cloud-ransomware.md)、[i-ask](../incidents/2026/scala-iask-supply-chain-breach.md)、[ApplyNow](../incidents/2026/applynow-recruitment-platform-breach.md) | 顧客組織数と人数の違い、委託先の隔離と顧客の業務復旧、企業別本人通知 |
| 事故の公表までにデータ照合が長期化した場合 | [HISタイ法人](../incidents/2026/his-thailand-passport-file-server-breach.md)、[NTT西日本](../incidents/2023/ntt-west-insider-data-exfiltration.md) | 検知・当局報告・範囲特定・本人連絡を別の時間軸で比較 |
| 事故前の統制公表と現実の実装・復旧を照合したい | [アサヒグループ](../incidents/2025/asahi-group-ransomware.md)、[ASKUL](../incidents/2025/askul-ransomware.md)、[イセトー](../incidents/2024/iseto-ransomware.md) | 監査・認証・MFA・EDR・代替運用と、本番資産への適用範囲・業務再開の証拠 |

件数の単位（人数、延べ問い合わせ、アカウント、ファイル、取引、組織）、確認した事実の範囲、公表資料の日時を先に照合し、**全体数・最終確定数・不正取得の実量**を混同しない。

# 比較時の前提

同じ「初動が速い」「復旧済み」「漏えいの可能性」といった表現でも、企業ごとに意味は異なる。比較では少なくとも次を分離する。

- 最初に観測された攻撃活動と、組織が事故を認知した時刻。
- 初期遮断と、全侵害範囲の確定・資格情報失効・永続化排除。
- 技術復旧と、顧客が利用できる業務復旧。
- 最大対象範囲、実際にアクセスされた範囲、外部取得が確認された範囲、本人通知対象。
- 事故前に公表された統制と、事故対象資産への実適用。
- 再発防止策の発表と、実装・試験・独立評価・実運用での確認。
- 会社公表、規制当局資料、株主・財務資料、攻撃者主張、第三者報道の証拠強度。
- AI能力の時代背景と、個別攻撃でAI/LLMが実際に使われたという因果証拠。
