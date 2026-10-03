---
type: Cybersecurity Incident
title: 池上通信機 — サーバー不正アクセス・ファイル暗号化と攻撃者サイト上の情報掲載確認
description: 2026年9月21日の外部情報を契機に発覚したサイバー攻撃、サーバーの暗号化、内部ネットワーク遮断、10月2日の攻撃者サイト掲載確認までを追跡する記録。
resource: https://www.ikegami.co.jp/news/detail/574/
tags: [japan, manufacturing, cyberattack, encryption, leak-site, availability, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 池上通信機株式会社
  sector: broadcasting-and-electronics-manufacturing
  jurisdiction: JP
  incident_status: investigating_and_network_isolated
  attack_type: "cyberattack with unauthorized server access and file encryption; ransomware family not publicly identified"
  earliest_known_activity: unknown
  detected_at: "2026-09-21 external information prompted investigation"
  first_disclosed_at: "2026-09-24"
  latest_public_update: "2026-10-02"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "some internal servers and internal network"
  data_exposure: "confirmed publication of information believed held by the company; exact authenticity/content/scope under investigation"
  availability_impact: "internal network disconnected; operational details not fully disclosed"
  restoration_state: "network isolation and investigation ongoing"
  secondary_abuse: unknown
  downstream_impact: unknown
  regulatory_response: not_publicly_detailed
  notification_state: "scope/content investigation continues"
  business_continuity: "internal network isolation maintained while investigating"
  data_sensitivity: "information believed to be company-held was observed on an attacker site; detailed categories not yet confirmed"
sources:
  - id: ikegami-first
    resource: https://www.ikegami.co.jp/news/detail/571/
    title: 当社に対するサイバー攻撃の可能性に関するお知らせ
    author: organization:池上通信機株式会社
  - id: ikegami-second
    resource: https://www.ikegami.co.jp/news/detail/573/
    title: 当社に対するサイバー攻撃に関するお知らせ（第2報）
    author: organization:池上通信機株式会社
  - id: ikegami-third
    resource: https://www.ikegami.co.jp/news/detail/574/
    title: 当社に対するサイバー攻撃に関するお知らせ（第3報）
    author: organization:池上通信機株式会社
---

# Executive summary

池上通信機は2026年9月21日、同社へのサイバー攻撃を示唆する外部情報を把握したことを契機に調査を開始した。9月30日の第2報で、一部サーバーに外部からの不正アクセスを示す痕跡と、一部ファイルの暗号化を確認したと公表し、内部ネットワークの遮断を継続した。[^ikegami-first][^ikegami-second]

10月2日の第3報では、攻撃者が運営するサイト上に同社が保有していたとみられる情報が掲載されていることを確認した。掲載内容の真正性、対象範囲、個人情報等の具体的内訳は調査中である。[^ikegami-third]

暗号化と攻撃者サイト掲載という事実は確認されているが、同社は公開資料でランサムウェアファミリや攻撃主体を認定していないため、外部の犯行声明のみで帰属を確定しない。

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-09-21 | 同社への攻撃を示唆する外部情報を把握し、調査を開始。[^ikegami-first] |
| 2026-09-24 | 第1報。サイバー攻撃の可能性を公表し、内部ネットワークを遮断して調査。[^ikegami-first] |
| 2026-09-30 | 第2報。一部サーバーの不正アクセス痕跡と一部ファイル暗号化を確認。[^ikegami-second] |
| 2026-10-02 | 第3報。攻撃者サイトに同社保有とみられる情報の掲載を確認。内容・影響範囲の精査を継続。[^ikegami-third] |

# Impact

## Integrity and availability

一部ファイルの暗号化が確認され、内部ネットワークは調査・拡大防止のため遮断された。具体的な停止業務、復旧率、顧客サービスへの影響は公開資料で十分に定量化されていない。[^ikegami-second]

## Confidentiality

10月2日には攻撃者サイトで同社保有とみられる情報の掲載が確認された。これは「漏えい可能性のみ」より強い外部観測だが、掲載情報の真正性・取得元・全範囲が未確定であるため、個人情報漏えい件数を推測しない。[^ikegami-third]

# Technical findings

公開技術事実は、外部からの不正アクセス痕跡、一部ファイル暗号化、攻撃者サイト掲載まで。初期侵入経路、暗号化ソフトウェア、横展開、外部送信手法、攻撃主体は公表されていない。暗号化という症状だけで特定ランサムウェアグループへ帰属しない。

# Response and recovery

- 外部情報把握後、内部ネットワークを遮断。[^ikegami-first]
- 外部専門家等と不正アクセス・暗号化・影響範囲を調査。[^ikegami-second]
- 攻撃者サイトの掲載内容について真正性と対象範囲を精査。[^ikegami-third]

# Prognosis / current state

10月2日時点で調査・ネットワーク隔離が継続し、掲載情報の詳細も未確定であるため `investigating_and_network_isolated` とする。

# Defensive lessons

- **外部リーク観測は内部フォレンジックと独立した検知面になる。** 本件は外部情報が調査開始の契機となった。
- **暗号化とデータ公開を別の影響軸として扱う。** 可用性/完全性被害と機密性被害は同じタイミングで確定しない。
- **攻撃者の自己申告と企業確認を分ける。** リークサイト掲載の事実を記録しても、攻撃者帰属やマルウェア族を自動確定しない。

# Unknowns / withheld details

- 初期侵入経路と侵害開始日時
- 暗号化されたファイル/サーバーの範囲
- 掲載情報の真正性・件数・データ種別
- 攻撃主体とマルウェア/ランサムウェアファミリ
- 全面復旧時期と恒久対策

[^ikegami-first]: 池上通信機「当社に対するサイバー攻撃の可能性に関するお知らせ」2026-09-24.
[^ikegami-second]: 池上通信機「当社に対するサイバー攻撃に関するお知らせ（第2報）」2026-09-30.
[^ikegami-third]: 池上通信機「当社に対するサイバー攻撃に関するお知らせ（第3報）」2026-10-02.
