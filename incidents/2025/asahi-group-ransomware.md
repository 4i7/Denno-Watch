---
type: Cybersecurity Incident
title: アサヒグループホールディングス — 2025年ランサムウェア攻撃と統制実装ギャップ
description: 2025年9月29日のランサムウェア攻撃を、約10日前の侵入、約4時間の可視障害から隔離、長期物流影響、事故前の統合報告書、2026年の重要な不備まで追跡する。
resource: https://www.asahigroup-holdings.com/newsroom/detail/20260218-0101.html
tags: [japan, food-beverage, ransomware, identity, zero-trust, business-continuity, financial-reporting, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: アサヒグループホールディングス株式会社 / 国内グループ会社
  sector: food-beverage
  jurisdiction: JP
  incident_status: remediation_and_control_deficiency_followup
  attack_type: ransomware and data exfiltration
  earliest_known_activity: "2025-09-19頃（障害発生の約10日前。正確な日時は特定されていない）"
  detected_at: "2025-09-29 07:00 JST頃"
  first_disclosed_at: "2025-09-29"
  latest_public_update: "2026-07-27"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: "国内グループ拠点のネットワーク機器を経由して侵入。その後メインデータセンターへ到達し、パスワード上の弱点を突いて管理者権限を取得したと公表"
  affected_services: "国内の受注・出荷、物流、社内業務・会計関連システム、複数サーバー、一部のゼロトラスト移行前PC"
  data_exposure: confirmed_and_possible
  availability_impact: "受注・出荷等のシステム停止。手作業等で一部業務を継続し、物流正常化は2026年2月まで長期化"
  restoration_state: "主要業務は段階復旧し物流リードタイムは2026年2月までに通常化。再発防止と内部統制是正は継続"
  regulatory_response: "個人情報保護委員会へ2025-09-30以降複数回報告。その他必要な関係機関対応を実施"
  market_disclosure: "決算・法定開示に影響し、有価証券報告書提出期限延長。2026-07-27に財務報告に係る内部統制の重要な不備を開示"
  ai_relation: era_context_only
  response_latency:
    detection_latency: "攻撃者の侵入は障害発生の約10日前。侵入時点での検知は公表上確認できない"
    containment_latency: "2025-09-29 07:00頃の障害確認から、11:00頃のネットワーク遮断・データセンター隔離まで約4時間"
    service_restoration_latency: "主要機能を段階復旧。EOS受注は2025-12-02〜03に再開、物流リードタイムの通常化は2026-02"
  pre_incident_control_disclosure:
    state: confirmed
    published_at: "2024"
    sources: [asahi-integrated-2024]
    declared_controls: ["グループ共通のサイバーセキュリティ基準", "対策状況の評価とセキュリティシステムの維持・強化", "グループのインシデント情報集約と対応強化"]
    applicability_to_failure_surface: direct_and_partial
  market_ir_effect:
    disclosure_present: confirmed
    disclosure_channels: [newsroom, securities_report, internal_control_report, shareholder_material]
    accounting_or_reporting_delay: confirmed
    disclosed_financial_effect: "会計システム停止等により決算・監査作業へ影響。法定提出期限延長を申請"
    executive_accountability: "ガバナンス強化と独立した情報セキュリティ組織・責任者、取締役会監督強化を公表"
sources:
  - id: asahi-final
    resource: https://www.asahigroup-holdings.com/newsroom/detail/20260218-0101.html
    title: サイバー攻撃被害の再発防止策とガバナンス体制の強化について
  - id: asahi-jul17
    resource: https://www.asahigroup-holdings.com/newsroom/detail/20260717-0101.html
    title: サイバー攻撃に係る漏えいのおそれがある個人情報について
  - id: asahi-control
    resource: https://www.asahigroup-holdings.com/en/newsroom/detail/20260727-0204.html
    title: Notice Regarding a Material Weakness in Internal Control over Financial Reporting
  - id: asahi-report-extension
    resource: https://www.asahigroup-holdings.com/newsroom/detail/20260324-0105.html
    title: 有価証券報告書の提出期限延長申請に関するお知らせ
  - id: asahi-integrated-2024
    resource: https://s3-ap-northeast-1.amazonaws.com/asahigroup-doc/company/policies-and-report/pdf/en/2024_all.pdf
    title: Asahi Group Integrated Report 2024
  - id: asahi-shareholders-2026
    resource: https://www.asahigroup-holdings.com/pdf/en/ir/event/shareholders/260220_1.pdf
    title: Convocation Notice of the 102nd Annual General Meeting of Shareholders
---

# 概要

2025年9月29日午前7時頃、アサヒグループの国内システムで障害が発生し、暗号化ファイルが確認された。同日11時頃にはネットワークを遮断し、データセンターを隔離した。後日の調査では、攻撃者は障害発生の約10日前に国内グループ拠点のネットワーク機器を経由して侵入し、メインデータセンターへ到達した後、パスワード上の弱点を突いて管理者権限を取得していたとされた。[^asahi-final]

これは「ランサムウェア実行後の封じ込めは数時間」であっても、「初期侵入からの検知」は別問題であることを示す。約10日間、攻撃者は主として業務時間外に複数サーバーを探索していた。[^asahi-final]

# 発生時の環境と攻撃経路

攻撃対象には複数サーバーと一部の会社支給PCが含まれた。特に、事故後の公表では暗号化・情報窃取を受けたPCの一部が**ゼロトラスト方式への移行前**だったことが明記された。従って「ゼロトラスト施策を進めていた」ことと、「全対象が移行済みだった」ことを混同できない。[^asahi-final]

侵入経路はグループ拠点のネットワーク機器であり、その後、管理者権限取得と内部探索が進んだ。公開記録だけから、特定のCVE、認証情報の取得手段、攻撃主体を補完推測しない。

# 即応と封じ込め

9月29日7時頃の障害認識から約4時間後の11時頃までに、内部・外部ネットワーク、リモートアクセスVPN、拠点間ネットワーク、クラウド専用線等を広く遮断し、データセンターを隔離した。被害拡大を抑えるための強い封じ込めである一方、受注・出荷・社内業務への影響も大きくなった。[^asahi-final]

初動の評価では、「遮断が速かった」ことと「約10日前の侵入を事前検知できなかった」ことを同時に保持する。

# 事業継続と復旧

国内の受注・出荷システムが停止し、手作業等の代替運用を行った。EOS受注は2025年12月2〜3日に再開し、配送リードタイムは2026年2月までに通常状態へ戻ったとされる。技術的な隔離から通常物流まで数か月を要したため、本件では「封じ込め」「システム再開」「通常業務への回復」を別の復旧段階として扱う。[^asahi-final]

# 情報影響

2026年2月公表では、一部の従業員関連情報と取引先関係者情報について外部流出を確認し、さらにデータセンター上の個人情報には漏えいの可能性が残った。7月17日の追加公表で対象範囲が再整理された。初報時の可能性、確認済み流出、後日の範囲訂正を同じ確度として扱わない。[^asahi-final][^asahi-jul17]

# 事故前の公表統制と、事故後に判明した実装差

事故前のIntegrated Report 2024では、サイバー攻撃による事業停止・情報漏えい等をリスクとして挙げ、グループ共通のサイバーセキュリティ基準、対策状況の評価、セキュリティシステムの維持・強化、グループ内インシデント情報の集約と対応強化を公表していた。[^asahi-integrated-2024]

しかし事故後の2026年7月、同社は財務報告に係る内部統制について、**日本地域のITインフラの一部でアクセス権限管理を含む運用が十分に実施されていなかった**として、開示すべき重要な不備と財務報告内部統制の非有効性を公表した。[^asahi-control]

これは事故前の公表が虚偽だったと直ちに意味しない。重要なのは、方針・基準の存在と、全拠点・全機器・全アカウントでの実装・運用品質を別々に検証することである。

# 株主・市場向け開示と予後

サイバー攻撃は会計システムと決算・監査作業にも影響し、2025年12月期有価証券報告書の提出期限延長申請につながった。[^asahi-report-extension] 2026年の株主総会招集通知にも事故概要と再発防止策が掲載され、事故が技術部門だけでなく株主向けガバナンス説明へ移行している。[^asahi-shareholders-2026]

再発防止として、リモートアクセスVPNや旧経路・旧機器の廃止、ゼロトラスト移行完了、ネットワーク分離、EDR強化、ペネトレーションテスト、脅威ハンティング、ログ分析・監視自動化、認証・権限管理、バックアップ・復旧訓練、独立した情報セキュリティ組織と取締役会監督強化などを公表した。これらは「発表済み」と「実装・試験済み」を今後も区別して追跡する必要がある。[^asahi-final]

# AI/LLMとの関係

本件で攻撃者がAIまたはLLMを利用したことを示す公開証拠は確認していない。ローカルLLMが実用可能な時代のインシデントという意味で `era_context_only` とする。

# 防御上の教訓

- 障害発生後の数時間の封じ込めと、初期侵入から約10日の潜伏を別の指標として評価する。
- グループ共通基準が存在しても、拠点ネットワーク機器、権限管理、移行前端末等の例外面を継続的に確認する。
- ゼロトラストは「移行中」を完了状態として評価しない。
- 会計・開示業務の復旧もBCP対象に含め、法定開示遅延まで追跡する。
- 再発防止策は公表時点で完了扱いにせず、実装・試験・独立評価・実運用の各段階で追跡する。

[^asahi-final]: アサヒグループホールディングス「サイバー攻撃被害の再発防止策とガバナンス体制の強化について」2026-02-18.
[^asahi-jul17]: アサヒグループホールディングス「サイバー攻撃に係る漏えいのおそれがある個人情報について」2026-07-17.
[^asahi-control]: Asahi Group Holdings, “Notice Regarding a Material Weakness in Internal Control over Financial Reporting,” 2026-07-27.
[^asahi-report-extension]: アサヒグループホールディングス「有価証券報告書の提出期限延長申請に関するお知らせ」2026-03-24.
[^asahi-integrated-2024]: Asahi Group Holdings, Integrated Report 2024.
[^asahi-shareholders-2026]: Asahi Group Holdings, Convocation Notice of the 102nd Annual General Meeting of Shareholders, 2026.
