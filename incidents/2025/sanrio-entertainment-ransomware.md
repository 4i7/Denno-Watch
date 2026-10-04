---
type: Cybersecurity Incident
title: サンリオエンターテイメント — 2025年ランサムウェアとリモートアクセス機器侵害
description: 2025年1月21日のランサムウェア攻撃、リモートアクセス機器の脆弱性、即時隔離、当初最大約200万件の漏えい可能性から最終的な漏えい未確認、約6か月のサービス復旧を追跡する。
resource: https://www.sanrio-entertainment.co.jp/news/250812/
tags: [japan, entertainment, ransomware, remote-access, vulnerability, service-outage, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: 株式会社サンリオエンターテイメント
  sector: entertainment-theme-park
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: ransomware via vulnerable remote-access equipment
  earliest_known_activity: "2025-01-21"
  detected_at: "2025-01-21"
  first_disclosed_at: "2025-01-22"
  latest_public_update: "2025-08-12"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: "リモートアクセス機器経由。通信ネットワークのセキュリティ体制に一部不備があり、当該機器の脆弱性を狙った不正アクセスに対処できなかったと公表"
  affected_services: "サンリオピューロランド公式Webのマイページ、来場予約、公式eパスポート購入、コーポレートサイト等"
  data_exposure: not_observed_after_initial_possible
  availability_impact: "一部顧客向けサービスが長期停止・制限"
  restoration_state: "2025-08-01までに復旧完了、2025-08-12に調査・復旧完了を公表"
  regulatory_response: "警察および個人情報保護委員会へ報告"
  ai_relation: era_context_only
  response_latency:
    containment_latency: "1月21日の認知後、対象サーバー機器・関連システムをネットワークから遮断。正確な時刻は非公表"
    public_disclosure_latency: "認知翌日の2025-01-22に第一報"
    service_restoration_latency: "一部サービスの利用不能が2025-01-23から継続し、2025-08-01に復旧完了"
sources:
  - id: sanrio-running
    resource: https://www.sanrio-entertainment.co.jp/news/250812/
    title: 当社への不正アクセスによるネットワークトラブルについて
  - id: sanrio-final
    resource: https://www.sanrio-entertainment.co.jp/news/559/
    title: 当社への不正アクセスならびに情報漏洩の可能性に関する調査結果のご報告
  - id: sanrio-final-pdf
    resource: https://www.sanrio-entertainment.co.jp/wp-content/uploads/2025/08/%E3%80%90%E3%82%B5%E3%83%B3%E3%83%AA%E3%82%AA%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%86%E3%82%A4%E3%83%A1%E3%83%B3%E3%83%88%E3%80%91%E5%BD%93%E7%A4%BE%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AA%E3%82%89%E3%81%B3%E3%81%AB%E6%83%85%E5%A0%B1%E6%BC%8F%E6%B4%A9%E3%81%AE%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E8%AA%BF%E6%9F%BB%E7%B5%90%E6%9E%9C%E3%81%AE%E3%81%94%E5%A0%B1%E5%91%8A20250812.pdf
    title: 当社への不正アクセスならびに情報漏洩の可能性に関する調査結果のご報告 PDF
---

# 概要

2025年1月21日、サンリオエンターテイメントのサーバーがランサムウェア攻撃を受け、社内システムとサンリオピューロランドの一部オンラインサービスに障害が発生した。認知後、対象サーバーと関連システムをネットワークから遮断し、外部専門機関と調査・復旧を開始した。[^sanrio-running]

1月22日に第一報、2月7日には個人情報・機密情報が最大約200万件外部へ漏えいした可能性があると公表したが、8月12日の最終調査では、本件に関わる情報漏えいは確認されなかった。[^sanrio-running][^sanrio-final]

この証拠状態の変化を保持し、「当初最大約200万件」だけを最終被害件数として残さない。

# 原因と発生時の環境

外部専門機関の解析で、侵入経路はリモートアクセス機器と特定された。同社は、通信ネットワークのセキュリティ体制に一部不備があり、リモートアクセス機器の脆弱性を狙った不正アクセスに対処できなかったことが原因と考えられると説明した。[^sanrio-final]

公表資料から特定のCVE番号や攻撃主体までは確認できないため推定しない。

# 即応性

1月21日に侵害を認知した後、対象サーバー機器と関連システムをネットワークから遮断し、対策本部を設置、外部アクセス制限、警察への通報等を進めた。1月21日に警察へ相談し22日までに報告、個人情報保護委員会には23日に相談し24日までに報告したと公表している。[^sanrio-running]

正確な検知時刻・隔離時刻は公表されていないため、時間単位の封じ込め速度は算出しない。

# 長期のサービス影響と復旧

マイページ、来場予約、公式eパスポート購入等の一部サービスは長期にわたり利用できない状態となり、代替手段も利用された。2025年7月に複数機能が段階復旧し、8月1日時点で復旧完了、8月12日に調査・復旧完了が公表された。[^sanrio-running]

このため、初動隔離が速くても、顧客向けデジタルサービスの安全な再構築には約6か月を要し得ることを示す。

# 情報影響の変化

2月7日時点では個人情報・機密情報最大約200万件に漏えい可能性があるとしたが、最終的な第三者調査では漏えいは確認されなかった。[^sanrio-running][^sanrio-final]

`not_observed` は「絶対に流出しなかったことの証明」ではなく、利用可能な調査結果で漏えいを示す証拠が確認されなかったという意味で用いる。

# 事故後の対策

認証情報のリセット、管理ポリシー見直し、社内外通信ネットワークのセキュリティ強化、管理機器のセキュリティ強化、従業員教育を再発防止策として公表した。[^sanrio-final-pdf]

今回の調査では、本件の失敗面であるリモートアクセス機器の脆弱性管理へ直接対応する事故前の詳細な統合報告・セキュリティPDFまでは確認していない。一般的なセキュリティ方針を事故前の具体的実装証拠へ置き換えない。

# AI/LLMとの関係

攻撃者によるAI/LLM利用を示す公開証拠は確認していない。`era_context_only` とする。

# 防御上の教訓

- リモートアクセス機器は外部公開境界として、資産台帳・脆弱性監視・代替経路・緊急遮断手順を持つ。
- 初動隔離の速さと、安全なサービス再構築に必要な月単位の復旧期間を別々に評価する。
- 初期の最大影響候補と、最終フォレンジック結果を上書きせず履歴として残す。
- 顧客向けデジタルサービスが止まった場合、代替予約・チケット経路もBCPの一部として評価する。

[^sanrio-running]: サンリオエンターテイメント「当社への不正アクセスによるネットワークトラブルについて」2025-01-22〜2025-08-12更新.
[^sanrio-final]: サンリオエンターテイメント「当社への不正アクセスならびに情報漏洩の可能性に関する調査結果のご報告」2025-08-12.
[^sanrio-final-pdf]: 同社最終調査結果PDF, 2025-08-12.
