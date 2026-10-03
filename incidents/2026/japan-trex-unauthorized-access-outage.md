---
type: Cybersecurity Incident
title: 日本トレクス — 不正アクセスによる業務システム停止と安全確認後の全面再開
description: 2026年9月に確認された第三者不正アクセス、受発注・部品注文・メールの停止、代替手段での事業継続、9月30日の漏えい未確認・全面再開までを追跡する記録。
resource: https://www.trex.co.jp/news/news20260930/
tags: [japan, manufacturing, unauthorized-access, availability, business-continuity, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 日本トレクス株式会社
  sector: manufacturing
  jurisdiction: JP
  incident_status: service_restored_public_investigation_concluded
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-08"
  first_disclosed_at: "2026-09-11"
  latest_public_update: "2026-09-30"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Internet procurement/order operations, partner parts-order system, customer/partner email"
  data_exposure: not_observed
  availability_impact: confirmed
  restoration_state: "safety confirmed and all suspended operations resumed by 2026-09-30"
  secondary_abuse: not_observed
  downstream_impact: "customers and partner companies experienced ordering and communication channel disruption"
  regulatory_response: not_publicly_detailed
  notification_state: "public updates issued during investigation and recovery"
  business_continuity: "business continued using alternate procedures; parts ordering could fall back to FAX"
  data_sensitivity: "customer and business-partner information was investigated; external leakage not confirmed"
sources:
  - id: trex-first
    resource: https://www.trex.co.jp/news/news20260911-12711/
    title: 当社システムへの不正アクセスに関するお知らせ
    author: organization:日本トレクス株式会社
  - id: trex-final
    resource: https://www.trex.co.jp/news/news20260930/
    title: 当社システムへの不正アクセスに関する調査結果およびシステム再開のお知らせ
    author: organization:日本トレクス株式会社
---

# Executive summary

日本トレクスは2026年9月8日、社内システムへの第三者不正アクセスを確認し、影響拡大防止のため複数の外部接続・業務システムを停止した。停止対象にはインターネット経由の受発注、取引先向け部品注文、顧客・取引先とのメール送受信が含まれた。[^trex-first]

同社は代替手段で事業を継続し、部品注文ではFAX等の代替経路を利用できる状態を維持した。外部専門家を含む調査と安全確認を経て、9月30日に停止していた全業務の再開を公表した。同日時点で個人情報・顧客情報等の外部漏えいは確認されていない。[^trex-final]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-09-08 | 第三者による不正アクセスを確認。影響拡大防止のため関連システムを停止。[^trex-first] |
| 2026-09-11 | 初回公表。受発注、部品注文、メール等への影響と代替運用を説明。[^trex-first] |
| 2026-09-11 – 09-30 | 外部専門家を含む調査、安全性確認、復旧を継続。[^trex-final] |
| 2026-09-30 | 安全性確認後、停止していた全業務を再開。個人情報・顧客情報の外部漏えいは確認されなかったと公表。[^trex-final] |

# Impact

## Availability / business operations

停止は製造事業そのものの全面停止ではなく、受発注・部品注文・メールという業務接点に集中した。顧客・取引先との通常チャネルが利用できない期間が生じたため、可用性影響は `confirmed` とする。[^trex-first]

## Confidentiality

初期調査では情報漏えい可能性を含めて確認を進めたが、9月30日の調査結果では個人情報・顧客情報等の外部漏えいは確認されていない。これは `not_observed` であり、公開資料が侵害手法や全ログを開示しているわけではないため、絶対的な不存在証明とは扱わない。[^trex-final]

## Business continuity

業務は代替手段で継続された。特に取引先の部品注文でFAX等へ切り替えられた点は、サイバー障害時の手動/異経路フォールバックが実際の事業継続に寄与した事例である。[^trex-first]

# Technical findings

第三者不正アクセスは確認されているが、侵入経路、悪用脆弱性、認証情報、マルウェア、攻撃主体は公表されていない。「業務システム停止」という症状だけからランサムウェア等を推測しない。

# Response and recovery

- 不正アクセス確認後、影響拡大防止のため関連システムを停止。[^trex-first]
- 外部専門家を含め原因・影響範囲・情報漏えい有無を調査。[^trex-final]
- 代替チャネルで業務を継続。[^trex-first]
- 安全性を確認したうえで停止業務を全面再開。[^trex-final]

# Prognosis / current state

9月30日時点で停止業務は再開し、公開調査では外部漏えいを確認しなかった。公開情報上は `service_restored_public_investigation_concluded` とする。新たな後続事実が公表された場合は確度を更新する。

# Defensive lessons

- **業務ごとの代替チャネルを事前に持つ。** FAX等の低依存経路でも、重要なB2B注文の継続性を確保できる場合がある。
- **侵害確認後の停止範囲を業務単位で記録する。** 「会社が止まった/止まっていない」の二値では復旧状況を表せない。
- **漏えい未確認と復旧を別に評価する。** 可用性に実害があっても、最終的な機密性評価は `not_observed` となり得る。

# Unknowns / withheld details

- 初期侵入経路と侵害開始日時
- 侵害された具体的サーバー/アカウント
- 停止した各サービスの詳細な復旧時刻
- 不正アクセス主体・目的

[^trex-first]: 日本トレクス株式会社「当社システムへの不正アクセスに関するお知らせ」2026-09-11.
[^trex-final]: 日本トレクス株式会社「当社システムへの不正アクセスに関する調査結果およびシステム再開のお知らせ」2026-09-30.
