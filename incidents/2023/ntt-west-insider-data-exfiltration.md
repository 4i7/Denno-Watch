---
type: Cybersecurity Incident
title: NTT西日本グループ — 約10年に及ぶ内部者による顧客情報不正持ち出し
description: NTTビジネスソリューションズの元派遣社員が管理者アカウントを悪用し、約928万件・69クライアントの情報を長期間持ち出した事案。2023年の初動調査失敗と2026年まで続く再発防止追跡を含む。
resource: https://www.ntt-west.co.jp/news/2402/pdf/240229a_1.pdf
tags: [japan, telecom, insider-threat, privileged-access, investigation-failure, governance, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: NTT西日本グループ / NTTビジネスソリューションズ / NTTマーケティングアクトProCX
  sector: telecom-bpo
  jurisdiction: JP
  incident_status: monitoring
  attack_type: insider unauthorized data exfiltration using privileged administrator access
  earliest_known_activity: "2013-07"
  detected_at: "2023-10"
  first_disclosed_at: "2023-10-17"
  latest_public_update: "2026-09-30"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: "authorized operational access and system administrator account abused by insider"
  affected_services: "contact-center customer-data systems"
  data_exposure: confirmed
  availability_impact: "no central prolonged public service outage; primary harm was confidentiality and governance"
  restoration_state: "immediate gaps remediated; group-wide multi-year security program continues to be tracked"
  regulatory_response: "PPC recommendation/guidance and MIC administrative guidance"
  ai_relation: not_applicable
sources:
  - id: ntt-initial
    resource: https://www.ntt-west.co.jp/news/2310/231017a.html
    title: お客さま情報の不正流出に関するお詫びとお知らせ
  - id: ntt-report
    resource: https://www.ntt-west.co.jp/news/2402/pdf/240229a_1.pdf
    title: お客さま情報の不正持ち出しを踏まえたNTT西日本グループの情報セキュリティ強化に向けた取組みについて
  - id: ntt-progress
    resource: https://www.ntt-west.co.jp/corporate/security/
    title: 情報セキュリティ強化に向けた取り組みの進捗状況
---

# 概要

NTTビジネスソリューションズへ派遣されていた元派遣社員が、システム管理者アカウントを悪用して顧客データへアクセスし、約10年にわたり情報を不正に持ち出した。2024年2月のグループ報告では、影響は**顧客情報928万件、クライアント69社**と整理された。[^ntt-report]

本件の比較価値は漏えい規模だけではない。2023年7月に顧客から流出可能性の調査依頼を受けた際、社内調査が漏えいを発見できず「問題なし」と回答しており、後の外部検証ではログ改変、虚偽回答、誤読、エスカレーション欠如等が明らかになった。[^ntt-report]

# 時系列と「最初の調査」の失敗

- 2013年7月頃〜2022年4月: 元派遣社員による不正持ち出し。活動は2023年2月頃まで続いたと整理。
- 2023年7月13日: クライアントから流出可能性の調査依頼。ProCX/BSが調査したが、当時の不適切な調査で事実を把握できず、問題なしと回答。
- 2023年10月17日: ProCX/BSおよびNTT西日本が公表。
- 2024年1月24日: 個人情報保護委員会が勧告・指導。
- 1月31日: 元派遣社員を逮捕。
- 2月9日: 総務省が行政指導。
- 2月29日: グループが詳細な原因分析・再発防止を公表。
- 2026年9月30日: 再発防止策の進捗ページを更新し、継続管理を公表。

# 発生時環境

元派遣社員は保守運用の立場と管理者アカウントを悪用できた。事故後のグループ緊急点検では、許可外記録媒体・端末の接続、アカウント共用、個人特定、ログ点検、リモート接続等の不備が他システムにも見つかった。[^ntt-report]

したがって、これは単一人物の逸脱だけでなく、**特権アクセス、職務分離、持ち出し制御、監視、調査ガバナンス**が重なった失敗として記録する。

# 調査能力も防御統制である

外部弁護士による検証は、2023年7月の調査について、十分な前提知識を持たない担当者によるログ誤読、限定された調査体制、適切なエスカレーションの欠如、委託元・委託先の責任境界の曖昧さ等を指摘した。漏えいを検知する設備だけでなく、**疑義を受けた時に正しい調査へエスカレーションできる能力**が防御の一部である。[^ntt-report]

# 事後対応と長期予後

NTT西日本グループは443システムの緊急総点検、運用責任者等約2,900人への調査を行い、記録媒体、個人識別可能なアカウント、ログ点検、リモート接続等の暫定対策を進めた。その後も組織・システム・人事・監視の再発防止策を継続し、2026年9月まで進捗を公開している。[^ntt-report][^ntt-progress]

# 防御上の教訓

- 特権アクセスは「正規アカウントだから安全」ではなく、操作量・出力・媒体への持ち出しを監視する。
- 長期間同一の強い権限を持つ担当者にはローテーション、職務分離、独立レビューを適用する。
- 顧客から漏えい疑義が来た時の調査は、現場だけで閉じずインシデント対応組織・法務・外部フォレンジックへ上げる。
- ログ自体の真正性、調査者の能力、経営エスカレーションを証拠保全の一部として設計する。
- 本件は内部者事案であり、ローカルLLM時代との因果比較対象にはしない。

[^ntt-initial]: NTT西日本「お客さま情報の不正流出に関するお詫びとお知らせ」2023-10-17.
[^ntt-report]: NTT西日本グループ「お客さま情報の不正持ち出しを踏まえたNTT西日本グループの情報セキュリティ強化に向けた取組みについて」2024-02-29.
[^ntt-progress]: NTT西日本「情報セキュリティ強化に向けた取り組みの進捗状況」2026-09-30時点.