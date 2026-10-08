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
  public_record_checked_at: "2026-10-08T14:54:00+09:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "IDCFクラウドのランサムウェア／495企業・自治体に障害"
  data_exposure: unknown
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
  - id: source-2
    resource: https://www.idcf.jp/pdf/cloud/pdf/IDCFCloud_security_WP.pdf
    title: 2026年4月1日発行IDCFクラウドセキュリティホワイトペーパー第13版
    author: organization:公開資料 
---

# IDCフロンティア — IDCFクラウドのランサムウェア／495企業・自治体に障害

## 事実・経過

2026年10月7日午前3時40分頃からIDCFクラウドの東日本リージョン1に障害が発生。初報では不正アクセスとされ、第2報において**ランサムウェア攻撃**と判明した。影響範囲はサービスを契約する**495の企業・自治体**。[^source-0]

被害拡大・漏えい防止のため対象リージョンのネットワークを遮断しシステムを停止した。他リージョンの外部公開管理コンソールも安全確認の間停止している。侵入経路、復旧時期、データ持ち出しの有無は調査中である。495は**影響顧客の組織数**であり、漏えい件数でも人数でもない。[^source-0]

## 事故前に公表された統制の比較

同社の2026年4月のセキュリティホワイトペーパー8〜9ページは、クラウド管理コンソールでの二段階認証の提供、管理者による適用強制、接続元IP制限、定期的な脆弱性診断、24時間監視体制、検知から30分以内の顧客通知を**目標**として記載する。[^source-2]

これは平時の**制度・機能の説明**であって、今回の侵害経路が管理コンソールだった証明でも、当該対策が破られた証明でも、通知目標の遵守実績でもない。後続の調査と通知実測値で対照する必要がある。

## 未確定

正確な侵入口、データ流出、別リージョンへの侵害、全顧客の復旧、財務影響、身代金要求はいずれも未確定。

[^source-0]: 発表資料／本文 — https://www.idcf.jp/news/topics/20261007002 （2026-10-08確認）。
[^source-1]: 10月7日初報 — https://www.idcf.jp/news/topics/20261007001 （2026-10-08確認）。
[^source-2]: 2026年4月1日発行IDCFクラウドセキュリティホワイトペーパー第13版 — https://www.idcf.jp/pdf/cloud/pdf/IDCFCloud_security_WP.pdf （2026-10-08確認）。
