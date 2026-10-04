---
type: Cybersecurity Incident
title: NTTコミュニケーションズ — 法人向けオーダ情報流通システム不正アクセス／17,891社
description: 2025年2月に内部監視で検知された不正アクセスについて、装置A/Bの調査・隔離、17,891法人顧客への影響可能性、通信・セキュリティ事業者としての平時統制との比較を整理する。
resource: https://www.ntt.com/about-us/press-releases/news/article/2025/0305_2.html
tags: [japan, telecom, enterprise, unauthorized-access, monitoring, ntt, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: NTTコミュニケーションズ株式会社
  sector: telecommunications-and-enterprise-services
  jurisdiction: JP
  incident_status: contained_and_investigated
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2025-02-05"
  first_disclosed_at: "2025-03-05"
  latest_public_update: "2025-03 public investigation status"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "order-information distribution system for certain enterprise services"
  data_exposure: possible
  availability_impact: "no broad service outage established"
  restoration_state: "affected network paths/devices isolated and monitoring strengthened"
  downstream_impact: "up to 17,891 corporate customers"
  notification_state: "affected customers notified by sales representatives or sealed postal letters, not incident-email"
sources:
  - id: nttcom-first
    resource: https://www.ntt.com/about-us/press-releases/news/article/2025/0305_2.html
    title: 当社への不正アクセスによる情報流出の可能性について
    author: organization:NTTコミュニケーションズ
---

# 概要

NTTコミュニケーションズは2025年2月5日、法人向けサービスのオーダ情報を社内で流通させるシステムに接続された装置で不審なログを検知した。調査の結果、外部からの不正アクセスを受け、最大17,891社の法人顧客情報が流出した可能性があると3月5日に公表した。[^first]

対象情報は契約番号、契約名、担当者名、電話番号、メールアドレス、住所、サービス利用に関する情報等だった。NTTドコモが提供する法人名義の携帯電話・スマートフォン契約は対象外とされた。[^first]

# 事故発生時の環境

NTTコミュニケーションズは通信・クラウド・セキュリティを提供する大規模事業者であり、平時からセキュリティ監視機能を持つ。本件は実際に**自社情報セキュリティ部門の監視ログが検知起点**となった点で、外部通報型のJAXAや長期未検知型のIIJ Secure MXと対照的である。

一方で、最初に異常を見つけた装置Aだけでなく、後のログ精査で別の装置Bに侵入経路があると判明した。初動時に目立つ侵害点を隔離しても、隣接装置・管理経路・認証関係まで遡る必要がある。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2025-02-05 | 情報セキュリティ部門が装置Aで不審ログを検知。即日、侵入元と考えられる通信を制限。[^first] |
| 2025-02-06 | 調査の結果、顧客情報が流出した可能性を認識。 |
| 2025-02-15 | ログ分析から別の装置Bにも不正アクセスを確認し、ネットワークから隔離。 |
| 2025-03-05 | 17,891社への影響可能性と対象情報を公表。顧客通知開始。 |

# 即応性

2月5日の自社検知当日に侵入元通信を制限し、翌日には情報流出可能性を認識した。ここは比較的速い。

ただし、より深い調査で装置Bを特定・隔離したのは2月15日である。これは「検知した装置＝侵入の根本原因」とは限らず、**封じ込め後も数日から数週間のログ横断調査が必要**なことを示す。

# 影響

公表時点で流出「可能性」がある法人顧客は17,891社。対象情報は次を含む。[^first]

- 契約番号。
- 顧客名・契約名。
- 顧客担当者名。
- 電話番号。
- メールアドレス。
- 住所。
- サービス利用に関する情報。

確認済み漏えい件数ではなく、調査で影響可能性を認めた最大範囲として保持する。

# 顧客通知の設計

NTTコミュニケーションズは、対象顧客へ営業担当または封書で案内し、**本件を電子メールで案内しない**と明記した。漏えいした可能性のあるメールアドレスを悪用したフィッシングを考慮すると、インシデント通知そのものを攻撃者のなりすましチャネルにしない設計として参考になる。

# 事故前の取り組みとの比較

通信・セキュリティ事業者として高度な監視能力を持つ企業でも侵害は発生した。一方、本件は監視部門が最初の異常を発見しており、「対策が全く機能しなかった」事例でもない。

比較すべきは、次の段階である。

1. 侵入を予防できたか。
2. 不審ログをどれだけ早く検知できたか。
3. 最初の検知点から真の侵入経路・隣接装置へどれだけ速く調査を広げたか。
4. 影響顧客をどれだけ正確に絞り込めたか。
5. 顧客通知をフィッシング耐性のある経路で行えたか。

# 2026年までの予後

2026年10月4日の公開情報再確認では、3月5日の17,891社という最大影響範囲を大幅に更新する新たな会社公表は確認していない。したがって、漏えいが全17,891社で確定したとは扱わない。

会社はセキュリティ対策・監視体制をさらに強化すると公表したが、具体的な独立評価結果が公開されていない部分は`implemented`や`tested`と推測しない。

# 防御上の教訓

- 自社監視による検知時刻をインシデントKPIとして保存する。
- 最初の異常装置だけで調査を閉じず、管理系・隣接装置・認証・ログを横断する。
- 企業向け基盤の顧客情報は下流の標的型攻撃に利用され得るため、連絡手段を事前設計する。
- 「流出可能性」と「確認済み流出」を区別する。
- セキュリティ事業者は自社監視が実際にどこで機能したかも公開資料から評価する。

# 不明点

- 初期侵入日時。
- 初期侵入手法・脆弱性・資格情報の詳細。
- 装置AとBの製品・役割。
- 実際に外部取得されたデータ量。
- 攻撃者の帰属。
- 本件にLLM/生成AIが利用された公開証拠はない。

[^first]: NTTコミュニケーションズ「当社への不正アクセスによる情報流出の可能性について」2025-03-05.