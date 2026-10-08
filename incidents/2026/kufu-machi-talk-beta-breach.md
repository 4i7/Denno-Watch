---
type: Cybersecurity Incident
title: "くふう まちトークβ版 — メールアドレス流出確認・サービス停止"
resource: https://kufu.co.jp/2026/10/05/kufu-announce/
tags: [japan, 2026, community, data-breach, service-suspension]
status: draft
stale_after: 2026-10-12T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
incident:
  organization: "くふうカンパニー／くふう まちトークβ版"
  sector: "consumer-platform"
  jurisdiction: "JP"
  incident_status: "investigating"
  attack_type: "unauthorized-access"
  first_disclosed_at: "2026-10-05"
  latest_public_update: "2026-10-05"
  public_record_checked_at: "2026-10-08T06:48:28.488+00:00"
  data_exposure: "confirmed"
  detected_at: "2026-10-02"
  affected_services: "くふう まちトークβ版"
  availability_impact: "2026-10-05停止"
  restoration_state: "安全確認後に再開予定、日時未公表"
  data_sensitivity: "少なくとも1名のメールは実漏えい確認、生年月日・性別は可能性"
  notification_state: "可能性対象者を含め順次通知"
  regulatory_response: "PPC報告済"
sources:
  - id: machi
    resource: https://kufu.co.jp/2026/10/05/kufu-announce/
    title: "くふう まちトークβ版への不正アクセスに関するお知らせとお詫び"
    author: "organization:くふうカンパニー"
---

# くふう まちトークβ版 — メールアドレス流出確認・サービス停止

## 情報被害と未確定範囲

10月2日に不審なアクセスを確認、第三者からの侵入と判定し、10月5日にβ版サービスを停止。**少なくとも1名のメールアドレスの実漏えいを確認**した。一方、生年月日・性別の漏えいは可能性にとどまり、影響人数の全容も調査中。[^machi]

対象者へ順次個別連絡しPPCへ報告。安全性確認後の再開を予定するが、完了と扱わない。Zaimの9月情報改ざんとは**同じ会社の別事故**。二件の同一犯行や共通入口との証拠はない。[^machi]

[^machi]: くふうカンパニー「くふう まちトークβ版への不正アクセスに関するお知らせとお詫び」. https://kufu.co.jp/2026/10/05/kufu-announce/
