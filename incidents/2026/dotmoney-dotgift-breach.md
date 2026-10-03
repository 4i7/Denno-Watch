---
type: Cybersecurity Incident
title: ドットマネー / ドットギフト — 不正アクセスによる長期全面停止・段階復旧とドットギフト終了
description: 2026年6月8日の不正アクセスを契機にポイント交換基盤を全面停止し、安全環境再構築後にドットマネーを段階再開する一方、ドットギフトは9月30日で終了した事案を追跡する。
resource: https://support.d-money.jp/hc/ja/articles/61069824277657-
tags: [japan, fintech, points, digital-gift, unauthorized-access, availability, service-termination, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T06:23:00+09:00 }
incident:
  organization: "ドットマネー / ドットギフト（事故当時サイバーエージェント系サービス、2026-08-10にドットマネー運営をGMOタウンWiFiへ変更）"
  sector: points-and-digital-gifts
  jurisdiction: JP
  incident_status: "dotmoney_restored_dotgift_terminated"
  attack_type: unauthorized-access
  earliest_known_activity: "2026-06-08"
  detected_at: "2026-06-08"
  first_disclosed_at: "2026-06-11 detailed public notice referenced by later notices"
  latest_public_update: "2026-09-30 service termination milestone for DotGift"
  public_record_checked_at: "2026-10-04T06:23:00+09:00"
  intrusion_vector: not_publicly_disclosed_in_reviewed_sources
  affected_services: "DotMoney and DotGift services"
  data_exposure: not_fully_publicly_disclosed_in_reviewed_sources
  availability_impact: "all services stopped from 2026-06-08; DotMoney began phased restart 2026-08-12; DotGift remained stopped and terminated 2026-09-30"
  restoration_state: "DotMoney resumed after security validation with mandatory phone verification for exchanges; DotGift was not restored and was terminated"
  secondary_abuse: "unauthorized use of customer-held DotMoney was reported as not observed before restart"
  downstream_impact: "exchange requests, partner-point conversions, expiring balances and unused digital gifts required remediation or replacement"
  regulatory_response: not_publicly_disclosed_in_reviewed_sources
  notification_state: "service-wide public notices and specific procedures for balance/gift remediation"
  business_continuity: "pending exchanges were cancelled/refunded to DotMoney balances; expired balances were re-granted; unused DotGift balances could be exchanged to an alternative product"
  data_sensitivity: "account, point/balance and exchange context; exact confidentiality impact not fully described in the reviewed public notices"
sources:
  - id: dotgift-end
    resource: https://support.d-money.jp/hc/ja/articles/46625076215577-
    title: 「ドットギフト」サービス終了のお知らせ
    author: organization:DotMoney
  - id: dotmoney-resume
    resource: https://support.d-money.jp/hc/ja/articles/61069824277657-
    title: ドットマネーのサービス再開および運営会社変更のお知らせ
    author: organization:DotMoney
  - id: dotmoney-phone-auth
    resource: https://support.d-money.jp/hc/ja/articles/60583753125529-
    title: 2026年8月 交換申請時に携帯電話番号による本人認証が必須となりました
    author: organization:DotMoney
---

# Executive summary

2026年6月8日、ドットマネー/ドットギフトのシステムへの不正アクセスが確認され、顧客情報・保有マネー等の安全確保を理由に**全サービスが停止**された。ドットマネーは安全性確認後、8月12日12時以降に機能単位で段階再開した。一方、ドットギフトは停止状態から復旧せず、9月30日をもってサービス提供を終了した。[^dotgift-end][^dotmoney-resume]

これは「サービス再開」を一律の成功状態として扱えない事例である。同一インシデント後に、一方のサービスはセキュリティ制御を追加して再開し、他方は**恒久終了**という異なる予後をたどった。[^dotgift-end][^dotmoney-resume]

再開時点で、顧客保有マネーの不正利用はないことを改めて確認したと公表され、全ユーザーの交換申請に携帯電話番号による本人認証が必須化された。停止中に未完了だった交換や失効した残高についても返却・再付与等の救済措置が実施された。[^dotmoney-resume][^dotmoney-phone-auth]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-06-08 | システムへの不正アクセスを確認。ドットマネー・ドットギフト全サービスを停止。[^dotgift-end][^dotmoney-resume] |
| 2026-06-11 | サービス一時停止と事故について詳細告知（後続公表から参照）。[^dotgift-end] |
| 2026-07-14 | ドットギフトを2026-09-30で終了する方針を公表。未使用ギフト/残高の代替交換を案内。[^dotgift-end] |
| 2026-07-13 / 08-05 | メンテナンス中に失効した一部マネーを再付与。[^dotmoney-resume] |
| 2026-08-10 | ドットマネー運営会社をGMOタウンWiFiへ変更。[^dotmoney-resume] |
| 2026-08-12 | 安全性確認済み機能からドットマネーを順次再開。交換申請時の携帯電話本人認証を必須化。[^dotmoney-resume][^dotmoney-phone-auth] |
| 2026-09-30 | ドットギフトを完全終了。[^dotgift-end] |
| 2026-10-04 | 現行公開記録を再確認。 |

# Impact

## Availability and business impact

6月8日からドットマネーの段階再開まで約2か月、ポイント交換を含むサービス全般が利用不能となった。ドットギフトは復旧せず終了した。[^dotgift-end][^dotmoney-resume]

停止前に申請済みで未完了だった交換は取り消され、残高へ返却された。停止中に失効した残高には再付与と新しい期限が設定された。サービス障害が資産・権利の有効期限へ波及したため、単なるWeb可用性障害ではない。[^dotmoney-resume]

## Confidentiality and fraud state

レビューした公開資料では、不正アクセスの具体的侵入経路や個人情報漏えい対象の詳細は十分に開示されていない。そのため情報漏えいの有無・件数を推定しない。

ドットマネー再開時、顧客の保有マネーに不正利用がない旨を改めて確認したと公表された。[^dotmoney-resume]

# Technical findings

公開資料から具体的な脆弱性、認証突破方式、攻撃主体は確定できない。安全な環境の再構築を進めたこと、再開時に交換申請へ携帯電話番号本人認証を追加したことは確認できる。[^dotgift-end][^dotmoney-resume]

本人認証必須化は、侵入経路そのものが電話認証欠如だったことを意味しない。公開された再発防止/安全性向上策として記録する。

# Response and recovery

- 6月8日に全サービス停止。[^dotmoney-resume]
- 原因究明と安全な環境の再構築を実施。[^dotgift-end]
- 未完了交換を取り消して残高へ返却。[^dotmoney-resume]
- メンテナンス中に失効したマネーを再付与。[^dotmoney-resume]
- ドットマネーは8月12日から段階再開。[^dotmoney-resume]
- 交換申請時の携帯電話番号本人認証を全ユーザーで必須化。[^dotmoney-phone-auth]
- ドットギフト未使用分/残高は代替の「えらべるPay」への交換窓口を設置。[^dotgift-end]
- ドットギフトは9月30日にサービス終了。[^dotgift-end]

# Prognosis / current state

ドットマネーは再開し、交換先も安全性確認済みのものから順次復旧した。ドットギフトは事故前状態へ戻すのではなくサービス終了が選択された。したがって予後は「復旧」と「廃止」に分岐している。[^dotgift-end][^dotmoney-resume]

# Defensive lessons

- **インシデントの最終状態に「サービス終了」を持つ。** 全面停止後に必ず旧サービスを復旧するとは限らない。
- **可用性障害が顧客資産の期限へ与える影響を管理する。** ポイント・残高・交換申請は停止期間中も時間依存であり、返却・期限延長/再付与が必要になる。
- **復旧を機能単位で段階化する。** 安全性を確認できた交換先・機能から再開することで、全系一斉復旧を避けた。
- **再開時に高リスク操作へ追加認証を導入する。** 交換申請という価値移転操作に電話番号本人認証を必須化した。
- **事業移管もインシデント後の予後として記録する。** 運営主体変更を事故そのものの原因と混同しない一方、長期的なサービス状態の一部として追跡する。

# Unknowns / withheld details

- 初期侵入経路・利用脆弱性・認証情報悪用の有無
- 個人情報またはサービス内部データの外部取得有無と範囲
- 攻撃者の滞留期間
- 安全な環境再構築の具体的技術内容
- ドットギフトを復旧せず終了する判断における技術要因と事業要因の内訳

[^dotgift-end]: ドットマネー「『ドットギフト』サービス終了のお知らせ」2026-07-14、サービス完全終了2026-09-30.
[^dotmoney-resume]: ドットマネー「ドットマネーのサービス再開および運営会社変更のお知らせ」2026-08-12以降の公開内容.
[^dotmoney-phone-auth]: ドットマネー「2026年8月 交換申請時に携帯電話番号による本人認証が必須となりました」.
