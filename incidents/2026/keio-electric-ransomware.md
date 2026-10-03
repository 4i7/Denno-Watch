---
type: Cybersecurity Incident
title: 京王電鉄グループ — ランサムウェア攻撃によるシステム障害
description: 2026年9月26日に確認された京王電鉄グループのランサムウェア被害と公開範囲の影響・対応記録。
resource: https://www.keio.co.jp/news/update/announce/nr260926v13404/
tags: [japan, transportation, ransomware, availability, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: 京王電鉄株式会社
  sector: transportation
  jurisdiction: JP
  incident_status: investigating
  attack_type: ransomware
  earliest_known_activity: unknown
  detected_at: "2026-09-26 (pre-dawn; exact time not publicly disclosed)"
  first_disclosed_at: "2026-09-26"
  latest_public_update: "2026-09-26"
  intrusion_vector: not_publicly_disclosed
  affected_services: "some sales/business systems at group companies"
  data_exposure: not_observed
  availability_impact: confirmed
  restoration_state: unknown
  secondary_abuse: not_observed
sources:
  - id: keio-20260926
    resource: https://www.keio.co.jp/news/update/announce/nr260926v13404/
    title: ランサムウェア攻撃によるシステム障害に関するお知らせとお詫び
  - id: keio-news-index
    resource: https://www.keio.co.jp/news/update/announce/news_all.html
    title: 京王電鉄 お知らせ一覧
---

# Executive summary

京王電鉄は2026年9月26日未明、同社グループのサーバーに対するランサムウェア攻撃と、それに伴うシステム障害を確認した。公表時点で一部グループ会社の営業システムに支障が出ていた一方、鉄道運行への支障はないとされた。情報漏えいは確認されていなかったが、事業上の機密事項や顧客情報を含む影響範囲の調査は継続中だった。[^keio-20260926]

同社は被害拡大防止のためネットワーク遮断を実施し、警察へ通報したうえで外部専門家と攻撃経路・被害範囲を調査している。[^keio-20260926]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-09-26 未明 | 京王電鉄がグループサーバーへのランサムウェア攻撃を確認。[^keio-20260926] |
| 2026-09-26 | 被害拡大防止のためネットワークを遮断。警察への通報、外部専門家を交えた侵入経路・影響調査を開始。[^keio-20260926] |
| 2026-09-26 | 一部グループ会社の営業システムへの支障を公表。鉄道運行への支障なし、情報漏えいは未確認と説明。[^keio-20260926] |
| 2026-10-03 review | 京王電鉄のお知らせ一覧上で、このランサムウェア事案に明示的に紐づく追加報告は確認できていない。9月28日以降の個別システム障害告知は、公式に因果関係が示されない限り本事案へ統合しない。[^keio-news-index] |

# Impact

## Availability

一部グループ会社の営業システムに支障が発生したことが確認されている。影響対象会社、停止機能、停止期間、復旧率は初報では公表されていない。[^keio-20260926]

鉄道運行は初報時点で支障なしと明示された。したがって、本記録では交通運行そのものへの影響を推定しない。[^keio-20260926]

## Confidentiality

京王電鉄は事業機密・顧客情報を含む流出可能性を調査しているが、初報時点では情報漏えいの事実を確認していない。これは「漏えいなしの確定」ではなく、調査時点での `not_observed` として扱う。[^keio-20260926]

## Integrity

データ改ざん・破壊の有無は公開されていない。ランサムウェアという分類だけから暗号化範囲や破壊行為を推測しない。

# Technical findings

公開情報で確認できる技術的事実は、グループサーバーへの攻撃がランサムウェアによるものと確認されたことまでである。ランサムウェアの名称、初期侵入経路、認証情報の悪用有無、横展開経路、暗号化対象、データ窃取の有無、侵害開始時刻は公表されていない。[^keio-20260926]

# Response and recovery

確認直後にネットワーク遮断による封じ込めを実施し、警察への通報と外部専門家による調査へ移行した。[^keio-20260926]

公開情報だけでは、復旧完了時期、再構築範囲、認証情報の失効、EDR/監視強化などの具体的な復旧・再発防止策はまだ判断できない。

# Prognosis / current state

2026年10月3日時点の公開記録では調査中として扱う。初報後の追加公表が出れば、情報漏えいの有無、影響したグループ会社と業務、復旧時期、侵入経路、再発防止策を優先して更新する。

# Defensive lessons

現時点で一般化できる公開事実は限定的だが、攻撃確認後にネットワーク遮断を即時実施し、事業継続上重要な鉄道運行とその他グループ業務の影響を分離して公表した点は、封じ込めと影響評価を別軸で管理する事例として有用である。[^keio-20260926]

# Unknowns / withheld details

- 最初の侵害時刻と侵入経路
- ランサムウェアの名称・攻撃主体
- 暗号化・破壊された資産の範囲
- データ窃取または外部送信の有無
- 影響を受けたグループ会社・業務の具体的範囲
- 復旧状況と再発防止策
- 初報後に告知された個別システム障害との因果関係

[^keio-20260926]: 京王電鉄「ランサムウェア攻撃によるシステム障害に関するお知らせとお詫び」2026-09-26.
[^keio-news-index]: 京王電鉄「お知らせ」一覧。2026-10-03確認。
