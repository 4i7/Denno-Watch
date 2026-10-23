---
type: Cybersecurity Incident
title: "H2Oリテイリング・阪急阪神百貨店 — 3サイト侵害・H2O ID約126万件流出とEC二次調査"
description: "予約サイトから共通顧客管理に到達しH2O ID会員約126万件の漏えいが判明。別のEC・リモート注文システムでも侵入を検知し3サービス停止。"
resource: https://www.h2o-retailing.co.jp/ja/news/auto_20261019552921.html
tags: [japan, 2026, retail, ecommerce, shared-identity, multi-site, personal-data]
status: draft
stale_after: 2026-10-27T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:47:11.196+00:00 }
incident:
  organization: "エイチ・ツー・オー リテイリング株式会社／株式会社阪急阪神百貨店"
  sector: "retail-ecommerce"
  jurisdiction: "JP"
  incident_status: "investigating_multiservice_suspension"
  attack_type: "unauthorized-access-multiple-service-systems"
  detected_at: "2026-10-16"
  first_disclosed_at: "2026-10-19"
  latest_public_update: "2026-10-19"
  intrusion_vector: "予約サイト経由でH2O ID管理系へ不正アクセス。詳しい入口や欠陥未公表"
  affected_services: "阪急百貨店・阪神百貨店予約サイト、HANKYU HANSHIN E-STORES、Remo Order、共通H2O ID"
  data_exposure: "confirmed"
  availability_impact: "10月16日予約サイト停止、10月17日ほか2サービス停止"
  restoration_state: "外部不正通信を遮断、3サイト停止・専門家調査継続。再開日未公表"
  secondary_abuse: "フィッシング等を注意喚起、当該侵害の実二次不正利用件数未公表"
  regulatory_response: "PPCへの報告と警察被害申告を実施と19日公表"
  notification_state: "Web・窓口で案内、全件個別通知の完了は未確定"
  data_sensitivity: "H2O ID、氏名、性別、生年月日、メール、住所、携帯電話番号等、ECでは一部のカード関連情報が調査対象"
  public_record_checked_at: "2026-10-23T09:47:11.196+00:00"
sources:
  - id: h2o
    resource: https://www.h2o-retailing.co.jp/ja/news/auto_20261019552921.html
    title: "第三者による不正アクセス発生と個人情報漏えいに関するお詫びとお知らせ"
    author: "organization:エイチ・ツー・オー リテイリング株式会社"
  - id: fnn
    resource: https://www.fnn.jp/articles/-/1135407
    title: "阪急阪神百貨店が運営する3つのサイトに不正アクセス"
    author: "organization:関西テレビ／FNN"
---

# H2Oリテイリング・阪急阪神百貨店 — 3サイト侵害・H2O ID約126万件流出とEC二次調査

## 共通IDの集中境界と3システム停止

エイチ・ツー・オー リテイリングは10月16日、阪急阪神百貨店の**予約サイトを経由した不正アクセス**を検知し、サイトへの外部通信遮断とサービス停止を実施。翌17日、別の2サイト「HANKYU HANSHIN E-STORES」「Remo Order」への不正アクセスも確認し両サービスを停止。10月19日に**H2O ID会員に関する約126万件の個人情報の一部が流出した**と公表した。[^h2o][^fnn]

| サービス・領域 | 侵害と対応 | 件数の認定 |
| --- | --- | --- |
| 阪急・阪神百貨店予約サイト | 10月16日侵害検知、外部アクセス遮断・サイト停止 | H2O ID登録会員**約126万件**の一部漏えいと公表 |
| HANKYU HANSHIN E-STORES | 10月17日不正アクセスを確認、停止 | 影響人数・最終情報項目を調査中 |
| Remo Order | 10月17日不正アクセスを確認、停止 | 影響人数・最終情報項目を調査中 |
| H2O ID共通基盤 | 氏名、住所、連絡先、生年月日など複数サイトで共有 | **約126万件＝対象の会員データ記録数**。別サイトの人数を無検証に加算しない |

## 支払情報の確度と悪用の評価

リリースではE-STORESとRemo Orderに保存した**カード関連データの一部の漏えい可能性**も調査対象である。ただし決済情報の非保持化対策を行い、ポイントカード番号も末尾4桁のみ保持しているため、それらからの不正利用可能性はないと会社が説明した。**完全なカード番号・セキュリティコード流出や実際のカード不正決済は確定していない**。[^h2o][^fnn]

## インシデント対応の進捗

会社は侵入への応急遮断、外部専門家との調査、PPCへの報告と警察への被害申告を説明。予約機能とEC・リモート注文という別系統の可用性損失を分離し、全サイト再開を安全確認前に既成事実化しない。[^h2o]

## 被害者対応・監査

利用者へは実際のグループ会員情報を悪用したメール・SMS・電話に注意喚起。顧客のID/氏名/注文履歴が悪用される可能性はあるが、実二次被害の具体的件数は未確認。責任分界上、予約入口と共通顧客管理のアクセス境界、EC個別の脆弱性との同一性、ログの保存、最終取得量、対象者通知、復旧日時、決算影響を追跡する。

**出典上の留保**：一次発表ページは会社の正式リリースURLであるが、取得環境で本文を直接展開できなかったため、該当公表を当日報道で交差照合した。後日一次PDF原本を取り直し、個別情報項目・各サイト件数の確度を再評価する。

[^h2o]: エイチ・ツー・オー リテイリング株式会社「第三者による不正アクセス発生と個人情報漏えいに関するお詫びとお知らせ」. https://www.h2o-retailing.co.jp/ja/news/auto_20261019552921.html
[^fnn]: 関西テレビ／FNN「阪急阪神百貨店が運営する3つのサイトに不正アクセス」. https://www.fnn.jp/articles/-/1135407
