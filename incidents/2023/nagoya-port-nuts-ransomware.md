---
type: Cybersecurity Incident
title: 名古屋港統一ターミナルシステム（NUTS）— ランサムウェアによる港湾物流停止
description: 2023年7月4日にNUTSが停止し、約2日半後に全ターミナル作業を再開した事案。保守VPNの外部到達性と認証、港湾物流の事業継続を比較する直前基準。
resource: https://www.mlit.go.jp/kowan/content/001879954.pdf
tags: [japan, port, logistics, ransomware, vpn, critical-infrastructure, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: 名古屋港運協会 / 名古屋港統一ターミナルシステム
  sector: port-logistics
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: ransomware
  earliest_known_activity: "2023-07-04"
  detected_at: "2023-07-04 06:30 JST"
  first_disclosed_at: "2023-07-04"
  latest_public_update: "2024-07-03"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: "maintenance VPN environment identified as a material weakness; exact credential-acquisition method not publicly established"
  affected_services: "Nagoya Port Unified Terminal System (NUTS)"
  data_exposure: unknown
  availability_impact: "container terminal operations were disrupted until 2023-07-06"
  restoration_state: "all terminal operations resumed 2023-07-06 18:15; subsequent government review completed"
  downstream_impact: "about 20,000 containers affected and vessel schedules delayed; manufacturing/logistics downstream effects were reported"
  ai_relation: era_context_only
sources:
  - id: mlit-review
    resource: https://www.mlit.go.jp/kowan/content/001879954.pdf
    title: 名古屋港コンテナターミナルにおけるサイバー攻撃への対応等に関する検討資料
---

# 概要

2023年7月4日6時30分頃、名古屋港のコンテナ搬出入を支えるNUTSに障害が発生し、ランサムウェア攻撃によるシステム停止へ発展した。国土交通省の検証資料は、障害認知から保守会社への調査依頼、物理・仮想サーバー復旧、マルウェア除去、バックアップ復元、ターミナル再開までを時刻単位で残している。[^mlit-review]

本件はLlama 2公開の約2週間前であるため、ローカルLLM時代のコア期間には入れず、直前比較ケースとして扱う。

# 公開時系列

| 時刻 | 出来事 |
| --- | --- |
| 7/4 06:30頃 | NUTS障害を認知。 |
| 07:15頃 | 保守・開発会社へ調査依頼。 |
| 07:30頃 | プリンタから脅迫文が出力されランサムウェア被害を認識。 |
| 08:15頃 | サーバー群が起動できない状態を確認。 |
| 7/5 02:00頃 | 物理サーバーを復旧。 |
| 21:00頃 | 復元した仮想環境からマルウェアを検出。 |
| 7/6 02:00頃 | 約130件のマルウェアを検出し除去作業。 |
| 07:15頃 | 除去完了、バックアップから復元。 |
| 15:00頃 | 各ターミナルが順次作業再開。 |
| 18:15頃 | 全ターミナルが作業再開。 |

# 発生時の環境と統制

国交省検証では、保守用VPNについて接続元IPアドレスの制限がなく、IDとパスワードが一致すれば外部から接続可能な構成が問題として整理された。これは「VPNが存在した」ことと「リモート保守境界が十分に強固だった」ことを分けて考える必要性を示す。[^mlit-review]

公開資料だけでは、攻撃者がVPN認証情報をどのように取得したか、初期侵入に用いた正確なアカウント、攻撃主体を確定できない。

# 即応性・復旧

障害認知から約45分で保守調査へ移り、約1時間でランサムウェアと認識した。復旧は単純なバックアップ戻しではなく、復元環境でマルウェアが再検出され、除去・再検証を挟んでいる。全ターミナルの再開は障害から約60時間後であった。

この経過は、バックアップの存在だけでなく、**復元先のクリーン性確認**がRTOを左右する実例である。

# 影響

国交省資料では約2万本のコンテナに影響し、船舶スケジュールの遅延も発生した。港湾ITの停止が荷主、陸送、船社、製造業へ短時間で波及し得ることを示した。

# 予後と防御上の教訓

事後検証では、保守VPN、認証、ネットワーク構成、バックアップ・復旧、関係者間の連絡体制が改善対象となった。重要なのは、侵害対象が単なる社内ITではなく、物理物流の制御点に近い業務基盤だったことである。

- リモート保守はIP制限、強い多要素認証、個人識別可能なアカウント、ログ監視を組み合わせる。
- 復旧時はバックアップデータだけでなく復元環境のマルウェア残存を検証する。
- 港湾等ではIT復旧と実オペレーション再開を別のマイルストーンとして測る。
- AI利用を示す公開証拠はなく、本件をAI起因とは扱わない。

[^mlit-review]: 国土交通省港湾局、名古屋港サイバー攻撃に関する検証資料。公開資料は後日の検証により事実関係が更新され得ることを明記している。