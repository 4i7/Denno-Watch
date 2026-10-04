---
type: Cybersecurity Incident
title: イセトー — VPN侵入・ランサムウェア／受託データ流出とISO・Pマーク一時停止
description: 2024年5月のランサムウェアについて、VPN侵入、不適切な受託データ保持、リークサイト、ISO27001/27017・プライバシーマーク一時停止、経営体制再構築、2026年の第三者評価まで追跡する。
resource: https://www.iseto.co.jp/news/news_202410.html
tags: [japan, ransomware, vpn, outsourcing, data-retention, iso27001, iso27017, privacy-mark, governance, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: 株式会社イセトー
  sector: information-processing-and-business-services
  jurisdiction: JP
  incident_status: recovered_with_certification_and_governance_followup
  attack_type: ransomware-via-vpn
  earliest_known_activity: unknown
  detected_at: "2024-05-26"
  first_disclosed_at: "2024-05-29"
  latest_public_update: "2026-09-29 third-party cloud security evaluation disclosure"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "unauthorized access through VPN"
  affected_services: "information-processing center, nationwide sales-office endpoints and servers; some entrusted-work data"
  data_exposure: confirmed
  availability_impact: "multiple servers/endpoints encrypted; production delays; affected area isolated from entrusted-data processing area"
  restoration_state: "forensic investigation completed; certifications reinstated in 2025; governance rebuilding continued"
  secondary_abuse: not_observed_in_public_updates
  downstream_impact: "personal information belonging to customers of multiple client organizations"
  regulatory_response: "PPC/client notifications; ISO27001/27017 certificates temporarily suspended; PrivacyMark temporarily suspended"
  notification_state: "affected clients coordinated notifications with data subjects"
sources:
  - id: iseto-first
    resource: https://www.iseto.co.jp/news/news_202405.html
    title: ランサムウェア被害の発生について
    author: organization:株式会社イセトー
  - id: iseto-second
    resource: https://www.iseto.co.jp/news/news_202406.html
    title: ランサムウェア被害の発生について（続報）
    author: organization:株式会社イセトー
  - id: iseto-final
    resource: https://www.iseto.co.jp/news/news_202410.html
    title: 不正アクセスによる個人情報漏えいに関するお詫びとご報告
    author: organization:株式会社イセトー
  - id: iseto-iso-stop
    resource: https://www.iseto.co.jp/news/news_202409.html
    title: ISO27001認証及びISO27017認証の一時停止について
    author: organization:株式会社イセトー
  - id: iseto-iso-resume
    resource: https://www.iseto.co.jp/news/news_202502.html
    title: ISO27001認証及びISO27017認証の一時停止解除について
    author: organization:株式会社イセトー
  - id: iseto-pmark
    resource: https://www.iseto.co.jp/news/news_202503-1.html
    title: プライバシーマーク付与の再開について
    author: organization:株式会社イセトー
  - id: iseto-governance
    resource: https://www.iseto.co.jp/news/news_202503.html
    title: 役員体制のお知らせ
    author: organization:株式会社イセトー
  - id: iseto-2026-assured
    resource: https://www.iseto.co.jp/news/news_202609-7.html
    title: 第三者セキュリティ信用評価サービス「Assuredクラウド評価」を活用
    author: organization:株式会社イセトー
---

# 概要

2024年5月26日、イセトーの情報処理センターおよび全国営業拠点の端末・サーバーがランサムウェアにより暗号化された。外部フォレンジック調査の結果、**VPNからの不正アクセス**で侵入され、一部受託業務で作成された帳票データ・検証物が窃取されたことが確認された。[^iseto-final]

被害を増幅したのは侵入だけではない。イセトーは、本来その情報を取り扱ってはならないサーバーに、作業効率のため便宜的にデータを保管し、業務終了後に削除すべきデータも削除できていなかったと自社公表で認めた。[^iseto-final]

事故時、同社は情報処理センター等を対象にISO/IEC 27001を、クラウドサービスを対象にISO/IEC 27017を取得し、プライバシーマークも保有していた。しかし事故後の特別審査でISO認証が一時停止され、Pマークも一時停止された。是正後、2025年に順次再開された。[^iseto-iso-stop][^iseto-iso-resume][^iseto-pmark]

# 事故前のセキュリティ環境

本件は「セキュリティ認証がなかった企業」の事故ではない。事故時点で、情報処理センター・関西情報処理センターはISO/IEC 27001の認証範囲であり、一部クラウドサービスはISO/IEC 27017も取得していた。さらにPマークを保持していた。[^iseto-iso-stop]

したがって比較上の問いは「認証を取得していたか」ではなく次になる。

- VPNの認証・監視が実環境でどこまで強かったか。
- 認証範囲内で、不要な受託データをルール通り削除できていたか。
- 便宜的なデータコピーを技術的に禁止できていたか。
- 認証審査と日常運用の間で、統制逸脱をどのように検知していたか。

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2024-05-26 | 複数サーバー・PC暗号化を確認。全社対策本部を設置し外部専門家と調査。[^iseto-first] |
| 2024-05-29 | 初報。イントラネット・感染疑いサーバー/PCを休止、警察へ連絡。 |
| 2024-06-06 | 続報。影響領域を受託データ処理領域から切り離し、生産体制は徐々に復旧。情報流出は未確認だが一部顧客で可能性を確認。[^iseto-second] |
| 2024-06-18 | 攻撃者リークサイトに窃取情報のダウンロードURL掲載。 |
| 2024-07-03 | 公開データに顧客個人情報が含まれることを公表。 |
| 2024-09-02 | BSI特別審査によりISO27001/27017認証の一時停止を公表。[^iseto-iso-stop] |
| 2024-10-04 | フォレンジック完了。VPN侵入、不要データ保持、再発防止策を確定公表。[^iseto-final] |
| 2024-12-24 | JIPDECがPマーク付与を3か月一時停止。 |
| 2025-02-10 | BSI特別審査後、ISO27001/27017の一時停止解除。[^iseto-iso-resume] |
| 2025-03-19 | 事故を受けたガバナンス再構築・事業再生を目的とする新経営体制を公表。[^iseto-governance] |
| 2025-03-25 | Pマーク付与再開。JIPDECが是正措置・再発防止策が有効に機能していると認めたと会社が公表。[^iseto-pmark] |
| 2026-09-29 | 第三者セキュリティ信用評価サービスを通じたクラウド評価の公開を開始。[^iseto-2026-assured] |

# 即応性

5月26日の検知後、直ちに全社対策本部を設置し、外部専門家と調査を開始した。感染疑いのイントラネット・サーバー・PCを休止し、警察にも連絡した。[^iseto-first]

6月6日時点では、被害領域を受託データ処理領域から切り離して業務を継続し、生産遅延も回復方向にあった。[^iseto-second]

一方、外部持ち出しは初期調査では確認されず、6月18日に攻撃者サイトへ実データが掲載され、その後の調査で自社サーバーからの流出と確認された。「初期ログで持ち出し未確認」を「流出なし」としなかった点は重要である。

# 原因

会社が最終公表で確認した原因は二層ある。[^iseto-final]

## 侵入

VPNからの不正アクセス。

## 被害増幅

- 受託工程で発生した帳票データ・検証物を、本来扱ってはならないサーバーに便宜的に保管。
- 業務終了後に速やかに削除すべきデータが残存。

つまり「VPNを破られたこと」と「侵害された際のデータ量を増やした情報ライフサイクル管理」は別の失敗である。

# 事故後対策

- 侵入経路となったVPNを使用しない体制へ移行。
- 認証強化。
- 新環境完成まで外部ネットワーク接続を制限。
- 管理区域外へ受託データを移送できない環境。
- 保管期限を明確化し業務終了後に確実に削除。
- ルール遵守監査を強化。
- 個人情報・情報セキュリティ教育とルール研修。

# 認証制度の予後

事故後、ISO27001/27017が一時停止された。クラウド認証対象サービス自体は本件の影響を受けなかったが、ISO27001を基礎とするためISO27017も停止対象となった。[^iseto-iso-stop]

2025年2月、BSIの特別審査後に停止解除。3月にはPマークも、JIPDECが是正措置・再発防止策の有効機能を認めたとして再開された。[^iseto-iso-resume][^iseto-pmark]

これは認証制度を「事故を防ぐ保証」ではなく、**事故後に是正状況を第三者が再評価する一つの証拠**として扱うべきことを示す。

# 経営・組織への長期影響

2025年3月、イセトーは新経営体制への移行を発表し、2024年事故を明示的に挙げて「ガバナンスの再構築による事業再生」を進めるとした。拠点集約・人員配置最適化も含まれた。[^iseto-governance]

2026年9月には、第三者セキュリティ信用評価サービスを通じ、自社クラウドサービスの評価情報を顧客企業が確認できる仕組みを導入した。[^iseto-2026-assured]

技術事故から2年以上経っても、信頼回復・透明性・ガバナンスの予後が継続している。

# 防御上の教訓

- ISO27001/Pマークを侵害耐性の代替指標にしない。
- VPNを使用するなら認証強度・異常検知・到達範囲を個別に評価する。
- データ保持期限を文書だけでなく技術制御で強制する。
- 作業効率を理由とするコピー・仮置きが被害量を増幅しないようDLP/保管境界を設計する。
- 「流出痕跡なし」とリークサイト・顧客通知等の外部証拠を継続突合する。
- 認証一時停止・再審査・復帰までを長期予後として記録する。

# 不明点

- VPN製品・認証方式の詳細。
- 初期アクセス日時・資格情報取得方法。
- 総ユニーク被害人数。
- 攻撃者グループの公的帰属。
- 本件でLLM/生成AIが利用された証拠はない。

[^iseto-first]: イセトー「ランサムウェア被害の発生について」2024-05-29.
[^iseto-second]: イセトー「ランサムウェア被害の発生について（続報）」2024-06-06.
[^iseto-final]: イセトー「不正アクセスによる個人情報漏えいに関するお詫びとご報告」2024-10-04.
[^iseto-iso-stop]: イセトー「ISO27001認証及びISO27017認証の一時停止について」2024-09-02.
[^iseto-iso-resume]: イセトー「ISO27001認証及びISO27017認証の一時停止解除について」2025-02-10.
[^iseto-pmark]: イセトー「プライバシーマーク付与の再開について」2025-03-24.
[^iseto-governance]: イセトー「役員体制のお知らせ」2025-03-19.
[^iseto-2026-assured]: イセトー「第三者セキュリティ信用評価サービス『Assuredクラウド評価』を活用」2026-09-29.