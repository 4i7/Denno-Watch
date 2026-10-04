---
type: Cybersecurity Incident
title: 保険見直し本舗グループ — 2025年ランサムウェアと保険代理店データの下流影響
description: 2025年2月16日のランサムウェア被害、ネットワーク機器を介した侵入可能性、即時隔離、委託元保険会社への波及、24時間監視・CISO体制等の事後強化を追跡する。
resource: https://hoken.mhompo.co.jp/news/20250225/
tags: [japan, insurance, ransomware, third-party, network-appliance, business-continuity, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: 株式会社保険見直し本舗グループ / 株式会社保険見直し本舗ほか
  sector: insurance-agency
  jurisdiction: JP
  incident_status: public_report_closed_with_monitoring
  attack_type: ransomware
  earliest_known_activity: "2025-02-16"
  detected_at: "2025-02-16"
  first_disclosed_at: "2025-02-25"
  latest_public_update: "2025-08-29"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: "グループ内で使用していた一部ネットワーク装置が侵入経路となった可能性が高いと外部専門機関が評価"
  affected_services: "グループのネットワーク・システム、一部端末・サーバー。保険代理店として保有・共同利用する顧客・従業員関連情報"
  data_exposure: not_observed_but_possible
  availability_impact: "各種サービス提供に支障。安全確認・強化後に通常業務へ復帰"
  restoration_state: "安全性を確認したサーバー・端末・ネットワークで通常業務を再開。外部公開監視を継続"
  downstream_impact: "委託元・提携先の保険会社が自社顧客情報への影響可能性を個別公表"
  regulatory_response: "警察・金融庁等の関係機関と連携したと最終報告で説明"
  ai_relation: era_context_only
  response_latency:
    containment_latency: "2月16日の被害認識後、関連サーバーを直ちにネットワークから切り離す緊急措置"
    public_disclosure_latency: "認知2025-02-16から第一報2025-02-25まで9日"
  pre_incident_control_disclosure:
    state: not_found_in_this_pass
    applicability_to_failure_surface: unknown
sources:
  - id: hmh-first
    resource: https://hoken.mhompo.co.jp/news/20250225/
    title: 当社グループにおけるランサムウェア被害に関しまして
  - id: hmh-first-pdf
    resource: https://hoken.mhompo.co.jp/news/20250225/pdf/ac183dcf.pdf
    title: 当社グループにおけるランサムウェア被害に関しまして PDF
  - id: hmh-second-pdf
    resource: https://www.mhompo.co.jp/news/20250430/pdf/20250430.pdf
    title: 当社グループにおけるランサムウェア被害に関しまして（第2報） PDF
  - id: hmh-final
    resource: https://hoken.mhompo.co.jp/whokenp/wp-content/uploads/2025/08/Release_20250829.pdf
    title: ランサムウェア被害に関する最終調査・再発防止公表
  - id: meijiyasuda-downstream
    resource: https://www.meijiyasuda.co.jp/profile/news/topics/20250430.html
    title: 当社の委託先保険代理店におけるランサムウェア被害による個人情報漏えい等のおそれについて
---

# 概要

2025年2月16日、保険見直し本舗グループでランサムウェア被害が確認され、ネットワーク・システム障害により各種サービスに支障が生じた。2月25日に第一報を公表し、4月30日の第2報では、被害認識後に関連サーバーを直ちにネットワークから切り離し、外部専門家と原因・影響範囲を調査してきたと説明した。[^hmh-first][^hmh-second-pdf]

# 原因と被害環境

最終調査では、グループ内で使用していた一部のネットワーク装置が侵入経路となった可能性が高いとされた。そこから社内ネットワークを通じて複数の端末・サーバーが攻撃を受け、ファイル暗号化等が発生した。[^hmh-final]

公開資料ではネットワーク装置の製品名、CVE、認証悪用の有無、攻撃主体は明らかにされていないため推定しない。

# 即応性

2月16日にランサムウェア被害を認識した後、関連サーバーを直ちにネットワークから切り離した。[^hmh-second-pdf] 外部専門家を起用し、影響範囲と流出の有無を調査した。

第一報は2月25日で、認知から9日後だった。技術的な隔離速度と、対外公表速度を分離して記録する。

# 情報影響と下流波及

暗号化されたファイルには顧客・従業員・元従業員等の個人情報を含むものがあったが、最終調査では外部への情報流出を示す証拠や、攻撃者による公開は確認されていないとされた。[^hmh-final]

一方、保険代理店として複数の保険会社の顧客情報を取り扱っていたため、明治安田生命、日本生命グループ、チューリッヒ生命等の委託元も、各社顧客情報に漏えい等のおそれがあるとして通知・公表を行った。[^meijiyasuda-downstream]

これは「代理店側で外部流出が確認された」ことを意味しない。委託元が保有主体として影響可能性を通知した事実と、フォレンジック上の漏えい確認を分離する。

# 復旧と事後対策

最終報告時点では、安全性を確認・強化したサーバー、端末、ネットワーク環境で通常業務を再開していた。再発防止として、ネットワーク装置・端末等の総点検、専門部門の設置、24時間体制のセキュリティ監視、早期検知・対応、業務インフラ見直し、CISOを中心とする組織体制、教育・訓練強化を公表した。[^hmh-final]

これらは事故後に導入・強化された統制である。今回の公開調査では、事故前に同等の監視・CISO体制等を明示した詳細な一次PDFを確認できなかったため、事故後統制を事故前から存在していた証拠へ遡及利用しない。

# 株主・関係者向け資料

同グループは初報、第2報、最終報告をPDFでも公開した。上場会社の適時開示のような市場開示より、委託元保険会社・顧客・規制当局への下流通知が本件の主要な外部説明面である。

# AI/LLMとの関係

本件で攻撃者がAI/LLMを利用したことを示す公開証拠は確認していない。`era_context_only` とする。

# 防御上の教訓

- 保険代理店のように複数事業者の顧客情報が集中する組織では、1社の侵害が多数の委託元通知へ波及する。
- ネットワーク装置を外部境界資産として独立監視し、侵害時に内部横展開を抑えるセグメンテーションを設計する。
- 「暗号化されたファイルに個人情報がある」と「外部流出が確認された」を分離する。
- 事故後の24時間監視やCISO体制は、今後実装・試験・運用効果まで追跡する。

[^hmh-first]: 保険見直し本舗「当社グループにおけるランサムウェア被害に関しまして」2025-02-25.
[^hmh-second-pdf]: 保険見直し本舗グループ「当社グループにおけるランサムウェア被害に関しまして（第2報）」2025-04-30.
[^hmh-final]: 保険見直し本舗「ランサムウェア被害に関する最終調査・再発防止公表」2025-08-29.
[^meijiyasuda-downstream]: 明治安田生命「当社の委託先保険代理店におけるランサムウェア被害による個人情報漏えい等のおそれについて」2025-04-30.
