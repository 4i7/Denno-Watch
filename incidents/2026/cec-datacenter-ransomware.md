---
type: Cybersecurity Incident
title: シーイーシー — 東京第二データセンターのランサムウェア障害
description: 2026年8月5日に発生したデータセンターサービス障害について、ランサムウェア確認から最終調査までを追跡する記録。
resource: https://www.cec-ltd.co.jp/news/2026/7385.html
tags: [japan, data-center, ransomware, availability, managed-services, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: 株式会社シーイーシー
  sector: information-technology-and-data-center
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: ransomware
  earliest_known_activity: not_publicly_disclosed
  detected_at: "2026-08-05 11:00 JST (approximately; outage/unauthorized access)"
  first_disclosed_at: "2026-08-06"
  latest_public_update: "2026-09-03"
  intrusion_vector: "identified by investigator but intentionally not publicly disclosed"
  affected_services: "a service area at Tokyo Second Data Center; temporary service outages for some customers"
  data_exposure: not_observed
  availability_impact: confirmed
  restoration_state: "restored in a safe/rebuilt environment; investigation completed"
  secondary_abuse: not_observed
sources:
  - id: cec-first
    resource: https://www.cec-ltd.co.jp/news/2026/7371.html
    title: 当社データセンターサービスの障害発生のお知らせ（第1報）
  - id: cec-ransomware
    resource: https://www.cec-ltd.co.jp/news/2026/7372.html
    title: 当社データセンターサービスの障害発生のお知らせ（続報）
  - id: cec-followup
    resource: https://www.cec-ltd.co.jp/news/2026/7378.html
    title: 当社データセンターサービスの障害発生のお知らせ（続報）
  - id: cec-final
    resource: https://www.cec-ltd.co.jp/news/2026/7385.html
    title: 当社データセンターサービスの障害発生のお知らせ（最終報）
---

# Executive summary

シーイーシー（CEC）は2026年8月5日11時頃、東京第二データセンターで不正アクセスに起因する障害を確認し、一部サービスに影響が発生した。翌8月7日までに原因をランサムウェア攻撃と確認した。[^cec-first][^cec-ransomware]

攻撃を受けた領域は、顧客から預かるシステム・データとは別領域だった。影響領域を隔離し、影響サービスを別環境で復旧した後、9月3日の最終報で調査完了と安全性確認を公表した。通信記録・トラフィックおよび復元データ・ログの解析では外部への異常通信や情報漏えいは確認されず、関連する顧客システムへの影響もないと判断された。[^cec-followup][^cec-final]

ランサムウェアの種別と侵入経路は特定済みだが、セキュリティ上の理由で詳細は非公表である。[^cec-final]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-08-05 11:00頃 | 東京第二データセンターで不正アクセスに起因する障害が発生。後にランサムウェアと確認される。[^cec-first][^cec-ransomware] |
| 2026-08-06 | 第1報。サービスは復旧済みと公表し、サイバー攻撃の可能性を調査。[^cec-first] |
| 2026-08-07 | ランサムウェア攻撃と確認。警察へ被害報告、個人情報保護委員会へ漏えい可能性がある事案として第一報。攻撃領域は顧客システム・データとは別領域と判明。[^cec-ransomware] |
| 2026-08-21 | 攻撃領域の隔離・遮断完了、影響サービスは別環境で復旧済み。ランサムウェア種別と侵入経路を特定し、経路遮断済みと公表。[^cec-followup] |
| 2026-09-03 | 最終報。社内調査完了、安全性確認。外部への異常通信および情報漏えいなし、関連システムへの影響なしと判断。[^cec-final] |

# Impact

## Availability

一部顧客に一時的なサービス停止が発生し、CECは対象顧客へ個別連絡を行った。具体的な顧客数、停止サービス名、停止時間は公開資料では示されていない。[^cec-final]

## Confidentiality

8月7日時点では漏えい可能性を否定しきれず個人情報保護委員会へ報告していたが、最終調査では攻撃時期から障害発生日までの外部通信記録・トラフィックに異常通信がないこと、復元データとログにも情報漏えいを示す結果がないことを確認した。[^cec-ransomware][^cec-final]

攻撃領域は顧客から預かるシステム・データとは分離されており、関連顧客システムへの影響と情報漏えいもないと判断された。[^cec-final]

## Integrity

ランサムウェアにより攻撃領域が影響を受け、復元作業が行われたことは公表されているが、暗号化・改ざん・破壊された具体的なファイルやデータ量は公表されていない。[^cec-followup]

# Technical findings

CECはランサムウェアの種別と侵入経路を特定したが、詳細は意図的に非公表とした。したがって本記録でもファミリ名や侵入ベクトルを推測しない。[^cec-final]

公開情報から確認できる構造上の重要点は、侵害領域が顧客預かりシステム・データの領域と分離されていたこと、侵入経路特定後に当該経路を遮断したこと、復旧を同じ侵害領域の継続利用ではなく別/再構築環境で実施したことである。[^cec-followup][^cec-final]

# Response and recovery

- 攻撃領域を隔離・遮断。[^cec-followup]
- 影響サービスを別環境で復旧。[^cec-followup]
- 複数の外部専門機関を含むフォレンジック、通信記録・トラフィック、復元データ・ログ解析を実施。[^cec-followup][^cec-final]
- 警察および個人情報保護委員会へ報告。[^cec-ransomware][^cec-final]
- インターネット接続機器と通信経路の再評価・総点検、ネットワーク防衛・監視体制の増強を再発防止策として表明。[^cec-final]

# Prognosis / current state

9月3日の最終報で調査完了、安全性確認、サービス継続が公表されているため、公開情報上は `public_report_closed` とする。新たな後続被害が公開されない限り、定期更新を要する進行中インシデントとは扱わない。

# Defensive lessons

- **管理・サービス領域の分離は被害境界を狭める。** 顧客システム/データと攻撃領域が別だったことが、最終的な顧客データ影響評価の重要な根拠になった。[^cec-final]
- **復旧とフォレンジックを並行する。** 影響サービスを別環境で復旧しつつ、侵害領域の復元データ・ログを調査できた。[^cec-followup][^cec-final]
- **初期報告の不確実性を更新する。** 当初は漏えい可能性として規制当局へ報告し、最終調査で「漏えいなし」と結論を更新している。[^cec-ransomware][^cec-final]

# Unknowns / withheld details

- ランサムウェアのファミリ名
- 具体的な初期侵入経路と利用された脆弱性/認証経路
- 侵害開始時刻
- 一時停止した具体的サービス・顧客数・停止時間
- 暗号化・破壊された資産の具体的範囲

[^cec-first]: CEC「当社データセンターサービスの障害発生のお知らせ（第1報）」2026-08-06.
[^cec-ransomware]: CEC「当社データセンターサービスの障害発生のお知らせ（続報）」2026-08-07.
[^cec-followup]: CEC「当社データセンターサービスの障害発生のお知らせ（続報）」2026-08-21.
[^cec-final]: CEC「当社データセンターサービスの障害発生のお知らせ（最終報）」2026-09-03.
