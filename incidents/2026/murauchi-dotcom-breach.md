---
type: Cybersecurity Incident
title: ムラウチドットコム — Webシステム脆弱性悪用による771万6811件の顧客情報流出
description: 2026年7月に発生し9月に影響範囲が確定した、ムラウチドットコムの大規模個人情報漏えいを追跡する記録。
resource: https://murauchi.com/static-pages/privacy/%E5%BC%8A%E7%A4%BE%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E3%81%8A%E5%AE%A2%E6%A7%98%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E8%A9%AB%E3%81%B3%E3%81%A8%E3%81%94%E5%A0%B1%E5%91%8A%EF%BC%88%E7%AC%AC%E4%BA%8C%E5%A0%B1%EF%BC%89.pdf
tags: [japan, ecommerce, unauthorized-access, vulnerability, data-breach, personal-data, 2026]
status: stable
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T14:45:00Z }
incident:
  organization: 株式会社ムラウチドットコム
  sector: ecommerce
  jurisdiction: JP
  incident_status: public_investigation_completed
  earliest_known_activity: unknown
  detected_at: "2026-07-16 during recovery from system failure"
  first_disclosed_at: "2026-07-24"
  latest_public_update: "2026-09-15"
  intrusion_vector: "vulnerability in part of a company-managed web system"
  affected_services: "multiple internal systems after initial web-system compromise"
  data_exposure: confirmed
  availability_impact: "system failure observed 2026-07-15; detailed service impact not fully public"
  restoration_state: "forensic investigation completed; security improvements announced"
  secondary_abuse: "not publicly confirmed in reviewed sources"
sources:
  - id: murauchi-primary
    resource: https://murauchi.com/static-pages/privacy/%E5%BC%8A%E7%A4%BE%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E3%81%8A%E5%AE%A2%E6%A7%98%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E8%A9%AB%E3%81%B3%E3%81%A8%E3%81%94%E5%A0%B1%E5%91%8A%EF%BC%88%E7%AC%AC%E4%BA%8C%E5%A0%B1%EF%BC%89.pdf
    title: 弊社における不正アクセスによるお客様情報漏えいに関するお詫びとご報告（第二報）
    author: organization:Murauchi.com
  - id: internet-watch
    resource: https://internet.watch.impress.co.jp/docs/news/2141530.html
    title: ムラウチドットコム、不正アクセスにより約771万件の個人情報漏えい
  - id: nexsight
    resource: https://cyber.nexsight.co/articles/2026/09/18/murauchi-dotcom-unauthorized-access-7716811-customer-info-2026-09-18/
    title: ムラウチドットコムの不正アクセスで771万6811件の顧客情報が流出
---

# Executive summary

ムラウチドットコムは2026年7月15日未明に社内システム障害を確認し、翌16日の復旧作業中に第三者による不正アクセスの痕跡を確認した。7月24日に第一報を公表し、外部専門会社によるフォレンジック調査を進めた。[^murauchi-primary][^internet-watch]

9月15日の第二報で、Webシステムの一部に存在していた脆弱性が悪用され、それを起点として複数システムへ不正アクセスが及んだこと、顧客の個人情報 **7,716,811件** が外部へ持ち出されたことを確認したと公表した。[^murauchi-primary][^nexsight]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-07-15 未明 | 社内システムで障害を確認。[^murauchi-primary] |
| 2026-07-16 | 復旧作業中に第三者による不正アクセス痕跡を確認。外部アクセスを遮断し調査を開始。[^murauchi-primary][^nexsight] |
| 2026-07-20 | 個人情報保護委員会へ速報を提出。[^nexsight] |
| 2026-07-23 | 警察へ被害相談。[^nexsight] |
| 2026-07-24 | 第一報を公表し、専用問い合わせ窓口を設置。[^nexsight] |
| 2026-07-27 | 外部情報セキュリティ専門会社によるフォレンジック調査を開始。[^nexsight] |
| 2026-09-14 | 個人情報保護委員会へ確報を提出。[^nexsight] |
| 2026-09-15 | 第二報を公表。771万6811件の漏えいを確定し、対象顧客への個別通知を順次開始。[^murauchi-primary][^nexsight] |

# Impact

外部への持ち出しが確認された顧客情報は7,716,811件。公表された情報項目は以下。[^murauchi-primary][^internet-watch]

- 氏名
- 住所
- 電話番号
- メールアドレス
- 生年月日
- 性別

クレジットカード情報とパスワードは対象に含まれていない。[^murauchi-primary][^internet-watch]

この件数は「漏えいの可能性がある最大母数」ではなく、外部専門会社の調査後に**外部へ持ち出されたことを確認した件数**として公表された点が重要である。

# Technical findings

公開情報では、会社管理のWebシステムの一部に存在した脆弱性が初期の起点となり、その後複数システムへ不正アクセスが及んだことが示されている。具体的な製品名、脆弱性識別子、攻撃開始日時、内部での移動経路は公表されていない。[^murauchi-primary][^nexsight]

# Response and recovery

公表された対応には、外部接続の遮断、外部専門会社によるフォレンジック、警察への相談、個人情報保護委員会への速報・確報、対象顧客への個別通知が含まれる。再発防止として以下が示されている。[^nexsight]

- 関連システムの安全性確認
- アクセス権限・認証情報管理の見直し
- サーバー・ネットワーク監視と不正アクセス検知体制の強化
- 定期的な脆弱性診断とセキュリティ点検

# Defensive observations

- 単一のWebシステムの問題が複数システムへ波及したため、インターネット公開系と後段システムの信頼境界・権限分離が重要な観点となる。
- 7月16日の侵害認識から9月15日の確定公表まで約2か月を要しており、初動封じ込めと「何が実際に持ち出されたか」の確定には大きな時間差があり得る。
- 漏えい件数の確定値、対象項目、除外項目を分けて保存することで、速報段階の推定値と最終値の混同を防げる。

# Unknowns / open questions

2026-10-03時点で公開情報から確定できない事項:

- 侵害の開始日時と滞在期間
- 原因脆弱性の具体的な識別情報
- 複数システムへ到達した経路と権限範囲
- データ持ち出しの具体的な期間・方法
- 本件に起因する二次被害の有無
- システム障害と不正アクセスの直接的な因果関係の詳細

[^murauchi-primary]: 株式会社ムラウチドットコム「弊社における不正アクセスによるお客様情報漏えいに関するお詫びとご報告（第二報）」
[^internet-watch]: INTERNET Watch「ムラウチドットコム、不正アクセスにより約771万件の個人情報漏えい」
[^nexsight]: NEXSIGHT CYBER WIRE「ムラウチドットコムの不正アクセスで771万6811件の顧客情報が流出」
