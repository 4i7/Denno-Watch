---
type: Cybersecurity Incident
title: カシオ計算機 — 2024年ランサムウェア攻撃とグローバルネットワーク統制の不備
description: 2024年10月5日に海外から侵入され、ランサムウェアでシステムが使用不能となり社内文書・個人情報が流出。前年のClassPad.net事故と分離しつつ統制の継続性を比較する。
resource: https://www.casio.co.jp/release/2025/0107-incident/
tags: [japan, electronics, ransomware, phishing, global-network, data-exfiltration, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
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
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: "overseas-origin intrusion; public root-cause analysis identified gaps in phishing countermeasures and global network security including overseas bases"
  affected_services: "internal servers and multiple services; CASIO ID and ClassPad.net were on separate systems and not affected"
  data_exposure: confirmed
  availability_impact: "multiple systems/services stopped; most later resumed"
  restoration_state: "most affected services resumed after safety checks; forensic investigation completed to publicly available extent"
  regulatory_response: "final report submitted to PPC 2024-12-03 and overseas regulators as applicable"
  secondary_abuse: "employee-targeted spam plausibly related to the incident was reported"
  ai_relation: era_context_only
sources:
  - id: casio-final
    resource: https://www.casio.co.jp/release/2025/0107-incident/
    title: ランサムウェア攻撃による情報漏えい等調査結果について
  - id: casio-2023
    resource: https://www.casio.co.jp/release/2023/1018-incident/
    title: 不正アクセスによる個人情報漏えいのお詫びとご報告
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

# 2023年事故との比較

前年のClassPad.net事故は開発環境DBの設定・運用管理が主要失敗面だった。2024年事故はフィッシング対策と海外を含むグローバルネットワーク統制が主要因として公表されており、同じ穴の再発とは言えない。[^casio-2023][^casio-final]

一方、事故前の統合報告・サステナビリティ資料ではCSIRT、BCP、グループセキュリティ、ゼロトラストを含む強化方針を公表していた。したがって長期評価では、個別対策の導入有無より**海外拠点まで含む実装範囲と運用品質**を確認する必要がある。

# 防御上の教訓

- グローバル企業では本社の統制状態を海外拠点へ外挿しない。
- フィッシング耐性は教育だけでなく、認証・端末・メール・ネットワーク境界を組み合わせる。
- 前年事故への対処と企業全体のリスク低減を区別する。
- 二次被害としての迷惑メール等も、一次流出の確度とは分離して追跡する。
- AI/LLM利用を示す公開証拠はない。

[^casio-final]: カシオ計算機「ランサムウェア攻撃による情報漏えい等調査結果について」2025-01-07.
[^casio-2023]: カシオ計算機「不正アクセスによる個人情報漏えいのお詫びとご報告」2023-10-18.