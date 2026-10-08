---
type: Cybersecurity Incident
title: IDCフロンティア — IDCFクラウドのランサムウェア／495企業・自治体に障害
description: IDCFクラウドのランサムウェア／495企業・自治体に障害
resource: https://www.idcf.jp/news/topics/20261007002
tags: [japan, 2026, cloud, ransomware, infrastructure, outage, shared-infrastructure]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 株式会社IDCフロンティア
  sector: cloud-infrastructure
  jurisdiction: JP
  incident_status: ongoing_incident_response
  attack_type: ransomware-confirmed
  detected_at: "2026-10-07 03:40 JST"
  first_disclosed_at: "2026-10-07"
  latest_public_update: "2026-10-07"
  public_record_checked_at: "2026-10-08T06:48:28.488+00:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "IDCFクラウドのランサムウェア／495企業・自治体に障害"
  data_exposure: unknown
  availability_impact: "東日本リージョン1遮断と他リージョンの管理コンソール停止、契約495組織への影響"
  restoration_state: "封じ込め実施、侵入経路特定中、全面復旧は未確認"
  downstream_impact: "ファイバーゲートはIDCF基盤利用を明示、ニッスイは日水物流の入出荷停止を公表するが一次資料には委託先名なし"
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.idcf.jp/news/topics/20261007002
    title: 発表資料／本文
    author: organization:株式会社IDCフロンティア 
  - id: source-1
    resource: https://www.idcf.jp/news/topics/20261007001
    title: 10月7日初報
    author: organization:公開資料 
  - id: fibergate
    resource: https://www.fibergate.co.jp/news/14742/
    title: クラウドサーバー停止に伴うサービス影響について
    author: organization:株式会社ファイバーゲート
  - id: nissui
    resource: https://www.nissui.co.jp/news/2026100702.html
    title: 日水物流株式会社におけるシステム障害について（第1報）
    author: organization:株式会社ニッスイ
  - id: source-2
    resource: https://www.idcf.jp/pdf/cloud/pdf/IDCFCloud_security_WP.pdf
    title: 2026年4月1日発行IDCFクラウドセキュリティホワイトペーパー第13版
    author: organization:公開資料 
---

# IDCフロンティア — IDCFクラウドのランサムウェア／495企業・自治体に障害

## 事実・経過

2026年10月7日午前3時40分頃からIDCFクラウドの東日本リージョン1に障害が発生。初報では不正アクセスとされ、第2報において**ランサムウェア攻撃**と判明した。影響範囲はサービスを契約する**495の企業・自治体**。[^source-0]

被害拡大・漏えい防止のため対象リージョンのネットワークを遮断しシステムを停止した。他リージョンの外部公開管理コンソールも安全確認の間停止している。侵入経路、復旧時期、データ持ち出しの有無は調査中である。495は**影響顧客の組織数**であり、漏えい件数でも人数でもない。[^source-0]

## 10月7日 下流のサービス・物流影響

**ファイバーゲート**は、自社のサービス・関連システムがIDCフロンティアのクラウド基盤に依存しており、IDCF側のランサムウェア攻撃による遮断・仮想マシン停止の影響を受けたと明示。顧客別復旧の実績・日時は別途確認する。[^fibergate]

**ニッスイ**は日水物流のシステム障害により、取り扱う商品の**入出荷ができない**と公表。委託先データセンターへの不正アクセスが原因とみられるが、ニッスイの一次公表は**IDCフロンティアという事業者名を示していない**。外部報道による関連付けとは明確に分離し、公式公表だけで同一インシデントだと確定しない。ニッスイ側の個人情報・顧客データ流出も調査中。[^nissui]

495は顧客組織数であり、すべての組織が商品入出荷停止を経験した数ではない。供給者の隔離・復旧と利用者の業務再開を別々に追跡する。

## 事故前に公表された統制の比較

同社の2026年4月のセキュリティホワイトペーパー8〜9ページは、クラウド管理コンソールでの二段階認証の提供、管理者による適用強制、接続元IP制限、定期的な脆弱性診断、24時間監視体制、検知から30分以内の顧客通知を**目標**として記載する。[^source-2]

これは平時の**制度・機能の説明**であって、今回の侵害経路が管理コンソールだった証明でも、当該対策が破られた証明でも、通知目標の遵守実績でもない。後続の調査と通知実測値で対照する必要がある。

## 未確定

正確な侵入口、データ流出、別リージョンへの侵害、全顧客の復旧、財務影響、身代金要求はいずれも未確定。

[^source-0]: 発表資料／本文 — https://www.idcf.jp/news/topics/20261007002 （2026-10-08確認）。
[^source-1]: 10月7日初報 — https://www.idcf.jp/news/topics/20261007001 （2026-10-08確認）。
[^fibergate]: ファイバーゲート「クラウドサーバー停止に伴うサービス影響について」2026-10-07. https://www.fibergate.co.jp/news/14742/
[^nissui]: ニッスイ「日水物流株式会社におけるシステム障害について（第1報）」2026-10-07. https://www.nissui.co.jp/news/2026100702.html
[^source-2]: 2026年4月1日発行IDCFクラウドセキュリティホワイトペーパー第13版 — https://www.idcf.jp/pdf/cloud/pdf/IDCFCloud_security_WP.pdf （2026-10-08確認）。
