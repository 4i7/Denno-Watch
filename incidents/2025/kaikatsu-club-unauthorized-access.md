---
type: Cybersecurity Incident
title: 快活CLUB / FiT24 — 2025年会員システム不正アクセスと729万件の漏えい可能性
resource: https://www.kaikatsu.jp/info/detail/ddos.html
tags: [japan, retail-services, membership, unauthorized-access, personal-data, incident-response, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: 株式会社快活フロンティア
  sector: leisure-fitness
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: unauthorized access to membership account system
  earliest_known_activity: unknown
  detected_at: "2025-01-18"
  first_disclosed_at: "2025-01-20"
  latest_public_update: "2025-03-17"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "攻撃要因と影響プログラムは会社調査で特定したと公表したが、公開ページでは具体的CVE・手口を非公表"
  affected_services: "快活CLUB・FiT24等の会員アカウント管理、会員アプリ"
  data_exposure: possible
  availability_impact: "会員アプリ機能を制限し、2月19〜28日に順次再開"
  restoration_state: "影響プログラム改修、セキュリティソフト・パッチ、監視・ブロック、パスワードポリシー、多層防御を実施"
  regulatory_response: "個人情報保護委員会へ2025-01-21初報、2025-03-13確報"
  secondary_abuse: not_observed
  ai_relation: era_context_only
  response_latency:
    containment_latency: "1月18日夕刻の検知後、直ちにサーバーをネットワークから切り離した"
    public_disclosure_latency: "検知から1月20日第一報まで約2日"
    service_restoration_latency: "アプリ制限開始1月20日から2月19〜28日の段階再開まで約1か月"
sources:
  - id: kaikatsu
    resource: https://www.kaikatsu.jp/info/detail/ddos.html
    title: 不正アクセスの発生及び個人情報漏えいの可能性に関するお知らせとお問い合わせ
---

# 概要

快活フロンティアは2025年1月18日夕刻、サーバーへの不正アクセスを検知し、直ちにネットワークから切り離した。その後の調査で会員アカウント管理システムへの不正アクセス痕跡が確認され、個人情報の一部が外部へ漏えいした可能性を公表した。[^kaikatsu]

最終公表で対象となった個人情報は**7,290,087件**。快活CLUBの会員・仮会員、FiT24・FiT24インドアゴルフ会員の一部が対象で、氏名、住所、電話番号、生年月日、会員番号、会員種別、ポイント、最終会計日時等を含む。一方、身分証明書情報、クレジットカード、メールアドレス、会員アプリのパスワードは対象外と公表された。[^kaikatsu]

# 初動と公表の変化

1月18日の検知直後にサーバーをネットワークから切り離し、20日に対策本部設置、会員アプリ制限、第一報を実施した。21日に個人情報保護委員会へ初報し、外部専門機関と調査を進め、2月14日に最終調査結果を受領した。アプリは2月19〜28日に順次再開し、3月13日に個人情報保護委員会へ確報、17日に第五報を公表した。[^kaikatsu]

初期の障害説明ではネットワーク混雑・DDoSに関する案内も含まれていたが、後続調査では会員管理システムへの不正アクセスを主たるインシデントとして扱っている。初報時点の症状と最終原因認識を分離する。

# 証拠状態

会社は攻撃要因と影響プログラムを特定したと公表しているものの、一般公開ページでは具体的なCVEや攻撃手順は示していない。したがってDenno Watchでは脆弱性名を推定しない。

2025年3月17日時点までに、対象個人情報が実際に漏えいした事実や漏えいに伴う二次被害は確認されていない。7,290,087件は「漏えい可能性のある個人情報の件数」であり、外部流出確認件数へ格上げしない。[^kaikatsu]

# 再発防止

影響を受けたプログラムの改修、新しいセキュリティ対策ソフト、パッチ適用、Web不正アクセス監視と検知時ブロックを実施した。影響を受けなかったサーバー・プログラムについても痕跡調査を行い、パスワードポリシー、外部アクセス防御・監視、多層防御を強化した。[^kaikatsu]

# 防御上の教訓

- 最初に観測した可用性症状と、後のフォレンジックで判明した機密性侵害を分離する。
- 影響可能性件数と確認済み流出件数を混同しない。
- 検知後のサーバー隔離が迅速でも、会員サービス再開にはフォレンジック、改修、規制報告を含む数週間の工程が必要になる。
- 身分証・カード・パスワード等が別管理だった点は、被害範囲を限定したデータ分離として評価する。
- 個別攻撃へのAI/LLM利用を示す公開証拠は確認していない。

[^kaikatsu]: 快活フロンティア「不正アクセスの発生及び個人情報漏えいの可能性に関するお知らせとお問い合わせ」2025-03-17最終更新.