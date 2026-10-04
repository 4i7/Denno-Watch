---
type: Cybersecurity Incident
title: アサヒグループ — 拠点ネットワーク機器侵入・管理者権限奪取／ランサムウェアと国内物流停止
description: 2025年9月のアサヒグループサイバー攻撃について、約10日前の侵入、パスワード弱点による管理者権限奪取、ゼロトラスト移行前端末、国内受注・出荷停止、株主総会・内部統制への長期影響まで追跡する。
resource: https://www.asahigroup-holdings.com/newsroom/detail/20260218-0101.html
tags: [japan, ransomware, manufacturing, logistics, zero-trust, governance, internal-control, asahi, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: アサヒグループホールディングス株式会社
  sector: food-and-beverage
  jurisdiction: JP
  incident_status: operations_recovered_long_term_financial_control_and_notification_followup
  attack_type: ransomware-after-network-appliance-intrusion
  earliest_known_activity: "approximately 10 days before 2025-09-29"
  detected_at: "2025-09-29T07:00:00+09:00"
  first_disclosed_at: "2025-09-29"
  latest_public_update: "2026-07-27 material weakness in internal control over financial reporting"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "network device at a group site; attacker later exploited password weakness to obtain administrative privileges"
  affected_services: "Japan-managed internal systems, main data center, order/shipment, call centers, multiple servers and pre-zero-trust endpoints"
  data_exposure: confirmed_and_possible_mixed
  availability_impact: "domestic order and shipment operations stopped; production and distribution constrained; financial reporting delayed"
  restoration_state: "manufacturing restarted in stages from early October 2025; EOS ordering resumed December 2025; logistics broadly normalized by February 2026"
  financial_reporting_impact: "FY2025 financial reporting was delayed; company later identified a material weakness in internal control over financial reporting"
  notification_state: "individual notifications continued after February and July 2026 scope updates"
sources:
  - id: asahi-first
    resource: https://www.asahigroup-holdings.com/newsroom/detail/20250929-0102.html
    title: サイバー攻撃によるシステム障害発生について
    author: organization:アサヒグループホールディングス
  - id: asahi-investigation
    resource: https://www.asahigroup-holdings.com/newsroom/detail/20260218-0101.html
    title: サイバー攻撃被害の再発防止策とガバナンス体制の強化について
    author: organization:アサヒグループホールディングス
  - id: asahi-july
    resource: https://www.asahigroup-holdings.com/newsroom/detail/20260717-0101.html
    title: サイバー攻撃に係る漏えいのおそれがある個人情報について
    author: organization:アサヒグループホールディングス
  - id: asahi-icfr
    resource: https://www.asahigroup-holdings.com/en/newsroom/detail/20260727-0204.html
    title: Notice Regarding a Material Weakness in Internal Control over Financial Reporting
    author: organization:Asahi Group Holdings
  - id: asahi-agm
    resource: https://www.asahigroup-holdings.com/pdf/ir/shareholders_guide/shareholders_meeting/2026_shoushu_01.pdf
    title: 第102回定時株主総会招集ご通知
    author: organization:アサヒグループホールディングス
---

# 概要

2025年9月29日午前7時頃、アサヒグループの国内システムに障害が発生し、調査でランサムウェアによる暗号化を確認した。午前11時頃にはネットワークを遮断し、主要データセンターを隔離した。国内グループ各社の受注・出荷、コールセンター等が停止し、製造・物流・決算へ広範な影響が出た。[^first][^investigation]

2026年2月の詳細調査で、攻撃者は障害発生の約10日前にグループ内拠点のネットワーク機器を経由して侵入し、主要データセンターへ到達、**パスワードの弱点を突いて管理者権限を奪取**したとされた。奪取アカウントを使い、主に業務時間外に複数サーバーで侵入・偵察を繰り返した後、9月29日にランサムウェアを一斉実行した。[^investigation]

# 事故前の環境 — ゼロトラスト移行の「途中」

事故後の会社調査は、暗号化された一部PCを**ゼロトラストモデルへの移行前端末**と明示し、その一部からデータが窃取されたと説明した。[^investigation]

この表現は重要である。事故当時アサヒはセキュリティ刷新を全く行っていなかったのではなく、旧来ネットワークからゼロトラストモデルへ移行途中だった。大企業では移行に年単位を要するため、次が独立した攻撃面になる。

- 移行前PC・サーバー。
- 旧拠点ネットワーク機器。
- VPN・専用線・クラウド接続の例外。
- 旧認証・パスワードポリシー。
- 新旧ネットワーク間の到達経路。

「ゼロトラスト導入企業が破られた」ではなく、**移行率と残存旧資産を測らないと安全性を評価できない**事例である。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2025-09中旬頃 | 後の調査で、障害の約10日前に拠点ネットワーク機器経由で侵入したと推定。[^investigation] |
| 2025-09-29 07:00頃 | システム障害、暗号化ファイルを確認。 |
| 2025-09-29 11:00頃 | ネットワーク遮断・データセンター隔離。受注・出荷、コールセンター等停止。[^first] |
| 2025-10-03 | ランサムウェア攻撃を公表。流出痕跡を調査中。 |
| 2025-10-08 | インターネット上に流出疑いデータを確認。国内各工場で生産を段階再開。 |
| 2025-11-27 | 調査結果と漏えい可能性を公表、11月26日にPPCへ確報済みと説明。 |
| 2025-12 | EOS等の受注機能を段階再開。 |
| 2026-02-18 | 侵入経路、管理者権限奪取、ゼロトラスト移行前端末、再発防止、ガバナンス強化を詳細公表。[^investigation] |
| 2026-02頃 | 国内物流が概ね正常化。 |
| 2026-07-17 | 追加精査で漏えいのおそれがある個人情報の対象範囲を再整理。[^july] |
| 2026-07-27 | FY2025内部統制報告書で、財務報告に係る内部統制に開示すべき重要な不備があり有効でなかったと公表。[^icfr] |

# 即応性

障害認知から約4時間でネットワーク遮断・データセンター隔離まで進んだ。この点は迅速である。被害拡大を防ぐため、リモートアクセスVPN、約300拠点をつなぐネットワーク、クラウド専用接続、インターネット接続等を広範に止めたと株主向け資料で説明している。[^agm]

しかし広範遮断は、受注・出荷・物流・社内処理も止めた。重要なのは「遮断が速かったか」だけでなく、**安全のため止めても事業を縮退継続できる代替経路があったか**である。

# 事業継続と復旧

国内の注文・出荷システム停止により、酒類・飲料・食品の供給へ直接影響した。製造は10月2日以降各工場で段階再開し、当初は電話・FAX・手作業等も組み合わせた限定的な受注・出荷で対応した。

会社はバックアップの健全性を確認しながら復旧を進め、EOSによる受注は2025年12月から段階的に戻し、物流は2026年2月頃までに概ね正常化した。[^investigation]

この期間は、単なるサーバ復元時間ではなく**商流・物流の正常化時間**として記録する。

# 情報漏えい

調査では、ゼロトラスト移行前の一部貸与PCからデータが窃取されたことを確認し、データセンター内サーバーの個人情報にも漏えい可能性を認めた。2026年2月時点の調査対象を公表後、7月17日に追加精査した対象範囲を再整理した。[^july]

2月時点で示された件数を最終確定値と固定せず、**調査進展で母集団が変化した**こと自体を記録する。

# 株主・財務報告への波及

本件は決算・監査プロセスにも長期影響を与えた。2026年の第102回定時株主総会では、事故に伴う決算手続の遅延が通常の財務報告・株主総会運営へ影響したことが説明された。[^agm]

さらに2026年7月27日、会社は2025年12月期の内部統制報告書について、サイバー攻撃の影響により財務報告に係る内部統制に**開示すべき重要な不備**が存在し、期末時点で有効ではなかったと公表した。[^icfr]

これは事故の予後が「工場再開」で終わらず、10か月後にも会計・内部統制評価へ残ることを示す。

# 事故前セキュリティ開示との比較

アサヒは事故以前からデジタル基盤刷新・グループIT変革を進めていた。事故後資料から、ゼロトラスト移行自体は進行していたことが確認できる。一方、攻撃は旧資産・拠点ネットワーク・弱いパスワードを足場に主要データセンターまで到達した。

したがって平時資料を読む際は、「ゼロトラストを推進」といった方針表現ではなく、事故時点の次の数値を可能な限り確認する。

- 移行済み端末率。
- 旧端末・旧サーバー数。
- 管理者アカウントのMFA適用率。
- 拠点ネットワーク機器の認証方式。
- 新旧境界の到達制御。

# 再発防止

会社は技術対策だけでなく、ガバナンス体制強化を含む再発防止を2026年2月に公表した。旧来環境からゼロトラストへの移行加速、認証・権限・監視、組織的セキュリティ統制を強化する方針である。[^investigation]

再発防止策は公表時点での`planned/implemented`を区別し、その後の統合報告・内部統制報告で実装証拠を追う。

# 重点PDF

- 第102回定時株主総会招集通知: `https://www.asahigroup-holdings.com/pdf/ir/shareholders_guide/shareholders_meeting/2026_shoushu_01.pdf`
- 英語版株主総会資料: `https://www.asahigroup-holdings.com/pdf/en/ir/event/shareholders/260220_1.pdf`

このPDFは、侵入系列、遮断した接続、バックアップ、手作業での出荷、物流正常化、株主総会への影響を一つの経営文書で追えるため重点保存対象とする。

# 防御上の教訓

- セキュリティ移行中は旧資産を独立した高リスク台帳で管理する。
- 管理者権限はパスワードだけで保護せず、MFA・端末条件・特権アクセス管理を組み合わせる。
- 拠点ネットワーク機器をインターネット境界と同等に扱う。
- 全面遮断しても注文・製造・物流を縮退継続できる手順を訓練する。
- バックアップ健全性と事業正常化を別の復旧KPIとして測る。
- 財務報告・内部統制への長期影響を事故後1年以上追う。

# 不明点

- 拠点ネットワーク機器の製品名・具体的脆弱性/侵入手法。
- パスワード弱点の具体的性質。
- 全ての侵害サーバー・端末数。
- 攻撃者の公的帰属。
- 本件でLLM/生成AIが使われた公開証拠はない。

[^first]: アサヒグループホールディングス「サイバー攻撃によるシステム障害発生について」2025-09-29.
[^investigation]: アサヒグループホールディングス「サイバー攻撃被害の再発防止策とガバナンス体制の強化について」2026-02-18.
[^july]: アサヒグループホールディングス「サイバー攻撃に係る漏えいのおそれがある個人情報について」2026-07-17.
[^icfr]: Asahi Group Holdings, “Notice Regarding a Material Weakness in Internal Control over Financial Reporting,” 2026-07-27.
[^agm]: アサヒグループホールディングス「第102回定時株主総会招集ご通知」2026.