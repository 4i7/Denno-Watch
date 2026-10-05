---
type: Cybersecurity Incident
title: ローレルバンクマシン / Jijilla — 2025年AI-OCR基盤への不正アクセス、データ削除・窃取可能性
resource: https://www.lbm.co.jp/news/2026/260109/
tags: [japan, ai-service, ocr, unauthorized-access, authentication, data-deletion, bcp, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: ローレルバンクマシン株式会社
  sector: financial-equipment-ai-service
  jurisdiction: JP
  incident_status: service_stopped_for_affected_server
  attack_type: unauthorized access with ransom demand, database deletion and possible data exfiltration
  earliest_known_activity: "2025-09-25"
  detected_at: "2025-09-25"
  first_disclosed_at: "2025-10-16"
  latest_public_update: "2026-01-09"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "辞書攻撃等を繰り返しデータベースへ侵入した可能性が高いとフォレンジックで評価"
  affected_services: "AI-OCRサービス Jijilla の対象サーバー"
  data_exposure: possible
  integrity_impact: "データベース内データ削除を確認"
  availability_impact: "一部サービスが利用不能。対象サーバーのサービス提供は2026-01-09時点で停止継続"
  restoration_state: "全サービスのセキュリティリスク再評価、運用チェックリスト、IR訓練、監査、教育を強化"
  regulatory_response: "警察・個人情報保護委員会へ相談・報告"
  ai_relation: era_context_only
  pre_incident_control_disclosure:
    state: confirmed
    sources: [lbm-security]
    declared_controls: ["情報セキュリティ基本方針", "組織内CSIRT", "取締役会直轄リスク管理委員会", "定期教育", "ISO 27001活用", "個人情報保護マネジメント", "BCP"]
    applicability_to_failure_surface: partial
sources:
  - id: lbm-final
    resource: https://www.lbm.co.jp/news/2026/260109/
    title: 不正アクセスによる個人情報漏えいに関するご報告とお詫び
  - id: lbm-security
    resource: https://www.lbm.co.jp/company/sustainability/security/
    title: 情報セキュリティへの取り組み
---

# 概要

2025年9月25日、ローレルバンクマシンのAI-OCRサービス「Jijilla」で一部サービスが利用できなくなり、顧客からの連絡を受けて調査したところ、対象サーバー内のファイル消失を確認した。会社は直ちにサーバー・関連システムを停止しネットワークを遮断、同日中に顧客へ障害状況を通知し、警察・個人情報保護委員会への相談・報告、外部専門家へのフォレンジック依頼を行った。[^lbm-final]

# 原因と被害

外部専門家は、第三者が辞書攻撃等を繰り返してデータベースへ不正侵入し、内部データを削除し、窃取した可能性が高いと評価した。会社は2025年10月15日にこの結果を把握した。ランサムウェア等のマルウェア感染は確認されていないため、「身代金要求を伴う不正アクセス」と「ランサムウェア感染」を区別する。[^lbm-final]

漏えい可能性のある範囲は、Jijilla利用顧客社員の氏名・メール18件、トライアル等利用者の氏名・メール361件、AI-OCRで処理した無記名アンケート22.3万帳票・回答項目55万箇所相当。アンケートには直接的に個人情報を入力する設問はなく、特定個人情報、機微情報、カード情報も含まれないと公表された。[^lbm-final]

# 可用性・完全性

本件は機密性だけでなく、データベース内データの削除が確認された完全性・可用性事故でもある。2026年1月9日時点で、対象サーバーを利用していた顧客の要望により同サーバーでのサービス提供は停止を継続している。[^lbm-final]

# 事故前のセキュリティ公表との比較

同社は事故以前から、情報セキュリティ基本方針、資産のリスクアセスメント、定期教育、事故対応体制、BCPを公表していた。組織面では管理部門を中心に必要に応じてCSIRTを組成し、取締役会直轄のリスク管理委員会と共有する体制、個人情報保護マネジメント、ISO 27001の活用も説明していた。[^lbm-security]

一方、本件では認証面への反復的な攻撃が侵入要因として評価されている。高位の方針・組織体制と、個別サービスの認証耐性・監視・運用を別レイヤーとして確認する必要がある。

# 再発防止

会社は、提供・利用する全サービスのセキュリティリスク再評価、システム運用チェックリスト改善、インシデント対応マニュアルと実地訓練、セキュリティ監査、従業員教育を再発防止策として示した。[^lbm-final]

# AI/LLMとの関係

対象サービス自体はAI-OCRであるが、攻撃者が生成AI/LLMを利用したことを示す公開証拠はない。サービスにAIが含まれることと、攻撃がAI支援だったことを混同しない。

# 防御上の教訓

- 認証試行への耐性はパスワード方針だけでなく、試行制限、追加認証、異常監視、サービス別リスク評価で確認する。
- AIサービスも通常のSaaS同様に、認証、データ保持、削除、バックアップ、ログ、IRを設計する。
- データ削除と持ち出し可能性を、完全性・機密性の別の被害軸として記録する。
- 「CSIRTがある」「ISO 27001を活用している」という高位統制を、個別サービスの防御実装へ自動的に外挿しない。

[^lbm-final]: ローレルバンクマシン「不正アクセスによる個人情報漏えいに関するご報告とお詫び」2026-01-09.
[^lbm-security]: ローレルバンクマシン「情報セキュリティへの取り組み」2026-10-05確認.