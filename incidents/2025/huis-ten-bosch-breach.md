---
type: Cybersecurity Incident
title: ハウステンボス — 2025年リモートアクセス経由の侵害、暗号化と約154万人規模の個人情報影響可能性
resource: https://www.huistenbosch.co.jp/htb-news/490
tags: [japan, tourism, remote-access, encryption, personal-data, bcp, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: ハウステンボス株式会社
  sector: tourism-theme-park
  jurisdiction: JP
  incident_status: restored_with_notification_followup
  attack_type: unauthorized access and data encryption
  earliest_known_activity: "2025-08-29"
  detected_at: "2025-08-29"
  first_disclosed_at: "2025-08-29"
  latest_public_update: "2025-12-12"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "リモートアクセス機器を経由して第三者がネットワークへ侵入"
  affected_services: "業務管理システム、複数サーバー、一部PC、公式アプリ待ち時間表示、一部発注等"
  data_exposure: possible
  availability_impact: "一部パーク業務・アプリ機能を制限。2025-10-01までに公表対象サービスを復旧"
  restoration_state: "通信経路再設計、認証・アカウント、デバイス管理、監視、バックアップ・BCP、教育を強化"
  regulatory_response: "検知当日に個人情報保護委員会・警察へ報告"
  secondary_abuse: not_observed
  ai_relation: era_context_only
  response_latency:
    containment_latency: "8月29日の確認後、直ちにサーバー・関連システム停止とネットワーク遮断"
    public_disclosure_latency: "同日公表"
    service_restoration_latency: "8月29日から10月1日までに公表対象サービス復旧"
sources:
  - id: htb-final
    resource: https://www.huistenbosch.co.jp/htb-news/490
    title: 不正アクセス事案に関する調査結果のご報告とお詫び
---

# 概要

ハウステンボスは2025年8月29日、システムへの不正アクセスと業務管理サーバー内ファイルの暗号化を確認した。直ちに対象サーバー・関連システムを停止しネットワークを遮断、同日中に個人情報保護委員会と警察へ報告し、外部専門家による調査・復旧を開始した。[^htb-final]

12月12日の調査結果では、リモートアクセス機器を経由して第三者がネットワークへ侵入し、複数サーバーと一部PCのデータを暗号化したことを確認した。個人情報の一部が外部に漏えいした可能性があるが、同日時点で二次被害は確認されていない。[^htb-final]

# 情報影響

漏えい可能性のある情報として、顧客約1,499,300人分、役職員・退職者・家族約37,300人分、取引先約9,400人分を公表した。役職員等の情報にはマイナンバー情報、健康診断結果、障がいに関する情報等を含む場合がある。取引先情報にも一部マイナンバー情報が含まれる。クレジットカード情報は保有していないため対象外とした。[^htb-final]

人数区分はそれぞれのステークホルダー母集団であり、重複の有無が公開情報から確定できない場合は合算値をユニーク人数として扱わない。

# 初動と事業継続

8月29日の認識後にシステム停止・ネットワーク遮断を即時実施し、同日公表・規制当局報告まで進めた。可用性影響として公式アプリのアトラクション待ち時間表示、一部発注システム、店舗レシート等に制限が生じたが、公開された影響サービスは10月1日までに復旧した。[^htb-final]

テーマパーク自体の営業継続と、内部IT・一部ゲスト向けデジタル機能の制限を分離して記録する。

# 再発防止

会社は、通信経路と用途別通信の再設計・厳格化、アカウントのセキュリティポリシーと認証方式の見直し、デバイス管理、監視体制再構築、バックアップ・BCP再整備、従業員教育を公表した。[^htb-final]

本件の公開情報だけでは、リモートアクセス機器の具体的製品名、CVE、資格情報取得方法を確定できないため推定しない。

# 防御上の教訓

- リモートアクセス機器を重要な外部境界として資産管理・認証・監視・更新の対象にする。
- 侵入後に複数サーバー・PCへ波及する前提で、通信経路・用途分離と端末管理を設計する。
- テーマパーク等では、物理サービス継続とデジタル機能・内部業務の復旧を別々のRTOとして測る。
- 健康情報・マイナンバー等は人数だけでなく長期悪用可能性を別軸で追跡する。
- 個別攻撃へのAI/LLM利用を示す公開証拠は確認していない。

[^htb-final]: ハウステンボス「不正アクセス事案に関する調査結果のご報告とお詫び」2025-12-12.