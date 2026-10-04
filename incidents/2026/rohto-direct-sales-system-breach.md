---
type: Cybersecurity Incident
title: ロート製薬 — 通信販売関連システムへの不正アクセスと顧客データ取得可能性
description: 2026年9月に通信販売関連システムで確認された不正アクセス、コールセンター音声・顧客管理情報の取得可能性、封じ込めと継続調査を記録する。
resource: https://www.rohto.co.jp/news/whatsnew/2026/0915_01
tags: [japan, healthcare, ecommerce, unauthorized-access, customer-data, call-recordings, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: ロート製薬株式会社
  sector: healthcare-and-consumer-products
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-10"
  first_disclosed_at: "2026-09-11"
  latest_public_update: "2026-09-15"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "direct-sales related systems, including customer-management information and some customer-support call audio"
  data_exposure: possible
  availability_impact: "containment restrictions were applied; no major company-wide business disruption publicly established"
  restoration_state: "access restrictions and containment applied; detailed scope investigation ongoing"
  secondary_abuse: unknown
  downstream_impact: "customers may face targeted impersonation/phishing using purchase/support context"
  regulatory_response: "reports/consultation with the Personal Information Protection Commission, police and relevant authorities"
  notification_state: "company states it will contact affected persons as scope is identified"
  business_continuity: "major operations continued while the affected route was restricted"
  data_sensitivity: "customer-management data and customer-support call audio with associated information"
sources:
  - id: rohto-first
    resource: https://www.shop.rohto.co.jp/news/news_2026-09-002.html
    title: 当社通信販売関連システムへの不正アクセスに関するお知らせ
    author: organization:ロート製薬株式会社
  - id: rohto-second
    resource: https://www.rohto.co.jp/news/whatsnew/2026/0915_01
    title: 当社通信販売関連システムへの不正アクセスに関する調査状況のお知らせ
    author: organization:ロート製薬株式会社
---

# 概要

ロート製薬は2026年9月10日、通信販売関連システムへの第三者不正アクセスを確認し、アクセス制限などの封じ込め措置を実施した。9月15日の更新では、顧客サポートで記録された一部の通話音声と関連情報、ならびに顧客管理情報が第三者に取得された可能性があることを公表した。[^rohto-first][^rohto-second]

対象人数、実際に取得されたデータ量、侵入経路は同日時点で確定しておらず、外部専門家を交えた調査が継続している。主要業務全体が停止した事実は公表されていない。[^rohto-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-10 | 通信販売関連システムへの不正アクセスを確認。アクセス制限等を実施。[^rohto-first] |
| 2026-09-11 | 初回公表。原因・影響範囲を調査中と説明。[^rohto-first] |
| 2026-09-15 | 調査状況更新。顧客サポート通話音声・関連情報、顧客管理情報が取得された可能性を公表。関係当局への報告・相談、顧客への注意喚起を実施。[^rohto-second] |
| 2026-10-04 review | 公式サイトを再確認した範囲で、9月15日より後の本件固有の確定報は確認できなかった。 |

# 影響

## 顧客情報

9月15日時点で公開された影響は「取得の可能性」であり、全対象データの外部取得が確認されたという意味ではない。対象には顧客管理情報と、一部の顧客サポート通話音声およびそれに付随する情報が含まれる。[^rohto-second]

通話音声は氏名・注文・相談内容等が会話に含まれ得るため、構造化DBとは異なる高情報密度のデータとして扱う。公開資料から個々の録音に含まれる具体項目や件数は確定できない。

## 二次被害リスク

同社は、本件を利用して同社・金融機関・公的機関等を装う電話、SMS、メール、返金・アカウント・決済確認を名目とする詐欺的連絡への注意を呼びかけている。これは二次被害が既に発生したという意味ではなく、公開されたデータ種別を踏まえた予防措置として記録する。[^rohto-second]

# 技術的に確認できた事項

不正アクセスは確認されているが、侵入経路、脆弱性、資格情報悪用、攻撃主体、マルウェア利用の有無は公表されていない。外部報道から特定手法を補わない。

# 対応と復旧

- 不正アクセス確認後、アクセス制限などの緊急措置。[^rohto-first]
- 外部専門家を含む原因・影響範囲調査。[^rohto-second]
- 個人情報保護委員会、警察等関係機関への報告・相談。[^rohto-second]
- 対象顧客の特定と必要な連絡を継続。[^rohto-second]
- なりすまし・フィッシング等への顧客注意喚起。[^rohto-second]

# 現在の状況と予後

2026年10月4日時点で、件数・侵入経路・最終取得範囲・二次被害評価の確定報は確認できない。封じ込めは進んでいるが影響評価が未完了のため `investigating` とする。

# 防御上の教訓

- **通話録音を高感度データストアとして管理する。** 非構造化音声はDB列以上の文脈を含み得る。
- **通信販売データの漏えい後は詐欺シナリオを具体化して通知する。** 購入・決済・サポート文脈を使ったなりすましは説得力を持ちやすい。
- **件数未確定の速報で影響規模を推定しない。** 「取得された可能性」と「取得確認」を分離し続ける。

# 不明点・未公表事項

- 初期侵入経路・脆弱性・認証情報利用の有無
- 侵害開始時刻・継続期間
- 実際に取得された顧客数・録音数
- 取得された個人情報項目の最終一覧
- 恒久対策と最終復旧状態
- 本件に起因する二次被害の有無

[^rohto-first]: ロート製薬「当社通信販売関連システムへの不正アクセスに関するお知らせ」2026-09-11.
[^rohto-second]: ロート製薬「当社通信販売関連システムへの不正アクセスに関する調査状況のお知らせ」2026-09-15.
