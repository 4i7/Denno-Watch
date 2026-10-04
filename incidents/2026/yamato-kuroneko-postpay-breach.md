---
type: Cybersecurity Incident
title: ヤマト運輸 — クロネコ代金後払いサービスへの不正アクセスと顧客・加盟店情報の漏えい可能性
description: 2026年9月28日に確認されたクロネコ代金後払いサービスへの不正アクセス、サービス停止、顧客の購入・請求文脈を含む情報の漏えい可能性を追跡する記録。
resource: https://www.yamato-hd.co.jp/important/info_260929_1.html
tags: [japan, logistics, payment, unauthorized-access, personal-data, ecommerce, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: ヤマト運輸株式会社
  sector: logistics-and-payment-services
  jurisdiction: JP
  incident_status: service_suspended_investigation_continues
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-28"
  first_disclosed_at: "2026-09-29"
  latest_public_update: "2026-10-02"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "クロネコ代金後払いサービス"
  data_exposure: possible
  availability_impact: "affected postpay service suspended; parcel-delivery and other Yamato services remain available"
  restoration_state: "service restoration date undecided as of 2026-10-02; investigation ongoing"
  secondary_abuse: unknown
  downstream_impact: "customers, merchants and service-assigned employees may be affected"
  regulatory_response: not_publicly_detailed
  notification_state: "individual notification planned where leakage is confirmed"
  business_continuity: "宅急便を含む他サービスは通常利用可能"
  data_sensitivity: "identity/contact data plus credit-assessment number, billed amount, receivable balance and product details; no credit-card data or passwords in the announced scope"
sources:
  - id: yamato-second
    resource: https://www.yamato-hd.co.jp/important/info_260929_1.html
    title: 〖第2報〗「クロネコ代金後払いサービス」への不正アクセスの発生について
    author: organization:ヤマトホールディングス株式会社
---

# 概要

ヤマト運輸は2026年9月28日、「クロネコ代金後払いサービス」が第三者による不正アクセスを受けたことを確認し、翌29日に初報を公表した。セキュリティ専門機関と調査を進める中で情報の一部が漏えいした可能性が判明し、10月2日に第2報を公表した。[^yamato-second]

漏えい可能性のある情報には、一部顧客の氏名・住所・電話番号・メールアドレスに加え、与信番号、請求金額、債権残高、商品明細が含まれる。加盟店名・加盟店コード、担当社員氏名も対象となり得る。クレジットカード情報とパスワード情報は公表対象に含まれていない。[^yamato-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-28 | クロネコ代金後払いサービスへの第三者不正アクセスを確認。[^yamato-second] |
| 2026-09-29 | 初報を公表し、対象サービスを停止。[^yamato-second] |
| 2026-10-02 | 第2報。顧客・加盟店・担当社員情報の一部に漏えい可能性があることを公表。復旧時期は未定。[^yamato-second] |

# 影響

## 顧客情報

対象には通常の連絡先PIIだけでなく、後払いの与信・請求・債権・商品情報が含まれる。これらは購入内容や支払い状況を示し得るため、漏えい件数が未確定でも社会工学的悪用の文脈価値が高い。[^yamato-second]

クレジットカード情報とパスワードは対象外と公表されている。これを「二次被害リスクなし」とは扱わず、購入・請求状況を知っているように見せる詐欺への利用可能性を別に評価する。

## 加盟店・従業員

一部加盟店の加盟店名・加盟店コード、同サービス担当社員の氏名も漏えい可能性のある情報に含まれる。顧客以外の関係主体も同じ侵害境界に存在したことを記録する。[^yamato-second]

## 可用性

クロネコ代金後払いサービスは停止中で、10月2日時点の復旧時期は未定。一方、宅急便を含む他サービスは通常どおり利用できると明示されている。[^yamato-second]

# 技術的に確認できた事項

第三者不正アクセスは確認されたが、侵入経路、脆弱性、認証情報悪用、攻撃主体、取得方法は公表されていない。後払いサービスという性質から決済基盤侵害やカード情報流出を推測しない。

# 対応と復旧

- 対象サービスを停止し、セキュリティ専門機関と調査。[^yamato-second]
- 漏えい可能性のある情報と範囲を継続特定。[^yamato-second]
- 漏えいが確認された対象者へ個別連絡する方針。[^yamato-second]
- 不審メール、SMS、電話、郵便物への注意を利用者へ要請。[^yamato-second]
- 情報セキュリティ強化と再発防止策を検討。[^yamato-second]

# 現在の状況と予後

10月2日時点で対象件数、侵入経路、復旧時期が未確定であり、サービスも停止中であるため `service_suspended_investigation_continues` とする。

# 防御上の教訓

- **決済カード以外の取引文脈も高感度である。** 請求額、債権残高、商品明細は精巧ななりすまし材料になり得る。
- **サービス境界を明示する。** 後払いサービス停止と宅急便の通常運行を混同しないことで、実際の可用性影響を正確に表せる。
- **対象者数未確定時はデータ種別を先に固定する。** 件数確定を待たず、詐欺防止に必要な注意喚起を行える。

# 不明点・未公表事項

- 初期侵入経路と侵害開始日時
- 漏えいが実際に確認された件数と対象者数
- 取得されたデータ項目ごとの件数
- サービス復旧時期
- 二次被害の有無

[^yamato-second]: ヤマトホールディングス「〖第2報〗『クロネコ代金後払いサービス』への不正アクセスの発生について」2026-10-02.
