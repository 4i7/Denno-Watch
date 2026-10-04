---
type: Cybersecurity Incident
title: LEAN BODY — Metabase脆弱性悪用による約44万アカウントの顧客情報取得
description: 2026年8月から9月にかけて社内分析ツールMetabaseの脆弱性を悪用され、退会者を含む約44万アカウントの顧客情報が外部取得された事案を追跡する記録。
resource: https://lean-body.co.jp/news/JlBWMCs7
tags: [japan, fitness, analytics, bi, metabase, vulnerability, data-breach, personal-data, 2026]
status: draft
stale_after: 2026-10-15T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T20:00:23Z }
incident:
  organization: 株式会社LEAN BODY
  sector: online-fitness
  jurisdiction: JP
  incident_status: contained_investigation_continues
  attack_type: unauthorized-access-via-vulnerability
  earliest_known_activity: "2026-08-11"
  detected_at: "2026-09-08"
  first_disclosed_at: "2026-09-15"
  latest_public_update: "2026-09-15"
  public_record_checked_at: "2026-10-04T05:00:23+09:00"
  intrusion_vector: "security vulnerability in the internally used Metabase analytics tool; CVE not publicly identified by the company"
  affected_services: "internal Metabase analytics environment and connected customer database"
  data_exposure: confirmed_acquisition
  availability_impact: not_observed
  restoration_state: "access route blocked and analytics tool updated on 2026-09-09; customer-facing LEAN BODY service continued normally"
  secondary_abuse: not_observed
sources:
  - id: lean-primary
    resource: https://lean-body.co.jp/news/JlBWMCs7
    title: 弊社が利用する分析ツールへの不正アクセスによるお客様情報の取得について（お詫び）
    author: organization:LEAN BODY
  - id: lean-news-index
    resource: https://lean-body.co.jp/newslist
    title: 株式会社LEAN BODY お知らせ一覧
    author: organization:LEAN BODY
  - id: gate02
    resource: https://www.gate02.ne.jp/lab/incident-news/lean-body-20260925/
    title: 株式会社 LEAN BODY が不正アクセス被害、約44万アカウントの顧客情報が漏えい
    author: organization:USEN ICT Solutions Cybersecurity Lab
  - id: nissan-kenpo
    resource: https://www.nissan-kenpo.or.jp/inm/news3/detail.html?articleid=179
    title: オンラインフィットネスサービス利用者情報に関するお知らせ
    author: organization:Nissan Motor Health Insurance Society
---

# 概要

株式会社LEAN BODYは2026年9月15日、社内でデータ分析に利用していた **Metabase** が第三者の不正アクセスを受け、同社データベースから顧客情報が外部に取得されたことを公表した。対象は退会者を含む**約44万アカウント**。[^lean-primary][^gate02]

不正アクセスは8月11日から複数回発生し、9月8日に異常を検知して調査を開始した。翌9日にも顧客情報の取得が確認されたため、同日、侵入経路を遮断してMetabaseを更新した。[^lean-primary][^gate02]

会社は原因として、利用していたMetabaseのセキュリティ上の脆弱性を第三者に悪用されたことを確認している。また、脆弱性情報の定期確認と必要な更新ができていなかったことが、被害要因となった可能性が高いと説明している。[^lean-primary][^gate02]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-08-11 | 公開調査で確認された不正アクセス期間の開始。以後複数回、顧客情報が取得された。[^gate02] |
| 2026-09-08 | 異常を検知し調査開始。[^gate02] |
| 2026-09-09 | 顧客情報の取得を再確認。侵入経路を遮断し、Metabaseを更新。[^gate02] |
| 2026-09-11 | 個人情報保護委員会へ速報を提出。[^gate02] |
| 2026-09-15 | 公式公表。対象者へのメール通知を順次開始。[^lean-primary][^gate02] |
| 2026-09-16 | 日産自動車健康保険組合が、2024年度のLEAN BODY利用者について一部情報漏えいの報告を受けたと加入者向けに公表。[^nissan-kenpo] |

# 影響

## 取得が確認されたデータ

本件は単なる「閲覧可能性」ではなく、第三者がMetabaseへ不正アクセスし、接続されたデータベースから顧客情報を**取得したことを会社が確認した**事案である。[^lean-primary][^gate02]

対象は退会者を含む約44万アカウント。これはアカウント数であり、一意人数と同一であることは公開情報から保証されないため、Denno Watchでは「約44万人」とは置き換えない。

## データ種別

公開された対象には、利用者によって異なるが以下が含まれ得る。[^gate02]

- メールアドレス
- ニックネーム
- 性別
- 生年月日
- 身長・体重
- サービス利用状況
- 暗号化されたパスワード
- 契約・支払いに関する情報

契約・支払い情報に含まれるカード情報はカード番号の下4桁であり、カード番号全体やセキュリティコードは同社データベースに保存していなかったと報告されている。[^gate02]

パスワードについては、解読に必要な別途管理情報が取得されておらず、元のパスワードが判明する可能性は低いと会社は説明している。[^gate02]

日産自動車健康保険組合は、自組合経由で2024年度に利用した対象者について、メールアドレスと一部利用者の生年月日が対象になったと公表し、同組合がLEAN BODYへ共有していない資格情報（記号番号、氏名）は影響対象外と説明している。[^nissan-kenpo]

# 技術的に確認できた事項

公開情報で確認できる原因は、**社内分析用Metabaseに存在したセキュリティ上の脆弱性の悪用**である。[^lean-primary][^gate02]

重要な境界は以下。

- LEAN BODY自身は悪用されたCVE番号やMetabaseバージョンを公表していない。
- 同時期にMetabaseで重大脆弱性が公開されていても、そのCVEを本件原因と自動的に同定しない。
- 顧客向けアプリ・Webフロントが直接の入口だったとする公開根拠はなく、社内分析基盤が侵入点だった。

会社は、脆弱性情報の定期的な確認や必要な更新ができていなかったことを被害要因の可能性として挙げている。[^gate02]

# 可用性と二次被害

公表時点でLEAN BODYサービスは通常どおり利用でき、サービス提供への影響は確認されていない。アカウントの不正利用や不正請求も確認されていなかった。[^lean-primary][^gate02]

したがって、情報取得が確認された重大な機密性侵害である一方、可用性障害を伴う事案としては扱わない。

# 対応と復旧

- 9月8日の異常検知後に調査開始。[^gate02]
- 9月9日に侵入経路を遮断しMetabaseを更新。[^gate02]
- 9月11日に個人情報保護委員会へ速報。[^gate02]
- 9月15日から対象者へ個別通知。[^lean-primary][^gate02]
- 利用者へパスワード変更を案内。[^gate02]
- 詳細調査後、個人情報保護委員会へ確報を提出する方針。[^gate02]

# 現在の状況と予後

2026年10月4日にLEAN BODYのお知らせ一覧を確認した時点で、本件に明示的に紐づく公開記事は9月15日の公表が最新として確認できる。[^lean-news-index]

侵入経路は遮断され顧客向けサービスは継続しているが、確報提出に向けた詳細調査が残るため `contained_investigation_continues` とする。

# 防御上の教訓

- **BI・分析基盤も本番データ境界として扱う。** 顧客向けサービスが正常でも、分析ツールから接続先データベースの顧客情報を取得され得る。
- **脆弱性情報の継続監視と更新責任を明確化する。** 補助的な社内ツールはパッチ運用から漏れやすく、本件では会社自身が定期確認・更新不足を要因として挙げている。
- **分析用途へ必要以上の属性を複製しない。** メールだけでなく身体情報、利用状況、契約・支払い属性まで影響対象になった。
- **カード情報の最小保持は被害を限定する。** 完全なカード番号やセキュリティコードを保持しない設計により、公開された影響範囲が限定された。
- **CVEの時系列一致だけで原因を決めない。** 製品側に同時期の既知脆弱性が存在しても、被害組織が識別子を公表していない限り別物として扱う。

# 不明点・要追跡事項

- 悪用された具体的なMetabase脆弱性/CVE
- 利用していたMetabaseバージョン
- Metabaseの公開・接続構成
- 約44万アカウントのうち項目別に取得された件数
- 取得データの二次公開・販売の有無
- 攻撃主体
- 個人情報保護委員会への確報内容
- 恒久対策の詳細

[^lean-primary]: LEAN BODY「弊社が利用する分析ツールへの不正アクセスによるお客様情報の取得について（お詫び）」2026-09-15.
[^gate02]: USEN ICT Solutions サイバーセキュリティラボ「株式会社 LEAN BODY が不正アクセス被害、約44万アカウントの顧客情報が漏えい」2026-09-25。LEAN BODY公式公表を参照した補助情報源。
[^nissan-kenpo]: 日産自動車健康保険組合「オンラインフィットネスサービス利用者情報に関するお知らせ」2026-09-16.
[^lean-news-index]: LEAN BODY お知らせ一覧。2026-10-04確認。
