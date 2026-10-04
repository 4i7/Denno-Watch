---
type: Cybersecurity Incident
title: IIJ Secure MX — 第三者製Active! mail未発見脆弱性／メール・認証情報漏えい
description: 2024年8月から2025年4月まで継続したIIJ Secure MX侵害について、当時未発見の第三者製ソフトウェア脆弱性、長期潜伏、メール・クラウド認証情報、総務省行政指導、事故前のセキュリティ専門性との比較を整理する。
resource: https://www.iij.ad.jp/news/pressrelease/2025/0422-2.html
tags: [japan, saas, email, zero-day, third-party, credentials, security-provider, iij, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: 株式会社インターネットイニシアティブ
  sector: internet-and-security-services
  jurisdiction: JP
  incident_status: contained_with_regulatory_followup
  attack_type: third-party-software-zero-day-exploitation
  earliest_known_activity: "2024-08-03"
  detected_at: "2025-04-10"
  first_disclosed_at: "2025-04-15"
  latest_public_update: "2025-08-21 dedicated incident inquiry closed; regulatory measures continued"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "then-undiscovered stack-based buffer-overflow vulnerability in third-party Active! mail software, later JVN#22348866"
  affected_services: "IIJ Secure MX Service infrastructure"
  data_exposure: confirmed
  availability_impact: "service remained available after malicious access route was isolated"
  restoration_state: "affected route isolated; Active! mail option had already been retired in February 2025; monitoring and security strengthening followed"
  downstream_impact: "enterprise mail accounts/passwords, email contents/headers, and credentials for connected third-party cloud services"
  regulatory_response: "MIC written administrative guidance on July 18 2025 regarding leakage of secrecy of communications"
sources:
  - id: iij-first
    resource: https://www.iij.ad.jp/news/pressrelease/2025/0415.html
    title: IIJセキュアMXサービスにおけるお客様情報の漏えいについて
    author: organization:IIJ
  - id: iij-second
    resource: https://www.iij.ad.jp/news/pressrelease/2025/0422-2.html
    title: IIJセキュアMXサービスにおけるお客様情報の漏えいについてのお詫びとご報告
    author: organization:IIJ
  - id: iij-mic
    resource: https://www.iij.ad.jp/news/pressrelease/2025/0718.html
    title: 当社に対する総務省からの行政指導について
    author: organization:IIJ
  - id: iij-ir2024
    resource: https://www.iij.ad.jp/ir/integrated-report/archives/pdf/integrated-repot2024.pdf
    title: 統合報告 2024
    author: organization:IIJ
---

# 概要

IIJが法人向けに提供するメールセキュリティサービス「IIJセキュアMXサービス」の設備が、2024年8月3日以降に不正アクセスを受け、悪意あるプログラムが実行されていたことが2025年4月10日に判明した。[^first]

初報では、影響可能性を否定できない最大範囲として**6,493契約、4,072,650メールアカウント**を通知対象とした。4月22日の追加調査では、実際の漏えいが確認された範囲を絞り込み、メールアカウント・パスワードは132契約・311,288アカウント、メール本文・ヘッダは6契約、連携する他社クラウドサービスの認証情報は488契約で確認した。重複除外後の影響契約数は586契約だった。[^second]

原因は第三者製ソフトウェアActive! mailの脆弱性で、侵害発生から発覚まで未発見だった。事案を通じて脆弱性が初めて明らかになり、後にJVN#22348866として公開された。[^second]

# 事故前の環境と公表統制

IIJはセキュリティを主力事業の一つとし、統合報告2024でSOC運用、セキュリティ人材育成、警察等とのサイバー人材連携を公表していた。したがって本件は、セキュリティ専門企業でも侵害され得るという点で重要である。

ただし「SOCがあったのに無意味だった」とは評価しない。第三者製ソフトウェア内部の未知脆弱性を悪用した不正プログラム実行が、既存監視でどの程度観測可能だったかは別問題である。比較すべきは、未知脆弱性そのものだけでなく、**侵害後の不審挙動・永続化・大量認証情報アクセスをどのテレメトリで検知できたか**である。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2024-08-03以降 | 後の調査でサービス設備への不正アクセス開始を確認。[^first] |
| 2025-02 | IIJは対象Active! mailを利用するオプション機能の提供を終了。事故発覚前の終了であり、事故対策として行ったとは扱わない。 |
| 2025-04-10 | 情報漏えい可能性を確認。不正アクセス経路を特定し切り離し。 |
| 2025-04-15 | 第一報。最大6,493契約・4,072,650アカウントへ影響可能性を通知。[^first] |
| 2025-04-18 | ソフトウェアベンダー修正後、JVNがActive! mail脆弱性を緊急情報として公開。 |
| 2025-04-22 | 第二報。確定漏えい範囲、原因、第三者クラウド認証情報への影響を公表。[^second] |
| 2025-07-18 | 通信の秘密の漏えい事案について総務省から書面による行政指導。[^mic] |
| 2025-08-21 | 事故専用問い合わせフォームを終了し通常窓口へ移行。 |

# 検知・即応性

最古の確認済み侵害活動から検知まで約8か月ある。これは長いが、未知脆弱性であったことだけで説明を終えない。脆弱性を知らなくても、サービス設備での不正プログラム実行、権限利用、メール・認証情報へのアクセス等を行動監視で早期検知できた可能性は別途評価対象となる。

4月10日に漏えい可能性を確認した後は侵入経路を特定・切り離し、5日後に全顧客を含む最大範囲で初報した。さらに1週間後には確定影響範囲を大幅に絞り込んだ。

# 被害の性質

特に重要なのは、メール本文だけでなく**認証情報がサービス集中点へ存在したこと**である。

- IIJ Secure MX上で作成されたメールアカウント・パスワード。
- メール本文・ヘッダ。
- Secure MXと連携する他社クラウドサービスの認証情報。

メールセキュリティサービスは防御機能である一方、利用企業の認証情報や通信内容が集中するため、侵害時には高い集中リスクを持つ。

# 事故前開示との比較

IIJはSOC・セキュリティ人材・外部連携を公表していた。事故では第三者製品の未発見脆弱性が突破口となったため、事故前のセキュリティ専門性と矛盾するとは限らない。

しかし、**2024年8月から2025年4月まで不正アクセスが継続した事実**は、未知脆弱性の予防だけでなく侵害後検知、第三者コンポーネント監視、長期的な設備挙動分析を評価する必要を示す。

# 規制・長期予後

総務省は2025年7月18日、通信の秘密の漏えいに関しIIJへ書面指導を行った。IIJは再発防止、セキュリティ対策、監視体制強化を進めるとした。[^mic]

2026年10月4日の再確認では、同事案について初回の586契約確定範囲を大きく覆す新たな漏えい公表は確認していない。

# 株主・投資家・PDF資料

- IIJ統合報告2024: `https://www.iij.ad.jp/ir/integrated-report/archives/pdf/integrated-repot2024.pdf`
- 2025-04-22事故報告PDF: `https://www.iij.ad.jp/news/pressrelease/2025/pdf/20250422_SMX_2.pdf`
- 2025-07-18行政指導公表はPDF版も会社ページから取得可能。

事故前の統合報告と事故後PDFを同じ時間軸へ載せるが、後者の統制強化を事故前能力へ遡及しない。

# 防御上の教訓

- セキュリティ製品もサプライチェーン部品を持つ通常のソフトウェアシステムとして扱う。
- 未知脆弱性前提で、サービス設備の挙動・プロセス・認証情報アクセスを監視する。
- 防御サービスへ保存する他社クラウド認証情報を最小化し、短期資格情報・ローテーションを優先する。
- 初報は最大影響範囲、続報は確定範囲として明確に分離する。
- SOCの有無ではなく、今回の攻撃経路を観測できたログ・保持期間・検知ルールを評価する。

# 不明点

- 2024年8月3日の初回悪用以前に偵察活動があったか。
- 攻撃者の帰属。
- 侵害期間中の不正プログラムの全機能・永続化手法。
- 事故前にどの検知ログが存在し、なぜ4月まで警報化されなかったかの詳細。
- 本件でLLM/生成AIが使われた公開証拠はない。

[^first]: IIJ「IIJセキュアMXサービスにおけるお客様情報の漏えいについて」2025-04-15.
[^second]: IIJ「IIJセキュアMXサービスにおけるお客様情報の漏えいについてのお詫びとご報告」2025-04-22.
[^mic]: IIJ「当社に対する総務省からの行政指導について」2025-07-18.