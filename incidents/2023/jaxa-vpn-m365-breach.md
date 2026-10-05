---
type: Cybersecurity Incident
title: JAXA — 2023年VPN装置侵害、内部横展開とMicrosoft 365情報漏えい
resource: https://www.jaxa.jp/press/2024/07/20240705-2_j.html
tags: [japan, government-research, vpn, microsoft365, credential-theft, lateral-movement, data-leak, zero-trust, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: 国立研究開発法人宇宙航空研究開発機構（JAXA）
  sector: space-research-government
  jurisdiction: JP
  incident_status: long_term_remediation
  attack_type: VPN appliance exploitation, lateral movement, credential theft and cloud account abuse
  earliest_known_activity: "2023-10"
  detected_at: "2023-10"
  first_disclosed_at: "2024-07-05"
  latest_public_update: "2025-08"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "VPN装置の脆弱性を起点とした侵入。先に公表された脆弱性が悪用された可能性が高いとJAXAが評価"
  affected_services: "業務用イントラネットの一部サーバー・端末、窃取アカウントを介したMicrosoft 365"
  data_exposure: confirmed
  availability_impact: "主要なロケット・衛星運用への影響なし。侵害ネットワークでは機微な運用情報を扱っていなかった"
  restoration_state: "不正通信遮断、マルウェア除去、侵害分析、脆弱性対応・ログ監視強化。VPNに代わる安全な外部接続、ネットワーク全体監視、ゼロトラスト基幹ネットワーク刷新等を長期実装"
  regulatory_response: "所管府省、NISC、警察、JPCERT/CC、IPA、Microsoft専門チーム等と連携"
  ai_relation: era_context_only
  pre_incident_control_disclosure:
    state: confirmed_with_document_revision_caveat
    sources: [jaxa-r5-plan, jaxa-r6-evaluation]
    declared_controls: ["教育・訓練", "運用改善", "システム監視強化", "クラウドを含むセキュリティ水準強化", "情報の重要度に応じたネットワーク・Webアクセス分離"]
    applicability_to_failure_surface: direct_and_partial
sources:
  - id: jaxa-incident
    resource: https://www.jaxa.jp/press/2024/07/20240705-2_j.html
    title: JAXAにおいて発生した不正アクセスによる情報漏洩について
  - id: jaxa-r5-plan
    resource: https://www.jaxa.jp/about/plan/pdf/r5nd-year_plan-b.pdf
    title: 令和5年度の業務運営に関する計画
  - id: jaxa-r6-evaluation
    resource: https://www.jaxa.jp/about/finance/pdf/2024dokuhouhyoukakekka.pdf
    title: 国立研究開発法人宇宙航空研究開発機構の令和6年度における業務の実績に関する評価
---

# 概要

JAXAは2023年10月、外部機関からの通報に基づき、業務用イントラネットの一部サーバーへの不正アクセスを認知した。直後に攻撃元との通信遮断、対象サーバー等のネットワーク切断を実施し、専門機関・セキュリティベンダー・Microsoftの専門チームと調査を行った。2024年7月の公式公表で、外部機関との共同業務情報と個人情報を含む一部情報の漏えいを確認した。[^jaxa-incident]

本件で侵害されたネットワークやシステムでは、ロケット・衛星の運用等に係る機微な情報は扱われていなかった。したがって、JAXA侵害をそのまま宇宙機運用系侵害へ拡大解釈しない。[^jaxa-incident]

# 侵入・横展開・クラウド到達

JAXAの調査では、第三者がVPN装置の脆弱性を起点に一部サーバー・端末へ侵入し、侵害範囲を広げてアカウント情報等を窃取、その資格情報を用いてMicrosoft 365へ正規ユーザーを装って不正アクセスした。侵害過程では複数の未知のマルウェアが使用され、検知を困難にしていた。[^jaxa-incident]

このため本件は、境界機器の侵害、内部横展開、資格情報窃取、クラウドSaaSへの正規認証悪用が一つの連鎖になった事例として記録する。

# 即応性

外部機関からの通報で事案を認知した後、JAXAは当日中に不正通信の遮断、サーバー等の切断を行ったと後の政府評価資料でも整理されている。JAXA自身の公表でも「速やかに」初期対応したことを示す。[^jaxa-incident][^jaxa-r6-evaluation]

一方、最初の認知が自組織の監視ではなく外部通報だったこと、未知マルウェアにより既存監視で検知困難だったことは、防御能力評価で重要である。検知後の封じ込め速度と、侵入自体を自律検知できたかを分離する。

# 事故前に公表されていた情報セキュリティ方針との比較

令和5年度計画は2023年3月30日に制定され、情報セキュリティインシデント防止と重要システム強化のため、教育・訓練、運用改善、システム監視強化、クラウドを含むセキュリティ水準強化等を掲げていた。[^jaxa-r5-plan]

ただし同PDFは事故後の2024年2月・3月にも改定されており、現行版には2023年度事故への対応も追記されている。したがって、事故前から存在した方針と、事故後に追加された再発防止記述を混同しない。

2024年度の政府評価資料は、JAXAが全社的な情報セキュリティを「しくみ」「人」「システム」の3側面から強化してきたにもかかわらず、2023年10月に重大インシデントが発生したと明記した。また、2019年度に整備した情報重要度に応じたネットワーク・Webアクセス分離によって、ロケットへの影響がないことを早期に確定できたとも評価している。[^jaxa-r6-evaluation]

これは「事前対策が無意味だった」のではなく、**侵入防止・検知には不足があった一方、情報・ネットワーク分離は被害境界の限定には機能した**と読むべきケースである。

# 事故後の長期対策と予後

JAXAは短期策として、脆弱性対応を迅速化する体制と内部通信ログ監視を強化した。恒久策にはエンドポイントを含むネットワーク全体の監視強化、VPNに代わる外部接続方式、通信・システム挙動の可視化、なりすまし対策が含まれる。[^jaxa-incident]

政府評価では、2024年度にVPNに代わる安全な外部接続サービス導入を完了し、専門家を副CISOへ招聘、セキュリティ人材を強化、ゼロトラストアーキテクチャを取り入れた基幹ネットワーク刷新を進めた。2025年度中に通信制御・可視化やなりすまし対策を完了する計画も示された。[^jaxa-r6-evaluation]

事故後の2024年にはVPN装置を狙った複数回の不正アクセス（ゼロデイ攻撃を含む）が再び発生したが、情報漏えい等の被害は確認されなかった。JAXAはこれを事故後対策下で被害を防いだ後続観測として公表している。[^jaxa-incident]

# 防御上の教訓

- VPN等の境界機器は、脆弱性公開から適用までの時間だけでなく、未知・ゼロデイを前提とする監視と代替接続方式を持つ。
- 境界侵害後は資格情報窃取とMicrosoft 365等のクラウド到達を前提に、認証・セッション・行動監視を連携させる。
- 「検知後の即応が速い」と「侵入を自組織で早期検知できた」は別の指標である。
- 情報・ネットワーク分離は侵入そのものを防げなくても、重大運用情報への到達を制限する被害限定統制として評価する。
- 事故後の対策は発表だけでなく、VPN代替、監視、ゼロトラスト刷新、後続攻撃での被害抑止等の実装・運用観測まで追う。
- 個別攻撃へのAI/LLM利用を示す公開証拠は確認していない。

[^jaxa-incident]: JAXA「JAXAにおいて発生した不正アクセスによる情報漏洩について」2024-07-05.
[^jaxa-r5-plan]: JAXA「令和5年度の業務運営に関する計画」2023-03-30制定（現行PDFは事故後改定を含むため、事故前部分と事後追記を区別して使用）.
[^jaxa-r6-evaluation]: 内閣総理大臣・総務大臣・文部科学大臣・経済産業大臣「国立研究開発法人宇宙航空研究開発機構の令和6年度における業務の実績に関する評価」2025-08.