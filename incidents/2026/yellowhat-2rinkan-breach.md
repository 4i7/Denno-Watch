---
type: Cybersecurity Incident
title: ２りんかんイエローハット — API悪用による317万9454名分の会員情報漏えい
description: 2026年4月に検知された２りんかん会員専用サーバーへの不正アクセスと、最終調査で3,179,454名分の会員データ取得が確認された事案を追跡する記録。
resource: https://www.yellowhat.jp/information/2rinnkan/202606.html
tags: [japan, retail, automotive, unauthorized-access, api, personal-data, credentials, 2026]
status: stable
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:30:00Z }
incident:
  organization: 株式会社２りんかんイエローハット / 株式会社イエローハット
  sector: automotive-retail
  jurisdiction: JP
  incident_status: public_report_closed_service_rebuild_pending
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-04-20 evening JST"
  first_disclosed_at: "2026-04-23"
  latest_public_update: "2026-06-19"
  intrusion_vector: "abuse of application API mechanism; lower-level technical cause not publicly disclosed"
  affected_services: "2りんかん member server and 2りんかん app"
  data_exposure: confirmed
  availability_impact: "2りんかん app functionality restricted during rebuild"
  restoration_state: "app rebuild underway; restart targeted for October 2026 as of final report"
  secondary_abuse: not_publicly_confirmed
sources:
  - id: yh-first
    resource: https://www.yellowhat.jp/information/2rinnkan/202604.html
    title: 当社連結子会社（株式会社２りんかんイエローハット）における個人情報漏えいの可能性に関するご報告
    author: organization:Yellow Hat Ltd.
  - id: yh-second
    resource: https://www.yellowhat.jp/information/2rinnkan/202605.html
    title: 当社連結子会社（株式会社２りんかんイエローハット）における個人情報漏えいの可能性に関するご報告（第二報）
    author: organization:Yellow Hat Ltd.
  - id: yh-final
    resource: https://www.yellowhat.jp/information/2rinnkan/202606.html
    title: 連結子会社における不正アクセスによる個人情報漏えいに関するお詫びとお知らせ（第三報・最終報）
    author: organization:Yellow Hat Ltd.
---

# 概要

2026年4月20日夕刻、２りんかんイエローハットが管理する会員専用サーバーへの不正アクセスを検知した。ネットワーク遮断などの緊急措置後、外部専門家による調査を開始し、4月23日に会員情報漏えいの可能性を公表した。[^yh-first]

5月1日の第二報では、サーバー管理会社が不正なデータ持ち出しの痕跡を確認し、漏えい可能性のある対象を最大3,455,754名分とした。[^yh-second]

6月19日の第三報・最終報では、詳細なログ解析により、アプリの仕組みであるAPIを悪用した不正アクセスで会員データが取得されたことを特定し、対象数を**3,179,454名分**に確定した。第二報の最大値から276,300名分下方修正された。[^yh-final]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-04-20 evening | 会員専用サーバーへの不正アクセスを検知。ネットワーク遮断等を実施。[^yh-first] |
| 2026-04-23 | 第一報。会員情報漏えいの可能性、アプリサービスの一部停止、外部調査開始を公表。[^yh-first] |
| 2026-05-01 | 第二報。データ持ち出し痕跡と最大3,455,754名分の対象データを公表。[^yh-second] |
| 2026-06-19 | 第三報・最終報。APIの仕組みを悪用した不正アクセスと、3,179,454名分の実際の取得を確定。個人情報保護委員会への確報提出済み。[^yh-final] |
| 2026-06-19 | ２りんかんアプリはシステム再構築中で、2026年10月を目途に再開予定と公表。[^yh-final] |

# 影響

## 露出が確認された対象者

最終的に3,179,454名分の会員データ取得が確認された。対象は２りんかん（旧ドライバースタンドを含む）のポイント会員、モバイル会員、アプリ会員。[^yh-final]

漏えい項目は、氏名、住所、電話番号、生年月日、性別、メールアドレス、会員番号、アプリユーザーID、アプリパスワード、ポイント残高、車両情報。[^yh-final]

クレジットカード情報は外部決済システムを使用しており社内に保持していなかったため、本件での漏えいは発生していない。また、イエローハット店舗および他ブランドの顧客情報への影響はないと確認された。[^yh-final]

## 可用性と顧客対応

事故後、２りんかんアプリの利用を制限し、アプリ本体のセキュリティ強化と通信監視強化を含むシステム再構築を実施。対象者にはホームページ、電話、アプリ内通知、メール、SMS、書面で個別案内を完了した。[^yh-final]

# 技術的に確認できた事項

公開された最終報告で確認できる技術的な原因表現は「アプリの仕組み（API）を悪用した不正アクセス」までである。具体的な脆弱性、認証・認可上の欠陥、攻撃開始日時、攻撃者、取得方法の詳細は公開されていない。[^yh-final]

したがって本記録では、API悪用が確認された事実と、その下位レベルの根本原因が未公表であることを分離する。

# 復旧と予後

最終報告時点で、個人情報保護委員会への確報提出と警察への被害申告・捜査協力を実施。アプリはセキュリティ強化を伴う再構築を進め、2026年10月を目途にサービス再開予定とされた。[^yh-final]

再開完了の実績、漏えい情報の二次利用の有無、アプリパスワードに対する追加措置の詳細は、この最終報告だけでは確認できない。

# 防御上の教訓

- **データ分離は実被害を限定した。** クレジットカード情報を別の外部決済系に分離し、本件対象サーバーに保持しなかったため、決済情報は漏えい対象外となった。[^yh-final]
- **論理的なサービス分離も被害範囲を制限した。** ２りんかんの会員システムと、イエローハット店舗・他ブランドの顧客システムが独立していたため、他ブランドへの横展開は確認されなかった。[^yh-first][^yh-final]
- **中間値と確定値を分離する必要がある。** 最大3,455,754名という第二報の値は、最終的に3,179,454名へ更新された。速報値を永続的な確定値として扱わないことが重要である。[^yh-second][^yh-final]
- **API層を独立した監視対象として扱う必要がある。** 公開情報は詳細な弱点を示していないが、最終報告がAPIの仕組みの悪用を明示しているため、Web画面だけでなくAPIの認証・認可・異常利用監視を別レイヤーとして扱うことが防御上重要である。[^yh-final]

# 不明点

- 不正アクセスの開始日時と滞在期間
- API悪用を可能にした具体的な設計・実装上の条件
- 攻撃者の属性・帰属
- 取得データの外部公開や二次利用の有無
- 2026年10月予定のアプリ再開が実際に完了した日時

これらは公開一次資料で確認できるまで推測しない。

[^yh-first]: イエローハット第一報。
[^yh-second]: イエローハット第二報。
[^yh-final]: イエローハット第三報・最終報。
