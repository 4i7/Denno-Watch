---
type: Cybersecurity Incident
title: マルタケ — 医薬品卸システムのランサムウェア被害・情報持ち出しとリークサイト掲載
description: 2026年4月27日の障害からランサムウェア確定、サーバー情報の暗号化・持ち出し・リークサイト掲載、仮サーバーによる医薬品安定供給継続までを追跡する記録。
resource: https://www.kk-marutake.co.jp/2026/06/24/6737
tags: [japan, pharmaceuticals, wholesale, ransomware, data-exfiltration, leak-site, business-continuity, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T06:23:00+09:00 }
incident:
  organization: 株式会社マルタケ
  sector: pharmaceutical-wholesale
  jurisdiction: JP
  incident_status: monitoring_after_confirmed_exfiltration
  attack_type: ransomware
  earliest_known_activity: "2026-04-27"
  detected_at: "2026-04-27"
  first_disclosed_at: "2026-04-28"
  latest_public_update: "2026-06-24"
  public_record_checked_at: "2026-10-04T06:23:00+09:00"
  intrusion_vector: "attacker used account information that had been illicitly created by an unspecified method; exact creation/acquisition path not publicly disclosed"
  affected_services: "some corporate servers and business systems supporting pharmaceutical-wholesale operations"
  data_exposure: confirmed_exfiltration_and_publication
  availability_impact: "server disruption and prolonged impairment of some normal business operations"
  restoration_state: "temporary server environment in use as of 2026-06-24 while full restoration continued"
  secondary_abuse: "information publication on an attacker-operated leak site confirmed; publication elsewhere not observed at latest report"
  downstream_impact: "operational risk to pharmaceutical distribution; counterparty, shareholder, officer and employee/affiliate information affected"
  regulatory_response: "police report filed and coordination with relevant authorities; external forensic specialists engaged"
  notification_state: "public notices and dedicated ransomware response contact; detailed person-level notification state not publicly described"
  business_continuity: "alternative procedures and later a temporary server environment used while prioritizing stable pharmaceutical supply"
  data_sensitivity: "counterparty, shareholder, officer, employee and affiliated-company information; exact field-level inventory not fully public"
sources:
  - id: marutake-second
    resource: https://www.kk-marutake.co.jp/2026/04/29/6621
    title: システム障害に関する続報（第2報）
    author: organization:株式会社マルタケ
  - id: marutake-third
    resource: https://www.kk-marutake.co.jp/2026/05/08/6669
    title: システム障害に関するお知らせ（第3報）
    author: organization:株式会社マルタケ
  - id: marutake-fourth
    resource: https://www.kk-marutake.co.jp/2026/06/24/6737
    title: システム障害に関するお知らせ（第4報）
    author: organization:株式会社マルタケ
---

# 概要

医薬品・医療機器卸のマルタケでは2026年4月27日に一部サーバーで障害が発生し、5月8日までに外部からの不正アクセスによる**ランサムウェア被害**と確定した。6月24日の第4報では、攻撃者が何らかの方法で不正に作成したアカウント情報を用いてサーバーへアクセスしたこと、保存されていた一部情報の**暗号化と持ち出し**、さらに攻撃者運営とされるリークサイトへの掲載が確認された。[^marutake-third][^marutake-fourth]

影響情報には取引先、株主、マルタケおよび関連会社の役員・社員情報が含まれる。第4報時点でリークサイト以外での公開は確認されていない。クライアントPC334台には外部不正アクセスやマルウェアの痕跡は確認されなかった。[^marutake-fourth]

可用性面では一部業務の通常対応が困難となり、代替手段を用いて医薬品等の安定供給を継続。その後も仮サーバー環境で業務を運用しながら本格復旧を進めた。[^marutake-third][^marutake-fourth]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-04-27 | 一部サーバーでシステム障害発生。[^marutake-fourth] |
| 2026-04-28 | 第一報。外部不正アクセス/ランサムウェア可能性を含め調査と復旧を開始。 |
| 2026-04-29 | 第二報。警察へ被害届、バックアップを基に復旧。個人情報外部流出はこの時点で未確認。[^marutake-second] |
| 2026-05-08 | 第三報。ランサムウェア障害と確定。完全復旧には相当日数を要する見通し。代替手段で医薬品安定供給を継続。[^marutake-third] |
| 2026-06-24 | 第4報。攻撃者による不正作成アカウント利用、一部情報の暗号化・持ち出し、リークサイト掲載を確認。仮サーバー環境で業務運用。[^marutake-fourth] |
| 2026-10-04 | 公式ニュース一覧を再確認。6月24日より新しい本件事故報告は確認できず。 |

# 影響

## 機密性

第4報で、取引先、株主、同社および関連会社の役員・社員情報を含む一部情報が攻撃者に持ち出され、リークサイトへ掲載されたことが確認された。件数や詳細な項目は公開資料では示されていない。[^marutake-fourth]

これは4月29日・5月8日時点の「外部流出未確認」から、6月24日の**持ち出し・公開確認**へ証拠状態が変化した事例であり、初期評価を最終結論として残さない。

## Availability and operations

一部業務で通常対応が困難となり、医薬品等の供給継続を優先して代替手段を使用した。6月24日時点でも仮サーバー環境で業務を継続しており、本格復旧は未完了だった。[^marutake-third][^marutake-fourth]

医薬品卸という業態上、IT復旧だけでなく物流・供給継続が重要な予後指標になる。

# 技術的に確認できた事項

外部専門機関のフォレンジック調査で、攻撃者が「何らかの方法で不正に作成したアカウント情報」を用いてサーバー内にアクセスしたと確認された。[^marutake-fourth]

この表現から、具体的なアカウント作成手段、認証情報窃取、脆弱性悪用、VPN侵害等を推測しない。クライアントPC334台では外部不正アクセスおよびマルウェア痕跡が確認されなかった点は、サーバー側被害とエンドポイント側観測を分離する材料である。[^marutake-fourth]

# 対応と復旧

- 警察へ被害届を提出し関係当局と連携。[^marutake-second]
- バックアップデータを基に復旧を開始。[^marutake-second]
- 外部専門家による調査と復旧を継続。[^marutake-third]
- 一部通常業務が困難な期間も代替手段で医薬品供給を継続。[^marutake-third]
- 仮サーバー環境へ移行して業務を継続し、本格復旧を並行。[^marutake-fourth]
- リークサイト掲載内容を精査し、追加掲載を継続監視。[^marutake-fourth]

# 現在の状況と予後

公開上の最新事故報告である6月24日時点では、本格的なシステム復旧とフォレンジック調査、リークサイト監視が継続中だった。その後公式ニュース一覧に本件の追加事故報告は確認できないため、公開情報だけから完全復旧・調査終了を推定せず `monitoring_after_confirmed_exfiltration` とする。

# 防御上の教訓

- **初期の「漏えい未確認」を固定しない。** ランサムウェア事案では後続フォレンジックや攻撃者公開により機密性評価が変わり得る。
- **重要供給業では代替業務系をBCPに含める。** 本件では医薬品の安定供給を最優先し、代替手段と仮サーバーで業務を継続した。
- **復旧環境を段階化する。** バックアップ→代替手段→仮サーバー→本格復旧という複数段階を別々に記録する。
- **リークサイト観測は外部公開証拠として扱う。** ただしリークサイト掲載を攻撃者の他の主張全体の真実性へ一般化しない。
- **端末無感染とサーバー無侵害を混同しない。** 334台のPCに痕跡がなくてもサーバー側の侵害・持ち出しは確認されている。

# 不明点・未公表事項

- 不正アカウントを作成できた具体的経路
- ランサムウェアファミリーと攻撃主体
- 持ち出しデータの総容量、件数、全項目
- 身代金要求・支払い有無
- 仮サーバーから本番環境への完全移行日
- 調査・通知・長期再発防止の最終完了状態

[^marutake-second]: 株式会社マルタケ「システム障害に関する続報（第2報）」2026-04-29.
[^marutake-third]: 株式会社マルタケ「システム障害に関するお知らせ（第3報）」2026-05-08.
[^marutake-fourth]: 株式会社マルタケ「システム障害に関するお知らせ（第4報）」2026-06-24.
