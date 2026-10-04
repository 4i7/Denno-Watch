---
type: Cybersecurity Incident
title: カシオ計算機 — 2024年ランサムウェア攻撃とグローバルネットワーク統制の不備
description: 2024年10月5日に海外から侵入され、ランサムウェアでシステムが使用不能となり社内文書・個人情報が流出。事故前に公表していた標的型メール訓練、不審通信監視、ゼロトラスト、ISO 27001等と、事故後に判明した海外拠点を含む統制上の不足を比較する。
resource: https://www.casio.co.jp/release/2025/0107-incident/
tags: [japan, electronics, ransomware, phishing, global-network, zero-trust, iso27001, data-exfiltration, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: カシオ計算機株式会社
  sector: electronics
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: ransomware and data exfiltration
  earliest_known_activity: "2024-10-05"
  detected_at: "2024-10-05"
  first_disclosed_at: "2024-10-08"
  latest_public_update: "2025-01-07"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: "海外からの不正アクセス。事故後の原因分析ではフィッシングメール対策と海外拠点を含むグローバルのネットワークセキュリティ体制の一部不備を公表"
  affected_services: "internal servers and multiple services; CASIO ID and ClassPad.net were on separate systems and not affected"
  data_exposure: confirmed
  availability_impact: "multiple systems/services stopped; most later resumed"
  restoration_state: "most affected services resumed after safety checks; forensic investigation completed to publicly available extent"
  regulatory_response: "final report submitted to PPC 2024-12-03 and overseas regulators as applicable"
  secondary_abuse: "employee-targeted spam plausibly related to the incident was reported"
  ai_relation: era_context_only
  pre_incident_control_disclosure:
    state: confirmed
    published_at: "2023"
    sources: [casio-sustainability-2023]
    declared_controls: ["全役員・従業員への定期情報セキュリティ教育", "海外グループ会社を含む教育", "標的型攻撃メール訓練", "Web不正アクセス・社内ネットワーク不審通信監視の強化", "ゼロトラストネットワークの構築導入", "クラウド利用ガイドライン・セキュリティチェックリスト", "ISO 27001認証範囲のデジタル統轄部全体への拡大"]
    applicability_to_failure_surface: direct_and_partial
sources:
  - id: casio-final
    resource: https://www.casio.co.jp/release/2025/0107-incident/
    title: ランサムウェア攻撃による情報漏えい等調査結果について
  - id: casio-2023
    resource: https://www.casio.co.jp/release/2023/1018-incident/
    title: 不正アクセスによる個人情報漏えいのお詫びとご報告
  - id: casio-sustainability-2023
    resource: https://www.casio.co.jp/content/dam/casio/global/corporate/csr/report/2023/sustainability-report-2023-10.pdf
    title: サステナビリティレポート2023 — ガバナンス／リスクマネジメント／情報セキュリティ
---

# 概要

2024年10月5日、カシオ計算機のサーバーが海外から不正アクセスを受け、ランサムウェアでシステムが使用不能となった。2025年1月の最終調査公表では、社内文書の一部が窃取され、従業員6,456人、取引先関係者1,931人、顧客91人の個人情報等の流出を確認した。[^casio-final]

顧客データベースや顧客個人情報を扱うシステムからの窃取痕跡は確認されず、CASIO IDとClassPad.netは別システムで本件の影響を受けていない。被害範囲を全顧客基盤へ拡大解釈しない。[^casio-final]

# 公開された原因

カシオは、サイバー攻撃増加を受けシステム・セキュリティ強化を進めていたものの、**フィッシングメール対策と、海外拠点を含むグローバルのネットワークセキュリティ体制に一部不備があった**ため、攻撃に対処できなかったと説明した。[^casio-final]

これは、平時の「セキュリティ強化」公表があっても、グループ全体で均一な境界・認証・メール対策が実効化されているとは限らないことを示す。

# 情報影響

従業員情報には、氏名・社員番号・メール・所属・人事情報のほか、一部で身分証明書や家族情報、海外関係者の納税者番号等が含まれた。取引先情報、採用応募者情報、少数の顧客配送情報も含まれた。カード情報は含まれない。[^casio-final]

同社はランサムウェアグループの要求に応じなかったことも公表している。

# 規制・復旧

2024年12月3日に個人情報保護委員会へ確報を提出し、海外監督当局にも適用法令に応じ報告した。2025年1月時点で、一部を除く停止サービスは安全確認後に再開済みだった。[^casio-final]

# 事故前の公表統制との比較

事故前のサステナビリティレポート2023は、情報セキュリティを重要リスクとして扱い、国内外を含む全役員・従業員への定期教育、標的型攻撃メール訓練、Webサイト不正アクセスと社内ネットワーク不審通信の監視強化、従業員PCを含む「ゼロトラストネットワーク」の構築導入、クラウド利用ガイドラインとセキュリティチェックリスト、ISO 27001認証範囲のデジタル統轄部全体への拡大を公表していた。[^casio-sustainability-2023]

一方、2024年事故後の最終報告は、フィッシング対策と海外拠点を含むグローバルネットワークセキュリティ体制の一部不備を原因側に挙げた。[^casio-final]

両者は矛盾と断定できない。事故前PDFは、施策・認証・教育の存在を示すが、全海外拠点・全ネットワーク境界への適用範囲、例外、更新状況、運用品質までは証明しない。本件では「ゼロトラストを掲げていたか」より、**どこまで展開済みで、どの拠点・機器・アカウントが対象外だったか**を調べる必要がある。

# 2023年事故との比較

前年のClassPad.net事故は開発環境DBの設定・運用管理が主要失敗面だった。2024年事故はフィッシング対策と海外を含むグローバルネットワーク統制が主要因として公表されており、同じ穴の再発とは言えない。[^casio-2023][^casio-final]

ただし、2年連続で異なる失敗面から重大な情報セキュリティ事故が起きたため、個別の是正完了だけでなく企業全体の統制カバレッジを長期追跡する価値が高い。

# AI/LLMとの関係

攻撃者がAIまたはLLMを本件で利用したことを示す公開証拠は確認していない。ローカルLLMが実用可能な時代の事例という意味で `era_context_only` とする。

# 防御上の教訓

- グローバル企業では本社の統制状態を海外拠点へ外挿しない。
- フィッシング耐性は教育だけでなく、認証・端末・メール・ネットワーク境界を組み合わせる。
- ゼロトラスト、ISO 27001、監視等の公表は、全資産への実装・運用カバレッジを意味しない。
- 前年事故への対処と企業全体のリスク低減を区別する。
- 二次被害としての迷惑メール等も、一次流出の確度とは分離して追跡する。

[^casio-final]: カシオ計算機「ランサムウェア攻撃による情報漏えい等調査結果について」2025-01-07.
[^casio-2023]: カシオ計算機「不正アクセスによる個人情報漏えいのお詫びとご報告」2023-10-18.
[^casio-sustainability-2023]: カシオ計算機「サステナビリティレポート2023」、ガバナンス／リスクマネジメント／情報セキュリティ、pp.243-245相当。
