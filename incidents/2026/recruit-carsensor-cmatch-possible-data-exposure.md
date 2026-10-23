---
type: Cybersecurity Incident
title: "リクルート／カーセンサーnet・C-MATCH — 最大3,709,551件に漏えい可能性・サービス停止"
description: "中古車情報サイトと販売事業者向けSaaSへの不正アクセスを検知、最大370万9551件の応募・顧客・加盟店情報に漏えい可能性。複数サービス停止と影響調査を継続。"
resource: https://www.recruit.co.jp/newsroom/pressrelease/2026/1021_149447.html
tags: [japan, 2026, ecommerce, automotive, marketplaces, supply-chain, personal-data, outage]
status: draft
stale_after: 2026-10-27T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:47:11.196+00:00 }
incident:
  organization: "株式会社リクルート／カーセンサーnet・C-MATCH"
  sector: "automotive-marketplace-SaaS"
  jurisdiction: "JP"
  incident_status: "investigating_services_suspended"
  attack_type: "unauthorized-access"
  detected_at: "2026-10-17"
  first_disclosed_at: "2026-10-21"
  latest_public_update: "2026-10-21"
  intrusion_vector: "カーセンサー関連システムに対する第三者不正アクセス。技術詳細・CVE未公表"
  affected_services: "カーセンサーnet／アプリ、販売店向けC-MATCHと関連サービス"
  data_exposure: "possible"
  availability_impact: "10月17日17時頃から関連サービスを停止"
  restoration_state: "10月20日までに影響範囲の上限把握、原因調査と安全確認継続、再開は未確定"
  secondary_abuse: "二次悪用の実件数未公表"
  downstream_impact: "中古車販売店へ問い合わせた一般消費者と加盟販売店の担当者情報に波及"
  notification_state: "21日に公表し対象者対応を進行、最終通知完了は未確定"
  data_sensitivity: "氏名、電話、住所、メール、購入・問い合わせ内容、加盟販売店の業務・連絡先。カード決済情報とログインパスワード流出は未確認"
  public_record_checked_at: "2026-10-23T09:47:11.196+00:00"
sources:
  - id: recruit
    resource: https://www.recruit.co.jp/newsroom/pressrelease/2026/1021_149447.html
    title: "カーセンサーnetおよびC-MATCHにおける不正アクセスに関する公表"
    author: "organization:株式会社リクルート"
  - id: carwatch
    resource: https://car.watch.impress.co.jp/docs/news/2150016.html
    title: "リクルート、カーセンサーnetなどに不正アクセス、最大370万9551件"
    author: "organization:Car Watch／インプレス"
---

# リクルート／カーセンサーnet・C-MATCH — 最大3,709,551件に漏えい可能性・サービス停止

## 事業者が把握した攻撃と初動

10月17日、カーセンサーnet関連システムの不審アクセスを検知。安全確保のため**同日17時頃**からカーセンサーnet（アプリを含む）や販売店業務を支援する「C-MATCH」等を一時停止。10月20日までの調査で**最大3,709,551件**が漏えいした可能性のある個人情報項目・件数を把握し、21日に公表した。公表件数は**「最大影響範囲」**であり実取得・外部流出の確定件数ではない。[^recruit][^carwatch]

## 影響する二つの異なる母集団

| 領域 | 対象となるデータ主体 | 防御上の重要性 |
| --- | --- | --- |
| カーセンサーnet／アプリ | 販売店への問い合わせ・レビュー等の一般消費者、氏名・住所・連絡先・入力内容 | 中古車購入状況や問い合わせ内容から本人を装う電話・SMSへの転用が懸念される |
| C-MATCH | 利用販売店担当者・取引先、業務上の連絡先・ログイン識別子等 | 取引先の営業・顧客情報が一つのSaaSへ集中し、販売店にも波及し得る |

**最大3,709,551件**は各種データ区分の会社提示上限であり、人物の一意人数ではない。一次の詳細表は閲覧制限があり、すべての区分内訳について原本から再計算できていないので、未照合内訳を創作しない。決済情報・ログインパスワードの外部流出は会社が確認していないと報じられる。[^carwatch]

## 調査・復旧・業務への波及

一般利用者が中古車情報を検索・販売店へ問い合わせる入口だけでなく、販売店が顧客問合せを処理する業務支援基盤も停止対象となった。サービス停止による販売機会・取引処理の影響はあり得るが、**損失金額は会社公表を確認できない**。第三者による取得方法、実件数、サービス再開、調査完了、各顧客への通知は未確定。[^carwatch]

## 再発防止の証拠条件

公開前面からの情報取得APIと業務支援側の認可境界、販売店テナント分離、アクセスログの保持、悪用された認証/連携情報の切替、問い合わせ文面の長期保存と削除、顧客・販売店別の通知、停止中の代替業務。これらは調査論点であり、未公表の欠陥を断定しない。

**出典制限**：公式のリリースURLは確認されたが調査環境で本文を直接取得できず、会社発表を引用したCar Watchを用いて主要事実を交差確認した。

[^recruit]: 株式会社リクルート「カーセンサーnetおよびC-MATCHにおける不正アクセスに関する公表」. https://www.recruit.co.jp/newsroom/pressrelease/2026/1021_149447.html
[^carwatch]: Car Watch／インプレス「リクルート、カーセンサーnetなどに不正アクセス、最大370万9551件」. https://car.watch.impress.co.jp/docs/news/2150016.html
