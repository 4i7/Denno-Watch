---
type: Cybersecurity Incident
title: カシオ計算機 / ClassPad.net — 開発環境データベースへの不正アクセス
description: 2023年10月、ClassPad.netの開発環境DBが外部から閲覧可能な状態となり、不正アクセスで国内外の個人情報が流出した事案。
resource: https://www.casio.co.jp/release/2023/1018-incident/
tags: [japan, education, cloud, development-environment, misconfiguration, personal-data, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: カシオ計算機株式会社
  sector: electronics-education
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: unauthorized access to development environment database
  earliest_known_activity: "2023-10"
  detected_at: "2023-10-11"
  first_disclosed_at: "2023-10-18"
  notification_state: "対象顧客へ電子メール等で順次連絡する予定、全通知完了は未公表"
  regulatory_response: "2023-10-16 個人情報保護委員会とJUASへ報告、警察へ相談"
  latest_public_update: "2023-10-18"
  public_record_checked_at: "2026-10-08T10:02:29.723+00:00"
  intrusion_vector: "development environment security setting disabled due operational error and insufficient operational management"
  affected_services: "ClassPad.net development environment database"
  data_exposure: confirmed
  availability_impact: "production ClassPad.net service itself was not identified as compromised"
  restoration_state: "settings corrected and technical/operational recurrence measures announced"
  ai_relation: era_context_only
sources:
  - id: casio-2023
    resource: https://www.casio.co.jp/release/2023/1018-incident/
    title: 不正アクセスによる個人情報漏えいのお詫びとご報告
---

# 概要

カシオ計算機は、教育サービス「ClassPad.net」の**開発環境**に置かれたデータベースへ第三者が不正アクセスし、国内外の利用者等の個人情報が流出したと公表した。対象は合計126,970件（国内91,921件、海外35,049件）とされた。[^casio-2023]

本番サービス全体が侵害された事案ではなく、開発環境の境界・設定・運用管理が中心となるケースである。

# 発生環境と原因

同社は、開発環境でネットワークセキュリティ設定の一部が解除された状態になり、運用管理も不十分だったことを原因として説明した。開発環境が本番より緩い統制になりやすいという一般的な問題を、具体的な情報漏えいとして示す。[^casio-2023]

公開調査では、開発環境DB以外へ侵入した痕跡は確認されず、本番ClassPad.net自体への侵入と同一視してはならない。

# 初動

10月11日夕方にデータベース障害を確認して調査を開始し、翌12日に海外からの不正アクセスと個人情報流出を確認、18日に公表した。公開時刻の精度が十分でない部分があるため、時間単位の封じ込め指標は作らない。

# 再発防止

同社はネットワーク・データベース両面の技術対策に加え、設定変更・開発運用の管理ルール、教育を見直すとした。防御上は、クラウドや開発環境の設定変更を一時作業として扱わず、構成状態を継続的に検証する必要がある。

# 長期比較上の重要性

カシオは翌2024年に別の全社的なランサムウェア被害を受けた。二つの事故は侵入面が異なり、2023年事故を2024年事故の直接原因とは扱わない。ただし、同一企業で異なる境界の重大事故が続いたため、再発防止策を「前事故の穴を塞いだか」だけでなく、組織全体のセキュリティ統制へ拡張できたかという観点で追う価値が高い。

# 防御上の教訓

- 開発・検証環境にも本番相当のデータを置く場合、ネットワーク境界とデータ保護を本番同等に監視する。
- 一時的な設定解除には自動復帰、期限、承認、構成監視を持たせる。
- 「事故後に対策した」と「企業全体で同種の統制が有効になった」を区別する。
- AI/LLMが攻撃に使われた証拠はない。


## 出典に基づくデータ項目と利用者の分類

2023年10月18日の一次公表で確認された漏えい項目は、**氏名・メールアドレス・国/地域、学校名・学年・学級・出席番号（学籍番号）、購入に関する注文内容・決済手段・ライセンスコード、サービス利用履歴・ニックネーム**等である。一方、**クレジットカード情報は会社が保持していない**。[^casio-2023]

| 区分 | 対象件数 | 注意点 |
| --- | ---: | --- |
| 国内 | 91,921件 | 個人と1,108教育機関を含むと公表。教育機関数と個人件数は同じ単位ではない |
| 海外 | 35,049件 | 148の国と地域の顧客 |
| 合計 | **126,970件** | 2023年10月18日時点の暫定値。ユニーク被害者人数とは限らない |

## 検知から遮断・報告まで

| 日付 | 事実 |
| --- | --- |
| 2023-10-11夕方 | 開発環境の作業時にDB障害を検知し調査開始 |
| 2023-10-12夕方 | 海外在住者の個人情報の外部漏えいを確認 |
| 2023-10-16 | **個人情報保護委員会と日本情報システム・ユーザー協会**（プライバシーマーク審査機関）に報告 |
| 2023-10-18 | 不正アクセス、原因、国内外の対象件数を公表 |

攻撃対象だった**開発DBは全停止**。会社は外部の技術専門家・法律事務所、警察と協力して調査・法的対応を進めるとした。利用者へのメール等の通知は予定であり、最終連絡完了は公表時点では未確定。**本番アプリ自体には不正アクセスがなく、利用に障害もない**との公表も保持する。[^casio-2023]

## 原因と実際の統制境界

会社が確認したのは、所管部門の**操作ミスと運用管理の不十分さ**により、開発環境の**ネットワークセキュリティ設定の一部が解除**され、外部から到達できる状態だったということ。CVEや特定のクラウド製品が悪用された証拠はなく、開発環境が本番DBと同じ管理境界だったとの推測もしない。[^casio-2023]

再発防止に向けて、ネットワーク・DBの技術的な安全管理、運用ルール、担当者教育を改善する方針を公表した。対応の**発表**と全環境での**実施・独立検証**を分け、翌2024年の別ランサムウェア事故の直接的な原因として結び付けない。

[^casio-2023]: カシオ計算機「不正アクセスによる個人情報漏えいのお詫びとご報告」2023-10-18.