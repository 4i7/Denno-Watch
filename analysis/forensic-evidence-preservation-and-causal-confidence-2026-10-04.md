---
type: Analysis Log
title: デジタル証拠の保全と因果関係の確度 — 「確認済み」の根拠を事故調査の証拠へ戻す
description: ログ、端末、クラウド、SaaS、ネットワーク、バックアップ等の証拠源、保全、時刻、原本性、管理履歴と、侵入経路・原因・影響範囲の確度を分けて記録するための枠組み。
tags: [analysis, forensics, evidence, provenance, causal-confidence, incident-response, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T21:55:00+09:00 }
sources:
  - id: nist-800-86
    resource: https://csrc.nist.gov/pubs/sp/800/86/final
    title: Guide to Integrating Forensic Techniques into Incident Response
    author: organization:NIST
  - id: nist-ir8387
    resource: https://www.nist.gov/publications/digital-evidence-preservation-considerations-evidence-handlers
    title: Digital Evidence Preservation: Considerations for Evidence Handlers
    author: organization:NIST
  - id: nist-ir
    resource: https://www.nist.gov/publications/incident-response-recommendations-and-considerations-cybersecurity-risk-management-csf
    title: Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile
    author: organization:NIST
---

# 目的

Denno Watchでは、`confirmed`、`possible`、`not_observed`、`unknown` 等を使い、公開根拠の確度を分けている。

しかし実際のインシデント調査では、その「確認済み」が何によって成立したかも重要になる。

- EDRが実行を記録した。
- IdPログに認証成功がある。
- SaaS監査ログに大量エクスポートがある。
- ネットワークログに外部転送がある。
- 攻撃者サイトに掲載された。
- 組織自身が「流出を確認した」とだけ公表した。

これらはすべて有用だが、同じ種類の証拠ではない。

NIST SP 800-86は、ファイル、OS、ネットワーク、アプリケーション等の異なる証拠源を事故対応へ統合し、証拠を適切に収集・保全し、取扱履歴を維持する重要性を示している。[^nist-800-86]

本資料は法執行機関向けの証拠手続を再現するものではなく、**公開インシデント記録の因果関係と不確実性をより正確に表現するための防御側モデル**である。

# 証拠を五つの問いで分ける

1. **何を示す証拠か** — 認証、実行、取得、転送、削除、改変等。
2. **どこで生成されたか** — 端末、IdP、SaaS、ネットワーク等。
3. **誰が保持しているか** — 被害組織、提供者、顧客、当局等。
4. **いつまで残るか** — 保持期間、上書き、揮発性。
5. **どこまで因果を支えるか** — 相関、直接観測、推定、否定不能等。

# 主な証拠源

| 証拠源 | 強い点 | 限界 |
| --- | --- | --- |
| IdP・認証ログ | 誰の資格情報で認証されたか | 本人操作か資格情報悪用かは別証拠が必要 |
| EDR・端末ログ | プロセス、実行、ファイル操作 | ログ欠落・端末未導入・攻撃者による無効化 |
| ネットワークログ | 通信先、量、時間 | 暗号化内容やホスト内操作は不明な場合 |
| SaaS監査ログ | 管理操作、共有、エクスポート | 提供者が公開するイベント範囲に依存 |
| クラウド管理ログ | API・管理プレーン操作 | データプレーン詳細は別ログの場合 |
| DB監査ログ | 読み出し・更新・削除 | 全操作を記録していない構成もある |
| メール・SMS送信ログ | 正規通信経路の悪用 | 認証情報取得経路は分からない場合 |
| バックアップ履歴 | 削除・復元・復旧点 | 侵入経路の証明にはならない |
| 攻撃者公開 | 保有を示す可能性 | 真偽・完全性・取得元の独立確認が必要 |
| 被害組織の調査報告 | 複数内部証拠を統合した結論 | 元証拠が公開されない場合がある |

# 「侵入経路」と「最初に観測できた活動」を分ける

最初に確認された不正操作が、侵入の瞬間とは限らない。

```text
実際の初期侵入
    ↓  （証拠なしの期間があるかもしれない）
最初に遡れた不正活動
    ↓
検知
```

したがって、Denno Watchの `earliest_known_activity` と `intrusion_vector` は別フィールドのまま維持する。

「最古のログが3月1日」から「3月1日に侵入した」と断定してはならない。

# 因果関係の確度

公開資料を次のように整理できる。

| 確度 | 意味 |
| --- | --- |
| `directly_observed` | 技術証拠又は調査報告が当該操作を直接確認 |
| `corroborated` | 複数の独立証拠が同じ結論を支持 |
| `organization_conclusion` | 組織・調査主体が結論を公表したが元証拠は非公開 |
| `supported_inference` | 複数事実から合理的に推測できるが確定ではない |
| `possible` | 否定できない、又は候補の一つ |
| `unknown` | 公開情報で判断不能 |

Denno Watchの本文では一般読者向けに既存の `confirmed` 等を使い続けてもよい。必要な事例だけ、内部の証拠確度を補助メタデータとして追加する。

# 原因を三層へ分ける

## 初期侵入要因

例:

- 認証情報悪用。
- 脆弱性悪用。
- 委託先経由。

## 被害拡大要因

例:

- 過大権限。
- 顧客分離不足。
- データ集中。
- ログ不足。

## 長期化要因

例:

- バックアップ不足。
- クリーン再構築不能。
- 影響対象特定の困難。
- 提供者側証拠への依存。

一つの「root cause」に全部を押し込まない。

# CVE・脆弱性の結び付け

事故で使用製品と脆弱性の時期が一致しても、それだけで当該CVEを侵入原因としない。

確定へ必要な例:

- 組織自身がCVE/JVNを明示。
- 調査会社・監督当局が当該事故との関連を明示。
- 技術報告が悪用痕跡を示す。

外部で実悪用が確認されていることは、背景情報としては強いが、当該組織での原因証明ではない。

# 攻撃者主張・リークサイト

攻撃者サイト掲載は、それ自体が観測事実になり得る。

しかし分ける。

```text
confirmed_listing
  掲載された事実を確認

claimed_data_volume
  攻撃者が主張した量

independently_verified_sample
  第三者・組織がサンプルの真正性を確認

organization_confirmed_exfiltration
  被害組織が外部取得を確認
```

掲載量をそのまま確認済み流出量へ変換しない。

# 証拠保全

NIST IR 8387は、デジタル証拠の保存が従来の物理証拠とは異なる固有の課題を持つと整理している。[^nist-ir8387]

事故対応側では次を考える。

- 原本ログと解析済みログを区別。
- 取得時刻を記録。
- ハッシュ等で完全性を確認できるようにする。
- 誰が取得・移動・解析したかを記録。
- 保管場所とアクセスを制限。
- 法務・規制上必要な保存期間を確認。

NIST SP 800-86は、原本ログ、中央集約ログ、解析済みデータを必要に応じて保持し、コピーや解釈の忠実性を後から説明できるようにすることを論じている。[^nist-800-86]

# 証拠管理履歴

厳格な法執行向け手続が必要かは事故・法域・訴訟可能性によるが、防御側でも最低限次を記録すると有用である。

```yaml
evidence_item:
  id: evidence-001
  source_type: idp_log
  acquired_at: 2026-10-04T10:00:00+09:00
  original_time_range: 2026-09-01/2026-10-04
  acquired_by: incident_response_team
  integrity_hash: null
  storage_location: restricted_evidence_store
  transformations:
    - parsed_to_timeline
```

公開KBへ内部保管場所・個人名等を出す必要はない。重要なのは、内部調査では原本と派生物を区別できる設計である。

# 時刻の問題

複数システムのログを一つの時系列へまとめるには時刻が重要である。

確認する。

- タイムゾーン。
- NTP等の同期状態。
- SaaSがUTCで出力するか。
- ローカル時刻へ変換したか。
- 端末時刻がずれていないか。
- 夏時間の影響があるか。

公表資料で「午前3時頃」等しか示されない場合、秒単位へ補完しない。

# `not_observed` の限界

「持ち出しを示すログを確認していない」が意味するものは、ログの可視性によって変わる。

- すべての出口通信を長期間保持していたのか。
- SaaS側にエクスポートログがあったのか。
- 攻撃者がログを削除できたのか。
- 保持期間より前の活動ではないか。

したがって、`not_observed` は**観測能力込みの結論**であり、論理的な不存在証明ではない。

# SaaS・クラウドでの証拠限界

[クラウド・SaaSの共有責任と証拠境界](cloud-saas-shared-responsibility-and-evidence-boundaries-2026-10-04.md)では、テナントが提供者の用意するログ以上を取得できない場合を扱う。

因果確度を評価する際は、次を併記すると有用である。

```yaml
evidence_visibility:
  customer_side: partial
  provider_side: required
  retention_limit_known: false
  provider_investigation_completed: unknown
```

# 復旧時に証拠を壊さない

封じ込め・復旧は急ぐ必要があるが、端末再初期化・ログ削除・資格情報更新等で証拠を失う場合がある。

一律に「証拠のため停止を遅らせる」のではなく、次の優先順位を事故ごとに判断する。

1. 人命・安全。
2. 被害拡大停止。
3. 必要な証拠の迅速保全。
4. 復旧。

重要システムでは、平時から「何を何分で保全してから再構築するか」を決めておく方がよい。

# メタデータ候補

```yaml
causal_evidence:
  initial_access:
    conclusion: unknown
    confidence: unknown
    evidence_sources: []
  exfiltration:
    conclusion: unknown
    confidence: unknown
    evidence_sources: []
  destructive_action:
    conclusion: unknown
    confidence: unknown
    evidence_sources: []
  limitations:
    - "公開資料では元ログ非公開"
```

公開レポートへ内部証拠そのものを添付するのではなく、結論の根拠種別と限界を記録する。

# 公開レポートで有用な表現

良い例:

- 「組織はVPNアカウントの不正利用を侵入経路として確認した。」
- 「外部通信ログから持ち出しが確認されたと公表している。」
- 「攻撃者サイトへの掲載は確認できるが、掲載量と実際の取得量の一致は未確認。」
- 「組織は当該CVEとの関連を公表していない。」

避ける例:

- 「おそらくこのCVEだろう。」
- 「ログがないので流出していない。」
- 「ランサムウェア集団が言っているので全件流出した。」
- 「最古ログの日に侵入した。」

# 関連資料

- [インシデント記録基準](../methodology/reporting-standard.md)
- [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md)
- [クラウド・SaaSの共有責任と証拠境界](cloud-saas-shared-responsibility-and-evidence-boundaries-2026-10-04.md)
- [完全性・破壊・不正操作の被害](integrity-and-destructive-impact-knowledge-base-2026-10-04.md)
- [サイバーインシデントのライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md)

[^nist-800-86]: NIST SP 800-86, “Guide to Integrating Forensic Techniques into Incident Response.” https://csrc.nist.gov/pubs/sp/800/86/final
[^nist-ir8387]: NIST IR 8387, “Digital Evidence Preservation: Considerations for Evidence Handlers.” https://www.nist.gov/publications/digital-evidence-preservation-considerations-evidence-handlers
