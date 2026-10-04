---
type: Cybersecurity Incident
title: 日本資産総研 — 認証情報窃取を起点とするランサムウェアと顧客個人データのリークサイト公開
description: 2026年5月の日本資産総研ランサムウェア事案について、認証情報窃取、暗号化、外部送信可能性、顧客個人データのリークサイト公開確認、復旧・再設計までを追跡する記録。
resource: https://www.nssg.co.jp/news/2026/0911-1600.html
tags: [japan, professional-services, ransomware, credential-theft, data-exfiltration, leak-site, personal-data, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:49:29Z }
incident:
  organization: 株式会社日本資産総研 / 日東不動産株式会社
  sector: asset-consulting-and-real-estate
  jurisdiction: JP
  incident_status: operations_restored_remediation_continues
  attack_type: ransomware
  earliest_known_activity: unknown
  detected_at: "2026-05-09"
  first_disclosed_at: "2026-05-14"
  latest_public_update: "2026-09-11"
  public_record_checked_at: "2026-10-04T04:49:29+09:00"
  intrusion_vector: "stolen authentication information; exact theft method not publicly disclosed"
  affected_services: "internal servers, business systems, file servers, mail environment and related endpoints"
  data_exposure: confirmed_publication_of_customer_personal_data
  availability_impact: confirmed
  restoration_state: "normal business operations resumed; environment rebuilt with security design changes rather than simple restoration"
  secondary_abuse: "not observed as of 2026-09-11"
sources:
  - id: nssg-1
    resource: https://www.nssg.co.jp/news/2026/0514-1246.html
    title: セキュリティインシデントの発生に関するご報告
    author: organization:Nihon Shisan Souken
  - id: nssg-2
    resource: https://www.nssg.co.jp/news/2026/0622-1300.html
    title: セキュリティインシデントの発生に関するご報告（第2報）
    author: organization:Nihon Shisan Souken
  - id: nssg-3
    resource: https://www.nssg.co.jp/news/2026/0731-1300.html
    title: セキュリティインシデントの発生に関するご報告（第3報）
    author: organization:Nihon Shisan Souken
  - id: nssg-4
    resource: https://www.nssg.co.jp/news/2026/0911-1600.html
    title: セキュリティインシデントの発生に関するご報告（第4報）
    author: organization:Nihon Shisan Souken
  - id: nssg-home
    resource: https://www.nssg.co.jp/
    title: 株式会社日本資産総研 トップページ / 最新情報
    author: organization:Nihon Shisan Souken
---

# 概要

日本資産総研は2026年5月9日、自社サーバがランサムウェアに感染していることを確認した。サーバ内ファイルが暗号化され、システムやPC等を停止して外部専門家と調査・復旧を開始し、5月14日に初報を公表した。[^nssg-1][^nssg-2]

7月31日の第3報では外部専門機関の調査により、第三者が**何らかの方法で認証情報を窃取し、その認証情報を用いてサーバ環境へ不正アクセスした上でランサムウェアを実行した**ことを確認した。保有データ全体の1%未満に相当する一部データが外部送信された可能性も確認されたが、その時点では具体的な送信対象を特定できなかった。[^nssg-3]

9月11日の第4報では、2026年8月26日時点で**顧客の個人データが攻撃者のリークサイトに公開されたことを確認**した。これにより、本件は「漏えい可能性」から「一部データ外部送信」さらに「顧客個人データの第三者公開確認」へ証拠状態が段階的に更新された。[^nssg-4]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-05-09 | サーバのランサムウェア感染を確認し、外部専門家と調査開始。日本資産総研および同社サーバを利用していた日東不動産のデータを含むファイル暗号化を確認。[^nssg-2] |
| 2026-05-14 | 初報。ファイル暗号化、システム・PC利用停止、情報漏えい可能性を公表。合同対策本部設置、関係当局・警察との連携を開始。[^nssg-1] |
| 2026-06-22 | 第2報。安全確認済み端末から復旧し、通常営業を再開。EDR導入を公表。データ窃取可能性は残るが実際の漏えいは未確認。[^nssg-2] |
| 2026-07-31 | 第3報。認証情報窃取を起点とした侵入とランサムウェア実行を確認。保有データの1%未満の一部が外部送信された可能性を確認。[^nssg-3] |
| 2026-08-26 | 後の調査により、この時点で顧客個人データが攻撃者のリークサイトに公開されていたことを確認。[^nssg-4] |
| 2026-09-11 | 第4報。リークサイト公開を正式公表し、対象データ属性、復旧・再発防止策、二次被害注意を更新。[^nssg-4] |

# 影響

## 可用性と事業運営

初期対応では暗号化と被害拡大防止のためシステム・PC等を利用停止したため業務影響が発生した。[^nssg-1]

6月22日時点では安全性を確認した端末・システムから順次復旧し、通常営業を再開していた。[^nssg-2]

## 機密性と外部公開

第4報で漏えい等が発生、または発生したおそれがあるとされた個人データは以下。[^nssg-4]

| Population | Publicly disclosed affected fields |
| --- | --- |
| コンサルティング業務の顧客 | 氏名、生年月日、住所 |
| 不動産取引業務の顧客 | 氏名、生年月日、住所、対象物件情報 |
| 従業員・従業員家族（退職者含む） | 氏名、生年月日、住所、電話番号 |

個別件数・一意人数は公表されていないため、Denno Watchでは推定しない。

第3報では保有データの1%未満のデータ量について外部送信可能性が確認されたものの対象特定には至らなかった。第4報では顧客個人データのリークサイト公開が確認されている。[^nssg-3][^nssg-4]

日東不動産は同じサーバを利用していたが、9月11日時点では同社保有データがリークサイトで公開された事実は確認されていない。その他の青山財産ネットワークスグループ会社のシステム・保有情報への影響も確認されていない。[^nssg-4]

## 二次被害

9月11日時点で、公開された個人データの不正利用や第三者による悪用等の二次被害を示す事実は確認されていない。[^nssg-4]

# 技術的に確認できた事項

外部専門機関の調査で確認された攻撃チェーンは、公開範囲では以下までである。[^nssg-3][^nssg-4]

1. 第三者が何らかの方法で認証情報を窃取。
2. 窃取した認証情報を用いてサーバ環境へ不正アクセス。
3. ランサムウェアを実行。
4. サーバ内の一部データを暗号化。
5. 一部データが外部へ送信。
6. 顧客個人データが攻撃者のリークサイトで公開。

認証情報の窃取手法、認証経路、MFAの有無、ランサムウェア名、横展開手段、攻撃主体、身代金要求・支払いの有無は公表されていない。

# 対応と復旧

- 合同対策本部を設置し、対象サーバ・端末をネットワークから隔離。[^nssg-1][^nssg-3]
- 外部専門家、外部弁護士、個人情報保護委員会、関東財務局、国土交通省、警察と連携。[^nssg-1][^nssg-2]
- 安全確認済み端末から順次復旧し、6月までに通常営業を再開。[^nssg-2]
- EDRを導入。[^nssg-2]
- 業務システム、ファイルサーバ、メール環境等を復旧。[^nssg-3]
- 従来環境を単純復元せず、未知の攻撃も想定してセキュリティ設計を全面的に見直した環境を構築。[^nssg-3][^nssg-4]
- 認証基盤強化、高度な脅威検知・IR体制、クラウドを含むセキュアなインフラ、継続的な評価・改善を実施または推進。[^nssg-4]

# 現在の状況と予後

2026年10月4日に日本資産総研の最新情報を再確認した時点で、本件の最新一次公表は9月11日の第4報である。[^nssg-home]

通常業務は再開済みだが、リークサイト上への個人データ公開が確認されているため、可用性復旧だけをもって事故終了とは扱わない。セキュリティ設計の再構築と再発防止は継続中であり、`operations_restored_remediation_continues` とする。

# 防御上の教訓

- **初報の「漏えい未確認」は最終結論ではない。** 本件は5月の未確認状態から、7月の外部送信可能性、9月のリークサイト公開確認へ段階的に更新された。
- **認証情報侵害は境界防御を迂回し得る。** 外部調査で認証情報窃取を起点とする侵入が確認されたため、MFA、セッション・資格情報保護、異常認証検知を独立した防御層として扱う必要がある。
- **復旧はクリーンリストアだけでなく再設計の機会になる。** 同社は従来環境を単純復旧せず、セキュリティ設計自体を見直した。[^nssg-3]
- **データ量比率と感度は別物である。** 外部送信可能性が保有データの1%未満でも、最終的に顧客個人データが公開された。
- **リークサイト確認は攻撃者主張そのものとは別に扱う。** 本記録は会社自身が外部専門家の調査結果として公開確認を公表した事実を根拠とする。

# 不明点・未公表事項

- 認証情報を窃取した具体的方法
- 認証基盤・MFA構成
- ランサムウェアの名称と攻撃主体
- 外部送信された全データの範囲・量・時刻
- 公開された個人データの件数・一意人数
- 身代金要求・交渉・支払いの有無
- 再設計後環境の具体的セキュリティ構成

[^nssg-1]: 日本資産総研「セキュリティインシデントの発生に関するご報告」2026-05-14.
[^nssg-2]: 日本資産総研「同（第2報）」2026-06-22.
[^nssg-3]: 日本資産総研「同（第3報）」2026-07-31.
[^nssg-4]: 日本資産総研「同（第4報）」2026-09-11.
[^nssg-home]: 日本資産総研トップページ「最新情報」。2026-10-04確認。
