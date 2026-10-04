---
type: Cybersecurity Incident
title: カシオ ClassPad.net — 開発環境のセキュリティ設定解除による個人情報漏えい
description: 2023年10月のClassPad.net開発環境侵害について、誤操作・運用管理不備、国内外約12.7万件、即時停止、当局対応、翌年の別ランサムウェア事故との比較基準として記録する。
resource: https://www.casio.co.jp/release/2023/1018-incident/
tags: [japan, education, cloud, development-environment, misconfiguration, data-breach, casio, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: カシオ計算機株式会社
  sector: electronics-and-education-service
  jurisdiction: JP
  incident_status: public_report_matured
  attack_type: unauthorized-access-enabled-by-security-misconfiguration
  earliest_known_activity: unknown
  detected_at: "2023-10-11"
  first_disclosed_at: "2023-10-18"
  latest_public_update: "2023-10-18"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "development-environment network security setting left disabled due to operational error and insufficient management"
  affected_services: "ClassPad.net development-environment database only; production app access not confirmed"
  data_exposure: confirmed
  availability_impact: "development database stopped; ClassPad.net application remained available"
  restoration_state: "affected development database stopped; technical and operational controls strengthened"
  downstream_impact: "education institutions and individual users in Japan and 148 countries/regions"
  regulatory_response: "reported to PPC and JIPDEC/PrivacyMark review body; police consulted"
  notification_state: "all potentially affected users were to be notified by email or equivalent means"
sources:
  - id: casio-classpad
    resource: https://www.casio.co.jp/release/2023/1018-incident/
    title: 不正アクセスによる個人情報漏えいのお詫びとご報告
    author: organization:カシオ計算機
---

# 概要

2023年10月、カシオ計算機のICT教育アプリ「ClassPad.net」の**開発環境データベース**が第三者から不正アクセスを受け、国内外の利用者情報が漏えいした。国内は個人と1,108教育機関を合わせ91,921件、海外は148か国・地域で35,049件と公表された。[^casio-classpad]

原因についてカシオ自身は、所管部門の**システム誤操作と不十分な運用管理により、開発環境のネットワークセキュリティ設定の一部が解除状態だった**ことを確認したと説明した。これはゼロデイや高度な認証突破ではなく、開発環境の設定・変更管理が主要因として公表された事例である。

# インシデント発生時の環境

本件は、Llama 2やMistral 7Bの公開と同じ2023年後半に発生したが、攻撃者がLLMを使った証拠はない。むしろ重要なのは、攻撃者側の高度な能力がなくても、**外部到達可能な開発環境で防御設定が解除されたままなら大規模な漏えいが成立する**ことである。

教育SaaSでは氏名・メールだけでなく、学校名、学年、学級、出席番号等が組み合わされるため、未成年を含む可能性のある教育コンテキストを持つデータとして扱う必要がある。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2023-10-11夕方 | 担当者が開発環境で作業しようとした際にDB障害を認識。[^casio-classpad] |
| 2023-10-12夕方 | 海外在住者の個人情報が外部漏えいした事実を確認。 |
| 2023-10-16 | 個人情報保護委員会とプライバシーマーク審査機関へ報告。 |
| 2023-10-18 | 事故原因、影響件数、対応策を公表。 |

# 即応性

10月11日の異常認知から翌12日に外部漏えいを確認し、16日に当局等へ報告、18日に公開した。侵害がいつ開始したかは公表されていないため、「検知まで1日」とは言えないが、**障害認知後の影響確認・当局報告・公表は1週間以内**で進んだ。

攻撃対象となった開発環境DBは全停止し、外部専門のセキュリティ対応機関・法律事務所へ調査と法的対応を依頼、警察にも相談した。

# 影響

漏えい項目は次を含む。[^casio-classpad]

- 氏名。
- メールアドレス。
- 国・地域。
- 学校名、学年、学級名、出席番号・学籍番号。
- 注文明細、決済手段、ライセンスコード等の購買関連情報。
- サービス利用履歴、ニックネーム等。

クレジットカード情報は保持していなかった。

対象件数:

- 国内: 個人および1,108教育機関、計91,921件。
- 海外: 148か国・地域、計35,049件。

国内・海外の件数を「人数」とは表現せず、会社公表の件数単位を保持する。

# 被害境界

会社は、**開発環境DB以外には不正侵入の形跡を確認していない**とした。またClassPad.netアプリ自体には不正アクセスが発生しておらず、サービス利用への不具合影響はなかった。

これは開発環境と本番アプリの分離が被害範囲を限定した一方、開発環境に本番利用者の相当量の個人情報が存在したことを意味する。開発・分析・検証環境も本番データ境界として扱う必要がある。

# 原因と再発防止

確認済み原因:

- システムの誤操作。
- 運用管理の不十分さ。
- 開発環境ネットワークのセキュリティ設定の一部が解除状態。

事故後対策:

- ネットワーク経路とDBの技術的安全管理を強化。
- セキュリティ運用ルールを見直し。
- セキュリティ教育を継続・徹底。

# 2024年ランサムウェアとの関係

カシオは約1年後の2024年10月に、別のランサムウェア侵害を受けた。2023年ClassPad事案と2024年事案を一つの攻撃系列とみなす公開根拠はない。

ただしDenno Watchでは、同一企業で**開発環境の設定・運用不備**に続き、翌年に**フィッシング対策とグローバルネットワークセキュリティ体制の一部不備**を会社自身が公表した点を、再発防止策の実効性・異なる失敗モードの比較対象として追跡する。

「再発したから2023年対策が無効だった」と単純化せず、2023年対策の対象は開発環境・設定運用、2024年対策対象はメール・グローバルネットワーク・ランサムウェア耐性等と分離する。

# 事故前セキュリティ開示との比較

本件で重要なのは、一般的なセキュリティ方針の有無よりも、**設定変更の承認・監視・自動検証、開発環境への本番データ保持、外部到達性**である。

2024年のカシオ統合報告書は後にゼロトラスト、ISMS、教育等のKPIを明示したが、これは2023年ClassPad事故後に作成された資料であるため、本件の「事故前能力」を示す資料として遡及利用しない。

# 2026年までの予後

2026年10月4日の再確認では、2023年10月18日公表内容を大幅に更新する独立した最終事故報告は確認できなかった。二次被害や追加件数を公開根拠なく補わない。

長期的には、翌2024年の別ランサムウェア事案と合わせ、カシオがセキュリティKPI、ゼロトラスト、SOC、第三者監査等をどこまで実装したかを企業単位の再発防止追跡で評価する。

# 防御上の教訓

- 開発環境も本番個人データを置くなら本番相当の安全基準を要求する。
- ネットワークセキュリティ設定の解除を、人手の注意だけでなくポリシー検査・変更監査で検知する。
- データ最小化により開発DBが侵害された際の対象件数を減らす。
- 障害認知から「不正アクセスか」を切り分ける手順を事前化する。
- 同一企業の複数事故は、同じ原因か異なる失敗境界かを分けて追う。

# 不明点

- 不正アクセス開始時刻・滞留期間。
- 攻撃者が設定解除状態をどのように発見したか。
- 漏えい件数のユニーク人数換算。
- 2023年対策の独立検証結果。
- 本件でLLM/生成AIが使用された公開証拠はない。

[^casio-classpad]: カシオ計算機「不正アクセスによる個人情報漏えいのお詫びとご報告」2023-10-18.