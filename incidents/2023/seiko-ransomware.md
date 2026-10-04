---
type: Cybersecurity Incident
title: セイコーグループ — 2023年ランサムウェア／約6万件の個人データ漏えい
description: 2023年7月のランサムウェア侵害について、初動、外部専門家、約6万件の漏えい、事故前の情報セキュリティ開示、事故後の全サーバ・全PCへのEDRとMFA等を追跡する。
resource: https://www.seiko.co.jp/information/202310251000.html
tags: [japan, ransomware, data-breach, edr, mfa, governance, seiko, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: セイコーグループ株式会社
  sector: manufacturing-and-retail
  jurisdiction: JP
  incident_status: public_report_matured
  attack_type: ransomware
  earliest_known_activity: unknown
  detected_at: "2023-07-28"
  first_disclosed_at: "2023-08-10"
  latest_public_update: "2023-10-25 detailed third report"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "some Seiko Group servers and related systems"
  data_exposure: confirmed
  availability_impact: "affected servers/systems required protection and restoration; broad consumer-service outage not established"
  restoration_state: "clean restoration and security enhancement undertaken; detailed public root cause not disclosed"
  downstream_impact: "customers, business contacts, applicants, current/former employees"
  regulatory_response: "reported to Personal Information Protection Commission and consulted Tokyo Metropolitan Police"
  notification_state: "affected parties contacted individually where applicable"
sources:
  - id: seiko-first
    resource: https://www.seiko.co.jp/information/202308101100.html
    title: 当社サーバへの不正アクセスについて
    author: organization:セイコーグループ
  - id: seiko-second
    resource: https://www.seiko.co.jp/information/202308221300.html
    title: 当社サーバへの不正アクセスによる情報漏えいについて
    author: organization:セイコーグループ
  - id: seiko-third
    resource: https://www.seiko.co.jp/information/202310251000.html
    title: 当社サーバに対する不正アクセスに関するお知らせ（第3報）
    author: organization:セイコーグループ
  - id: seiko-ir2023
    resource: https://www.seiko.co.jp/en/ir/library/pdf/SEIKO_value_report_2023_all_forPrint.pdf
    title: SEIKO GROUP VALUE REPORT 2023
    author: organization:Seiko Group Corporation
---

# 概要

セイコーグループは2023年7月28日、一部サーバーへの不正アクセスを検知した。外部専門家との調査でランサムウェア攻撃と判明し、10月25日の第3報までに、セイコーグループ、セイコーウオッチ、セイコーインスツルが保有する**約6万件の個人データが外部へ漏えいしたこと**を確認した。[^seiko-third]

対象には顧客、取引先担当者、採用応募者、現職・退職従業員の情報が含まれた。クレジットカード情報は対象外と公表された。

# 事故前のセキュリティ環境

事故前に公表されたValue Report 2023では、標的型メールやマルウェア等のサイバー攻撃脅威が増大しているとの認識を示し、グループ会社間で連携した継続的対策、従業員意識向上、情報セキュリティ・災害対策を備えたデータセンターへの集約、仮想化による冗長化等を説明していた。[^seiko-ir2023]

したがって本件は、「セキュリティを経営リスクとして認識していなかった企業」の事故ではない。一方、事故後に**全サーバー・全PCへのEDR導入を早急に進め、MFA等を導入**したと会社自身が公表しているため、事故前の検知・認証統制が全資産へ同等に展開済みだったと遡及解釈しない。[^seiko-third]

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2023-07-28 | 一部サーバーへの不正アクセスを検知。緊急点検開始。[^seiko-third] |
| 2023-08-02 | 外部サイバーセキュリティ専門家チームへ調査・評価を依頼。[^seiko-first] |
| 2023-08-10 | 初報。不正アクセスと情報侵害可能性を公表。 |
| 2023-08-22 | ランサムウェア攻撃であり、グループ従業員・関係者情報の一部漏えいを確認したと続報。[^seiko-second] |
| 2023-10-25 | 第3報。約6万件の個人データ漏えい、事故後統制強化、今後の調査・BCP・第三者評価方針を公表。[^seiko-third] |

# 即応性

7月28日の検知後、データセンター内サーバーを緊急点検し、外部専門会社へ支援を依頼した。ランサムウェアと把握後は対策本部を設置し、複数の外部専門家と被害範囲の解明・システム復旧を進めた。個人情報保護委員会・警察にも連携した。[^seiko-third]

初報は検知から13日後である。ただし8月2日には外部専門家へ調査を委託しており、公表前にフォレンジック・影響把握を進めていたことが確認できる。

# 影響

確認済みの個人データは約6万件。主な分類は次の通り。[^seiko-third]

- セイコーウオッチ顧客: 氏名、住所、電話番号、メールアドレス等。
- 取引先担当者: 氏名、会社名、役職、勤務先住所・電話・メール等。
- 採用応募者: 氏名、住所、電話、メール、学歴等。
- 現職・退職従業員: 氏名、人事情報、メールアドレス等。

事故が広範な販売・製造停止に至ったという公表は確認できず、可用性影響より機密性・復旧・グループガバナンスへの影響が中心だった。

# 事故後の統制変更

会社が明示した事故後措置は重要である。[^seiko-third]

- 外部通信を遮断。
- 全サーバー・全PCへEDRを早急に展開。
- MFA等による不正アクセス防止。
- IT機器の脆弱性調査。
- 情報漏えい範囲特定・原因追究。
- 監視・セキュリティ強化。
- IT運営・体制見直し。
- グループガバナンス強化。
- BCP見直し。
- 第三者評価。

これらは「事故前に存在しなかった」と直接読み替えず、事故後に全社適用・強化・再確認が必要と判断された統制として記録する。

# 事故前開示との比較

Value Report 2023はサイバー脅威の認識と継続対策を明記していた。対して実事故後は、EDR全展開、MFA、脆弱性調査、監視、BCP、第三者評価まで追加強化が必要となった。

ここから得られるのは「統合報告書が間違っていた」という結論ではなく、**経営方針上のセキュリティ認識と、全資産における具体的な検知・認証・復旧能力を分けて評価する必要性**である。

# 2026年までの予後

2026年10月4日の公開記録再確認では、2023年10月25日第3報より後に、本件の初期侵入経路や最終フォレンジック結果を詳述する独立した事故報告は確認できなかった。したがって、未知の詳細を「解決済み」と補完しない。

一方、セイコーはその後も統合報告書を継続発行しており、情報セキュリティをグループリスク管理の対象として扱っている。本件の長期予後評価では、事故後に掲げた統制が後年の統合報告・監査等でどの程度実装済みとして確認できるかを追跡対象とする。

# 防御上の教訓

- 統合報告書で「情報セキュリティ強化」を掲げるだけでなく、EDR/MFA等の資産適用率を測る。
- 初動ではネットワーク遮断・外部専門家・警察/PPC連携を並行する。
- 顧客だけでなく応募者・退職者等の長期保有データも被害対象となる。
- 事故後統制の「導入」を、全資産への適用と運用試験まで追う。
- BCP・第三者評価をランサムウェア後の技術復旧と別の長期課題として扱う。

# 不明点

- 初期侵入経路。
- 攻撃者の滞留期間・横展開経路。
- 暗号化対象と情報窃取対象の詳細なシステム数。
- 約6万件の重複排除されたユニーク人数。
- 事故後EDR/MFAの最終適用率と独立評価結果。
- 本件でLLM/生成AIが用いられた公開証拠はない。

[^seiko-first]: セイコーグループ「当社サーバへの不正アクセスについて」2023-08-10.
[^seiko-second]: セイコーグループ「当社サーバへの不正アクセスによる情報漏えいについて」2023-08-22.
[^seiko-third]: セイコーグループ「当社サーバに対する不正アクセスに関するお知らせ（第3報）」2023-10-25.
[^seiko-ir2023]: Seiko Group Corporation, SEIKO GROUP VALUE REPORT 2023.