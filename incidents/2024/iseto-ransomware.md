---
type: Cybersecurity Incident
title: イセトー — 2024年ランサムウェア、VPN侵入と受託データ管理不備、認証一時停止
resource: https://www.iseto.co.jp/news/news_202410.html
tags: [japan, bpo, ransomware, vpn, data-retention, iso27001, iso27017, privacy-mark, supply-chain, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: 株式会社イセトー
  sector: information-processing-bpo
  jurisdiction: JP
  incident_status: restored_with_certification_followup
  attack_type: ransomware and data exfiltration
  earliest_known_activity: "2024-05-26"
  detected_at: "2024-05-26"
  first_disclosed_at: "2024-05-29"
  latest_public_update: "2026-03-06"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "VPNからの不正アクセス。認証情報取得方法等の詳細は公開情報では確定できない"
  affected_services: "情報処理センター、全国営業拠点の端末・サーバー、受託業務データ"
  data_exposure: confirmed
  availability_impact: "複数端末・サーバーが暗号化され、一部業務へ影響"
  restoration_state: "侵入VPNの不使用、認証強化、データ管理区域・保持削除ルールの是正を実施。ISO/IEC 27001・27017とプライバシーマークは一時停止後に再開"
  regulatory_response: "JIPDECによるプライバシーマーク一時停止。ISMS審査機関によるISO/IEC 27001・27017一時停止・特別審査"
  ai_relation: era_context_only
  pre_incident_control_disclosure:
    state: confirmed
    sources: [iseto-security-policy, iseto-iso-suspension]
    declared_controls: ["情報セキュリティ方針", "ISO/IEC 27001", "ISO/IEC 27017", "プライバシーマーク"]
    applicability_to_failure_surface: direct
sources:
  - id: iseto-final
    resource: https://www.iseto.co.jp/news/news_202410.html
    title: 不正アクセスによる個人情報漏えいに関するお詫びとご報告
  - id: iseto-iso-suspension
    resource: https://www.iseto.co.jp/news/news_202409.html
    title: ISO27001認証及びISO27017認証の一時停止について
  - id: iseto-pmark-suspension
    resource: https://www.iseto.co.jp/news/news_202412.html
    title: プライバシーマーク付与の一時停止について
  - id: iseto-iso-resume
    resource: https://www.iseto.co.jp/news/news_202502.html
    title: ISO27001認証及びISO27017認証の一時停止解除について
  - id: iseto-pmark-resume
    resource: https://www.iseto.co.jp/news/news_202503-1.html
    title: プライバシーマーク付与の再開について
  - id: iseto-iso-2026
    resource: https://www.iseto.co.jp/news/news_202603.html
    title: ISMS認証 ISO/IEC 27001:2022 および ISO/IEC 27017:2015 更新のお知らせ
  - id: iseto-security-policy
    resource: https://www.iseto.co.jp/security.html
    title: 情報セキュリティ方針
---

# 概要

2024年5月26日、イセトーは悪意ある第三者による不正アクセスを受け、情報処理センターおよび全国営業拠点の端末・サーバーがランサムウェアにより暗号化された。6月18日には攻撃者グループのリークサイトに窃取情報へのリンクが掲載され、会社は10月4日のフォレンジック完了報告で、公開されたデータが自社サーバーから流出したものであり、一部取引先の顧客個人情報を含んでいたことを確認した。[^iseto-final]

個別の受託元・下流組織が公表した対象件数は母集団が重複し得るため、Denno Watchでは根拠なくユニーク人数として合算しない。

# 侵入経路と発生時の環境

最終報告では、攻撃者がVPNから不正アクセスして社内ネットワークへ侵入したことが公表された。侵害後、受託業務の工程で生成された帳票データや検証物の一部が窃取された。[^iseto-final]

重要なのは、単なるVPN侵害ではない。会社自身が、**本来その情報を扱ってはならないサーバーに作業効率を理由として便宜的に保管し、業務終了後に速やかに削除すべきデータも削除できていなかった**と原因側に明記した。したがって被害規模は、侵入経路だけでなくデータ配置と保持期限の運用品質によって拡大した。

# 初動・封じ込め

5月26日の被害認識後、外部ネットワークとの接続制限、調査・復旧、外部専門家によるフォレンジックへ進んだ。公開情報から侵入開始時刻を検知以前へ遡って確定できないため、detection latencyは算出しない。

最終的には侵入経路となったVPNを使用しない体制へ変更し、認証を強化する方針を公表した。また、受託データを管理区域外へ移送できない環境、保管期限・削除ルール、遵守監査、社員教育を再発防止策とした。[^iseto-final]

# 事故前統制と実侵害の比較

本件は「セキュリティ認証を持つ企業も侵害される」という抽象論より強い比較材料を持つ。事故当時、情報処理センター等はISO/IEC 27001の認証範囲に含まれ、クラウドサービスではISO/IEC 27017も取得していた。ところが事故後の特別審査により、2024年9月に両認証が一時停止された。[^iseto-iso-suspension]

さらにJIPDECは同年12月、プライバシーマーク付与を3か月間一時停止した。[^iseto-pmark-suspension] これは、事故発生だけを理由に「認証が無意味」と評価する材料ではない。むしろ、**認証された管理システムが存在していても、VPN境界、データの実配置、保存期限・削除といった具体的運用で不適合が起き得る**ことを示す。

# 長期予後

ISO/IEC 27001・27017は特別審査後の2025年2月に一時停止解除となった。[^iseto-iso-resume] プライバシーマークも是正措置・再発防止策が有効に機能していると認められ、同年3月25日から付与再開となった。[^iseto-pmark-resume]

2026年2月13日付でISO/IEC 27001:2022およびISO/IEC 27017:2015の認証更新も行われている。[^iseto-iso-2026] そのため本件は、事故発生→認証停止→是正→認証再開→次回更新まで約2年を追える長期予後ケースである。

# 防御上の教訓

- VPN/MFA等の入口防御と、侵入後に読めるデータ量を制限するデータ配置・保持管理を別々に評価する。
- 作業効率のための一時コピーや検証データを、正式な保存領域・削除期限の例外にしない。
- ISO 27001、ISO 27017、プライバシーマークは取得有無だけでなく、事故後の特別審査・停止・是正・再開まで追跡する。
- 委託業務では事故主体と委託元の通知を分離し、重複する人数・レコードを単純合算しない。
- 個別攻撃へのAI/LLM利用を示す公開証拠は確認していない。

[^iseto-final]: イセトー「不正アクセスによる個人情報漏えいに関するお詫びとご報告」2024-10-04.
[^iseto-iso-suspension]: イセトー「ISO27001認証及びISO27017認証の一時停止について」2024-09-02.
[^iseto-pmark-suspension]: イセトー「プライバシーマーク付与の一時停止について」2024-12-24.
[^iseto-iso-resume]: イセトー「ISO27001認証及びISO27017認証の一時停止解除について」2025-02-10.
[^iseto-pmark-resume]: イセトー「プライバシーマーク付与の再開について」2025-03-24.
[^iseto-iso-2026]: イセトー「ISMS認証『ISO/IEC 27001:2022』および『ISO/IEC 27017:2015』更新のお知らせ」2026-03-06.