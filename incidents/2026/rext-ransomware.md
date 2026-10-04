---
type: Cybersecurity Incident
title: REXT Holdings / REXT — ランサムウェアによる店舗・社内ネットワーク障害と情報公開確認
description: 2026年8月に発生したREXT系社内ネットワークのランサムウェア被害、店舗影響、9月の情報掲載確認までの公開記録。
tags: [japan, retail, ransomware, availability, data-exposure, 2026]
status: draft
stale_after: 2026-10-10T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: REXT Holdings株式会社 / REXT株式会社
  sector: retail
  jurisdiction: JP
  incident_status: investigating
  attack_type: ransomware
  earliest_known_activity: unknown
  detected_at: not_publicly_disclosed
  first_disclosed_at: "2026-08-10"
  latest_public_update: "2026-09-11"
  intrusion_vector: not_publicly_disclosed
  affected_services: "parts of internal network; store operations, services and payment methods"
  data_exposure: "confirmed online publication of information described as possibly leaked; scope under investigation"
  availability_impact: confirmed
  restoration_state: "all affected closed stores reopened by 2026-08-16; service/payment restrictions were being removed"
  secondary_abuse: not_observed
sources:
  - id: rext-fourth
    resource: https://www.rext.jp/ir/attachment/?/%E5%BD%93%E7%A4%BE%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84%E3%81%AE%E3%81%8A%E3%81%9D%E3%82%8C%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B%E3%81%A8%E3%81%8A%E8%A9%AB%E3%81%B3%EF%BC%88%E7%AC%AC4%E5%A0%B1%EF%BC%89.pdf=&field=0&id=87&inline=1
    title: 当社ネットワークへの不正アクセスによる情報漏えいのおそれに関するお知らせとお詫び（第4報）
  - id: rext-third
    resource: https://www.rext.jp/ir/attachment/?/REXT+Holdings(%E6%A0%AA)%E5%BD%93%E7%A4%BE%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%94%E5%A0%B1%E5%91%8A_(%E7%AC%AC3%E5%A0%B1%EF%BC%89.pdf=&field=0&id=86&inline=1
    title: 当社ネットワークへの不正アクセスによるシステム障害および一部店舗の営業変更について（第3報）
  - id: rext-second
    resource: https://www.rext.jp/ir/attachment/?/REXT+Holdings%EF%BC%88%E6%A0%AA%EF%BC%89%E5%BD%93%E7%A4%BE%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%94%E5%A0%B1%E5%91%8A_%E7%AC%AC2%E5%A0%B1.pdf=&field=0&id=83&inline=1
    title: 当社ネットワークへの不正アクセスによるシステム障害および一部店舗の営業変更について（第2報）
  - id: rext-index
    resource: https://www.rext.jp/
    title: REXT株式会社 ニュースリリース
---

# 概要

REXT Holdingsおよび子会社REXTは、2026年8月10日から、一部社内ネットワークシステムに対するランサムウェア被害を公表した。被害により一部店舗が休業し、営業再開後も店舗ごとに一部サービス・決済方法が制限された。8月16日までに被害を受け休業していた全店舗が営業再開し、8月31日時点では残る制限も順次復旧していた。[^rext-second][^rext-third]

9月11日の第4報では、外部専門機関の調査が継続中の段階で、REXT側から流出した可能性のある情報の一部がインターネット上に掲載されていることを確認したと公表した。掲載情報の内容・影響範囲は調査中で、対象者への個別通知は調査完了後に順次行うとされた。[^rext-fourth]

同日時点で、不正利用や不当請求などの二次被害は確認されておらず、ダークウェブ等の外部監視を継続している。[^rext-fourth]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-08-10 | ランサムウェアによる一部社内ネットワークへの不正アクセス被害を初回公表。後続報がこの日付を参照している。[^rext-second] |
| 2026-08-12 onward | 外部専門機関による詳細調査を開始し、警察・個人情報保護委員会へ報告。[^rext-second] |
| 2026-08-14 | 第2報。一部店舗が休業またはサービス・決済制限を伴って営業。顧客個人情報・取引先情報等の外部漏えい可能性は「極めて低いと推定」としつつ完全否定はせず。[^rext-second] |
| 2026-08-16 | 被害を受け休業していた全店舗が営業再開。[^rext-third] |
| 2026-08-31 | 第3報。店舗ごとのサービス・決済制限を順次復旧し、9月上旬を目処に全店で制限解消見込みと公表。原因・影響範囲の調査は継続。[^rext-third] |
| 2026-09-11 | 第4報。流出した可能性のある情報の一部がインターネット上に掲載されていることを確認。内容・影響範囲、対象者の特定を継続調査。[^rext-fourth] |

# 影響

## 可用性と事業運営

ランサムウェアは社内ネットワークだけでなく実店舗運営にも影響し、一部店舗が休業した。全休業店舗は8月16日に再開したが、その後も店舗ごとに一部サービスや決済方法の制限が残り、8月31日時点で段階復旧中だった。[^rext-second][^rext-third]

公開資料は、休業店舗数、売上影響額、具体的に停止したバックエンドシステムを確定していない。したがってDenno Watchでは店舗運営への実害は `confirmed` とする一方、経済損失額は `unknown` とする。

## 機密性

8月14日時点では外部漏えい可能性を低いと推定していたが、9月11日には「当社らから流出した可能性のある情報の一部」がインターネット上に掲載されていることを確認した。[^rext-second][^rext-fourth]

この更新は重要である。初期評価を「漏えいなし」と固定せず、後続の外部観測で状態が変わったため、本記録では9月11日を境にデータ影響を `possible` から「公開情報の掲載確認あり」へ更新する。ただし、掲載情報の種類、件数、個人情報の範囲、実際の窃取経路は未確定である。[^rext-fourth]

## 二次被害

9月11日時点で、掲載または漏えいしたおそれのある情報を悪用した不正利用・不当請求等の二次被害は確認されていない。外部専門機関とダークウェブ等の監視を継続している。[^rext-fourth]

# 技術的に確認できた事項

公開資料はランサムウェア被害であることを確認しているが、ランサムウェアファミリ、初期侵入経路、侵害時刻、認証情報利用、横展開、暗号化対象、データ窃取手段を公表していない。これらを外部の攻撃者主張だけで補完しない。

# 対応と復旧

- 8月12日以降、外部専門機関による詳細調査を開始。[^rext-second]
- 警察へ相談・被害状況を共有し、個人情報保護委員会へ報告。[^rext-second][^rext-fourth]
- 店舗は段階的に復旧し、8月16日までに休業店舗が全て再開。[^rext-third]
- 9月11日時点でも外部専門機関による調査、インターネット/ダークウェブ監視を継続。[^rext-fourth]
- 調査完了後、漏えいまたはそのおそれが確認された対象者に順次個別通知する方針。連絡困難者はWeb公表で代替。[^rext-fourth]
- 原因究明と並行し、システムセキュリティ体制の再構築と全社的な管理強化を進めるとしている。[^rext-fourth]

# 現在の状況と予後

2026年10月3日時点で、REXT公式サイトに掲載されている最新のインシデント報告は9月11日の第4報であり、その時点では外部専門機関の調査は未完了である。[^rext-index][^rext-fourth]

特に、公開済みデータの具体的内容・対象者数・侵入経路・最終的な二次被害評価が未確定であるため、`investigating` とする。

# 防御上の教訓

- **業務復旧と情報漏えい調査は別の時計で進む。** 店舗は8月中に再開した一方、9月になって外部掲載が確認され、情報影響の評価は継続した。[^rext-third][^rext-fourth]
- **初期の低リスク評価を固定しない。** 8月14日の「可能性は極めて低い」という評価は、9月11日の外部掲載確認によって更新を要した。[^rext-second][^rext-fourth]
- **外部公開監視はフォレンジックを補完する。** 内部調査だけでなく、インターネット/ダークウェブ監視が後続影響の検知に使われている。[^rext-fourth]

# 不明点・未公表事項

- 初期侵入経路、侵害開始時刻、ランサムウェアファミリ
- 侵害された具体的サーバー・端末・認証基盤
- インターネット上に掲載された情報の種類、件数、対象者
- 情報窃取の経路と窃取時刻
- 最終的な店舗・売上・取引先への影響
- 調査完了報と最終再発防止策

[^rext-second]: REXT Holdings「当社ネットワークへの不正アクセスによるシステム障害および一部店舗の営業変更について（第2報）」2026-08-14.
[^rext-third]: REXT Holdings「当社ネットワークへの不正アクセスによるシステム障害および一部店舗の営業変更について（第3報）」2026-08-31.
[^rext-fourth]: REXT Holdings「当社ネットワークへの不正アクセスによる情報漏えいのおそれに関するお知らせとお詫び（第4報）」2026-09-11.
[^rext-index]: REXT株式会社ニュースリリース一覧。2026-10-03確認。
