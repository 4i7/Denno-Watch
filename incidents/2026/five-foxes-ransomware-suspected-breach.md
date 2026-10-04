---
type: Cybersecurity Incident
title: ファイブフォックス — ランサムウェア感染疑いを伴う不正アクセスと顧客・従業員情報流出可能性
description: 2026年7月に検知されたファイブフォックスグループの不正アクセスと、9月の第二報で明らかになった顧客・従業員情報の流出可能性を追跡する記録。
resource: https://www.fivefoxes.co.jp/2026/09/post-23.html
tags: [japan, retail, apparel, unauthorized-access, ransomware-suspected, personal-data, employee-data, 2026]
status: draft
stale_after: 2026-10-31T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:55:00Z }
incident:
  organization: 株式会社ファイブフォックス / 株式会社コムサ
  sector: apparel-retail
  jurisdiction: JP
  incident_status: investigating
  attack_type: "unauthorized access; ransomware infection was suspected in the first report but not publicly confirmed in the second"
  earliest_known_activity: unknown
  detected_at: "2026-07-08"
  first_disclosed_at: "2026-07-14"
  latest_public_update: "2026-09-08"
  intrusion_vector: not_publicly_disclosed
  affected_services: "part of Five Foxes group internal systems; internet and mail functions were stopped during containment"
  data_exposure: possible_not_confirmed
  availability_impact: "affected internal systems, internet and mail functions stopped; stores and online store remained operational"
  restoration_state: "affected environment remains stopped; customer information moved to a new environment with additional safeguards"
  secondary_abuse: "not observed as of 2026-09-08"
sources:
  - id: five-first
    resource: https://www.fivefoxes.co.jp/2026/07/post-20.html
    title: ランサムウェア感染の可能性に関するお知らせとお詫び
    author: organization:Five Foxes
  - id: five-second
    resource: https://www.fivefoxes.co.jp/2026/09/post-23.html
    title: 不正アクセスによる個人情報流出の可能性についてのお知らせとお詫び（第二報）
    author: organization:Five Foxes
---

# 概要

2026年7月8日、ファイブフォックスは第三者による不正アクセスを確認し、対象システムを停止してネットワークを遮断した。同日、対策本部を立ち上げ、外部専門調査機関と影響範囲・原因・復旧の調査を開始した。[^five-second]

7月14日の第一報では、本社サーバーの一部が「ランサムウェアに感染している可能性」があると公表した。被害拡大抑止のためサーバー、インターネット、メール機能等を停止した一方、店舗と別システムのオンラインストアは通常営業を継続した。[^five-first]

9月8日の第二報では表現が「一部システムに対する不正アクセス」となり、一部の顧客・従業員情報に流出の可能性が判明したと公表した。ランサムウェア感染が最終的に確認されたとは記載されていないため、本記録では**ランサムウェア感染疑いを伴う不正アクセス**として扱う。[^five-second]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-07-08 | 第三者による不正アクセスを確認。対象システム停止、ネットワーク遮断。対策本部設置、外部専門調査機関との調査開始。[^five-second] |
| 2026-07-14 | 第一報。本社サーバーの一部でランサムウェア感染の可能性を公表。インターネット・メール機能等を停止。店舗とオンラインストアは営業継続。[^five-first] |
| 2026-09-08 | 第二報。一部の顧客・従業員情報について流出の可能性を公表。対象者への封書通知開始。[^five-second] |
| 2026-09-08 | 影響を受けた環境は停止継続。顧客情報は必要な安全対策を講じた新しい環境で管理していると説明。[^five-second] |

# 影響

## 顧客情報

流出可能性が公表された顧客情報は二群に分かれる。[^five-second]

- 2021年9月〜2026年6月のファイブフォックスメンバーズカードVIP/GOLDランクの一部: **59,504件**
  - 氏名、住所、電話番号、生年月日、性別、登録店舗、会員ランク、会員番号
- 2008年1月〜2026年6月のカスタマーサービス問い合わせ利用者の一部: **8,403件**
  - 氏名、住所、電話番号

両群の重複有無は公表されていないため、単純合計67,907件をそのまま67,907人と解釈しない。

## 従業員情報

- 2024年1月〜2026年6月にファイブフォックスへ在籍していた現・元従業員: **2,450件**
  - 氏名、住所、電話番号、生年月日、性別、人事情報
- 2011年10月〜2026年3月に株式会社コムサへ在籍していた現・元従業員: **2,828件**
  - 氏名、住所、電話番号、生年月日、性別、口座情報、人事情報等[^five-second]

全区分の単純合計は73,185件だが、重複を除いた人数としては扱えない。

## 明示的に対象外とされたデータ

クレジットカード情報とマイナンバー情報は影響を受けたシステムで取得しておらず、流出可能性のある情報に含まれないと公表された。[^five-second]

9月8日時点で、本件に関わる個人情報の不正利用等は確認されていない。[^five-second]

# 可用性と事業継続

第一報では、被害拡大抑止のためサーバー、インターネット、メール機能等を停止した。一方、店舗は通常営業を継続し、オンラインストアも別システムで運営されていたため影響なしとされた。[^five-first]

この点は、内部業務系の侵害が発生しても販売チャネルを全停止させない分離設計が事業継続に寄与した観測例として重要である。

# 技術的所見と証拠状態

確認済みなのは第三者による不正アクセスと、影響を受けた環境の停止・隔離である。第一報は本社サーバーの一部についてランサムウェア感染の「可能性」を述べたが、第二報はランサムウェア感染を確定事項として再掲していない。[^five-first][^five-second]

公開されていないもの:

- 侵入経路
- 攻撃開始時刻・滞在期間
- ランサムウェア感染が最終的に確認されたか
- マルウェア・ランサムウェアの名称
- 攻撃主体
- データの外部持ち出しが実際に確認されたか
- 身代金要求・支払いの有無

外部の攻撃者主張や第三者推測を、会社が確認した事実と混同しない。

# 復旧と予後

9月8日時点で影響を受けた環境は停止されたままで、顧客情報は必要な安全対策を講じた新しい環境へ移行されている。対象者には順次封書で個別通知し、なりすまし連絡やフィッシングへの注意を呼びかけた。[^five-second]

新環境の具体的な構成や導入対策、旧環境の廃止・復旧方針、フォレンジック調査の最終結果は公表されていない。このため `draft` とし、後続公表を追跡する。

# 防御上の教訓

- **ランサムウェアは確度を維持して記録する。** 初報の「感染可能性」を、後続で確認されていないまま「ランサムウェア攻撃確定」に昇格させない。
- **別システム化が事業継続に寄与した。** 内部環境を止めても、店舗とオンラインストアを継続できた。[^five-first]
- **顧客情報だけでなく人事情報も同じインシデント台帳で評価する。** 退職者や口座情報を含む長期保存データは、侵害時の影響範囲を拡大し得る。[^five-second]
- **件数と人数を分離する。** 複数データ集合に重複があり得る場合、単純合計を被害者人数としない。
- **影響環境を再利用しない選択肢を持つ。** 同社は影響を受けた環境を停止し、新環境で顧客情報を管理している。[^five-second]

# 不明点・要追跡事項

- ランサムウェア感染の最終判定
- 実際に外部取得されたデータと確定件数
- 侵入経路、侵害開始日時、攻撃主体
- 新環境で導入した技術的再発防止策
- 後続の不正利用・外部公開の有無

[^five-first]: ファイブフォックス、2026年7月14日第一報。
[^five-second]: ファイブフォックス、2026年9月8日第二報。
