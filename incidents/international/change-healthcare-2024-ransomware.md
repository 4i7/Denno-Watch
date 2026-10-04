---
type: Cybersecurity Incident
title: Change Healthcare — 認証情報悪用から全米医療決済へ波及した2024年ランサムウェア
summary: 2024年2月、窃取済み認証情報とMFA未適用のリモートアクセスを起点としてChange Healthcareが侵害され、医療請求・決済基盤が大規模停止した。影響人数、事業影響、財務負担がその後1年以上にわたり更新された長期予後の比較ケース。
resource: https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm
tags: [international, united-states, healthcare, ransomware, identity, concentration-risk, long-tail, 2024]
status: draft
stale_after: 2027-01-04T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T13:08:00+09:00 }
comparative_case: true
included_in_japan_corpus: false
incident:
  organization: Change Healthcare / UnitedHealth Group
  sector: healthcare-claims-and-payments
  jurisdiction: US
  incident_status: long_tail_monitoring
  attack_type: ransomware-and-data-exfiltration
  earliest_known_activity: "2024-02-12"
  detected_at: "2024-02-21"
  first_disclosed_at: "2024-02-21"
  latest_public_update: "2026-03-02"
  public_record_checked_at: "2026-10-04T13:08:00+09:00"
  intrusion_vector: "compromised credentials used against a remote Citrix portal without MFA"
  affected_services: "medical claims, payment, pharmacy and related transaction services"
  data_exposure: confirmed
  availability_impact: major
  restoration_state: "majority of services restored or replaced by 2024 year-end; financial and legal tail persisted into 2026"
  secondary_abuse: unknown
sources:
  - id: unh-first
    resource: https://www.sec.gov/Archives/edgar/data/731766/000073176624000045/unh-20240221.htm
    title: UnitedHealth Group Form 8-K — 2024-02-21
  - id: witty-testimony
    resource: https://www.finance.senate.gov/imo/media/doc/0501_witty_testimony.pdf
    title: Andrew Witty testimony — U.S. Senate Committee on Finance, 2024-05-01
  - id: hhs-faq
    resource: https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html
    title: HHS Change Healthcare Cybersecurity Incident FAQ
  - id: unh-2024
    resource: https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm
    title: UnitedHealth Group Form 10-K — 2024
  - id: unh-2025
    resource: https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm
    title: UnitedHealth Group Form 10-K — 2025
---

# 概要

Change Healthcareは、米国の医療請求・決済等を支える大規模な取引基盤である。2024年2月21日、UnitedHealth GroupはChange HealthcareのITシステムへの外部侵入を検知し、他の接続先を守るため影響システムを隔離した。これにより医療請求、支払い、薬局等の取引へ広範な停止・遅延が発生した。[^unh-first]

後日のCEO証言では、攻撃者は2月12日に窃取済み認証情報を使ってChange HealthcareのCitrixリモートアクセスポータルへ侵入した。このポータルにはMFAが設定されていなかった。侵入後に横展開とデータ持ち出しが行われ、9日後にランサムウェアが展開された。[^witty-testimony]

本件の比較価値は、単なる「ランサムウェアによる一社の停止」ではない。集中した医療取引基盤が止まった結果、下流の医療提供者へ資金繰り支援まで必要となり、影響人数、直接対応費、事業中断、融資回収リスクが別々の時間軸で更新された。

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2024-02-12 | 後日の議会証言によると、窃取済み認証情報を使ってMFA未適用のCitrixポータルへ不正アクセス。[^witty-testimony] |
| 2024-02-21 | ランサムウェア展開。UnitedHealth Groupは外部脅威を検知し、影響システムを隔離。医療取引サービスに大規模な停止が発生。[^unh-first][^witty-testimony] |
| 2024-04 | UnitedHealth Groupは、侵害データの標本調査でPHI/PIIを含むファイルを確認し、米国の相当数の人々へ影響し得ると説明。 |
| 2024-05-01 | CEO Andrew Wittyが米上院で侵入経路、MFA未設定、横展開、データ持ち出し、身代金支払い判断等を証言。[^witty-testimony] |
| 2024-07-19 | Change HealthcareがHHS OCRへHIPAA上の侵害報告を提出。[^hhs-faq] |
| 2024-10-22 | HHSへの報告で約1億件の個人通知を送付済みと更新。[^hhs-faq] |
| 2025-01-24 | Change Healthcareが約1億9,000万人に影響したとHHSへ更新。[^hhs-faq] |
| 2025-07-31 | HHSへの更新で影響人数が約1億9,270万人へ拡大。[^hhs-faq] |
| 2026-03-02 | UnitedHealth Groupの2025年10-Kで、医療提供者向け融資等の回収見込みに関し7億9,900万ドルの引当増加を開示。[^unh-2025] |

# 影響

## 可用性と社会的波及

Change Healthcareの停止は、自社システムだけでなく、医療機関・薬局・保険者等の請求・支払い処理へ広範に波及した。UnitedHealth Groupは2024年末までに医療提供者へ90億ドル超の無利子融資を提供している。[^unh-2024]

これは「第三者サービスが止まった」だけではなく、**下流組織の資金繰りを支える必要が出るほど業務集中度が高かった**ことを示す。

## 個人情報・健康情報

HHSへの報告は時間とともに拡大し、2025年7月31日時点で約1億9,270万人が影響を受けたと更新された。[^hhs-faq]

この数値が事故直後に確定しなかった点が重要である。巨大なデータ集合では、通知母集団の特定自体が長期作業となり、技術復旧と影響範囲確定が大きくずれる。

## 財務影響

UnitedHealth Groupは2024年について、Change Healthcare攻撃に関連する直接対応費を22億ドル、Optum Insightの事業中断影響を8億6,700万ドルと開示した。さらに医療提供者へ90億ドル超の無利子融資を提供した。[^unh-2024]

2025年第4四半期には、医療提供者向け融資等の純回収見込みに関して7億9,900万ドルの引当増加を計上した。[^unh-2025]

したがって最終的な事故コストは、フォレンジックや復旧費だけではなく、**売上・事業中断、下流支援、資金回収リスク、通知、再構築**へ広がる。

# 技術的に確認できた事項

- 初期侵入は窃取済み認証情報によるリモートアクセス。[^witty-testimony]
- 対象CitrixポータルにはMFAが設定されていなかった。[^witty-testimony]
- 侵入後に横展開とデータ持ち出しが行われた。[^witty-testimony]
- ランサムウェアは初期侵入から9日後に展開された。[^witty-testimony]

ここから得られる重要な知見は、暗号化が「侵入の始まり」ではなく、既に侵入・探索・持ち出しが進行した後の可視化された症状になり得ることである。

# 対応と復旧

UnitedHealth Groupは2月21日の検知後、影響システムを他の接続先から隔離した。[^unh-first]

2024年末の10-Kでは、影響を受けたサービスの大部分を復旧または代替したと説明している一方、2025年にも取引量を事故前水準へ戻す作業や追加費用が続く見込みとしていた。[^unh-2024]

したがって本件では、次を別状態として扱う必要がある。

1. 攻撃者活動の封じ込め。
2. 主要取引サービスの技術復旧。
3. 医療提供者の業務・資金繰り正常化。
4. 個人情報影響の特定・通知。
5. 攻撃後の財務負債の収束。

# 現在の状況と予後

2026年3月の2025年10-Kでも、事故に伴う医療提供者向け融資等の回収見込みに追加引当が発生しており、技術復旧から2年近く経過しても財務的な尾部が残った。[^unh-2025]

HHS側では2025年7月まで影響人数が更新された。[^hhs-faq] つまり「何人が影響したか」と「サービスが戻ったか」と「いくら損失になるか」は同時には確定しない。

# 防御上の教訓

- **MFA未適用の一つのリモート入口が巨大な集中基盤への入口になり得る。** 重要第三者・共有基盤ではMFAを任意設定ではなく強制条件として扱う。
- **認証情報の漏えい時点と実悪用時点は離れ得る。** 長寿命認証情報を残さず、漏えい監視、強制ローテーション、端末信頼、接続元制限を組み合わせる。
- **重要第三者のBCPは「その会社が復旧するのを待つ」だけでは不足。** 代替経路、手作業、別提供事業者、支払い・請求の暫定手段を用意する。
- **事故コストは直接復旧費より広い。** 下流支援、事業中断、融資・売掛金回収、通知、規制、長期再構築までストレステストする。
- **影響範囲確定を独立したマイルストーンにする。** 大規模データ事故では、技術復旧後も人数・データ種別が長期間更新される。

# 日本の事例へ読み替える際の注意

米国医療制度、HIPAA、訴訟・財務制度は日本と異なるため、影響額や法的義務をそのまま国内へ当てはめてはならない。

比較価値があるのは、**高集中な第三者基盤、MFA未適用の認証入口、下流業務への連鎖、復旧後も続く影響人数・財務負債の更新**という構造である。

# 不明点・未公表事項

- 公開資料だけでは、2月12日の認証情報がいつ・どの経路で最初に窃取されたかを完全には確定できない。
- 二次不正利用の全件数や長期的な本人被害を本資料から確定することはできない。
- 最終的な事故総費用は今後も変動し得る。

[^unh-first]: UnitedHealth Group, Form 8-K, 2024-02-21.
[^witty-testimony]: Andrew Witty, UnitedHealth Group CEO testimony, U.S. Senate Committee on Finance, 2024-05-01.
[^hhs-faq]: U.S. Department of Health and Human Services, Change Healthcare Cybersecurity Incident FAQ. 2025-07-31更新で約1億9,270万人への影響を記載。
[^unh-2024]: UnitedHealth Group, Form 10-K for 2024. 2024年直接対応費22億ドル、Optum Insight事業中断影響8億6,700万ドル、医療提供者向け無利子融資90億ドル超を開示。
[^unh-2025]: UnitedHealth Group, Form 10-K for 2025, filed 2026-03-02. 医療提供者向け融資等の純回収見込みについて7億9,900万ドルの引当増加を開示。
