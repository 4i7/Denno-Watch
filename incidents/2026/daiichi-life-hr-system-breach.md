---
type: Cybersecurity Incident
title: 第一生命グループ — 共通人事システムへの不正アクセスと現・元従業員約12万人の情報流出可能性
description: 2026年9月24日に検知された共通人事システムへの第三者不正アクセスと、1967年以降の元従業員を含む長期保有人事データの潜在影響を追跡する記録。
resource: https://www.dai-ichi-life.co.jp/information/pdf/index_192.pdf
tags: [japan, insurance, hr, unauthorized-access, employee-data, data-retention, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 第一生命保険株式会社 / 第一生命グループ
  sector: insurance
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-24"
  first_disclosed_at: "2026-10-02"
  latest_public_update: "2026-10-02"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "group-shared employee human-resources system"
  data_exposure: possible
  availability_impact: not_publicly_disclosed
  restoration_state: "investigation and containment ongoing in the first public report"
  secondary_abuse: "not observed for former employees as of the first report"
  downstream_impact: "current/former employees and certain secondees across group companies"
  regulatory_response: not_publicly_detailed
  notification_state: "affected population identified at approximately 120,000; further investigation ongoing"
  business_continuity: "customer-service impact not publicly established"
  data_sensitivity: "employee ID, name, address, phone, sex, department, grade/title, role and manager; long-retained former-employee data"
sources:
  - id: daiichi-primary
    resource: https://www.dai-ichi-life.co.jp/information/pdf/index_192.pdf
    title: 当社グループ共通人事システムへの不正アクセスに関するお知らせ
    author: organization:第一生命保険株式会社
---

# 概要

第一生命グループは2026年9月24日、グループ共通人事システムへの第三者不正アクセスを検知した。10月2日の公表では、現役・元従業員等の個人情報が閲覧・外部持ち出しされた可能性があるとして、対象を約12万人と示した。[^daiichi-primary]

内訳は現役従業員約5万人（内勤約1.3万人、営業約3.7万人）と元従業員約7万人。元従業員は内勤について1967年以降、営業について2017年以降の情報が対象に含まれ、長期保有データが侵害時の影響範囲を大きくした。特定のグループ会社からの出向者等も対象に含まれる。[^daiichi-primary]

顧客情報への不正アクセスは同日時点で確認されていない。これは顧客情報が絶対に影響を受けていないことの一般化ではなく、公表時点の調査結果として扱う。[^daiichi-primary]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-24 | グループ共通人事システムへの第三者不正アクセスを検知。[^daiichi-primary] |
| 2026-09-24 onward | 原因・影響範囲調査と対応を実施。[^daiichi-primary] |
| 2026-10-02 | 約12万人の現・元従業員等の情報が閲覧・外部持ち出しされた可能性を公表。顧客情報への不正アクセスは確認されていないと説明。[^daiichi-primary] |

# 影響

## Population

| Population | Approximate count | Historical scope |
| --- | ---: | --- |
| Current employees | ~50,000 | current; approx. 13,000 office + 37,000 sales |
| Former employees | ~70,000 | office staff since 1967; sales staff since 2017 |
| Total announced population | ~120,000 | includes specified group-company secondees/related staff |

公表値は約値であり、より精密な確定値へ勝手に変換しない。[^daiichi-primary]

## Data categories

対象情報には従業員番号、氏名、住所、電話番号、性別、所属部署、職位・職級、役割、上司氏名等が含まれる。組織上の役割や上司関係は、単純な連絡先以上に社内なりすましの信憑性を高め得るため、組織グラフ情報としても感度がある。[^daiichi-primary]

## Customer data

10月2日時点で顧客情報への不正アクセスは確認されていない。人事システムの侵害を、根拠なく保険契約データ侵害へ拡張しない。[^daiichi-primary]

# 技術的に確認できた事項

公開情報は第三者不正アクセスまでで、認証情報、脆弱性、攻撃元、アクセス経路、取得方法を明らかにしていない。共有人事システムという構成事実から具体的な認証・ネットワーク設計を推測しない。

# 対応と復旧

- 不正アクセス検知後、原因・影響範囲調査を開始。[^daiichi-primary]
- 現・元従業員を含む対象母集団を約12万人として公表。[^daiichi-primary]
- 元従業員について本件に起因する二次被害は公表時点で確認されていないと説明。[^daiichi-primary]
- 顧客情報へのアクセス有無も並行調査し、初報時点では確認されていないと公表。[^daiichi-primary]

# 現在の状況と予後

2026年10月2日の初回詳細公表段階であり、侵入経路、実際の取得量、恒久対策、通知完了状態は未確定である。`investigating` を維持する。

# 防御上の教訓

- **退職者データの保持年数は侵害時の最大被害半径になる。** 1967年以降という長期保有は、現在の従業員数を大幅に超える影響母集団を形成した。
- **人事データの組織関係を高感度として扱う。** 職位、役割、上司情報は標的型なりすましに利用できる文脈を持つ。
- **共有基盤ではグループ会社境界を明示する。** 出向者等を含むため、法人単位ではなくシステム単位のデータ所有関係を把握する必要がある。

# 不明点・未公表事項

- 初期侵入経路と侵害開始日時
- 実際に外部持ち出しが確認された件数
- 12万人の最終確定値と法人別内訳
- 顧客情報を対象外と判断する最終調査結果
- 恒久対策と通知完了状態

[^daiichi-primary]: 第一生命保険「当社グループ共通人事システムへの不正アクセスに関するお知らせ」2026-10-02.
