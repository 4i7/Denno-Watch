---
type: Analysis Log
title: 再発防止策の実効性と再発追跡 — 「対策予定」を長期的な証拠へ変える
description: 事故後に公表された再発防止策を、予定、実装、検証、定着、再発の状態へ分解し、同一組織・同一共有基盤を数年単位で追跡するための枠組み。
tags: [analysis, remediation, recurrence, longitudinal, controls, lessons-learned, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T21:45:00+09:00 }
sources:
  - id: nist-ir
    resource: https://www.nist.gov/publications/incident-response-recommendations-and-considerations-cybersecurity-risk-management-csf
    title: Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile
    author: organization:NIST
  - id: nist-csf
    resource: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1299.pdf
    title: NIST Cybersecurity Framework 2.0 Resource & Overview Guide
    author: organization:NIST
---

# 目的

インシデント公表の末尾には、しばしば「MFAを強化する」「監視を強化する」「教育を徹底する」「ネットワークを再構築する」といった再発防止策が並ぶ。

しかし、**公表された対策と、実際に実装され有効性が確認された対策は同じではない。**

NIST SP 800-61r3は、インシデント対応を単独の緊急作業ではなく、組織全体のサイバーリスク管理へ統合し、事故からの学習を将来の準備・防御・検知・対応・復旧へ戻す循環として扱う。[^nist-ir]

本資料は、Denno Watchで再発防止策を「書かれた内容」で終わらせず、数か月〜数年後まで追跡できる証拠状態へ分解する。

# 再発防止策の七状態

| 状態 | 意味 |
| --- | --- |
| `announced` | 対策方針が公表された |
| `planned` | 実施計画・期限等が示された |
| `in_progress` | 導入・移行中と公表された |
| `implemented` | 実装済みと公表された |
| `tested` | 演習・復元試験・侵入試験等で動作を確認した証拠がある |
| `independently_assessed` | 独立第三者・監査等による確認が公表されている |
| `operationally_observed` | 後続事故・演習・運用実績で期待した効果が観測された |

一つの統制が全状態を通る必要はない。重要なのは `announced` を `implemented` と読み替えないこと。

# 再発防止策を種類別に追う

## 侵入確率を下げる

- MFA・FIDO等の認証強化。
- パッチ・脆弱性管理。
- 外部公開面削減。
- メール・Web・端末防御。

## 被害範囲を下げる

- 最小権限。
- テナント・ネットワーク・管理面分離。
- 高感度データ分離。
- 長期保持データ削減。

## 検知を早める

- EDR・SIEM。
- ログ保持・集中。
- 異常アクセス・大量取得検知。
- 管理操作監視。

## 復旧を早める

- 分離バックアップ。
- ゴールデンイメージ。
- 復元試験。
- 代替業務・縮退運転。

## 制度・組織対応を改善する

- 報告・通知手順。
- 連絡網。
- 外部専門家契約。
- 経営判断基準。
- 委託先事故時の契約条項。

対策名ではなく、**どの失敗モードを減らす目的か**を記録する。

# 効果を確認する証拠

## 実装証拠

- 組織の後続公表。
- 決算・統合報告書。
- 認証・規格取得そのものではなく、その対象範囲。
- システム移行・廃止の公表。

## 試験証拠

- 復旧演習。
- テーブル演習。
- ペネトレーションテスト。
- レッドチーム。
- フェイルオーバー試験。
- バックアップ復元試験。

## 運用証拠

- 実測RTO/RPO。
- MFA適用率。
- 特権アカウント削減。
- パッチ所要時間。
- ログ保持期間。
- 検知時間。

## 後続事故での証拠

同じ組織が再び攻撃された場合、事故の発生自体だけで過去対策を「失敗」と判定しない。

見るべきなのは次である。

- 同じ侵入経路だったか。
- 過去と同じ境界を越えたか。
- 被害範囲が小さくなったか。
- 検知が早くなったか。
- 復旧が早くなったか。
- 過去対策の対象外から侵入したか。

攻撃を完全にゼロにできなくても、被害を局所化できていれば対策の効果を示す場合がある。

# 再発を四種類へ分ける

| 類型 | 意味 |
| --- | --- |
| `same_vector` | 同じ又は実質同等の侵入経路が再び成立 |
| `same_boundary_failure` | 入口は違うが同じ分離・権限境界の欠陥で拡大 |
| `same_dependency_failure` | 同じ委託先・共有基盤・復旧依存が再び障害点になる |
| `different_failure_mode` | 過去対策とは別の失敗モードで新しい事故が発生 |

これにより「また事故が起きた」だけで対策効果を判断しない。

# 再発防止策の主張を三層へ分ける

## A. 組織自身の主張

「MFAを導入した」「監視を強化した」等。

これは重要な一次情報だが、実効性そのものの独立証明ではない。

## B. 独立した確認

監査、第三者評価、認証の対象範囲、規制当局の確認等。

ただし認証取得を「事故が起きない保証」と扱わない。

## C. 運用結果

後続演習や事故で、検知・封じ込め・復旧・波及抑制が実際に観測された。

実効性の評価にはCが最も強いが、観測機会自体が少ない。

# 依存グラフを使った実効性評価

[システム依存・集中リスクのグラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md)と組み合わせると、再発防止策を関係の変化として評価できる。

例:

```text
事故前:
[本番] ─ administered_by → [共通管理ID]
[Backup] ─ administered_by → [共通管理ID]

事故後:
[本番] ─ administered_by → [本番管理ID]
[Backup] ─ administered_by → [独立復旧ID]
```

「バックアップを強化した」という文章より、**同時侵害される管理依存が減った**ことを表しやすい。

# データ保持策の実効性

事故後に「不要データを削除する」と公表した場合、次を追う。

- 保持期限が定義されたか。
- 既存の過去データを実際に削除したか。
- バックアップ・分析複製も対象か。
- 後続事故で過去データ母集団が縮小したか。

保持ポリシーだけでなく、実際の被害母集団への効果を長期追跡する。

# 復旧策の実効性

バックアップ・DR強化は、[バックアップ・復元可能性・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md)の指標へ接続する。

追跡候補:

- 復元試験を実施したか。
- 実測RTO/RPOが公表されたか。
- 管理面を分離したか。
- クリーン環境へ再構築できるか。
- 後続事故で実際に復旧時間が短縮したか。

# 公表された再発防止策をそのまま一般化しない

被害組織の対策は、その組織の環境・制約・事故原因へ最適化される。

例:

- 一社がVPN廃止を選んでも、すべての組織がVPNを廃止すべきとは限らない。
- 一社が特定製品へ移行しても、その製品が一般解とは限らない。
- 教育強化が公表されても、事故原因が技術的な脆弱性なら主要統制ではない場合がある。

Denno Watchでは、個別対策を [失敗モードと防御統制](control-failure-mode-crosswalk-2026-10-04.md)へ写像して一般化する。

# 追跡間隔

これは法的期限ではなく、ナレッジベース保守上の目安である。

| 時点 | 主な確認 |
| --- | --- |
| 30〜90日 | 緊急対策・通知・再構築の進捗 |
| 6か月 | 中期対策の実装、決算影響、監査・演習 |
| 1年 | 恒久対策、組織・契約変更、長期予後 |
| 2〜3年 | 再発、同じ共有基盤の事故、対策の定着・陳腐化 |

更新はカレンダーだけでなく、新しい事故・決算・規制・監査公表があれば前倒しする。

# メタデータ候補

```yaml
remediation_tracking:
  - action: "MFA強化"
    target_failure_mode: credential_compromise
    announced_at: 2026-01-01
    state: implemented
    implemented_at: 2026-03-01
    evidence_source_ids: []
    independent_assessment: unknown
    operational_effect: unknown
    superseded_by: null

recurrence_tracking:
  follow_up_checked_at: null
  recurrence_observed: unknown
  recurrence_type: null
  same_control_boundary: unknown
  effect_on_detection_time: unknown
  effect_on_blast_radius: unknown
  effect_on_recovery_time: unknown
```

# 「再発なし」の扱い

公開情報で新事故が見つからないことは、統制が有効だった証明ではない。

理由:

- 攻撃されていない可能性。
- 事故が非公表の可能性。
- 別経路で防いだ可能性。
- 観測期間が短い可能性。

したがって、`recurrence_observed: not_observed` と `remediation_effective: confirmed` を同義にしない。

# 長期比較で価値が高いケース

- 同一組織で複数回の事故がある。
- 同一提供者から複数顧客へ時期を変えて波及する。
- 事故後にサービス・基盤を全面再構築した。
- 大規模なID・ネットワーク分離を行った。
- 後続の演習・監査結果を公表している。
- 後年の事故で被害局所化・早期復旧が観測された。

# Denno Watchでの運用

1. 初回事故で、再発防止策を原文の粒度で記録する。
2. `announced` と `implemented` を分ける。
3. 各対策を失敗モード・依存関係へ対応付ける。
4. 情報源の再確認キューへ6か月・1年等の節目を登録する。
5. 後続公表で実装・試験・独立評価を更新する。
6. 再発時は同じ失敗モードかを比較する。
7. 「事故が起きなかった」だけで有効性を断定しない。

# 関連資料

- [失敗モードと防御統制の対応表](control-failure-mode-crosswalk-2026-10-04.md)
- [システム依存・集中リスクのグラフモデル](systemic-dependency-and-concentration-graph-model-2026-10-04.md)
- [バックアップ・復元可能性・クリーン復旧](backup-recoverability-and-clean-restoration-knowledge-base-2026-10-04.md)
- [インシデント後の長期予後](post-incident-long-tail-prognosis-2026-10-04.md)
- [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md)

[^nist-ir]: NIST SP 800-61r3, “Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile”, 2025. https://www.nist.gov/publications/incident-response-recommendations-and-considerations-cybersecurity-risk-management-csf
