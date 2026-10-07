---
type: Cybersecurity Incident
title: 大阪公立大学 — ランサムウェア攻撃疑い／約500台停止・13万人超の個人情報に漏えい可能性
description: 大阪公立大学の基盤システムで大規模障害が発生し、約500台のサーバー停止と全学休講に発展。大学はランサムウェア攻撃の可能性が高いと説明し、13万人超の個人情報流出可能性を調査している事案。
resource: https://e.omu.ac.jp/announce/?p=6
tags: [japan, education, university, ransomware, outage, personal-data, integrity, 2026]
status: draft
stale_after: 2026-10-09T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: 大阪公立大学
  sector: higher-education
  jurisdiction: JP
  incident_status: recovering_and_investigating
  attack_type: ransomware-suspected
  earliest_known_activity: "2026-10-02 00:30 JST large-scale outage"
  detected_at: "2026-10-02"
  first_disclosed_at: "2026-10-02"
  latest_public_update: "2026-10-05"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: unknown
  affected_services: "基盤システム、各種学内システム、ネットワーク"
  data_exposure: possible
  availability_impact: "約500台の関連サーバー停止、各種システム利用不能、2026-10-02〜10-08全授業休講"
  restoration_state: "2026-10-05時点で全面復旧見通し未確定、対面授業は10-09再開予定"
  secondary_abuse: not_publicly_disclosed
  downstream_impact: "学生・卒業生等13万人超の個人情報に流出可能性、証明書発行・支援金・出願等へ影響"
  regulatory_response: "大阪府警、文部科学省へ報告、個人情報保護委員会へ連絡"
  notification_state: "影響範囲調査中"
  business_continuity: "医学部附属病院は電子カルテに問題なく診療継続、対面授業再開を計画"
  data_sensitivity: "氏名、住所、メールアドレス、学生証写真等"
sources:
  - id: omu-outage-primary
    resource: https://e.omu.ac.jp/announce/?p=6
    title: 障害・メンテナンス情報 — 基盤及び各種学内システムの障害について／休講のお知らせ
    author: organization:大阪公立大学
  - id: omu-sankei-itmedia
    resource: https://www.itmedia.co.jp/news/article/2610/05/2000002018/
    title: 大阪公立大の大規模システム障害、サイバー攻撃が原因か 13万人超の個人情報流出恐れ
    author: organization:産経新聞 via ITmedia NEWS
---

# 概要

大阪公立大学では2026年10月2日0時30分頃から基盤システム、各種学内システム、ネットワークが利用できない大規模障害が発生した。大学は同日、全キャンパスで授業を休講し、その後10月8日まで全授業を終日休講すると案内した。[^omu-outage-primary]

10月5日の大学発表・記者会見を報じた産経新聞によれば、大学はランサムウェアによる攻撃を受けた可能性が高いと説明した。関連サーバー約500台が停止し、一部データに改ざんの形跡があり、学生・卒業生等13万人超の個人情報が流出した可能性を調査している。[^omu-sankei-itmedia]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-10-02 00:30頃 | 基盤・学内システム・ネットワークの大規模障害を確認。[^omu-outage-primary] |
| 2026-10-02 | 全授業休講。後に10月8日まで休講を延長。[^omu-outage-primary] |
| 2026-10-05 | 大学がランサムウェア攻撃の可能性が高いと説明。約500台停止、13万人超の個人情報流出可能性、一部データ改ざん痕跡が報道される。[^omu-sankei-itmedia] |

# 影響

## 可用性

基盤システム、各種学内システム、ネットワークが広範囲に停止し、授業を約1週間全面休講する事態となった。履修登録、奨学・授業料支援申請等も影響を受け、大学は代替メールアドレス利用や日程変更を案内している。[^omu-outage-primary]

## 機密性・完全性

報道された大学説明では、学生・卒業生等13万人超に関する氏名、住所、メールアドレス、学生証写真等が保管されており、流出の有無を調査中である。また一部データに改ざんの形跡があったとされる。[^omu-sankei-itmedia]

したがって、データ流出は possible、完全性影響は「改ざん痕跡が大学説明として報道」と区別する。

# 対応と復旧

大学は大阪府警、文部科学省へ報告し、10月5日に個人情報保護委員会へも連絡したと報じられている。[^omu-sankei-itmedia]

対面授業は10月9日から再開予定とされた。医学部附属病院ではWebサイト閲覧不能の影響がある一方、電子カルテに問題はなく診療を継続している。[^omu-sankei-itmedia]

# 現在の状況と予後

2026年10月5日時点で全面復旧の見通しは確定していない。授業・学生手続き・証明書等への影響と、個人情報・データ完全性の調査を並行して追跡する必要がある。

# 防御上の教訓

- **大学基盤は授業だけでなく、奨学、証明、入試、メール等の生活・行政機能を集中して支える。** 停止影響を「IT停止」だけで評価しない。
- **病院・診療系の分離は事業継続上の重要な境界になる。** 大学全体の基盤障害下でも電子カルテが継続した点は、依存関係の分離として追跡価値がある。
- **ランサムウェアでは機密性・完全性・可用性を三つに分ける。** 暗号化や停止だけでなく、改ざん痕跡と流出可能性を別に扱う。
- **授業再開はシステム全面復旧と同義ではない。** 対面代替を含む業務復旧と技術復旧を分離する。

# 不明点・未公表事項

- 初期侵入経路
- ランサムウェア種別・攻撃主体
- バックアップの暗号化・復元状態の一次公表
- 実際の個人情報流出有無
- 改ざんされたデータ範囲
- 約500台のうち侵害・暗号化・停止のみの内訳
- 全面技術復旧日

[^omu-outage-primary]: 大阪公立大学「障害・メンテナンス情報」2026-10-02更新.
[^omu-sankei-itmedia]: 産経新聞（ITmedia NEWS掲載）「大阪公立大の大規模システム障害、サイバー攻撃が原因か 13万人超の個人情報流出恐れ」2026-10-05.
