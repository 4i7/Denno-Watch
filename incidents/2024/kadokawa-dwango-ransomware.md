---
type: Cybersecurity Incident
title: KADOKAWA / ドワンゴ — 大規模ランサムウェア／ニコニコ・出版・経理へ波及
description: 2024年6月の大規模サイバー攻撃について、プライベートクラウド暗号化、継続攻撃、ニコニコ長期停止、出版・経理への波及、情報漏えい、補償、IR上の売上・利益・特別損失影響まで追跡する。
resource: https://group.kadokawa.co.jp/system_failure/
tags: [japan, ransomware, private-cloud, media, publishing, business-interruption, financial-impact, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: KADOKAWAグループ / 株式会社ドワンゴ
  sector: media-publishing-web-services
  jurisdiction: JP
  incident_status: services_recovered_long_term_governance_followup
  attack_type: ransomware
  earliest_known_activity: unknown
  detected_at: "2024-06-08T03:30:00+09:00"
  incident_known_at: "2024-06-08T08:00:00+09:00"
  first_disclosed_at: "2024-06-08"
  latest_public_update: "2026 integrated reports continue governance/security follow-up"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: not_fully_publicly_disclosed
  affected_services: "KADOKAWA group private cloud/data-center systems, Niconico services, publishing/logistics systems, selected accounting/internal systems"
  data_exposure: confirmed
  availability_impact: "Niconico unavailable for nearly two months; publishing shipments and accounting operations materially affected"
  restoration_state: "Niconico resumed 2024-08-05; publishing and accounting operations progressively normalized"
  financial_impact: "August 2024 forecast estimated JPY 8.4bn revenue impact, JPY 6.4bn operating-profit impact, and JPY 3.6bn extraordinary loss"
  notification_state: "affected individuals and related parties notified as investigation progressed"
sources:
  - id: kadokawa-hub
    resource: https://group.kadokawa.co.jp/system_failure/
    title: システム障害関連
    author: organization:KADOKAWA
  - id: dwango-june14
    resource: https://group.kadokawa.co.jp/information/media-download/1360/73b7af68478b8a51/
    title: 当社サービスへのサイバー攻撃に関するご報告とお詫び
    author: organization:ドワンゴ
  - id: kadokawa-financial
    resource: https://group.kadokawa.co.jp/information/ir_news/article-10653.html
    title: 大規模サイバー攻撃による業績影響、特別損失の計上および通期連結業績予想の修正に関するお知らせ
    author: organization:KADOKAWA
  - id: kadokawa-ir
    resource: https://group.kadokawa.co.jp/ir/integratedreport/
    title: 統合報告書
    author: organization:KADOKAWA
---

# 概要

2024年6月8日未明、KADOKAWAグループのデータセンター内プライベートクラウドがランサムウェアを含む大規模サイバー攻撃を受けた。ドワンゴの「ニコニコ」をはじめとするWebサービス、出版の生産・出荷、グループ内部の一部業務・経理機能にまで影響が拡大した。[^hub][^dwango]

ドワンゴ公表では、6月8日03:30頃にサービス障害を認識し、08:00頃までにランサムウェアによる暗号化を確認。サーバーを遠隔で停止した後も攻撃者がサーバーを再起動して感染拡大を試みる行動が観測された。単発の暗号化ではなく、**初動中にも攻撃者が能動的に妨害・横展開を継続したインシデント**だった。[^dwango]

# 事故発生時の環境

ニコニコはパブリッククラウドと、グループ企業が提供するデータセンター内のプライベートクラウドを併用していた。攻撃によりプライベートクラウド側の相当数の仮想マシンが暗号化され、サービス全般停止へ至った。[^dwango]

2023年の統合報告書時点でKADOKAWAはリスク管理・コンプライアンス体制を経営資料上に示していたが、本件ではグループデータセンターに複数の事業・内部業務が集中していたことが可用性上の大きな波及点となった。

本件で攻撃者がLLM/生成AIを利用した公開証拠はない。ローカルLLM時代の比較では、AI以前から存在するランサムウェア、仮想化基盤集中、復旧系・認証・運用ネットワークの防御が重大であることを示す事例として扱う。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2024-06-08 03:30頃 | ニコニコ等で異常を認識し調査開始。[^dwango] |
| 2024-06-08 08:00頃 | ランサムウェアを含む攻撃と確認。サービス停止、サーバー停止、ネットワーク遮断、対策本部設置。 |
| 2024-06-09 | 警察へ連絡、外部専門機関へ打診。歌舞伎座オフィス閉鎖。KADOKAWA初報。 |
| 2024-06-10 | 個人情報保護委員会へ初報。 |
| 2024-06-14 | ドワンゴがプライベートクラウド暗号化、継続攻撃、復旧見通しを詳細公表。 |
| 2024-06-27〜07-29 | KADOKAWAが事業復旧状況を継続公表。 |
| 2024-06-28以降 | 情報漏えい、攻撃者の犯行声明・公開行為について複数回公表。 |
| 2024-07-26 | ニコニコを8月5日に再開すると発表、停止期間への補償方針を公表。 |
| 2024-08-05 | ニコニコを新バージョンとして再開。[^niconico] |
| 2024-08-14 | 業績影響・特別損失・通期予想修正をIR開示。[^financial] |
| 2024-09以降 | 出版・経理等が概ね平常状態へ。再発防止・ガバナンス強化を統合報告へ反映。 |

# 初動と即応性

異常認識から数時間で暗号化を特定し、同日に対策本部設置、サービス停止、サーバー停止、通信遮断を実行した。翌日に警察・外部専門家へ連携し、10日にはPPCへ報告した。[^dwango]

一方、停止操作後も攻撃者によるサーバー再起動が観測されており、管理経路の奪取・残存セッション・認証支配を含む可能性を考慮し、単なる「電源断」で終わらない封じ込めが必要だった。

# 事業影響

## Webサービス

ニコニコのサービス全般が約2か月停止し、8月5日に段階再開した。プレミアム会員・チャンネル等への補償も実施した。

## 出版

紙書籍では生産・出荷へ影響し、既刊の1日当たり出荷部数が一時平常時の約3分の1まで低下した。8月中旬以降は概ね平常水準へ戻る見通しとされた。[^financial]

## 経理

一部基幹システム停止により経理機能にも影響し、アナログ対応を含めて7月末頃までに平常化した。これはサイバー事故が外向けサービスだけでなく財務・決算業務へ波及する例である。

# 情報漏えい

KADOKAWA/ドワンゴは攻撃者による情報公開後も調査を継続し、従業者、取引先、契約者、クリエイター等に関わる情報の漏えいを確認した。漏えい総数は資料ごとに単位・対象が異なるため、単純合算ではなく各公表の母集団を保持する。

攻撃者サイト・犯行声明は被害確認の外部証拠にはなり得るが、攻撃者の主張を無検証で事実扱いしない。会社のフォレンジック結果と突合する。

# IR・株主への財務開示

2024年8月14日のIRでは、通期への影響として次を見込んだ。[^financial]

- 売上高減少影響: 84億円。
- 営業利益減少影響: 64億円。
- クリエイター補償、調査・復旧費等の特別損失: 36億円。
- 親会社株主帰属利益の予想を37億円下方修正。

他事業の好調で連結売上高予想は維持できたため、「サイバー事故の事業損失」と「企業全体の最終業績」を分離する必要がある。

# 事故前のセキュリティ開示との比較

KADOKAWAは事故前の統合報告でリスク管理・コンプライアンス推進体制を開示していたが、公開資料だけでは侵害されたプライベートクラウドにおけるMFA・EDR・バックアップ分離等の事故前適用範囲を確定できない。

事故後の2024年統合報告はサイバー攻撃を大きく扱うが、これは事故前能力の証拠ではなく、**事故後の説明・学習・統制更新**として扱う。

# 復旧と長期予後

サービスを完全に旧環境へ戻すのではなく、ニコニコは新しい構成・バージョンで再開した。出版・経理も段階復旧し、2024年9月頃までに主要事業は平常化へ向かった。

事故後は統合報告書でサイバーリスク・復旧・ガバナンス強化を継続的に扱っている。2026年時点ではサービスは継続しているが、事故が情報セキュリティの経営監督、BCP、インフラ構成の見直しへ長期影響を残した。

# 防御上の教訓

- 仮想化・プライベートクラウドの集中は効率化と同時に障害半径を拡大する。
- 攻撃中の管理権限奪取を想定し、通常の管理プレーンとは独立した緊急遮断手段を持つ。
- Webサービス、出版物流、経理など異質な業務が同じ基盤へ依存していないか可視化する。
- バックアップだけでなく、クリーンな代替環境へ再構築できる設計を持つ。
- 長期停止時の顧客・クリエイター補償をBCPと財務計画へ含める。
- IRでは売上・営業利益・特別損失を分けて追跡する。

# 不明点

- 初期侵入経路の完全な技術詳細。
- 攻撃者の初回侵入日時・滞留期間。
- 各侵害システムで事故前に有効だったMFA/EDR等の適用状況。
- 本件にLLM/生成AIが用いられた公開証拠はない。

[^hub]: KADOKAWA「システム障害関連」https://group.kadokawa.co.jp/system_failure/
[^dwango]: ドワンゴ「当社サービスへのサイバー攻撃に関するご報告とお詫び」2024-06-14.
[^niconico]: ドワンゴ「8月5日15時、ニコニコが再開」2024-08-05.
[^financial]: KADOKAWA「大規模サイバー攻撃による業績影響、特別損失の計上および2025年3月期通期連結業績予想の修正に関するお知らせ」2024-08-14.