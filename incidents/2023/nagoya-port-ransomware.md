---
type: Cybersecurity Incident
title: 名古屋港 — NUTSランサムウェア／約3日間のコンテナ搬出入停止
description: 2023年7月の名古屋港統一ターミナルシステム停止について、復旧時系列、物流影響、保守VPN・バックアップ・初動手順上の課題、制度改正まで追跡する。
resource: https://www.mlit.go.jp/kowan/kowan_mn2_000006.html
tags: [japan, port, critical-infrastructure, ransomware, logistics, vpn, backup, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: 名古屋港運協会／名古屋港統一ターミナルシステム
  sector: port-and-logistics
  jurisdiction: JP
  incident_status: recovered_with_regulatory_and_sector_followup
  attack_type: ransomware
  earliest_known_activity: unknown
  detected_at: "2023-07-04T06:30:00+09:00"
  first_disclosed_at: "2023-07-05"
  latest_public_update: "2026 sector-level security measures continue"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "maintenance VPN is considered a likely route in public review, but other routes were not completely excluded"
  affected_services: "Nagoya Port Unified Terminal System (NUTS) used across five container terminals and centralized gate"
  data_exposure: not_established
  availability_impact: "container gate-in/gate-out stopped for about three days; vessel handling continued partly by manual procedures"
  restoration_state: "system restored in about 2.5 days; sector guidance and institutional countermeasures continued thereafter"
  downstream_impact: "37 vessels experienced cargo-handling schedule effects and an estimated roughly 20,000 containers were affected"
  business_continuity: "manual cargo-handling procedures continued using printed work information"
sources:
  - id: mlit-committee
    resource: https://www.mlit.go.jp/kowan/kowan_mn2_000006.html
    title: コンテナターミナルにおける情報セキュリティ対策等検討委員会について
    author: organization:国土交通省
  - id: mlit-timeline
    resource: https://www.mlit.go.jp/kowan/content/001719866.pdf
    title: 名古屋港事案の時系列を含む委員会資料
    author: organization:国土交通省
  - id: mlit-summary
    resource: https://www.mlit.go.jp/kowan/content/001710842.pdf
    title: コンテナターミナルにおける情報セキュリティ対策等検討委員会 取りまとめ
    author: organization:国土交通省
  - id: mlit-guide
    resource: https://www.mlit.go.jp/report/press/port07_hh_000245.html
    title: 港湾分野における情報セキュリティ確保に係る安全ガイドライン（第2版）の公表
    author: organization:国土交通省
---

# 概要

2023年7月4日早朝、名古屋港の5つのコンテナターミナルと集中管理ゲートで利用するNUTSが停止した。07:30頃には専用プリンターからランサムウェアの脅迫文が印刷され、14:00頃までに物理サーバ基盤と全仮想サーバの暗号化が判明した。[^mlit-timeline]

コンテナの搬入・搬出は約3日間停止し、国土交通省資料では荷役スケジュールに影響した船舶37隻、搬入・搬出に影響したコンテナ約2万本と整理されている。一方、船舶との荷役は紙に印刷した作業情報を用いるマニュアル作業で継続された。[^mlit-committee][^mlit-summary]

# 当時の脅威・防御環境

2023年は国内ランサムウェア被害が高水準で、RaaSや二重恐喝が既に一般化していた。ローカルLLMが利用しやすくなり始めた時期と重なるが、本件で攻撃者がLLMを利用した公開証拠はない。

港湾分野では、IT停止がそのまま物理物流へ波及する一方、一般企業のWebシステムとは異なり、可用性・復旧時間・現場手順が国家的な物流継続へ直結する。本件は日本の港湾施設で初の大規模サイバー攻撃として国土交通省が制度検討を開始する契機となった。[^mlit-committee]

# 公開情報で確認できる時系列

| 時刻・日付 | 出来事 |
| --- | --- |
| 7/4 06:30頃 | NUTS停止を確認。[^mlit-timeline] |
| 07:15頃 | 保守会社・開発会社へ調査依頼。 |
| 07:30頃 | 専用プリンターからランサムウェア脅迫文。 |
| 09:00頃 | 愛知県警へ連絡。ランサムウェア感染可能性との見解。 |
| 10:30頃 | 物流再開を優先し復旧作業開始。 |
| 14:00頃 | 物理サーバ基盤・全仮想サーバ暗号化を確認。 |
| 7/5 02:00頃 | 物理サーバ基盤8台復旧、仮想サーバ45台復元開始。 |
| 12:00頃 | 仮想サーバ復元完了、ウイルスチェック開始。 |
| 21:00頃 | 復元サーバからウイルスを検知、駆除が必要と判明。 |
| 7/6 | 駆除・整合性確認を経て段階的に業務再開。 |
| 7/31以降 | 国交省検討委員会で原因・対策・制度措置を検討。[^mlit-committee] |
| 2024 | 名古屋港事案を反映した港湾安全ガイドライン第2版へ。[^mlit-guide] |
| 2025-2026 | 港湾事業者向け訓練、脆弱性診断、制度措置が継続。 |

# 技術的に確認できた事項

公的取りまとめでは、保守用VPNを経由した侵入が有力な経路と整理される一方、他の経路を完全に排除していない。したがって「VPNが確定原因」とは記載しない。

調査で問題として整理された主な領域は次の通り。

- 保守用外部接続のセキュリティ対策が十分に考慮されていなかった。
- サーバー・ネットワーク機器の脆弱性管理が不十分だった。
- バックアップ対象・保存の考え方に改善余地があった。
- インシデント対応手順が十分に整備されていなかった。

復元した仮想サーバからマルウェアが検出された事実は、**バックアップや仮想マシンを戻すだけでは安全な復旧にならない**ことを示す。[^mlit-timeline]

# 初動と即応性

本件の即応性は、弱点と強みが同時に観測できる。

**強かった点**

- 停止から45分程度で保守・開発会社へ調査を依頼。
- 約2時間半で警察へ連絡。
- 物流継続を優先する判断を同日午前に実施。
- 物理基盤を翌日早朝までに復旧し、全VM復元へ進んだ。
- 旧来のマニュアル運用経験者が残っており、船舶荷役そのものは継続した。

**弱かった点**

- 侵入防止・外部接続管理に構造的課題。
- 復旧後VMからマルウェアが検出され、復元と安全確認を別工程にする必要があった。
- 事前の事故対応手順・演習が十分でなかった。

# 事業継続・影響

NUTS停止によりゲート搬出入が止まり、物流へ直接影響した。国交省資料では37隻、約2万コンテナ規模の影響が示される。[^mlit-summary]

一方、マニュアル荷役で船舶自体の作業を継続できたことは重要なBCP証拠である。ただし委員会は、これはシステム化以前の手作業経験者がいたから可能だった面があり、全面手作業を恒久BCPとすることは非現実的だと指摘している。[^mlit-summary]

# 公表・制度対応

本件は一企業の再発防止に留まらず、国土交通省が専門委員会を設置し、港湾運送事業法、サイバーセキュリティ基本法、経済安全保障推進法の観点から制度措置を検討する契機となった。2024年には名古屋港事案を反映した港湾分野の安全ガイドライン第2版が公表された。[^mlit-guide]

# 現在までの予後

2026年時点でも、名古屋港事案は港湾分野のサイバーセキュリティ訓練、脆弱性診断、制度設計の基準事例として利用されている。技術復旧は2023年7月に完了したが、**制度上の予後は数年継続している**。

# 防御上の教訓

- 重要インフラでは復旧時間をサービス画面だけでなく物理物流で測る。
- 保守VPN・委託先経路を通常利用者とは別の高リスク境界として管理する。
- バックアップは復元可能性だけでなく、復元後のマルウェア検査・整合性検証まで試験する。
- マニュアル運用は有効だが、特定の熟練者の経験に依存するBCPは継続性が弱い。
- 一社の事故が業界ガイドライン・法制度を更新するほどの社会波及を持ち得る。

# 不明点・未公表事項

- 初期侵入の厳密な日時。
- 保守VPN以外の経路を完全に排除できるか。
- 攻撃者の内部滞留期間。
- 情報窃取の有無・範囲。
- 事故前の個別装置ごとの認証方式、MFA適用状況。

[^mlit-committee]: 国土交通省「コンテナターミナルにおける情報セキュリティ対策等検討委員会について」.
[^mlit-timeline]: 国土交通省 委員会資料「名古屋港事案の時系列」https://www.mlit.go.jp/kowan/content/001719866.pdf
[^mlit-summary]: 国土交通省「コンテナターミナルにおける情報セキュリティ対策等検討委員会 取りまとめ」https://www.mlit.go.jp/kowan/content/001710842.pdf
[^mlit-guide]: 国土交通省「港湾分野における情報セキュリティ確保に係る安全ガイドライン（第2版）の公表」2025-03-31.