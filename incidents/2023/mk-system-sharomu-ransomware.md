---
type: Cybersecurity Incident
title: エムケイシステム — 2023年「社労夢」ランサムウェア、SaaS集中リスクと安全管理不備
resource: https://www.ppc.go.jp/news/press/2023/240325_houdou/
tags: [japan, saas, hr, payroll, ransomware, supply-chain, cloud, identity, vulnerability-management, logging, privacy, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: 株式会社エムケイシステム
  sector: hr-payroll-saas
  jurisdiction: JP
  incident_status: restored_with_regulatory_followup
  attack_type: ransomware and unauthorized access
  earliest_known_activity: "2023-06-05"
  detected_at: "2023-06-05"
  first_disclosed_at: "2023-06-05"
  latest_public_update: "2024-07-18"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "公開資料で単一の侵入経路は特定されていない。個人情報保護委員会は、脆弱なユーザー/管理者パスワード、未適用のセキュリティ更新による深刻な脆弱性残存、ログ保管・管理・監視不足を技術的安全管理措置の不備として認定"
  affected_services: "社労夢シリーズ、SR-SaaS、ネットde顧問、MYNABOX、DirectHR等の人事労務SaaS"
  data_exposure: possible_not_confirmed
  availability_impact: "2023-06-05から主要クラウドサービスを長期停止。6月16日に暫定オンプレ版、6月30日から新AWS基盤で一部再開し、7月に段階復旧"
  restoration_state: "新クラウド基盤へ再構築し段階復旧。PPC指導後に再発防止策の実施状況を報告し、2024-07に委員会で報告内容が公表"
  regulatory_response: "2024-03-25に個人情報保護委員会が法147条に基づく指導等。2024-04-23に会社が再発防止策実施状況を報告、7月にPPCが内容を公表"
  market_disclosure: "業績予想修正、特別損失、配当予想修正、役員報酬減額、資金借入まで適時開示"
  ai_relation: pre_core_anchor_era_context_only
  response_latency:
    visible_failure_to_disclosure: "6月5日に障害を公表し、翌6月6日にランサムウェア感染を適時開示"
    service_restoration_latency: "6月30日に新AWS基盤で主要サービスの一部再開。サービスごとの完全復旧は7月へ継続"
  pre_incident_control_disclosure:
    state: confirmed_by_regulator
    sources: [ppc-action]
    declared_controls: ["万全のデータセンターとセキュリティ管理", "漏えい対策について万全の体制"]
    applicability_to_failure_surface: direct
  market_ir_effect:
    disclosure_present: confirmed
    disclosure_channels: [timely_disclosure, earnings, securities_report]
    accounting_or_reporting_delay: not_primary
    disclosed_financial_effect: "2023-08-08に特別損失、業績予想・配当予想修正、役員報酬減額を開示。資金借入も同日開示"
sources:
  - id: mk-first
    resource: https://www.mks.jp/company/topics/20230605
    title: 弊社製品障害に関するご報告
  - id: mk-final
    resource: https://www.mks.jp/company/topics/20230731
    title: 当社サーバーへの不正アクセスに関する調査結果のご報告
  - id: ppc-action
    resource: https://www.ppc.go.jp/files/pdf/240325_houdou.pdf
    title: 株式会社エムケイシステムに対する個人情報の保護に関する法律に基づく行政上の対応について
  - id: mk-ir
    resource: https://www.mks.jp/company/ir-information/ir-library/disclosure/year/2023
    title: 2023年適時開示情報
  - id: mk-ppc-followup
    resource: https://www.mks.jp/company/topics/20240718a
    title: 個人情報保護委員会の定例委員会で当社の再発防止策についての報告がされた件について
  - id: mk-iso
    resource: https://www.mks.jp/company/topics/20230911a
    title: ISMS認証（ISO27001）取得しました
---

# 概要

2023年6月5日、エムケイシステムが社会保険労務士事務所・企業向けに提供していた「社労夢」等のSaaSで接続障害が発生し、翌6日にランサムウェア被害であることを適時開示した。サービスは社会保険申請、給与計算、人事労務管理などに利用され、単一のSaaS事故が多数の社労士事務所とその顧問先へ波及した。[^mk-first][^ppc-action]

個人情報保護委員会の2024年3月資料では、当時の利用実績は社労士事務所2,754事業所、管理事業所約57万、本件システムで管理する本人数は最大約2,242万人と整理された。委員会が受領した漏えい等報告は3,067件で、報告上の本人数合計は7,496,080人だったが、委託元・社労士事務所等で重複報告があり得るため、ユニーク人数とは扱わない。[^ppc-action]

# 発生時のセキュリティ環境と規制当局が認定した不備

個人情報保護委員会は、事故前の同社Webサイトが本サービスについて「万全のデータセンターとセキュリティ管理」「漏えい対策についても万全の体制」と説明していたことを行政対応資料に明記した。[^ppc-action]

一方、事故後の調査では、ユーザーのパスワードルールが脆弱で、管理者権限パスワードも脆弱かつ類推可能だったこと、ソフトウェアのセキュリティ更新が適切に行われず深刻な脆弱性が残存していたこと、ログの保管・管理・監視が適切でなく、不正アクセスを迅速に検知できなかったことが認定された。PPCはこれらを技術的安全管理措置の不備と評価した。[^ppc-action]

また、保守用IDにより同社が本件システム内の個人データへアクセスでき、個人データ取得を防ぐ技術的アクセス制御もなかった。このため、クラウドサービス事業者が「データを取り扱わない」ケースではなく、個人データの取扱いを委託されていたと判断された。[^ppc-action]

# 初動・業務継続・復旧

6月5日に障害を公表し、6日にランサムウェア感染を適時開示した。その後、外部専門家による調査と新環境の構築を進め、6月16日に暫定的なオンプレミス版を稼働、6月30日午前0時から新しいAWS基盤で社労夢V5.0、DirectHR等を再開し、その他サービスも7月へかけて段階再開した。[^mk-first][^mk-final]

最終フォレンジックでは、ランサムウェア被害であるため窃取可能性を完全には否定できないものの、データ外部転送の痕跡やダークウェブ掲載は確認されず、情報漏えいの事実は確認されなかったと会社は公表した。マイナンバーは高度な暗号化により今回の流出懸念範囲には含まれないと説明された。[^mk-final]

# 規制対応と委託構造

2024年3月25日、個人情報保護委員会はエムケイシステムへ個人情報保護法147条に基づく指導等を実施し、再発防止策の確実な実施と安全管理措置の継続を求めた。会社は4月23日に実施状況を報告し、7月17日の定例委員会でその内容が報告された。[^ppc-action][^mk-ppc-followup]

本件は、SaaS事業者だけでなく、社労士事務所、その顧問先企業まで多段の委託・再委託関係を持つ。PPCは多くの利用者・顧問先が個人データ取扱いの委託・再委託を十分認識せず、委託先監督が結果的に不十分だった可能性も指摘した。[^ppc-action]

# 株主・財務への予後

事故は技術復旧だけで閉じなかった。2023年6月29日に業績予想を修正し、8月8日にはサイバー事故対応等に関連する特別損失、業績予想・配当予想修正、役員報酬減額、資金借入を適時開示した。[^mk-ir]

同社は事故後の2023年9月5日付で、社会保険労務士事務所・一般企業向けシステム開発およびクラウドサービス提供を認証範囲としてISO/IEC 27001:2013を取得した。これは事故前統制の証拠ではなく、事故後の是正・管理体制強化の一部として分離して記録する。[^mk-iso]

# AI/LLMとの関係

本件は2023年7月18日のコア境界より約1か月前であるが、ChatGPT普及後かつローカル実行可能なオープンウェイトLLMが急速に実用化へ向かう直前の重要なSaaS集中リスク事例として比較対象に含める。攻撃者がAI/LLMを利用したことを示す公開証拠は確認していない。

# 防御上の教訓

- SaaSの「セキュリティを万全に管理」という表示と、実際のパスワード規則、管理者認証、パッチ適用、ログ監視を分けて確認する。
- 委託・再委託の責任境界を契約文言だけでなく、実際に誰が保守IDでデータへアクセスできるかから判断する。
- 多数の顧客組織が同じSaaSへ集中する場合、1社の技術的不備が数千件の法定報告へ増幅する。
- サービス復旧と情報流出調査完了、規制対応、財務影響の解消を別々のマイルストーンとして追う。
- 事故後取得したISO認証を事故前の防御実績へ遡及させない。

[^mk-first]: エムケイシステム「弊社製品障害に関するご報告」2023-06-05.
[^mk-final]: エムケイシステム「当社サーバーへの不正アクセスに関する調査結果のご報告」2023-07-31.
[^ppc-action]: 個人情報保護委員会「株式会社エムケイシステムに対する個人情報の保護に関する法律に基づく行政上の対応について」2024-03-25.
[^mk-ir]: エムケイシステム「2023年 適時開示情報」.
[^mk-ppc-followup]: エムケイシステム「個人情報保護委員会の定例委員会で当社の再発防止策についての報告がされた件について」2024-07-18.
[^mk-iso]: エムケイシステム「ISMS認証（ISO27001）取得しました」2023-09-11.
