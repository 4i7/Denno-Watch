---
type: Cybersecurity Incident
title: "HISタイ法人 — 2025年12月検知、最大627人の旅券情報に流出可能性"
resource: https://www.his.co.jp/assets/20261007.pdf
tags: [japan, 2026, travel, passport, cross-border, long-tail]
status: draft
stale_after: 2026-10-12T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
incident:
  organization: "エイチ・アイ・エス／H.I.S. TOURS CO., LTD."
  sector: "travel"
  jurisdiction: "JP"
  incident_status: "investigating"
  attack_type: "unauthorized-file-server-access"
  first_disclosed_at: "2026-10-07"
  latest_public_update: "2026-10-07 (19:30 addendum)"
  public_record_checked_at: "2026-10-08T06:48:28.488+00:00"
  data_exposure: "possible"
  detected_at: "2025-12-11"
  earliest_known_activity: "unknown"
  affected_services: "タイ法人ファイルサーバ"
  intrusion_vector: "具体的侵入経路未公表"
  regulatory_response: "2025-12-29 PPC・JIPDECへ報告"
  notification_state: "対象者に順次個別通知、全件完了未確定"
  restoration_state: "全ファイルの人手を含む精査完了、海外管理体制強化計画"
  data_sensitivity: "最大627人の旅券氏名・性別・生年月日・番号・期限・署名欄名およびアレルギー情報"
sources:
  - id: his
    resource: https://www.his.co.jp/assets/20261007.pdf
    title: "子会社ファイルサーバへの不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ（2頁PDF）"
    author: "organization:エイチ・アイ・エス"
---

# HISタイ法人 — 2025年12月検知、最大627人の旅券情報に流出可能性

## 時系列と初動

- **2025-12-11** 検知ソフトが不正アクセスを警告し、ファイルサーバを切断。
- **2025-12-29** 日本で取得した個人情報を確認し、PPCとJIPDECへ報告。
- **2026-02-24** 保存データ中に最大627名の旅券情報が存在すると把握、全ファイル精査を決定。
- **2026-10-07** 精査完了と対象者への順次通知を公表、19:30に一部項目を追記。[^his]

## データと確度

第三者にファイルの一部を不正に引き出された**可能性**があり、影響候補は2017、2019〜20、2024〜25年に日本からタイへ出発した一部顧客最大627人。旅券情報とアレルギー情報はデータ感度が高い。電話、住所、メール、カード情報は対象外。**627人全員のファイル外部取得が確認されたわけではない**。[^his]

## 調査長期化と予後

会計情報等の大量の無関係ファイルと形式の混在により、機械的検索が難しく、人手で照合したと説明。検知、当局報告、対象人数の把握、公表と連絡を混同しない。最終的な悪用、通知完了、海外子会社の継続監査実績は未確認。[^his]

[^his]: エイチ・アイ・エス「子会社ファイルサーバへの不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ（2頁PDF）」. https://www.his.co.jp/assets/20261007.pdf
