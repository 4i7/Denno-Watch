---
type: Cybersecurity Incident
title: アスクル — 2025年ランサムウェア／EC・物流長期停止、クラウド二次侵入、52.16億円特別損失
description: 2025年10月のアスクルランサムウェアについて、即時遮断後のクラウド二次侵入、注文・物流停止、段階復旧、情報漏えい、2026年7月の追加本人通知、決算延期・特別損失・配当・役員報酬への影響まで追跡する。
resource: https://www.askul.co.jp/corp/security/
tags: [japan, ransomware, ecommerce, logistics, cloud, financial-impact, ir, askul, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: アスクル株式会社
  sector: ecommerce-and-logistics
  jurisdiction: JP
  incident_status: services_recovered_long_term_notification_and_financial_followup
  attack_type: ransomware-with-post-containment-cloud-access
  earliest_known_activity: unknown
  detected_at: "2025-10-19"
  first_disclosed_at: "2025-10-19"
  latest_public_update: "2026-08-04 security portal update after July 30 additional notification"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: not_fully_publicly_disclosed
  affected_services: "ASKUL/LOHACO related systems, order and logistics operations, selected third-party/cloud services"
  data_exposure: confirmed_and_possible_mixed
  availability_impact: "major ordering and shipping functions stopped and were restored in stages"
  restoration_state: "web ordering resumed from November 2025 in stages; broader service recovery continued into February 2026"
  financial_impact: "JPY 5.216bn extraordinary loss disclosed January 28 2026; earnings forecast withdrawn, interim dividend zero, year-end dividend forecast undecided, directors' fixed compensation reduced 20%"
  notification_state: "initial notifications followed by additional individual notification for about 600,000 personal-information records identified by July 2026"
sources:
  - id: askul-security
    resource: https://www.askul.co.jp/corp/security/
    title: アスクルのサイバーセキュリティ
    author: organization:アスクル
  - id: askul-archive
    resource: https://www.askul.co.jp/corp/news/archive/?year=2025
    title: 2025年ニュースリリースアーカイブ
    author: organization:アスクル
  - id: askul-ir
    resource: https://www.askul.co.jp/corp/investor/release/
    title: IRニュース
    author: organization:アスクル
  - id: askul-additional
    resource: https://www.askul.co.jp/shopnews/news_260730_rw_notification.html
    title: ランサムウェア攻撃に伴う情報漏えいのおそれに関する追加の本人通知について
    author: organization:アスクル
  - id: askul-report2024
    resource: https://www.askul.co.jp/corp/investor/library/ir/index.html
    title: ASKUL Report 2024
    author: organization:アスクル
---

# 概要

アスクルは2025年10月19日、外部からの不正アクセスによりランサムウェアへ感染し、主要サービスを停止した。ECと物流を一体運営する企業であるため、事故はWeb画面だけでなく受注・出荷・物流、取引先、3PL事業、決算へ長期波及した。[^security]

事故当日にネットワーク遮断、全パスワード変更、サービス停止を開始したが、10月22日には外部クラウドサービスへの不正アクセスも発生した。23日までに主要クラウドのパスワード変更、24日には認証情報リセット、管理アカウントへのMFA、EDRシグネチャ更新を完了した。[^security]

この系列は、オンプレミス/社内ネットワークを遮断しても、**既に窃取された資格情報・セッションが外部SaaS/クラウド側に残ると二次侵入が続く**ことを示す。

# 事故前の環境と資料

事故前の企業説明を確認する基準資料として、2024年5月期の`ASKUL Report 2024`を保存対象とする。[^report2024] ただし、現在の「アスクルのサイバーセキュリティ」特設ページは事故後に更新された内容を多く含むため、そこに書かれたSOC、EDR、MFA等を事故前能力へ遡及しない。

ASKULは物流DX、EC、データ活用を競争力の中心としてきたため、デジタル基盤停止は売上チャネルだけでなく物理配送能力へ直結する。事故前資料の再読では、一般的な「リスク管理」記載より以下を優先する。

- ECと倉庫管理・配送の依存関係。
- ID管理と外部クラウドの接続。
- バックアップ・代替受注経路。
- 物流現場の縮退運転。
- 3PL顧客データの分離。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2025-10-19 | 攻撃検知。ネットワーク遮断、全パスワード変更開始、サービス停止。初報。[^security] |
| 2025-10-20 | 適時開示でランサムウェア感染・業務影響を株主向けにも公表。 |
| 2025-10-22 | 外部クラウドサービスへの不正アクセスを確認。 |
| 2025-10-23 | 主要外部クラウドサービスのパスワード変更完了。以後、新たな侵入は確認されていないと会社公表。[^security] |
| 2025-10-24 | 認証情報リセット、管理アカウントMFA、EDRシグネチャ更新完了。 |
| 2025-10-29 | 一部商品の出荷トライアル開始。 |
| 2025-10-31 | 外部への情報公開を確認し、情報流出を公表。 |
| 2025-11-11〜14 | 情報流出・3PL関連への影響を続報。 |
| 2025-11-12 | 残存脅威調査を踏まえ安全性を確保したと判断し、ソロエルアリーナからWeb注文を再開。[^security] |
| 2025-12-01 | 第2四半期決算発表延期をIR開示。 |
| 2025-12-12 | 影響調査結果・安全性強化策を第13報として公表。 |
| 2025-12-25〜26 | 半期報告書の提出期限延長を申請・承認。 |
| 2026-01-28 | 52億16百万円の特別損失、通期予想取り下げ、配当修正、役員報酬減額を適時開示。[^ir] |
| 2026-02-13 | 第18報までサービス復旧状況を継続公表。 |
| 2026-07-30 | 追加精査で、外部漏えいのおそれを否定できない個人情報約60万件を追加特定し本人通知を公表。実漏えい・不正利用は未確認。[^additional] |
| 2026-08-04 | セキュリティ特設ページを更新し、中長期強化策を整理。[^security] |

# 即応性と封じ込め

事故当日にネットワーク遮断と全パスワード変更を開始した点は速い。一方、3日後に外部クラウドへ不正アクセスが発生したため、初動時には次を同時実施する必要があると分かる。

- オンプレミス通信遮断。
- IdP/AD/ローカル認証情報の失効。
- SaaS・クラウドのセッション失効。
- APIキー・サービスアカウント・秘密情報のローテーション。
- 管理アカウントへのMFA強制。

「全パスワード変更」という表現だけでは、既存セッションや非パスワード資格情報が無効化されたか判断できない。

# 物流・事業継続

主要EC/物流機能を止めたため、通常の注文・出荷能力が大きく低下した。10月29日の出荷トライアル、11月12日のWeb注文再開など、復旧は段階的だった。[^archive]

これは技術復旧を`server restored`で測らず、次の業務KPIで追う必要がある例である。

- Web注文受付率。
- 出荷可能SKU・顧客範囲。
- 倉庫稼働率。
- 配送リードタイム。
- 3PL顧客への影響。
- 通常受注へ戻るまでの日数。

# 情報漏えい

10月31日以降に外部公開データを確認し、本人・関係先通知を継続した。12月12日にその時点の調査結果をまとめたが、そこで確定終了しなかった。

2026年7月30日、追加調査で**外部への漏えいのおそれを否定できない個人情報約60万件**を新たに特定し、本人通知を追加した。会社はこの追加対象について、実際の外部漏えい・不正利用は確認されていないと明記した。[^additional]

したがって「漏えい確定」と「漏えい可能性」を分離し、最終母集団は調査進展で変化し得る。

# 財務・株主への影響

2026年1月28日、アスクルは事故関連で**52億16百万円の特別損失**を計上すると適時開示した。同時に、通期連結業績予想を取り下げ、中間配当を無配、期末配当予想を未定へ変更し、取締役の固定報酬を20%減額した。[^ir]

また、半期決算発表・半期報告書提出も延期された。事故コストは以下へ拡張した。

- 調査・復旧。
- 売上・物流機会損失。
- 財務報告遅延。
- 株主還元。
- 経営責任。

# 事故後のセキュリティ強化

2026年8月更新の特設ページでは、短期措置に加え中長期の監視・検知、EDR、メール/ネットワーク防御、SOC、IT/OTを含むリスク管理、BCP、外部評価等を示している。[^security]

これは事故後の状態であり、「事故前から24/365 SOCや全管理者MFAが同じ範囲で存在した」とは扱わない。再発防止追跡では、計画・実装・テスト・第三者評価を分ける。

# 重点IR・PDF資料

アスクルIRページには、事故初期から復旧、決算延期、特別損失までのPDFが連続して保存されている。[^ir]

特に保存価値が高いもの:

- 2025-10-20 ランサムウェア感染によるシステム障害発生について。
- 2025-12-01 第2四半期決算発表延期。
- 2025-12-16 サービス復旧状況の適時開示。
- 2025-12-25/26 半期報告書提出期限延長。
- 2026-01-28 特別損失・業績予想・配当・役員報酬に関する適時開示。
- ASKUL Report 2024 — 事故前の経営・デジタル・リスク説明を固定する基準資料。

# 2026年までの予後

2026年2月まで復旧報告が続き、7月にも情報範囲の追加通知が発生した。つまり、EC画面が再開してもインシデントは終わらず、**フォレンジック、本人通知、財務、セキュリティ再設計が9か月以上継続**した。

# 防御上の教訓

- ランサムウェア封じ込め時はSaaS/クラウドの既存セッションとAPI資格情報も同時失効する。
- EC企業では物流設備・WMS・配送・3PL依存を含む復旧順序を事前設計する。
- 安全性確認前に全面再開せず、限定顧客・SKUで段階復旧する。
- 漏えい母集団は初回調査で固定せず、長期精査と追加通知を前提にする。
- IRでは特別損失だけでなく決算延期、配当、役員報酬まで追跡する。
- 事故後のセキュリティ特設ページを事故前統制の証拠へ遡及利用しない。

# 不明点

- 初期侵入経路の完全な技術詳細。
- 攻撃者の侵入・滞留開始日時。
- 外部クラウド二次侵入で利用された資格情報・セッション種別。
- 攻撃者の公的帰属。
- 身代金要求・支払の詳細。
- 本件でLLM/生成AIが使われた公開証拠はない。

[^security]: アスクル「アスクルのサイバーセキュリティ」2026-08-04更新.
[^archive]: アスクル「ニュースリリースアーカイブ 2025」.
[^ir]: アスクル「IRニュース」事故関連適時開示一覧.
[^additional]: アスクル「ランサムウェア攻撃に伴う情報漏えいのおそれに関する追加の本人通知について」2026-07-30.
[^report2024]: アスクル「ASKUL Report 2024」.