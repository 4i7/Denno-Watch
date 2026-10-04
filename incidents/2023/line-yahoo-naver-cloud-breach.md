---
type: Cybersecurity Incident
title: LINEヤフー — NAVER Cloud・共通認証基盤を介した大規模情報漏えい
description: 2023年9月からのサプライチェーン型不正アクセスについて、委託先PC感染、共通認証基盤・ネットワーク接続、検知遅延、行政指導、2026年7月の再発防止報告完了まで追跡する。
resource: https://www.lycorp.co.jp/ja/news/announcements/007712/
tags: [japan, supply-chain, identity, network-trust, personal-data, regulatory, line-yahoo, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: LINEヤフー株式会社
  sector: internet-platform
  jurisdiction: JP
  incident_status: public_report_closed_with_recurrence_program_completed_2026
  attack_type: supply-chain-unauthorized-access
  earliest_known_activity: "2023-09-14"
  detected_at: "2023-10-17"
  incident_known_at: "2023-10-27"
  first_disclosed_at: "2023-11-27"
  latest_public_update: "2026-07-21 recurrence-prevention final reporting completed"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "malware infection on a contractor employee PC, followed by access through NAVER Cloud systems and a shared employee authentication/network trust relationship"
  affected_services: "former LINE internal systems including analytics, source-code management, employee authentication and internal communication systems"
  data_exposure: confirmed_and_possible_mixed
  availability_impact: "no broad LINE service outage established; internal connections and access routes were restricted"
  restoration_state: "technical containment completed; multi-year recurrence-prevention and regulatory reporting completed July 2026"
  secondary_abuse: not_observed_in_reviewed_public_updates
  downstream_impact: "LINE users, business partners, LY group employees/contractors and NAVER-group employee data"
  regulatory_response: "MIC administrative guidance March 5 and April 16 2024; PPC recommendation/reporting request March 28 2024; periodic reports through 2026"
  notification_state: "user, business-partner and employee notifications initiated November 27 2023; impact investigation completed February 2024"
sources:
  - id: ly-final-impact
    resource: https://www.lycorp.co.jp/ja/news/announcements/007712/
    title: 不正アクセスによる、情報漏えいに関するお知らせとお詫び（2024/2/14更新）
    author: organization:LINEヤフー
  - id: ly-recurrence
    resource: https://www.lycorp.co.jp/ja/privacy-security/recurrence-prevention/
    title: 不正アクセスによる情報漏えいへの再発防止策及び実施結果
    author: organization:LINEヤフー
  - id: ly-mic
    resource: https://www.lycorp.co.jp/ja/privacy-security/recurrence-prevention/mic/
    title: 総務省からの行政指導を踏まえた再発防止策及び実施結果
    author: organization:LINEヤフー
  - id: ppc-response
    resource: https://www.ppc.go.jp/files/pdf/240328_houdou.pdf
    title: LINEヤフー株式会社に対する個人情報保護法に基づく行政上の対応について
    author: organization:個人情報保護委員会
  - id: ly-complete
    resource: https://www.lycorp.co.jp/ja/news/announcements/020659/
    title: 不正アクセスによる情報漏えいへの再発防止策に関する報告完了のお知らせ
    author: organization:LINEヤフー
---

# 概要

2023年、LINEヤフーの旧LINE系社内システムが不正アクセスを受け、LINEユーザー、取引先、従業者等の個人データが漏えい、または漏えいした可能性が生じた。起点は、韓国NAVER Cloud社とLINEヤフー双方の委託先企業の従業者PCへのマルウェア感染である。その後、NAVER Cloud側と旧LINE側が共通利用していた従業者認証基盤および両データセンター間の広いネットワーク接続を足場として侵入が拡大した。[^ly-final-impact][^ppc-response]

2024年2月の最終影響調査では、ユーザーに関する個人データ302,980件、取引先等86,211件、従業者等130,315件について漏えい又は漏えい可能性が確認された。これらは母集団や単位が異なり、単純合算してユニーク人数とはしない。ユーザー情報のうち22,239件は「通信の秘密」に該当する情報を含んだ。一方、口座情報、クレジットカード情報、LINEトーク本文は対象に含まれないとされた。[^ly-final-impact]

本件は技術復旧後も終わらず、総務省・個人情報保護委員会による行政上の対応、ネットワーク分離、認証基盤見直し、委託関係の再設計等が数年継続し、2026年7月に両当局への再発防止策の最終報告が受領された。[^ly-recurrence][^ly-complete]

# インシデント発生時の環境

本件は、2023年のローカルLLM普及開始期と重なるが、攻撃者がLLMを使用した公開証拠はない。防御上重要なのは、AIではなく**既存の組織間ネットワーク信頼、共通認証、委託先PC、業務委託関係が一つの侵入経路へ連結したこと**である。

旧LINE社とNAVERグループは歴史的・業務的経緯から従業者情報を扱う認証基盤を共同利用し、NAVER CloudのデータセンターとLINEヤフーのデータセンターの間には広い接続が存在していた。個人情報保護委員会は、業務上必要な通信だけに適切に制御していればLINEヤフー側への侵入を防止できた可能性があると指摘した。[^ppc-response]

一方、LINEアカウント情報、メッセージ、通話音声、動画配信等を管理する本番ユーザー向けサーバへの不正アクセスは確認されていない。重要度の高い本番向け個別認証システムには、過去の行政指導を踏まえた強化が存在し、今回の侵害範囲と一致しなかった。これは「何も分離されていなかった」という単純な事例ではない。

# 公開情報で確認できる時系列

| 日付 | 出来事 |
| --- | --- |
| 2023-09-14 | 後の調査で、LINEヤフー社内システムへの不正アクセス開始を確認。委託先従業者PCへのマルウェア感染が起点。[^ly-final-impact] |
| 2023-10-09 | NAVER Cloud側システムを経由してLINEヤフー側へのアクセス開始。 |
| 2023-10-17 | LINEヤフーのセキュリティ部門が不審アクセスを検知し調査開始。 |
| 2023-10-27 | 外部不正アクセスの蓋然性が高いと判断。関連パスワードをリセットし、NAVER Cloud等からの経路を順次遮断。 |
| 2023-10-28 | 従業者の社内システム接続を再ログイン強制。 |
| 2023-11-27 | 初回公表、ユーザー・従業者等への通知開始。IR向けPDFも公表。 |
| 2023-12-27 | 調査拡大により不正アクセス開始日を10月9日から9月14日へ訂正し、追加影響を公表。 |
| 2024-02-14 | 社外メール・Slack等まで追加調査し、影響範囲の最終調査を完了。再発防止策を公表。[^ly-final-impact] |
| 2024-03-05 | 総務省による行政指導。 |
| 2024-03-28 | 個人情報保護委員会が勧告・報告等を要求。[^ppc-response] |
| 2024-04-16 | 総務省が追加の行政指導。 |
| 2024-2025 | ネットワーク分離、国内移転、委託関係見直し等の進捗を当局へ定期報告。[^ly-mic] |
| 2026-07-15 | 総務省・個人情報保護委員会へ最終報告。 |
| 2026-07-21 | LINEヤフーが再発防止策の報告完了を公表。[^ly-complete] |

# 即応性の評価

## 検知

最古の確認済み不正アクセス9月14日から、自社セキュリティ部門の検知10月17日まで約33日ある。検知当日に攻撃と断定したわけではなく、10月27日に外部不正アクセスの蓋然性が高いと判断した。

この約1か月を「無監視」と断定してはならないが、**侵害が継続した期間と、自社検知・確信までに差があった**ことは公開情報から確認できる。

## 封じ込め

10月27日の判断後、侵害に用いられた可能性のある従業者パスワードをリセットし、関係会社側からLINEヤフーへのアクセス経路を順次遮断した。翌日には従業者へ再ログインを強制した。資格情報とネットワーク経路の双方を封じ込め対象にした点は妥当である。

## 影響範囲確定

初報後も12月、翌2月に影響件数・侵入開始日が更新された。初期の公表値を固定せず、社外SaaSのメール・Slackまで調査対象を広げた結果、従業者等の影響が大幅に増えた。これは「訂正があったこと」自体より、調査範囲を拡張して過去の認識を更新した点を評価する。

# 影響

## ユーザー

最終公表ではユーザー個人データ302,980件、うち日本ユーザー130,192件。推計値を含む。22,239件には通信の秘密に該当する情報が含まれた。LINEトーク本文、口座、クレジットカード情報は対象外とされた。[^ly-final-impact]

## 取引先

取引先等の個人データ86,211件。主に社外メールアドレス等で、Slackプロフィール等も含む。

## 従業者・委託関係者

130,315件。共通認証基盤の51,347アカウントと、社内コミュニケーション等78,962件等を含む。アカウント数と従業者人数は一致しない。

# 規制・ガバナンス上の評価

個人情報保護委員会は本件を、セキュリティ保守委託先への不正アクセスからNAVER Cloudを踏み台にした**サプライチェーン型侵害**として整理した。また、共通認証基盤と広いネットワーク接続、安全管理措置、委託先管理等を問題として扱った。[^ppc-response]

総務省は2024年3月5日と4月16日に行政指導を行い、ネットワーク分離、安全管理、委託先管理、ガバナンス等の抜本的見直しを求めた。[^ly-recurrence]

# 再発防止と2026年までの予後

LINEヤフーは次のような対策を段階実施した。

- NAVER社・NAVER Cloud社との不必要な通信を遮断。
- ファイアウォール設置・ポリシー見直し。
- サーバー・データの日本国内移転に伴うネットワーク再設計。
- 不要なファイアウォールポリシーを定期削除。
- 委託業務の終了・縮小計画。
- 共通認証・ネットワーク依存の見直し。
- 再発防止進捗の定期的な対外公開。

2026年7月15日に総務省・個人情報保護委員会への最終報告を行い、受領された。技術事故は2023年に封じ込められたが、制度・ガバナンス面の予後は約3年続いた。[^ly-mic][^ly-complete]

# 事故前セキュリティ開示との比較

本件では、LINEサービス本番系の一部重要システムに過去の行政指導を受けた強化が存在し、今回不正アクセスを受けた社内系とは被害境界が異なった。したがって「セキュリティ投資が全て無効だった」とは評価しない。

一方、委託先・NAVER Cloud・共通認証・社内システム間の信頼境界については、事故後に大幅な分離と委託関係見直しが必要となった。**高度な本番サービス防御と、社内・サプライチェーンの信頼境界は別々に成熟度を測る必要がある**。

# 株主・投資家向け資料

LINEヤフーは2023年11月27日の事故公表をIRニュースとしてPDFでも掲載した。事故レポートではWeb公表だけでなく、このIR PDFを投資家向け説明の一次資料として保存する。

- 2023-11-27 IR PDF: `https://www.lycorp.co.jp/ja/ir/news/auto_20231127594672/main/0/link/Notice%20and%20apology%20regarding%20information%20leakage%20due%20to%20unauthorized%20access_JP.pdf`

# 防御上の教訓

- 共通認証基盤は利便性だけでなく組織間の横展開可能性として評価する。
- 委託先PCの侵害から本社環境へ届くネットワーク経路を最小化する。
- 本番サービスが強固でも、社内分析・ソースコード・コミュニケーション環境が同じ信頼経路にあると別の被害面が残る。
- 初報後にSaaS・外部サービスまでフォレンジック範囲を拡張する。
- 再発防止は「計画」ではなく、当局報告完了まで数年単位で追跡する。

# 不明点・限界

- 攻撃者の属性・帰属。
- マルウェアの侵入手法と初期感染経路の詳細。
- 9月14日より前の攻撃準備活動。
- 個々の流出データが実際に二次悪用されたかの長期定量値。
- 本件でLLM/生成AIが使われた証拠はない。

[^ly-final-impact]: LINEヤフー「不正アクセスによる、情報漏えいに関するお知らせとお詫び（2024/2/14更新）」.
[^ly-recurrence]: LINEヤフー「不正アクセスによる情報漏えいへの再発防止策及び実施結果」.
[^ly-mic]: LINEヤフー「総務省からの行政指導を踏まえた再発防止策及び実施結果」.
[^ppc-response]: 個人情報保護委員会「LINEヤフー株式会社に対する個人情報保護法に基づく行政上の対応について」2024-03-28.
[^ly-complete]: LINEヤフー「不正アクセスによる情報漏えいへの再発防止策に関する報告完了のお知らせ」2026-07-21.