---
type: Cybersecurity Incident
title: アスクル — 2025年ランサムウェア攻撃、長期潜伏と統制カバレッジの欠落
description: 2025年6月5日の初期侵入から10月19日のランサムウェア検知までの長期潜伏、MFA例外、サーバーEDR・24時間監視・バックアップ設計の不足、サービス停止とIR影響を追跡する。
resource: https://pdf.irpocket.com/C0032/PDLX/O3bg/N4O3.pdf
tags: [japan, ecommerce, logistics, ransomware, identity, mfa, edr, backup, business-continuity, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: アスクル株式会社
  sector: ecommerce-logistics
  jurisdiction: JP
  incident_status: restored_with_remediation_followup
  attack_type: ransomware, credential abuse, lateral movement, data exfiltration
  earliest_known_activity: "2025-06-05"
  detected_at: "2025-10-19"
  first_disclosed_at: "2025-10-19"
  latest_public_update: "2026-08-04"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: "委託先作業用の管理アカウントのID・パスワードを悪用。取得方法は公表上特定されていない。対象アカウントはMFA適用の例外だった"
  affected_services: "ASKUL、ソロエルアリーナ、LOHACO、物流・受注関連システム、外部クラウドの一部"
  data_exposure: confirmed
  availability_impact: "Web受注・出荷等を大規模停止し、段階的に再開"
  restoration_state: "新しい安全なネットワーク・システム構成で段階復旧。2026年も通知・監視高度化・BCP強化を継続"
  regulatory_response: "関係当局・警察等と連携。対象者への個別通知を継続"
  market_disclosure: "決算発表延期、半期報告書提出期限延長、特別損失、通期業績予想取り下げ、配当予想修正、役員報酬減額へ波及"
  ai_relation: era_context_only
  response_latency:
    detection_latency: "公開調査で確認された初期侵入2025-06-05からランサムウェア検知2025-10-19まで約4か月半"
    containment_latency: "10-19検知後、同日ネットワークを物理的に遮断し全パスワード変更を開始。ただし10-22に外部クラウドへの不正アクセスが発生し、主要クラウドのパスワード変更完了は10-23"
    service_restoration_latency: "10-29から一部出荷を試行し、11-12にWeb注文を段階再開。完全な事業回復は複数月に及んだ"
  pre_incident_control_disclosure:
    state: confirmed
    published_at: "2024"
    sources: [askul-report-2024]
    declared_controls: ["情報セキュリティを重要な経営課題として位置付け", "ISMS", "サーバー増強・分散・モダナイズ", "基幹システム冗長化", "バックアップ体制", "セキュリティ強化"]
    applicability_to_failure_surface: direct_and_partial
  market_ir_effect:
    disclosure_present: confirmed
    disclosure_channels: [timely_disclosure, earnings, securities_report]
    accounting_or_reporting_delay: confirmed
    disclosed_financial_effect: "2026-01-28にサイバー攻撃関連の特別損失、通期業績予想取り下げ、配当予想修正等を開示"
    executive_accountability: "役員報酬減額を開示"
sources:
  - id: askul-final
    resource: https://pdf.irpocket.com/C0032/PDLX/O3bg/N4O3.pdf
    title: ランサムウェア攻撃の影響調査結果および安全性強化に向けた取り組みのご報告
  - id: askul-security
    resource: https://www.askul.co.jp/corp/security/
    title: アスクルのサイバーセキュリティ
  - id: askul-ir
    resource: https://www.askul.co.jp/corp/investor/release/
    title: IRニュース
  - id: askul-report-2024
    resource: https://www.askul.co.jp/corp/assets/pdf/ir_2024j_04.pdf
    title: ASKUL Report 2024 — リスクマネジメント・情報セキュリティ関連部分
---

# 概要

アスクルは2025年10月19日にランサムウェア攻撃を検知し、ASKUL、ソロエルアリーナ、LOHACO等のサービスを停止した。後日の外部専門機関を含む調査では、確認できる最初の侵入は**2025年6月5日**まで遡り、6月から10月にかけて内部探索と権限拡大・横展開が進んだ後、10月19日に複数種のランサムウェアが実行された。[^askul-final]

したがって本件は、ランサムウェアが可視化された10月19日だけを「攻撃開始」と扱うと、約4か月半の攻撃準備期間を失う事例である。

# 初期侵入と発生時の統制環境

調査では、委託先作業に利用されていた管理アカウントのID・パスワードが何らかの方法で攻撃者に取得され、不正利用された。このアカウントはMFA適用の例外だった。認証情報がどのように流出したかは公表上特定されていないため、フィッシング、端末マルウェア等を推定しない。[^askul-final]

攻撃者は侵入後、EDRや脆弱性対策ソフトの停止、内部探索、横展開を行った。データセンター内の一部サーバーにはEDRが導入されておらず、24時間365日の監視対象にもなっていなかったことが、検知遅延の一因として事故後に説明された。[^askul-final]

# 初動と封じ込め

10月19日朝の検知後、ネットワークを物理的に遮断し、全パスワード変更を開始した。同日14時には事業継続・IT復旧を含む対策体制を設け、16時30分頃までに主要サービスの注文・出荷を停止した。[^askul-final]

一方で、10月22日には外部クラウドサービスへの不正アクセスが発生し、主要外部クラウドのパスワード変更完了は10月23日、認証情報リセット、管理アカウントMFA、EDRシグネチャ更新は10月24日となった。[^askul-security] このため「10月19日のネットワーク遮断＝全攻撃面の封じ込め完了」とは評価しない。

# 情報流出と証拠限界

2025年12月12日までの調査で、法人向け顧客約59万件、個人向け顧客約13.2万件、取引先関係約1.5万件、従業員等約2,700件を含む情報流出が確認された。[^askul-final] 一部ログが失われているため、調査で確認できた範囲を「理論上の最大影響」と同一視しない。

LOHACOのクレジットカード情報は同社が受け取らない構成であり、保有していない情報まで被害対象へ拡張しない。[^askul-security]

# バックアップと復旧

オンラインバックアップは存在したが、ランサムウェアへの耐性を持つ構成になっておらず、一部バックアップも暗号化された。[^askul-final] 事故後は、侵害機器・サーバーを新環境へそのまま戻すのではなく、安全確認済みの新しいネットワーク構成でシステムを再構築し、10月29日から出荷試行、11月12日からWeb注文を段階再開した。[^askul-security]

この事例では「バックアップがあるか」ではなく、攻撃者からの分離、復元可能性、クリーンな復旧先、復旧時の認証情報再確立まで確認する必要がある。

# 事故前の公表統制との比較

ASKUL Report 2024では、情報セキュリティを重要な経営課題として扱い、システム障害・サイバー攻撃に対するサーバーの増強・分散・モダナイズ、ネットワーク増強、基幹システム冗長化、バックアップ体制、セキュリティ強化をリスク対応として記載していた。また、個人情報・機密情報についてISMSを含む管理体制を説明していた。[^askul-report-2024]

事故後に判明したのは、これらの高位統制が存在しなかったという単純な話ではなく、**MFAの例外、サーバーEDRの未適用、24時間監視の対象外、オンラインバックアップのランサムウェア耐性不足**という具体的なカバレッジと設計の穴だった。[^askul-final]

従って、統合報告書に「MFA」「EDR」「バックアップ」「ISMS」等が存在するかだけでなく、例外アカウント数、サーバーカバレッジ、監視対象、復元試験の実績を確認する必要がある。

# 株主・財務への予後

事故は物流・販売だけでなく財務報告へ波及した。2025年12月には第2四半期決算発表の延期、半期報告書提出期限の延長が公表され、2026年1月28日にはサイバー攻撃に伴う特別損失、通期連結業績予想の取り下げ、中間・期末配当予想の修正、役員報酬減額が適時開示された。[^askul-ir]

2026年8月4日時点のサイバーセキュリティページでは、SaaSを含むログ監視、EDR、SOCによる24時間365日監視、IT/OT統合リスク、教育・訓練、BCP、外部評価等を継続強化策として公表している。[^askul-security] 事故後の対策は、発表済みであることと実装・試験済みであることを分離して今後も追跡する。

# AI/LLMとの関係

攻撃者がAIまたはLLMを本件で利用したことを示す公開証拠は確認していない。`era_context_only` とし、2025年という時代背景だけを保持する。

# 防御上の教訓

- MFAの導入率だけでなく、特権・委託先・緊急用等の例外をゼロベースで監査する。
- EDR/SOCは「導入済み」ではなく、サーバー・クラウド・SaaSを含む実カバレッジを測る。
- ネットワーク遮断後もクラウド認証情報が生きていれば攻撃面は残る。
- バックアップは攻撃者から独立し、復元試験済みでなければランサムウェア時の復旧能力を意味しない。
- 技術復旧だけでなく、物流、決算、法定開示、配当、経営責任まで長期予後として追跡する。

[^askul-final]: アスクル「ランサムウェア攻撃の影響調査結果および安全性強化に向けた取り組みのご報告」2025-12-12.
[^askul-security]: アスクル「アスクルのサイバーセキュリティ」最終確認2026-10-05、ページ更新2026-08-04.
[^askul-ir]: アスクル「IRニュース」2025-10〜2026-10公表一覧.
[^askul-report-2024]: アスクル「ASKUL Report 2024」情報セキュリティ・リスクマネジメント関連部分.
