---
type: Cybersecurity Incident
title: ApplyNow — 採用管理基盤への不正アクセスと複数顧客組織への個人情報漏えい
description: データ分析ツールへの不正アクセスを起点に、Interview Cloud・ApplyNow・ApplyNow Signの採用/雇用関連データへ波及し、自治体・企業の過去応募者を含む通知へ発展した事案。
resource: https://applynow.co.jp/news/20260909
tags: [japan, saas, recruitment, supply-chain, personal-data, my-number, analytics, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 株式会社ApplyNow
  sector: recruitment-software-as-a-service
  jurisdiction: JP
  incident_status: downstream_notification_and_investigation
  attack_type: unauthorized-access
  earliest_known_activity: "2026-08-09"
  detected_at: "2026-09-07"
  first_disclosed_at: "2026-09-09"
  latest_public_update: "2026-09-30 downstream customer disclosure"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: "vulnerability in a data analytics tool; exact product/CVE and exploitation details not publicly disclosed"
  affected_services: "Interview Cloud, ApplyNow, ApplyNow Sign data handled through the affected analytics environment"
  data_exposure: confirmed
  availability_impact: not_publicly_disclosed
  restoration_state: "affected route blocked and security update applied; customer-by-customer impact identification and notification continue"
  secondary_abuse: not_observed_in_reviewed_downstream_disclosures
  downstream_impact: "multiple customer organizations, including public-sector recruitment and private employers"
  regulatory_response: "customer organizations are conducting notifications; provider response includes investigation and remediation"
  notification_state: "provider and affected customers are notifying identified individuals"
  business_continuity: "image, PDF and interview-video data were reportedly stored in a separate area outside the attacked scope"
  data_sensitivity: "applicant identity/contact data; depending on service, employment-contract, My Number, basic pension and bank-account information"
sources:
  - id: applynow-primary
    resource: https://applynow.co.jp/news/20260909
    title: 採用管理プラットフォームへの不正アクセスに関するお知らせ
    author: organization:株式会社ApplyNow
  - id: tokorozawa
    resource: https://www.city.tokorozawa.saitama.jp/tokoronews/press/r8/9gatu/kojinjyohou.html
    title: 職員採用試験動画投稿型面接システム事業者における個人情報の漏えいについて
    author: organization:所沢市
  - id: yoshinoya
    resource: https://www.yoshinoya.com/
    title: ApplyNow採用管理プラットフォームへの不正アクセスによる個人情報漏えいに関するお知らせとお詫び
    author: organization:株式会社吉野家
---

# Executive summary

株式会社ApplyNowは、採用管理基盤で利用していたデータ分析ツールの脆弱性を通じた第三者の不正アクセスを確認した。公開情報では不正アクセスが2026年8月9日から9月7日にかけて観測され、9月7日に異常なアクセスログを検知した。影響は「Interview Cloud」「ApplyNow」「ApplyNow Sign」で扱われるデータへ及び、顧客組織ごとの調査・通知が続いている。[^applynow-primary]

重要なのは、単一企業の応募者データだけでなく、SaaS提供者に集約された複数顧客の採用・雇用関連情報が下流へ波及した点である。所沢市では2022〜2025年度の職員採用試験受験者1,701件について氏名・メールアドレス・電話番号の漏えいを確認した。一方、動画データは別保管領域にあり、本件の対象外と報告されている。[^tokorozawa]

ApplyNow Signでは利用状況によって雇用契約情報、マイナンバー、基礎年金番号、銀行口座情報等が扱われ得るため、件数だけでなくデータ感度を分離して追跡する必要がある。公開情報から全顧客横断の最終ユニーク人数は確定できない。

# Observable timeline

| Date / period | Observable event |
| --- | --- |
| 2026-08-09 – 09-07 | 後の調査で不正アクセスが確認された期間。[^applynow-primary] |
| 2026-09-07 | 異常なアクセスログを検知し、調査・封じ込めを開始。[^applynow-primary] |
| 2026-09-09 | ApplyNowが不正アクセスと影響サービスを公表。[^applynow-primary] |
| 2026-09-16 | 所沢市が、同市受験者情報の漏えいを確認した日として公表。[^tokorozawa] |
| 2026-09-19 | 所沢市が1,701件の漏えいと対象項目、動画が別領域で対象外であることを公表。[^tokorozawa] |
| 2026-09-30 | 吉野家など顧客企業側の通知が継続していることを公式サイトで確認。[^yoshinoya] |

# Impact

## Cross-customer exposure

本件は採用管理SaaSの供給者側で発生したため、影響単位は「ApplyNow自身の従業員」ではなく、同基盤を利用した顧客組織と応募者・採用者である。顧客ごとに保存項目・利用期間・サービスが異なるため、各社の公表数を無条件に合算しない。

所沢市の確定事例では1,701件、対象は氏名、メールアドレス、電話番号。動画は別領域で対象外だった。[^tokorozawa]

## High-sensitivity employment data

ApplyNow Signのデータ範囲には、利用状況により雇用契約情報、マイナンバー、基礎年金番号、銀行口座情報などが含まれ得る。個々の顧客で実際にどの項目が漏えいしたかは顧客単位の通知で確認する必要があり、「サービスが保持可能な項目」を「全対象者で漏えいした項目」と読み替えない。

## Retention / offboarding risk

後続顧客公表からは、既に採用サービスの利用を終了していた期間の応募者データも影響調査対象になっていることが観測できる。SaaS契約終了とデータ削除完了を同一視せず、削除の実施・証跡・バックアップ/分析系コピーまで確認する必要がある。

# Technical findings

公開された原因粒度は「データ分析ツールの脆弱性を通じた不正アクセス」である。ツール製品名、CVE、攻撃主体、具体的なペイロードや認証突破方法は公表されていないため推測しない。[^applynow-primary]

画像・PDF・面接動画が別領域に保管され、本件の攻撃対象外とされた事例は、機能/データ分離が観測された被害境界として記録する。[^tokorozawa]

# Response and recovery

- 不正アクセス経路を遮断し、対象ツールへセキュリティ更新を適用。[^applynow-primary]
- 影響範囲を顧客単位で特定し、顧客企業・自治体と連携して対象者通知を継続。[^tokorozawa][^yoshinoya]
- 所沢市ではApplyNowと市から対象者へ個別メール通知を予定。[^tokorozawa]

# Prognosis / current state

2026年10月4日時点でも顧客組織ごとの通知が続いており、全顧客横断の最終対象人数、各データ項目の実漏えい件数、最終調査報告は確認できない。そのため `downstream_notification_and_investigation` とする。

# Defensive lessons

- **分析基盤も本番データ境界として扱う。** 顧客向け本体とは別の分析ツールが、集約データへの侵入点になり得る。
- **SaaSの契約終了とデータ消去を別の検証項目にする。** 顧客側は削除完了証跡、保持期間、派生コピーを監査すべきである。
- **分離保管は実際の被害境界を作る。** 動画・画像等が別領域だったことで、少なくとも確認済み対象から外れた顧客が存在する。[^tokorozawa]
- **供給者の総件数と顧客側の確定件数を混ぜない。** 顧客通知が進むほど対象が具体化するため、母数・確定漏えい・通知済み人数を分離する。

# Unknowns / withheld details

- データ分析ツールの製品名・CVE
- 不正アクセスの具体的操作と取得量
- 全顧客横断の最終ユニーク対象人数
- 各顧客で実際に漏えいした高感度項目の件数
- 契約終了済み顧客データが残存した全ケースと保持理由
- 最終的な二次被害評価

[^applynow-primary]: 株式会社ApplyNow「採用管理プラットフォームへの不正アクセスに関するお知らせ」2026-09-09.
[^tokorozawa]: 所沢市「職員採用試験動画投稿型面接システム事業者における個人情報の漏えいについて」2026-09-19.
[^yoshinoya]: 吉野家公式サイト「ApplyNow採用管理プラットフォームへの不正アクセスによる個人情報漏えいに関するお知らせとお詫び」2026-09-30.
