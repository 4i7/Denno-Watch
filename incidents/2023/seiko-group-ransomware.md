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
  latest_public_update: "2023-10-25"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
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

[^seiko-third]: セイコーグループ「当社サーバに対する不正アクセスに関するお知らせ（第3報）」2023-10-25.