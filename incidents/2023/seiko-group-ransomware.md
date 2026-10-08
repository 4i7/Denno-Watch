---
type: Cybersecurity Incident
title: セイコーグループ — 2023年ランサムウェア攻撃と約6万人の個人情報流出
description: 2023年7月に検知したサーバー侵害について、ランサムウェアと情報流出を確認し、EDR・MFA等を追加した事案。
resource: https://www.seiko.co.jp/information/202310251000.html
tags: [japan, manufacturing, ransomware, personal-data, edr, mfa, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: セイコーグループ株式会社
  sector: manufacturing
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: ransomware and unauthorized access
  earliest_known_activity: "2023-07-28"
  detected_at: "2023-07-28"
  first_disclosed_at: "2023-08-10"
  regulatory_response: "PPC報告と警察相談を実施"
  notification_state: "関係者へ個別対応を実施、全件完了時点は未公表"
  latest_public_update: "2023-10-25"
  public_record_checked_at: "2026-10-08T10:02:29.723+00:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "some Seiko Group servers and internal information systems"
  data_exposure: confirmed
  availability_impact: "some systems were affected; detailed service-by-service downtime not fully public"
  restoration_state: "investigation and recovery progressed under incident headquarters; final public scope published"
  secondary_abuse: not_observed
  ai_relation: era_context_only
sources:
  - id: seiko-third
    resource: https://www.seiko.co.jp/information/202310251000.html
    title: 当社サーバに対する不正アクセスに関するお知らせ（第3報）
---

# 概要

セイコーグループは2023年7月28日に一部サーバーへの不正アクセスを検知し、その後ランサムウェア攻撃と情報流出を確認した。対策本部を設置し、外部専門家と連携して原因・影響調査と復旧を進め、10月25日の第3報で当時判明していた個人情報流出範囲と再発防止策を公表した。[^seiko-third]

公開された流出対象は、従業員・退職者、取引先、顧客等を含む**約6万人**規模である。攻撃者によるAI/LLM利用を示す一次情報はない。

# 初動と情報公開

- 7月28日: 不正アクセスを検知。
- 8月10日: 初回公表。
- 8月22日: 情報漏えいを確認した続報。
- 10月25日: 第3報で調査結果・対象・追加対策を公表。

検知後に対策本部と外部専門家を投入している一方、公開資料から正確な侵入開始時刻は分からないため、侵入から検知までの時間は算出しない。

# 発生時環境と再発防止

第3報では、外部との通信遮断、調査・復旧に加え、事後対策としてEDRをサーバーとPCへ展開し、多要素認証を追加するなどの強化が示された。これは、事故前にどの範囲まで同等の統制が有効だったかを公開資料だけで断定できないことも意味する。[^seiko-third]

# 影響と予後

個人情報の外部流出が確認されたため、単なる可用性事故ではなく機密性侵害として扱う。10月25日時点では、公開上の主要な範囲確定と再発防止策の説明まで進んでいる。以後、同社一次情報で本件に直接ひも付く重大な追加被害公表は今回の再確認では見つからなかった。

# 防御上の教訓

- EDR/MFAは「導入予定・導入済み」の二値ではなく、事故時点の適用範囲を確認する。
- ランサムウェアでは暗号化だけでなく持ち出しを独立して評価する。
- 初期侵入経路が非公表なら、一般論からVPN、フィッシング、脆弱性等を推定しない。
- 本件はローカルLLM時代の初期に位置するが、AI利用の証拠はない。


## 影響を受けた組織とデータ区分

2023年10月25日の第3報でセイコーグループ、セイコーウオッチ、セイコーインスツルが保有する**約60,000件の個人データ**の外部漏えいを確認した。これを「6万人の一意の被害者」と断定しない。[^seiko-third]

| データ所有側 | 漏えい確認された情報 | 限界 |
| --- | --- | --- |
| セイコーウオッチ顧客 | 氏名・住所・電話・メール等 | **クレジットカード情報は含まない** |
| 3社の取引先担当者 | 氏名・会社名・役職・業務連絡先等 | 連絡先の悪用・不審営業の発生件数は未公表 |
| セイコーグループ・セイコーウオッチ採用応募者 | 住所、電話、メール、**学歴**等 | 応募者の本人別確定件数は未公表 |
| グループの現職・退職者 | 氏名、**人事情報**、メール等 | 在職・退職で細分化した対象人数は未公表 |

会社は当局への報告と警察への相談を実施。対象となる関係者には個別に対応し、新たな漏えい事実が判明すれば追加で個別対応すると公表した。これは**個別対応の実施**を意味するが、全対象への通知完了日を示していない。[^seiko-third]

## 実装済みの措置と計画を分離

事故後の**外部通信の遮断**と、EDRの全サーバ・全PCへの展開を「早急に進めた」、多要素認証等の不正アクセス防止措置を講じたというのが第3報の説明である。EDR全台配備の**完了日や独立した稼働検証**までは示されていない。[^seiko-third]

今後の方針として、脆弱性再調査、監視、IT運用体制、グループ・ガバナンス、BCP、第三者評価を掲げた。これらは2023年10月時点で計画されていた事項であり、すべて実施・検証済みと記載しない。特定の侵入CVEや最初の侵入日、暗号化範囲、損害金額は不明。[^seiko-third]

[^seiko-third]: セイコーグループ「当社サーバに対する不正アクセスに関するお知らせ（第3報）」2023-10-25.