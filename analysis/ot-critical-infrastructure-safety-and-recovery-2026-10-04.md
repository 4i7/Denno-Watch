---
type: Analysis Log
title: OT・重要インフラの安全・復旧リスク — IT事故とは異なる評価軸を追加する
description: 物理プロセスへ影響するOT・重要インフラについて、安全、操業、遠隔アクセス、構成バックアップ、縮退運転、相互依存、復旧検証の観点を整理する。
tags: [analysis, ot, critical-infrastructure, safety, recovery, resilience, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: nco-critical-infra
    resource: https://www.cyber.go.jp/policy/group/infra/policy.html
    title: 重要インフラ対策関連
    author: organization:国家サイバー統括室
  - id: nist-800-82r3
    resource: https://csrc.nist.gov/pubs/sp/800/82/r3/final
    title: Guide to Operational Technology (OT) Security
    author: organization:NIST
  - id: nist-800-82r4-draft
    resource: https://csrc.nist.gov/Projects/operational-technology-security/publications
    title: Operational Technology Security Publications
    author: organization:NIST
  - id: nist-1339
    resource: https://csrc.nist.gov/pubs/sp/1339/final
    title: OT Backup Quick Start Guide
    author: organization:NIST
  - id: nist-1800-45
    resource: https://www.nist.gov/publications/cybersecurity-water-and-wastewater-sector
    title: Cybersecurity for the Water and Wastewater Sector: Build Architecture
    author: organization:NIST
---

# 目的

Denno Watchの2026年国内事例は、Web、SaaS、メール、認証、物流、業務システム等の情報システム事故を豊富に含む。一方、製造設備、交通制御、ビル制御、水処理、エネルギー等のOTでは、同じ「可用性」「復旧」という言葉でも評価基準が変わる。

OTでは、サーバーが起動しただけでは復旧ではない。制御ロジック、センサー、アクチュエーター、安全系、現場手順、工程条件が整合し、物理プロセスを安全に再開できることが必要になる。

本資料は、Denno Watchの既存ライフサイクルへ**安全・物理影響・縮退運転・工学的復旧**の軸を追加する。

# 2026年10月1日の国内制度変更

国家サイバー統括室は、2026年10月1日に「重要インフラのサイバーセキュリティ対策のための統一基準」を施行した。分野・事業者ごとに対策水準のばらつきがあったことを背景に、分野横断の統一基準を整備したと説明している。併せて「重要インフラのサイバーセキュリティに係る安全基準等策定ガイドライン」も施行された。[^nco-critical-infra]

Denno Watchでは、重要インフラ事例を今後収録する際、一般企業のIT事故と同じテンプレートだけで終わらせず、社会機能・安全・他分野依存を追加する必要がある。

# OTとITで異なる基本前提

NIST SP 800-82 Rev.3は、OTを物理環境と相互作用し、機器・プロセス・イベントを監視・制御するシステムとして扱い、性能、信頼性、安全性の要求を考慮した保護が必要としている。[^nist-800-82r3]

| 観点 | 一般IT | OT・制御系 |
| --- | --- | --- |
| 主目的 | 情報処理・サービス提供 | 物理プロセスの監視・制御 |
| 停止判断 | 隔離・停止が安全な場合が多い | 突然停止自体が危険な場合がある |
| 更新 | 比較的頻繁に可能 | 工程停止・認証・ベンダー制約で難しい場合がある |
| 復旧 | データ・サービス復元 | 構成、ロジック、機器、工程、安全確認まで必要 |
| 影響 | 情報・金銭・業務 | 人命、環境、設備損傷、供給停止を含む |
| 代替 | 別システム・手作業 | 手動運転・縮退運転に専門技能が必要 |

# Denno Watchへ追加すべき影響軸

## 1. 安全影響

従来のCIA（機密性・完全性・可用性）だけでなく、次を別に記録する。

- 人命・負傷の可能性又は確認済み影響。
- 危険物、圧力、温度、回転体等の危険状態。
- 安全計装・保護装置への影響。
- 環境放出・水質・品質等への影響。
- 公共サービス利用者への直接影響。

安全影響が公表されていない場合は `unknown` 又は `not_publicly_disclosed` とする。「事故報告に死傷者記載なし」を「安全影響なし」と読み替えない。

## 2. 操業・供給影響

- 全面停止か、部分停止か。
- 生産量・輸送量・処理能力の低下。
- 手動運転・縮退運転でどこまで継続できたか。
- 原料、物流、電力、通信、クラウド等の外部依存。
- 復旧後に品質検査・再認証・廃棄が必要だったか。

## 3. 物理完全性

OTではデータ改変がそのまま物理操作へ結び付く場合がある。

観測例:

- PLC等の制御ロジック変更。
- セットポイント変更。
- センサー値の改変・隠蔽。
- アラーム無効化。
- 安全系設定変更。
- リモート操作履歴。

公開情報に根拠がなければ、ランサムウェア感染だけから制御ロジック改変を推定しない。

# 遠隔アクセスを独立した境界として扱う

NIST SP 1800-45は、水・下水分野のOTを題材に、遠隔アクセスの参照設計を提示している。NISTは、接続されたセンサー、ネットワーク機器、分析ソフトウェア等の導入がリスクを増やすことを説明し、組織規模に応じた安全な遠隔アクセスを扱っている。[^nist-1800-45]

調査項目:

- インターネットからOT機器へ直接到達できるか。
- VPN、ジャンプホスト、リモート保守基盤を介するか。
- 遠隔操作にMFA・端末制限・時間制限があるか。
- ベンダー保守アカウントは常時有効か。
- 遠隔セッションを記録・監査できるか。
- IT側のID侵害がそのままOT管理権限へ連鎖するか。

# バックアップは「データ」だけではない

NIST SP 1339は、OTバックアップを信頼性・サイバー事故からの復旧に重要とし、変更管理との統合、定期取得、テスト、復旧演習での確認を挙げている。[^nist-1339]

OTで保存すべき対象には次が含まれ得る。

- PLC/DCS等の制御ロジック。
- HMI/SCADA設定。
- ネットワーク構成。
- 機器設定・ファームウェア情報。
- I/O一覧。
- 工程・制御記述。
- 配線図・ネットワーク図。
- 安全要求仕様。
- 原因結果表。
- ヒストリアン設定。

データベースだけ復元できても、工学文書や制御ロジックがないと安全な復旧ができない場合がある。

# 復旧判定を六段階に分ける

```text
1. 通信・管理面を封じ込めた
2. 制御系の信頼境界を再構築した
3. 構成・ロジックを既知良好状態へ戻した
4. センサー・アクチュエーター・安全系を検証した
5. 縮退又は限定条件で運転を再開した
6. 通常運転と安全余裕を確認した
```

Denno Watchで `restoration_state: restored` とだけ記録すると、3〜6のどこまで終わったか不明になる。OT事例では、少なくとも「IT通信復旧」「制御復旧」「安全確認」「通常操業」の節目を分離する。

# 手動運転・縮退運転

重要インフラでは、完全停止と通常運転の間に複数の中間状態がある。

例:

- 受注は手作業、設備は継続。
- 自動制御を止め、現地操作へ切替。
- 一部設備だけ稼働。
- 処理能力を下げて安全余裕を確保。
- 顧客向け機能を停止し、基幹供給を維持。

これらは単なる「復旧遅延」ではなく、レジリエンス能力の証拠になる。

# 相互依存

重要インフラ事故は一社で閉じない。

主な依存:

- 電力 → 通信、交通、水、医療、データセンター。
- 通信 → 決済、物流、クラウド管理、遠隔保守。
- クラウド・ID基盤 → 複数分野の業務システム。
- 物流 → 医薬、食品、製造、燃料。
- 水・空調 → データセンター・製造設備。

Denno Watchの [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md) は主にデジタル依存を扱うが、OTでは**物理供給の依存グラフ**も必要になる。

# OT事例の標準メタデータ候補

```yaml
ot_impact:
  physical_process_affected: unknown
  safety_impact: not_publicly_disclosed
  control_integrity: unknown
  remote_access_involved: unknown
  manual_operation_available: unknown
  degraded_operation_used: unknown
  engineering_backups_available: unknown
  safety_validation_completed_at: null
  normal_operations_restored_at: null
  cross_infrastructure_dependency: []
```

公開根拠がない項目は埋めない。テンプレートの存在が推測を正当化するわけではない。

# OT防御で優先して確認する統制

1. **IT/OTの境界** — ルーティング、ID、管理端末、バックアップを共用し過ぎていないか。
2. **遠隔アクセス** — 常時開放ではなく、認証・端末・時間・承認を絞れるか。
3. **資産把握** — PLC、HMI、エンジニアリング端末、ネットワーク機器、ベンダー接続を把握しているか。
4. **構成・ロジックバックアップ** — 取得だけでなく復元・照合を試しているか。
5. **安全側故障** — 通信断・制御不能時に安全状態へ遷移できるか。
6. **手動・縮退運転** — 実際に人員・手順・紙資料が残っているか。
7. **変更管理** — 正規変更と不正変更を区別できるか。
8. **時刻・ログ** — ITとOTのイベントを同じ時間軸で再構成できるか。
9. **復旧演習** — サーバー復元だけでなく現場操作・安全確認まで含むか。

# 国内事例集との接続

現在の国内42件にも、物流、鉄道、データセンター、医薬品卸など社会機能へ波及し得る事例がある。ただし公開資料上、OT制御系そのものの侵害が確認されていない事例をOT事故へ格上げしてはならない。

たとえば:

- [京王電鉄](../incidents/2026/keio-electric-ransomware.md) は鉄道運行への影響有無を、グループ業務システム障害と分離して記録する。
- [ニチレイ](../incidents/2026/nichirei-cyberattack-logistics-breach.md) は低温物流の業務影響を、制御システム侵害の有無とは分離する。
- [シーイーシー](../incidents/2026/cec-datacenter-ransomware.md) はデータセンターサービス影響を、物理設備制御の侵害と混同しない。
- [マルタケ](../incidents/2026/marutake-ransomware-leak.md) は医薬品供給への業務影響を、製造OT侵害と混同しない。

# 今後収録価値が高い比較ケース

国内公開事例が不足する場合、海外比較ケースとして次の型を追加する価値が高い。

- 水・下水の遠隔アクセス侵害。
- 製造ライン停止と安全確認を伴う事故。
- エネルギー・パイプライン等でIT停止が物理供給へ波及した事故。
- 医療機器・病院設備とIT障害が交差した事故。
- ビル制御・物理アクセス管理の侵害。

海外事例は国内統計へ混ぜず、[海外比較ケース記録基準](../methodology/international-comparative-case-standard.md) に従う。

# 2026年時点の研究上の注意

NISTではSP 800-82 Rev.4の初期公開草案が2026年9月21日に公開されている。一方、現時点の確定版はRev.3である。Denno Watchの規範的な引用は確定版を基礎にし、Rev.4草案は将来変更され得る資料として明示して扱う。[^nist-800-82r4-draft]

# 関連資料

- [全業種サイバー侵害・最大被害ストレスマトリクス](sector-worst-case-impact-matrix-2026-10-04.md)
- [サイバーインシデントのライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md)
- [インシデント対応指標と経営判断トリガー](incident-response-metrics-and-decision-triggers-2026-10-04.md)
- [報告・通知・公表マップ](regulatory-reporting-and-disclosure-map-2026-10-04.md)

[^nco-critical-infra]: 国家サイバー統括室「重要インフラ対策関連」 https://www.cyber.go.jp/policy/group/infra/policy.html
[^nist-800-82r3]: NIST SP 800-82 Rev.3, “Guide to Operational Technology (OT) Security” https://csrc.nist.gov/pubs/sp/800/82/r3/final
[^nist-800-82r4-draft]: NIST “Operational Technology Security Publications” https://csrc.nist.gov/Projects/operational-technology-security/publications
[^nist-1339]: NIST SP 1339, “OT Backup Quick Start Guide” https://csrc.nist.gov/pubs/sp/1339/final
[^nist-1800-45]: NIST SP 1800-45, “Cybersecurity for the Water and Wastewater Sector: Build Architecture” https://www.nist.gov/publications/cybersecurity-water-and-wastewater-sector
