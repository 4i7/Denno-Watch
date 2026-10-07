---
type: Cybersecurity Incident
title: 旭化成セラピューティクス / Pharma DIGITAL — 委託先運用DB侵害／医療従事者最大約51.4万人
description: 医療従事者向けPharma DIGITALの運営・情報管理委託先から会員DBへの不正アクセスが報告され、医療従事者最大約51.4万人と従業員約700人の個人情報が閲覧・取得された可能性がある事案。
resource: https://www.asahi-kasei.co.jp/pharma/oshirase_20261006.html
tags: [japan, healthcare, pharmaceutical, third-party, web-service, personal-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 旭化成セラピューティクス株式会社
  sector: pharmaceutical
  jurisdiction: JP
  incident_status: service_suspended_and_investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-10-02 provider notification"
  first_disclosed_at: "2026-10-06"
  latest_public_update: "2026-10-06"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: "third-party-operated member database; exact route not publicly disclosed, route remediation completed"
  affected_services: "医療従事者向け情報提供ウェブサイト Pharma DIGITAL"
  data_exposure: possible
  availability_impact: "Pharma DIGITALを即時停止し、停止を継続"
  restoration_state: "不正アクセス経路の是正済み、再アクセス未確認、外部専門組織・委託先と調査中"
  secondary_abuse: not_observed
  downstream_impact: "医療従事者最大約51.4万人、うちメールアドレス等を含む対象最大約4.4万人、従業員約700人"
  regulatory_response: "関係当局へ報告"
  notification_state: "対象医療従事者へ電子メール等で個別連絡予定・実施"
  data_sensitivity: "氏名、所属施設、施設住所、職種、診療科、メールアドレス等。クレジットカード情報・要配慮個人情報は非保管"
sources:
  - id: asahi-pharma-primary
    resource: https://www.asahi-kasei.co.jp/pharma/oshirase_20261006.html
    title: 医療従事者向け情報提供ウェブサイト「Pharma DIGITAL」への不正アクセスおよび個人情報漏えいの可能性について
    author: organization:旭化成セラピューティクス株式会社
---

# 概要

旭化成セラピューティクスは2026年10月2日、Pharma DIGITALの運営・情報管理を委託する医薬情報ネットから、同サービスに連携する会員データベースへのサイバー攻撃と不正アクセスが確認されたとの報告を受けた。個人情報が不正に閲覧または取得された可能性があるとして、Webサイトを即時停止し、10月6日に公表した。[^asahi-pharma-primary]

# 影響

対象となる可能性があるのは、医療従事者の氏名、所属施設名、施設住所、職種、診療科等で最大約**51万4,000人**。そのうちメールアドレス等も対象となる可能性がある人数は最大約**4万4,000人**で、これは別母集団として加算する数字ではなく「上記に加え」と公表されている。従業員については氏名、メールアドレス、写真が最大約700人対象となる。[^asahi-pharma-primary]

同社はクレジットカード情報と要配慮個人情報を保管していないとしている。公表時点で本件に起因する不正利用・被害は確認されていない。[^asahi-pharma-primary]

# 技術的に確認できた事項

侵害対象は委託先が運用・管理するPharma DIGITAL連携会員DBである。不正アクセス経路は既に是正されたとされるが、具体的な経路、製品、脆弱性、資格情報悪用の有無は公表されていない。[^asahi-pharma-primary]

# 対応と復旧

- 委託先からの報告後、Pharma DIGITALを即時停止。[^asahi-pharma-primary]
- 追加被害防止措置を実施し、不正アクセス経路を是正。[^asahi-pharma-primary]
- 公表時点で再度の不正アクセスは未確認。[^asahi-pharma-primary]
- 関係当局へ報告。[^asahi-pharma-primary]
- 外部専門組織・委託先と原因・影響範囲を調査。[^asahi-pharma-primary]
- 委託先管理・監督体制と情報セキュリティ管理体制の見直しを予定。[^asahi-pharma-primary]
- 対象医療従事者へ電子メール等で個別連絡。[^asahi-pharma-primary]

# 現在の状況と予後

2026年10月6日時点でサイト停止は継続している。侵入経路の是正は済んでいるが、原因詳細と最終影響範囲は調査中である。データ影響は possible として維持する。

# 防御上の教訓

- **委託先運用DBも自社データ境界として監督する。** Webサイト運営と情報管理を外部委託していても、通知・本人保護・サービス停止判断はデータ管理側へ戻る。
- **業務属性データの連結性を評価する。** 氏名、勤務先、職種、診療科、メールの組合せは、決済情報がなくても医療従事者を狙うなりすましの材料になり得る。
- **「51.4万人 + 4.4万人」と足さない。** 4.4万人は上位母集団の一部として追加項目が含まれると読む。
- **サイト停止と侵入経路是正は別マイルストーンで記録する。**

# 不明点・未公表事項

- 初期侵入経路
- 攻撃開始日時と滞留期間
- 実際に取得されたユニーク人数
- 委託先環境の他顧客・他サービスへの影響
- サービス再開時期
- 最終調査・再発防止結果

[^asahi-pharma-primary]: 旭化成セラピューティクス株式会社「医療従事者向け情報提供ウェブサイト『Pharma DIGITAL』への不正アクセスおよび個人情報漏えいの可能性について」2026-10-06.
