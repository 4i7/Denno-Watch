---
type: Cybersecurity Incident
title: "セレス／ポイントインカム — 会員88件・従業員等107件に閲覧可能性"
resource: https://next.ceres-inc.jp/news/detail/20261007-2/
tags: [japan, 2026, loyalty, service-suspension, data-exposure]
status: draft
stale_after: 2026-10-12T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
incident:
  organization: "セレス／ポイントインカム"
  sector: "internet-service"
  jurisdiction: "JP"
  incident_status: "investigating"
  attack_type: "unauthorized-access"
  first_disclosed_at: "2026-10-07"
  latest_public_update: "2026-10-07"
  public_record_checked_at: "2026-10-08T06:48:28.488+00:00"
  data_exposure: "possible"
  detected_at: "2026-10-05"
  affected_services: "ポイントインカム"
  availability_impact: "2026-10-05から緊急メンテナンス"
  restoration_state: "10月7日21時再開予定と公表。実際の再開を証明する公表未確認"
  regulatory_response: "PPC報告済"
  notification_state: "可能性対象会員へ個別通知"
  data_sensitivity: "195件のうち会員88件・従業員等107件。決済カード等は自社サーバで不保持"
sources:
  - id: ceres
    resource: https://next.ceres-inc.jp/news/detail/20261007-2/
    title: "ポイントインカムへの不正アクセス検知に伴う緊急メンテナンスおよびセキュリティ強化"
    author: "organization:セレス"
---

# セレス／ポイントインカム — 会員88件・従業員等107件に閲覧可能性

## 検知・規模とサービス対応

10月5日未明から不審アクセスを断続的に検知、提供を一時停止。調査により不正アクセスを確認してPPCに報告、遮断とセキュリティ点検を実施した。会員情報88件、従業員等107件、合計**195件**について第三者から閲覧された**可能性**を公表。件数を人数と同一視しない。[^ceres]

カード決済情報は自社サーバに保持していない。10月7日21時からのサービス再開を**予定**したが、予定を復旧完了の証明としない。最終復旧、実閲覧量、ポイントの不正交換、追加本人通知を確認対象とする。[^ceres]

[^ceres]: セレス「ポイントインカムへの不正アクセス検知に伴う緊急メンテナンスおよびセキュリティ強化」. https://next.ceres-inc.jp/news/detail/20261007-2/
