---
type: Cybersecurity Incident
title: さくらインターネット — レンタルサーバー・販売管理システムへの不正アクセス
description: 2026年8月に検知され、過去の販売管理システム侵害も判明した不正アクセスとマルウェア事案の調査記録。
resource: https://www.sakura.ad.jp/corporate/information/newsreleases/2026/09/10/1968225692/
tags: [japan, cloud, hosting, unauthorized-access, malware, credentials, personal-data, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: さくらインターネット株式会社
  sector: cloud-and-hosting
  jurisdiction: JP
  incident_status: monitoring
  attack_type: "unauthorized access and malware installation"
  earliest_known_activity: "2023-04 (sales-management system); suspicious hosting-environment traces considered from 2025-07"
  detected_at: "2026-08-09"
  first_disclosed_at: "2026-08-17"
  latest_public_update: "2026-09-10"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Sakura Rental Server maintenance/hosting environment and sales-management system"
  data_exposure: possible
  availability_impact: limited_or_not_publicly_quantified
  restoration_state: "containment completed; affected servers rebuilt/cleanup continuing as preventive work"
  secondary_abuse: not_observed
sources:
  - id: sakura-final
    resource: https://www.sakura.ad.jp/corporate/information/newsreleases/2026/09/10/1968225692/
    title: 当社システムへの不正アクセスに関する調査結果および再発防止策について（第三報）
  - id: sakura-first
    resource: https://www.sakura.ad.jp/corporate/information/newsreleases/2026/08/17/1968225614/
    title: 当社レンタルサーバーサービスの一部環境に対する不正なアクセスについて
  - id: sakura-faq
    resource: https://help.sakura.ad.jp/unauth-access-faq/
    title: 当社システムへの不正アクセスに関するご案内
---

# 概要

さくらインターネットは2026年8月9日、「さくらのレンタルサーバ」のメンテナンス用サーバーで異常を検知した。調査により、一部サーバーへの不正アクセス、マルウェア設置、さらに契約情報などを扱う販売管理システムのデータベースへの不正アクセスが判明した。[^sakura-final]

最終調査では、レンタルサーバー側で第三者に閲覧・取得された可能性を否定できない対象が951アカウント、販売管理システムでは最大1,360,563アカウントの会員情報等が閲覧・取得された可能性があるとされた。後者のうち30アカウントではハッシュ化された会員IDのパスワード情報が閲覧された可能性がある。さらに販売管理システムには、一部レンタルサーバーの初期サーバーパスワードと一部VPSの管理者初期パスワードが平文相当の状態で保存されていた。[^sakura-final]

一方、調査ではデータの外部持ち出しを裏付ける明確な事実、インターネット/ダークウェブ公開、不正利用、金銭被害、フィッシング等の二次被害は確認されなかった。これは「閲覧・取得可能性」と「外部持ち出しの痕跡」を分けて評価した事例である。[^sakura-final]

# 公開情報で確認できる時系列

| Date / period | Observable event |
| --- | --- |
| 2023-04 to 2026-03 | 販売管理システムに対する不正アクセスがこの期間に発生していたことを調査で確認。[^sakura-final] |
| from 2025-07 | レンタルサーバー環境に不審な活動の痕跡。継続侵害を示すものではないとされたが、記録制約により2026年8月事案との同一性・具体的経路・顧客影響は客観的に確定できず。[^sakura-final] |
| 2026-08-09 | メンテナンス用サーバーで異常を検知し調査開始。[^sakura-final] |
| after detection | 不審通信遮断、環境隔離、マルウェア除去、認証情報見直し等を実施。[^sakura-final] |
| 2026-08-17 | 初報。レンタルサーバーの一部顧客環境への不正アクセスと個人データ閲覧・取得可能性を公表。当初対象は583アカウント。[^sakura-first] |
| 2026-09-10 | 一連の調査完了を公表。対象を951アカウントへ拡大し、販売管理システム側の最大1,360,563アカウントの影響可能性、過去の侵害期間、認証情報の扱い、封じ込め・再発防止策を公表。[^sakura-final] |

# 影響

## Rental Server environment

8月17日時点の583アカウントに加え、追加調査で368アカウントについても閲覧・取得の可能性を完全には否定できず、最終的に951アカウントを対応対象とした。ただし追加368アカウントについては、最初の583アカウントへの不正アクセスとの関連を示す明確な根拠は確認されていない。[^sakura-final]

これは「同一攻撃と確認した951件」ではない。最終件数には、関連性を客観的に確認できないものの顧客影響を否定できない対象も含まれる。[^sakura-final]

## Sales-management system

販売管理システムには各サービスの契約情報等が保存されており、最大1,360,563アカウントの会員情報等が第三者に閲覧または取得された可能性がある。30アカウントではハッシュ化された会員IDパスワード情報が閲覧された可能性も確認された。[^sakura-final]

1,360,563はアカウント数であり、実際に全項目が閲覧・取得された人数や漏えい確定件数を意味しない。同社自身も、保存項目のすべてを各顧客について保有していた、または第三者が実際に取得したことを示す数字ではないと注意している。[^sakura-final]

## Credential exposure

販売管理システムには、一部レンタルサーバーの初期サーバーパスワードと一部VPSの管理者初期パスワードが保存されていた。これらは30アカウント分のハッシュ化パスワードとは別で、ハッシュ化されていなかった。現用の初期パスワードが影響を受け得る契約では同社側で変更を行い、VPS利用者にも変更を案内した。[^sakura-final]

クレジットカード情報は同社が保持しておらず、入力画面の改ざんも確認されなかったため、カード番号漏えいのおそれはないと説明している。[^sakura-final]

# 技術的に確認できた事項

確認された技術事象は、不正アクセス、レンタルサーバーの一部へのマルウェア設置、販売管理DBへの不正アクセスである。具体的な攻撃コード、IPアドレス、ネットワーク構成、認証方式、侵入経路は、模倣攻撃防止等の理由で非公表。[^sakura-final]

重要なのは、レンタルサーバー側と販売管理システム側の二つの事象について、調査で明確な関連性が確認されなかった点である。時間的・技術的な関連を推測して一つの攻撃チェーンとして扱わない。[^sakura-final]

# 対応と復旧

同社が公表した封じ込め・影響拡大防止策には、認証情報の無効化、不審通信遮断、接続元制限強化、環境隔離、マルウェア/不正設定除去、緊急点検、侵害サーバー再構築、EDR導入範囲拡大、対象顧客への個別対応、関係機関への報告、外部専門機関による検証が含まれる。[^sakura-final]

再発防止として、管理者権限・アクセス権の総点検、重要システムへの接続経路と認証管理の見直し、監視強化を実施済み。さらに多層アクセス制御、検知対象拡充、ログ取得範囲・保管期間・分析体制の見直し、「さくらのレンタルサーバ」全サーバー再構築、外部監査、訓練、経営層を含むガバナンス強化を予定している。[^sakura-final]

# 現在の状況と予後

9月10日時点で一連の調査と主要な封じ込めは完了している。外部持ち出し・不正利用等は確認されていないが、同社はインターネット上の公開や不正利用の監視を継続するとしている。[^sakura-final]

このためDenno Watchでは `monitoring` とする。新たな二次被害、公表情報、追加の技術説明が出た場合に更新する。

# 防御上の教訓

- **認証情報の保管場所そのものを資産として監査する。** 初期パスワードでも、現用のまま残れば侵害後の横展開・再侵入リスクになる。[^sakura-final]
- **ログ保持期間はフォレンジック能力の上限になる。** 2025年7月以降と考えられる痕跡は、時間経過による記録制約から同一性や侵入経路を客観的に確定できなかった。[^sakura-final]
- **提供環境と管理系を分けて評価する。** サービス本体と販売管理システムは別系統であり、調査・件数・因果関係も別々に管理された。[^sakura-final]
- **「可能性」と「外部持ち出し確認」を分離する。** アクセス可能性の対象が大きくても、外部送信痕跡や二次被害は別の証拠で判断する必要がある。[^sakura-final]

# 不明点・未公表事項

- レンタルサーバー側と販売管理システム側それぞれの具体的侵入経路
- 両事象を実行した主体が同一かどうか
- 2025年7月以降の不審活動と2026年8月事案の同一性
- 実際に閲覧・取得された個別レコードの確定範囲
- 公表されていないマルウェア種別・攻撃コード・IP等

[^sakura-final]: さくらインターネット「当社システムへの不正アクセスに関する調査結果および再発防止策について（第三報）」2026-09-10.
[^sakura-first]: さくらインターネット「当社レンタルサーバーサービスの一部環境に対する不正なアクセスについて」2026-08-17.
[^sakura-faq]: さくらインターネット「当社システムへの不正アクセスに関するご案内」2026-09-10更新.
