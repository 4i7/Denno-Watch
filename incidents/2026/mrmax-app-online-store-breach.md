---
type: Cybersecurity Incident
title: MrMax — アプリ・オンラインストア侵害／最大1,735,154人の会員情報流出
description: MrMaxアプリとオンラインストアを構成するソフトウェアの機能が不正利用され、最大1,735,154人の会員情報の一部が外部へ流出した事案。
resource: https://www.mrmax.co.jp/info/incident_20261006/
tags: [japan, retail, mobile-app, ecommerce, unauthorized-access, personal-data, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 株式会社ミスターマックス
  sector: retail
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: "2026-10-03"
  detected_at: "2026-10-03 evening"
  first_disclosed_at: "2026-10-06"
  latest_public_update: "2026-10-06"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: "unauthorized use of a function in software composing the service; further details under investigation"
  affected_services: "MrMaxアプリ、オンラインストア"
  data_exposure: confirmed
  availability_impact: "発覚後にサービスを一時停止"
  restoration_state: "外部アクセス遮断・侵入経路対策済み、外部専門機関と詳細調査中"
  secondary_abuse: not_observed
  downstream_impact: "最大1,735,154人の会員情報"
  regulatory_response: "個人情報保護委員会へ報告、警察へ相談"
  notification_state: "対象者へメールで個別連絡"
  data_sensitivity: "会員ID、氏名、メールアドレス、電話番号"
sources:
  - id: mrmax-primary
    resource: https://www.mrmax.co.jp/info/incident_20261006/
    title: 不正アクセスによる情報流出に関するお詫びとお知らせ
    author: organization:株式会社ミスターマックス
---

# 概要

ミスターマックスは2026年10月3日夕方、MrMaxアプリおよびオンラインストアのサーバーに対する不審なアクセスを確認した。サービスを一時停止し、同日中に外部からのアクセスを遮断した。その後の調査で、第三者がサービスを構成するソフトウェアの機能を不正利用してサーバーへ侵入し、会員の個人情報の一部が外部へ流出したことを確認した。[^mrmax-primary]

対象は10月3日時点のアプリ会員・オンラインストア会員の最大**1,735,154人**で、会員ID、氏名、メールアドレス、電話番号が対象となる。住所、生年月日、クレジットカード情報、パスワード、購入履歴は流出していないことを確認している。[^mrmax-primary]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-10-03 夕方 | サーバーへの不審なアクセスを確認。サービス一時停止。[^mrmax-primary] |
| 2026-10-03 | 同日中に外部アクセスを遮断。[^mrmax-primary] |
| 2026-10-06 | 個人情報流出、最大対象人数、対象・非対象項目を公表。[^mrmax-primary] |

# 影響

最大1,735,154人の会員情報が対象となるが、登録状況によって各人の対象項目は異なる。公表時点で流出情報を悪用した被害は確認されていない。[^mrmax-primary]

# 技術的に確認できた事項

同社は「本サービスを構成するソフトウェアの機能を不正に利用してサーバーに侵入」と説明している。具体的なソフトウェア名、脆弱性識別子、悪用方法は公表していないため、一般的な脆弱性攻撃へ勝手に置き換えない。[^mrmax-primary]

# 対応と復旧

- 発覚後ただちにサービスを一時停止。[^mrmax-primary]
- 同日中に外部からのアクセスを遮断。[^mrmax-primary]
- 外部専門機関と詳細調査を実施し、監視体制を強化。[^mrmax-primary]
- 個人情報保護委員会へ報告し、警察へ相談。[^mrmax-primary]
- 対象会員へメールで個別連絡。[^mrmax-primary]

# 現在の状況と予後

2026年10月6日時点で侵入経路の遮断措置は実施済みだが、詳細調査は継続している。二次被害は未確認である。

# 防御上の教訓

- **アプリとECで共通する会員基盤は被害を横断させる共有境界になる。**
- **漏えい対象と非対象のデータクラスを明示する。** 購入履歴・決済・パスワードが対象外であることは被害評価に重要である。
- **「不正な機能利用」という公表粒度を守る。** 製品名やCVEが未公表の段階で、既知脆弱性へ結び付けない。

# 不明点・未公表事項

- 具体的な侵入機能・製品・脆弱性
- 不正アクセス開始時刻と滞留時間
- 実際に流出したユニーク人数
- サービス全面復旧時刻
- 最終フォレンジック結果

[^mrmax-primary]: 株式会社ミスターマックス「不正アクセスによる情報流出に関するお詫びとお知らせ」2026-10-06.
