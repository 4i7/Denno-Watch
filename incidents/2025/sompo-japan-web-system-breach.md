---
type: Cybersecurity Incident
title: 損保ジャパン — 2025年Webサブシステム侵害、大規模保険データ影響と金融庁報告徴求
resource: https://www.sompo-japan.co.jp/announce/2025/202504_01/
tags: [japan, insurance, unauthorized-access, web-system, financial-regulation, zero-trust, soc, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: 損害保険ジャパン株式会社
  sector: insurance
  jurisdiction: JP
  incident_status: monitoring
  attack_type: unauthorized access to internal web subsystem
  earliest_known_activity: "2025-04-17"
  detected_at: "2025-04-21"
  first_disclosed_at: "2025-04-25"
  latest_public_update: "2025-07-25"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "公開情報では具体的脆弱性・侵入手口は未確定。侵害したWebシステムと同様の脆弱性が他システムにないことを事後確認"
  affected_services: "各種指標管理を主とした独立Webサブシステム"
  data_exposure: possible
  availability_impact: "侵害Webシステムを停止・ネットワーク遮断。他システムへの影響なしと公表"
  restoration_state: "侵害システムを隔離し、他システム点検・Web監視強化。対象者通知と規制対応を継続"
  regulatory_response: "金融庁から保険業法第128条第1項および個人情報保護法第146条第1項に基づく報告徴求命令"
  ai_relation: era_context_only
  response_latency:
    detection_latency: "フォレンジックで推定されたアクセス可能期間開始4月17日から4月21日検知まで最大約4日"
    containment_latency: "4月21日の検知後、Webシステム停止・ネットワーク遮断を即時実施と公表"
    public_disclosure_latency: "4月21日検知から4月25日第1報まで4日"
  pre_incident_control_disclosure:
    state: confirmed
    published_at: "2024"
    sources: [sompo-sustainability-2024]
    declared_controls: ["多層防御", "ゼロトラスト", "SASE", "SOC監視", "クラウドセキュリティガードレール", "サイバーパトロール", "脆弱性診断・侵入テスト"]
    applicability_to_failure_surface: direct_and_partial
sources:
  - id: sompo-list
    resource: https://www.sompo-japan.co.jp/announce/2025/202504_01/
    title: 当社システムに対する不正アクセスの発生及び情報漏えいの可能性について
  - id: sompo-second
    resource: https://www.sompo-japan.co.jp/-/media/SJNK/files/news/2025/20250611_1.pdf?la=ja-JP
    title: 当社システムに対する不正アクセスの発生及び情報漏えいの可能性について（第2報）
  - id: sompo-fsa
    resource: https://www.sompo-japan.co.jp/-/media/SJNK/files/news/2025/20250613_2.pdf?la=ja-JP
    title: 報告徴求命令の受領
  - id: sompo-sustainability-2024
    resource: https://www.sompo-hd.com/-/media/hd/files/csr/communications/pdf/2024/report2024.pdf
    title: SOMPOホールディングス サステナビリティレポート2024
---

# 概要

損保ジャパンは2025年4月21日、社内の各種指標管理を主とするWebサブシステムへの第三者不正アクセスを確認した。専門業者によるフォレンジックでは、4月17〜21日に外部から侵入した第三者が顧客情報へアクセスできる状態だったと推測され、外部漏えいの可能性を否定できないと判断した。[^sompo-second]

公開件数は複数のデータ区分で示され、重複を含む。氏名・連絡先・証券番号等を含む約337万件、氏名・証券番号約187万件、連絡先・証券番号約119万件、その他約83万件、代理店関連約178万件に加え、内部DBと照合しなければ個人特定できない証券番号・事故番号のみ約844万件がある。これらを単純合算してユニーク人数とはしない。[^sompo-second]

# データの感度

影響可能性のある情報には氏名、住所、電話番号、メールアドレス、生年月日等のほか、金融機関口座情報1,638件、代理店募集人の生年月日9,366件が含まれた。マイナンバーカード・クレジットカード情報は対象外と公表された。[^sompo-second]

2025年7月25日時点でも、実際に外部漏えいした事実・不正利用は確認されていないと会社は説明している。[^sompo-list]

# 初動とスコープ確定

不正侵入検知後、Webシステム停止とネットワーク遮断を即時に実施した。当該Webシステムは独立して稼働しており、他システムへの影響はないことを確認したと公表している。さらに他システムに同様の脆弱性がないことを点検し、Webサイトの不正アクセス監視を強化した。[^sompo-second]

公開情報では侵入に用いられた具体的CVEや認証情報取得手口は示されていないため、一般的なWeb脆弱性名を推定しない。

# 事故前のセキュリティ公表との比較

SOMPOホールディングスの2024年サステナビリティレポートは、多層防御を前提とする技術対策、ゼロトラストの考え方、SASE、SOC監視、クラウド設定ミスを防ぐガードレール、インターネット資産のサイバーパトロール、国内外IT資産への脆弱性診断・侵入テスト等を公表していた。[^sompo-sustainability-2024]

本件は、これらが「存在しなかった」と結論づける材料ではない。むしろ、**グループ高位統制と個別の社内Webサブシステムに残る脆弱性・監視カバレッジを分けて検証する必要**を示す。事故後に「他システムに同様の脆弱性がないこと」を確認したという公表自体が、個別システム単位の露出管理の重要性を示す。

# 規制対応と予後

2025年6月12日、金融庁は本件について保険業法第128条第1項および個人情報保護法第146条第1項に基づく報告徴求命令を発出し、損保ジャパンは翌13日に受領を公表した。調査対象には不正アクセス手口、顧客対応、原因分析、再発防止策が含まれる。[^sompo-fsa]

7月末以降、漏えい可能性のある対象者へ順次個別通知すると会社は公表した。技術的なネットワーク隔離が早くても、通知・規制対応の尾部は数か月以上続く。

# 防御上の教訓

- SOCやSASE等の全社施策と、個別Webアプリの脆弱性・認証・監視を同じ粒度とみなさない。
- 巨大な保険データではファイル件数、証券番号件数、重複を含む対象数をユニーク人数へ変換しない。
- 独立システム化による横展開抑制は、侵入防止とは別の被害限定統制として評価する。
- 金融機関では技術復旧だけでなく、監督当局の報告徴求・原因分析・顧客通知まで予後として追跡する。
- 個別攻撃へのAI/LLM利用を示す公開証拠は確認していない。

[^sompo-second]: 損保ジャパン「当社システムに対する不正アクセスの発生及び情報漏えいの可能性について（第2報）」2025-06-11.
[^sompo-list]: 損保ジャパン「当社システムに対する不正アクセスの発生及び情報漏えいの可能性について」2025-07-25更新.
[^sompo-fsa]: 損保ジャパン「報告徴求命令の受領」2025-06-13.
[^sompo-sustainability-2024]: SOMPOホールディングス「サステナビリティレポート2024」ITガバナンス／サイバーセキュリティ.