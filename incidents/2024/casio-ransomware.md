---
type: Cybersecurity Incident
title: カシオ計算機 — 2024年ランサムウェア／グローバルネットワーク・フィッシング対策の不備
description: 2024年10月のランサムウェアについて、事故前の統合報告書KPI、侵害・情報流出、決算延期、事故後のSOC・第三者監査等を比較する。
resource: https://www.casio.co.jp/release/2025/0107-incident/
tags: [japan, ransomware, phishing, global-network, zero-trust, ir, casio, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: カシオ計算機株式会社
  sector: electronics
  jurisdiction: JP
  incident_status: services_mostly_restored_and_controls_strengthened
  attack_type: ransomware
  earliest_known_activity: "2024-10-05"
  detected_at: "2024-10-05"
  first_disclosed_at: "2024-10-08"
  latest_public_update: "2025-01-07 detailed investigation result; subsequent security KPIs tracked in corporate reporting"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "exact initial technique not fully disclosed; company identified weaknesses in phishing countermeasures and global network security including overseas sites"
  affected_services: "multiple internal systems and selected customer-facing services"
  data_exposure: confirmed
  availability_impact: "multiple systems unavailable; some services suspended; accounting data access disruption delayed financial reporting"
  restoration_state: "most suspended services restored after safety checks by January 2025"
  secondary_abuse: "employees reported suspicious emails apparently related to leaked information"
  regulatory_response: "PPC final report submitted 2024-12-03 and foreign data-protection authorities notified as required"
sources:
  - id: casio-final
    resource: https://www.casio.co.jp/release/2025/0107-incident/
    title: ランサムウェア攻撃による情報漏えい等調査結果について
    author: organization:カシオ計算機
  - id: casio-oct11
    resource: https://www.casio.co.jp/release/2024/1011-incident/
    title: ランサムウェア被害に伴うサービスの一部停止と情報漏えいに関するお知らせ
    author: organization:カシオ計算機
  - id: casio-ir2024
    resource: https://www.casio.co.jp/ir/library/annual/2024/
    title: 統合報告書2024
    author: organization:カシオ計算機
  - id: casio-results-delay
    resource: https://www.casio.co.jp/content/dam/casio/global/corporate/ir/2024/20241022.pdf
    title: 2025年3月期第2四半期決算発表日の延期について
    author: organization:カシオ計算機
---

# 概要

カシオ計算機は2024年10月5日、海外からの不正アクセスを受け、一部サーバーがランサムウェア攻撃により使用不能になった。10月8日にシステム障害を公表し、11日にランサムウェアと情報漏えいを確認、2025年1月7日にフォレンジック調査結果を公表した。[^final]

会社は原因説明として、サイバー攻撃増加を受けてシステム・セキュリティ強化を進めていた一方、**フィッシングメール対策と、海外拠点を含むグローバルのネットワークセキュリティ体制に一部不備があり、巧妙な攻撃に対処できなかった**と明示した。[^final]

# 事故前の公表統制

事故前に作成された統合報告書2024では、「DXの推進と情報セキュリティの強化」をマテリアリティとして扱い、ISMS認証維持、ゼロトラストネットワークのグループ会社導入率、国内外従業員への情報セキュリティ教育、システム管理者向け専門教育、サイバーセキュリティ訓練をKPI化していた。[^ir]

ゼロトラスト導入は段階目標であり、2024年度60%、2025年度90%という移行途中の指標だった。したがって本件を「ゼロトラスト導入済み企業が完全に破られた」と単純化しない。**導入率と海外拠点・例外資産を含む適用範囲**が重要である。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2024-10-05 | 一部サーバーで障害。不正アクセスの形跡を確認。[^oct11] |
| 2024-10-08 | ネットワーク不正アクセスとシステム障害を初報。 |
| 2024-10-11 | ランサムウェア、サービス一部停止、情報漏えいを公表。 |
| 2024-10-22 | 経理関連データへのアクセス制限で決算・監査手続が遅れ、第2四半期決算発表延期をIR開示。[^delay] |
| 2024-12-03 | 個人情報保護委員会へ確報。 |
| 2025-01-07 | フォレンジック調査結果、漏えい対象、原因評価、再発防止を公表。[^final] |

# 即応性

障害認知後、社内外ネットワークへのアクセス制限、外部専門家による調査、捜査機関・弁護士との連携を行った。利用停止したサービスは安全確認後に順次再開し、2025年1月時点で一部を除き復旧した。

一方、経理関連データへのアクセス遮断が決算・監査法人レビューまで遅延させた。サイバー事故時の隔離判断が財務報告へ影響するため、**セキュリティ封じ込めと決算継続の代替手順**をBCPへ含める必要がある。

# 漏えい

2025年1月公表で確認された主な個人情報は次の通り。[^final]

- 従業員等: 6,456人。
- 取引先関係者・過去の採用応募者等: 1,931人。
- 顧客: 91人。
- その他、請求書、契約書、売上、会議資料、社内システム関連データ等。

クレジットカード情報の漏えいは確認されなかった。CASIO IDやClassPad.netは別システムで稼働しており、本件影響外とされた。

# 2023年ClassPad事故との比較

カシオは2023年10月にもClassPad.net開発環境で、セキュリティ設定解除状態を原因とする個人情報漏えいを公表している。2024年ランサムウェアと同一攻撃系列ではない。

ただし企業単位では、2023年の**開発環境設定・運用管理**と、2024年の**フィッシング・海外を含むネットワーク統制**という異なる失敗境界が連続した。再発防止追跡では「同じ脆弱性の再発」だけでなく、異なる境界で重大事故が続く場合も見る必要がある。

# 事故後対策

会社はグループ全体のITセキュリティ強化、情報管理体制見直し、教育強化を表明した。後の企業資料ではSOC導入、第三者監査、フィッシング訓練等が情報セキュリティKPIとして強化されている。

事故後対策を事故前能力へ遡及させず、`planned`、`implemented`、`tested` を分離して追跡する。

# IR・株主向け影響

2024年10月22日、経理データにアクセスできない状態が決算作業・監査法人レビューを遅延させたとして、中間決算発表を延期した。[^delay]

この資料は、技術障害が**財務報告の可用性・内部統制**へ波及した一次証拠である。

# 防御上の教訓

- セキュリティKPIは「導入の有無」ではなく全社適用率を開示・監視する。
- 海外拠点・子会社を国内本社と別のセキュリティ成熟度で評価する。
- フィッシング対策は教育だけでなくメール防御、認証、端末、セッション、権限最小化を組み合わせる。
- 経理・監査に必要な証拠・データへ安全な代替アクセス手段を準備する。
- 前年事故と原因が違っても、企業全体の再発防止成熟度として横断追跡する。

# 不明点

- 初期侵入手法の完全な技術詳細。
- 海外のどの拠点・資産が最初の侵害点だったか。
- 攻撃者の滞留期間。
- 身代金要求額。会社は不当要求に応じなかったと公表。
- LLM/生成AIの利用を示す公開証拠はない。

[^final]: カシオ計算機「ランサムウェア攻撃による情報漏えい等調査結果について」2025-01-07.
[^oct11]: カシオ計算機「ランサムウェア被害に伴うサービスの一部停止と情報漏えいに関するお知らせ」2024-10-11.
[^ir]: カシオ計算機「統合報告書2024」.
[^delay]: カシオ計算機「2025年3月期第2四半期決算発表日の延期について」2024-10-22.