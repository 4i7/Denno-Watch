---
type: Cybersecurity Incident
title: LINEヤフー — 委託先PCマルウェア感染から共通認証・ネットワークを介した情報漏えい
description: NAVER Cloudと旧LINE環境の共有・接続関係を経路として2023年に発生した侵害。2026年7月の規制当局向け再発防止最終報告まで追跡する。
resource: https://www.lycorp.co.jp/ja/news/announcements/007712/
tags: [japan, internet-platform, supply-chain, identity, shared-authentication, malware, personal-data, regulation, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: LINEヤフー株式会社
  sector: internet-platform
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: "contractor endpoint malware leading to unauthorized access through shared identity/network relationships"
  earliest_known_activity: "2023-09-14"
  detected_at: "2023-10-17"
  incident_known_at: "2023-10-27"
  first_disclosed_at: "2023-11-27"
  latest_public_update: "2026-07-21"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: "malware-infected contractor employee PC; related-company systems and shared authentication/network connectivity"
  affected_services: "internal systems and employee-related shared authentication environment"
  data_exposure: confirmed
  availability_impact: "no comparable prolonged public-service outage; access paths were blocked and employee sessions reauthenticated"
  restoration_state: "recurrence-prevention final reports accepted by MIC and PPC on 2026-07-15"
  regulatory_response: "MIC and PPC oversight and multi-year recurrence-prevention reporting"
  ai_relation: era_context_only
sources:
  - id: ly-initial
    resource: https://www.lycorp.co.jp/ja/news/announcements/001002/
    title: 不正アクセスによる、情報漏えいに関するお知らせとお詫び
  - id: ly-dec
    resource: https://www.lycorp.co.jp/ja/news/announcements/001166/
    title: 不正アクセスによる、情報漏えいに関するお知らせとお詫び（12/27更新）
  - id: ly-final-scope
    resource: https://www.lycorp.co.jp/ja/news/announcements/007712/
    title: 不正アクセスによる、情報漏えいに関するお知らせとお詫び（2024/2/14更新）
  - id: ly-remediation
    resource: https://www.lycorp.co.jp/ja/news/announcements/007710/
    title: 不正アクセスによる個人情報漏えいへの再発防止策に関するお知らせ
  - id: ly-final-report
    resource: https://www.lycorp.co.jp/ja/news/announcements/020659/
    title: 不正アクセスによる情報漏えいへの再発防止策に関する報告完了のお知らせ
---

# 概要

LINEヤフーの委託先でもある企業の従業者PCがマルウェア感染したことを契機に、NAVER Cloudと旧LINE環境の認証・ネットワーク上の関係を介して不正アクセスが行われた。最終的な2024年2月14日公表では、ユーザー個人データ302,980件、取引先等86,211件、従業者等130,315件が漏えい又はその可能性を含む対象として示された。件数は母集団が異なり、単純合算してユニーク人数とはしない。[^ly-final-scope]

# 時系列と即応性

- 2023-09-14: 後日の調査で確認された不正アクセス開始。
- 10-09: 関係会社サーバー経由で当社サーバーへ不正アクセス。
- 10-17: セキュリティ部門が不審アクセスを検知し調査開始。
- 10-27: 外部不正アクセスの蓋然性が高いと判断。関連パスワードのリセットと関係会社からの経路遮断を順次実施。
- 10-28: 従業者の社内システム接続を強制再認証。
- 11-27: 初回公表と対象者通知開始。
- 12-27: 最初の不正アクセス日を10月9日から9月14日に訂正。
- 2024-02-14: 影響範囲と再発防止策を更新。
- 2026-07-15: 総務省・個人情報保護委員会へ再発防止策の最終報告。
- 07-21: 最終報告が受領されたことを公表。[^ly-dec][^ly-final-report]

最初に観測された活動から検知まで約33日、検知から外部不正アクセスとの判断まで10日を要している。これは後知恵で算出した観測値であり、当時9月14日の活動を即時に識別可能だったと意味しない。

# 技術環境と失敗面

同社は原因を、委託先企業への安全管理措置、NAVERと旧LINE間のシステム・ネットワーク構成、旧LINE側の従業員システムのセキュリティという複数の課題に整理した。単一の脆弱性より、**委託先端末、認証基盤、ネットワーク信頼関係が連鎖した事故**である。[^ly-remediation]

# 再発防止

公表された対策には、委託先のリスク評価・監督強化、社内ネットワークへ接続する委託先端末の管理、二要素認証、ネットワークのファイアウォール・セーフリスト化、NAVER Cloudとの従業者認証基盤の分離が含まれる。[^ly-remediation]

2026年7月に総務省と個人情報保護委員会への最終報告が受領されており、本件は約2年9か月に及ぶ規制・ガバナンス上の尾部を持った。[^ly-final-report]

# 公表品質上の特徴

12月27日に侵入開始日を10月9日から9月14日へ訂正し、2024年2月にも対象件数を更新した。初報を固定せず、調査進展による訂正履歴を残している点は、Denno Watchの証拠状態モデルの基準例となる。

# 防御上の教訓

- 委託先端末から社内ネットワークへ到達する経路は、端末信頼、MFA、ネットワーク分離を重ねる。
- 企業境界をまたぐ共通認証は、利便性だけでなく障害・侵害の集中点として評価する。
- 「検知日」「外部侵害と判断した日」「公表日」を分離し、各段階の遅延を測る。
- AI/LLM利用を裏付ける公開証拠はなく、時代背景以上の因果関係は付与しない。

[^ly-initial]: LINEヤフー「不正アクセスによる、情報漏えいに関するお知らせとお詫び」2023-11-27.
[^ly-dec]: LINEヤフー「同（12/27更新）」2023-12-27.
[^ly-final-scope]: LINEヤフー「同（2024/2/14更新）」2024-02-14.
[^ly-remediation]: LINEヤフー「不正アクセスによる個人情報漏えいへの再発防止策に関するお知らせ」2024-02-14.
[^ly-final-report]: LINEヤフー「再発防止策に関する報告完了のお知らせ」2026-07-21.