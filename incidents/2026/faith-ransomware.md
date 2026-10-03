---
type: Cybersecurity Incident
title: フェースグループ — VPN経由のランサムウェア侵害とデータ暗号化・消去
description: 2026年6月に発生したVPN機器経由の侵入、サーバー・PCへのランサムウェア攻撃、顧客認証情報への影響可能性と復旧を追跡する記録。
resource: https://www.faith-gr.co.jp/news/2026/system-failure_20260821.html
tags: [japan, ransomware, vpn, credentials, availability, destructive-impact, 2026]
status: draft
stale_after: 2026-11-05T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: 株式会社フェース / フェースグループ
  sector: cosmetics-and-ecommerce
  jurisdiction: JP
  incident_status: recovering
  attack_type: ransomware
  earliest_known_activity: "2026-06-18 22:46 JST"
  detected_at: "2026-06-19"
  first_disclosed_at: "2026-06-22"
  latest_public_update: "2026-08-21"
  intrusion_vector: "external-facing VPN device"
  affected_services: "internal servers and PCs; order-shipment operations; EC credentials stored on compromised internal server"
  data_exposure: possible
  availability_impact: confirmed
  restoration_state: "safe PC replacement completed; full-system recovery expected around end of October 2026"
  secondary_abuse: not_observed
sources:
  - id: faith-first
    resource: https://www.faith-gr.co.jp/news/2026/system-failure_20260622.html
    title: 弊社システム障害発生に関するご案内（第一報）
  - id: faith-second
    resource: https://www.faith-gr.co.jp/news/2026/system-failure_20260625.html
    title: 弊社システム障害発生に関するご案内（第二報）
  - id: faith-third
    resource: https://faith-gr.co.jp/news/2026/system-failure_20260626.html
    title: 弊社システム障害発生に関するご案内（第三報）
  - id: faith-final
    resource: https://www.faith-gr.co.jp/news/2026/system-failure_20260821.html
    title: 弊社システムへのランサムウェア攻撃に関する調査結果および再発防止策のご報告
  - id: faith-news
    resource: https://faith-gr.co.jp/
    title: フェースグループ 公式サイト
---

# Executive summary

フェースグループでは2026年6月19日にシステム障害が発生し、後の外部専門機関による調査で、前日の6月18日22時46分頃、外部通信に利用するVPN機器を経由して第三者がシステムへ不正侵入していたことが判明した。侵入後、一部サーバーとPCが不正操作され、データの暗号化と消去が行われた。[^faith-final]

侵害サーバーには顧客の氏名、生年月日、性別、住所、電話番号、メールアドレス、ログインID、パスワードが保存されていた。外部へ持ち出された具体的痕跡や不正利用被害は確認されなかったが、外部流出を完全には否定できないとされた。[^faith-final]

ECサイトそのものへの侵入は確認されていないものの、ECサイトで利用するログインID・パスワードが侵害された内部サーバーに保存されていたため、顧客へパスワード変更と他サービスでの使い回し解消を要請した。[^faith-final]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-06-18 22:46頃 | VPN機器を経由して第三者がシステムへ不正侵入。後の調査で特定。[^faith-final] |
| 2026-06-19 | システム障害発生。ランサムウェア攻撃によるものと後に確定。[^faith-final] |
| 2026-06-19 – 06-24 | EC注文商品の発送手続きが停止。[^faith-second] |
| 2026-06-22 | 第一報。外部不正アクセスに起因するランサムウェア被害の可能性を公表。[^faith-first] |
| 2026-06-24 | 商品発送手配を再開。ただし通常ペースまで回復せず、一部配送遅延が発生。[^faith-second] |
| 2026-06-26 | 第三報。ランサムウェア攻撃を確認したと公表し、専門機関による原因・影響・復旧調査を継続。[^faith-third] |
| 2026-08-21 | 外部専門機関の調査結果、VPN経由の侵入、暗号化・消去、顧客情報の影響可能性、再発防止策を公表。[^faith-final] |
| 2026-10末見込み | 8月21日時点でシステム全体の復旧目標時期として公表。[^faith-final] |

# Impact

## Availability and business operations

システム障害により6月19日以降ECサイト注文商品の発送手続きが停止し、6月24日に再開した。再開直後は通常と同じ処理ペースではなく、一部配送指定日に間に合わないケースが発生した。[^faith-second]

8月21日時点で社内PCは安全性を確認した端末への切り替えを完了していたが、システム全体の復旧は10月末頃を見込んでいた。[^faith-final]

## Integrity / destructive impact

侵入後、一部サーバーとPCが不正操作され、**データの暗号化だけでなく消去**も確認された。[^faith-final]

ランサムウェア事案を単なる可用性障害として扱わず、完全性・復元性に対する破壊的影響として記録する。

## Confidentiality and credentials

侵害サーバーには氏名、生年月日、性別、住所、電話番号、メールアドレス、ログインID、パスワードが保存されていた。外部持ち出しの具体的痕跡は確認されていないが、外部流出を完全に否定できない。[^faith-final]

ECサイトそのものは侵入されていない一方、その認証情報が別の侵害サーバーに保存されていたため、EC側のアカウント保護措置が必要になった。[^faith-final]

## Secondary abuse

8月21日時点で、対象情報の不正利用による被害は確認されていない。[^faith-final]

# Technical findings

外部専門機関の調査で、初期侵入は外部通信に使用するVPN機器を経由したものと特定された。侵入後、内部の一部サーバー・PCが操作され、ランサムウェアによる暗号化・消去が行われた。[^faith-final]

公開資料はVPN製品名、脆弱性/CVE、認証情報の利用有無、攻撃主体、ランサムウェアファミリ、横展開手法を明らかにしていない。したがって「VPN経由」という事実から、脆弱性悪用か資格情報侵害かを推測しない。

# Response and recovery

- 外部専門機関とフォレンジック・復旧調査を実施。[^faith-third][^faith-final]
- ECの発送業務を段階復旧。[^faith-second]
- 顧客へECパスワード変更と他サービスでの同一パスワード使い回し解消を要請。[^faith-final]
- 侵入経路となった機器とネットワーク環境の見直し。[^faith-final]
- 認証方式を強化。[^faith-final]
- 端末・サーバーのセキュリティ対策を強化。[^faith-final]
- ネットワーク監視体制を強化。[^faith-final]
- バックアップ環境と復旧体制を再整備。[^faith-final]
- 社内PCを安全確認済み端末へ切り替え。[^faith-final]
- 個人情報保護委員会へ法令に基づく報告。[^faith-final]

# Prognosis / current state

8月21日時点では完全復旧前で、システム全体の復旧を2026年10月末頃と見込んでいた。外部流出は確認されていないものの完全否定できず、継続監視も表明している。[^faith-final]

そのため `recovering` とし、10月末以降に公式サイト上で完全復旧や追加の漏えい確認が公表されたか再確認する。

# Defensive lessons

- **VPNは「入口」だけでなく侵害後の観測点として管理する。** VPN経由で内部侵入し、その後サーバー・PCへ操作が広がったため、境界装置の認証・脆弱性管理と内部横展開検知の両方が必要になる。[^faith-final]
- **アプリが侵害されていなくても、その資格情報を保持する別システムの侵害で利用者リスクが生じる。** EC本体は非侵害でもログインID/パスワードが内部サーバーに保存されていたため顧客対応が必要になった。[^faith-final]
- **暗号化だけでなく消去を想定した復旧テストが必要。** バックアップの存在ではなく、侵害環境から独立した復元可能性と復旧時間を検証する必要がある。[^faith-final]
- **業務復旧は段階的に計測する。** 発送再開とシステム完全復旧は別であり、業務プロセス単位で復旧状態を記録する方が実態に近い。[^faith-second][^faith-final]

# Unknowns / withheld details

- VPN機器の製品・バージョン
- VPN侵入が脆弱性悪用か認証情報悪用か
- ランサムウェアファミリと攻撃主体
- 横展開手法・権限昇格経路
- 暗号化・消去されたデータ量
- 顧客情報の対象人数
- 10月末目標に対する完全復旧実績

[^faith-first]: フェースグループ「弊社システム障害発生に関するご案内（第一報）」2026-06-22.
[^faith-second]: フェースグループ「弊社システム障害発生に関するご案内（第二報）」2026-06-25.
[^faith-third]: フェースグループ「弊社システム障害発生に関するご案内（第三報）」2026-06-26.
[^faith-final]: フェースグループ「弊社システムへのランサムウェア攻撃に関する調査結果および再発防止策のご報告」2026-08-21.
[^faith-news]: フェースグループ公式サイト。2026-10-03確認。
