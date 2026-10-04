---
type: Cybersecurity Incident
title: NTT西日本グループ — 約10年にわたる内部不正・約928万人分の顧客情報持ち出し
description: コールセンターシステムの運用保守担当者による長期内部不正について、管理者権限、USB持ち出し、2023年7月の調査失敗、行政対応、2026年9月までの再発防止実装を追跡する。
resource: https://www.ntt-west.co.jp/news/2402/240229a.html
tags: [japan, insider-threat, outsourcing, privileged-access, data-exfiltration, governance, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: NTT西日本グループ／NTTマーケティングアクトProCX／NTTビジネスソリューションズ
  sector: telecommunications-and-bpo
  jurisdiction: JP
  incident_status: long_term_remediation_in_progress
  attack_type: malicious-insider-data-exfiltration
  earliest_known_activity: "2013-07"
  detected_at: "2023-10-17 police investigation made incident public; customer warning existed 2023-07-13"
  first_disclosed_at: "2023-10-17"
  latest_public_update: "2026-09-30 remediation progress"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "authorized operational access and system administrator account abused by a dispatched maintenance worker"
  affected_services: "contact-center systems operated for multiple private-sector, public-sector and local-government clients"
  data_exposure: confirmed
  availability_impact: none_established
  restoration_state: "data leakage stopped; group-wide insider-risk remediation and governance improvements continue"
  secondary_abuse: "data was sold to third parties; no confirmed downstream misuse for individual NTT West customers in reviewed updates"
  downstream_impact: "approximately 9.28 million people across 69 client organizations in the final group investigation"
  regulatory_response: "PPC recommendation/guidance January 24 2024; MIC guidance to NTT West February 9 2024; criminal arrest and prosecution"
  notification_state: "client and affected-person notifications continued as matching/identification progressed"
sources:
  - id: ntt-initial
    resource: https://www.ntt-west.co.jp/news/2310/231017a.html
    title: お客さま情報の不正流出に関するお詫びとお知らせ
    author: organization:NTT西日本
  - id: ntt-investigation
    resource: https://www.ntt-west.co.jp/news/2402/pdf/240229a_1.pdf
    title: お客さま情報の不正持ち出しを踏まえたNTT西日本グループの情報セキュリティ強化に向けた取組みについて
    author: organization:NTT西日本グループ
  - id: ppc-ntt
    resource: https://www.ppc.go.jp/files/pdf/240124_houdou.pdf
    title: NTTマーケティングアクトProCX及びNTTビジネスソリューションズに対する行政上の対応
    author: organization:個人情報保護委員会
  - id: ntt-progress
    resource: https://www.ntt-west.co.jp/corporate/security/
    title: 情報セキュリティ強化に向けた取り組みの進捗状況
    author: organization:NTT西日本
---

# 概要

NTT西日本グループのコールセンター基盤で、NTTビジネスソリューションズに派遣されていた運用保守担当者がシステム管理者アカウントを悪用し、顧客データ保管サーバーへアクセスして情報を持ち出していた。グループ調査では、2013年7月頃から2023年2月頃まで約10年間、**約928万人分・69クライアント**の情報が不正に持ち出され、一部が第三者へ売却されていた。[^ntt-investigation][^ppc-ntt]

これは2023年に「発生」した攻撃ではなく、ローカルLLM時代が始まる以前から長期間続いていた内部不正が2023年に表面化した事例である。したがってAI時代の比較コーパスでは、**外部攻撃の高度化だけを見ても長期権限乱用・委託先統制・ログ監視を説明できない**基準点として収録する。

# インシデント発生時の環境

運用保守担当者は業務上必要な高い権限を持ち、システム管理者アカウントで顧客データ保管サーバーへ到達できた。公表資料では、保守端末側から情報を取得し、外部へ持ち出す経路が長期間存在した。[^ntt-investigation]

事故前の防御には規程・システム・運用管理が存在したが、調査委員会は後に、情報セキュリティ管理体制そのものの不足、委託元・委託先の役割不明確、管理者権限、ログ分析・エスカレーション、外部記録媒体等の複数の欠陥を指摘した。

# 時系列

| 時期 | 出来事 |
| --- | --- |
| 2013年7月頃〜2023年2月頃 | 元派遣社員が管理者アカウントを悪用し、顧客情報を継続的に持ち出し。[^ntt-investigation] |
| 2023-07-13 | クライアント1社が情報流出可能性を指摘し社内調査を要請。 |
| 2023年7月 | ProCX/BSの「過去調査」は流出なしと回答。後の検証で調査の重大な不備が判明。 |
| 2023-10-17 | 警察捜査を受け、ProCX/BSおよびNTT西日本が公表。[^ntt-initial] |
| 2023-12-19 | クライアントとの紐付け結果を続報。 |
| 2024-01-24 | 個人情報保護委員会がProCX/BSへ勧告・指導。[^ppc-ntt] |
| 2024-01-31 | 元派遣社員を逮捕。2月21日起訴。 |
| 2024-02-09 | 総務省がNTT西日本へ委託先監督に関する行政指導。 |
| 2024-02-29 | 外部専門家を交えた調査・原因分析・グループ再発防止策を公表。[^ntt-investigation] |
| 2024-09以降 | 再発防止策の進捗を半期ごとに公開。 |
| 2026-07-01 | NTTビジネスソリューションズの事業をNTT西日本等へ統合。 |
| 2026-09-30 | 最新の強化策進捗を公開。計画は概ね予定通り進捗。[^ntt-progress] |

# 即応性と「最初の調査失敗」

本件で最も重要なのは、2023年10月の公表後の対応より**7月13日の警告を正しく扱えなかったこと**である。

クライアントから情報流出可能性の調査依頼があったにもかかわらず、当時の社内調査は不適切で、流出はないと回答した。外部弁護士のみで後日再検証した結果、次が明らかになった。[^ntt-investigation]

- エクスポートログを改変して「問題なし」と回答。
- USBポートや暗号化ソフト、保守者体制について虚偽回答。
- 調査担当者を限定し、十分な専門性・前提情報なしにログを誤読。
- 社内幹部やNTT西日本への適切なエスカレーションを実施しなかった。
- 委託元・委託先という責任分界が曖昧だった。

調査委員会はこの過去調査を、実質的に「調査」ではなく事なかれ主義的な作業と評価した。これは、**インシデント対応能力はSOCや製品導入だけではなく、不都合な兆候をエスカレーションできる組織文化・調査独立性まで含む**ことを示す。

# 影響

個人情報保護委員会は、2024年1月時点で約928万人分を確認し、委託元は民間事業者30社、独立行政法人1機関、地方公共団体38団体と整理した。[^ppc-ntt]

NTT西日本自身の対象顧客には氏名、住所、電話番号、生年月日、メールアドレス、サービス種別、回線ID等が含まれ、決済情報・各種パスワードは対象外とされた。

本件はBPO・コールセンターという共有基盤で発生したため、一事業者の内部不正が多数の委託元とその顧客・住民へ下流波及した。

# 再発防止

2024年以降、NTT西日本グループは次を進めた。

- 私有USBメモリ等の外部記録媒体を接続できない措置。
- 中継サーバーを設置し、保守端末への直接ダウンロードを禁止。
- 保守端末のインターネット接続無効化、MACアドレス認証。
- 作業者へ顧客データのダウンロード権限を与えない運用形態。
- 中継サーバーへのEDR・MFA。
- 重要情報システムを4つの利用者立場×44項目で点検。
- IT資産リスク管理データベース、SDLCガバナンス。
- 特権アカウントを持つ長期配置者への対処。
- 不正操作・不審アクセスをAI/相関分析する監視。
- 規程・マニュアルの簡素化、階層別研修、職場ディスカッション。

2026年9月時点でも半期進捗公表が継続しており、NTT西日本は「セキュリティファーストカンパニー」への転換を掲げている。[^ntt-progress]

# 事故前セキュリティ取り組みとの比較

通信大手としてNTT西日本グループは外部サイバー攻撃へのセキュリティ能力・事業を保有していたが、本件の中心は**正当な管理権限を持つ保守人員の内部不正**だった。

したがって「NTTのSOCや外部攻撃対策が無意味だった」とは評価しない。一方、運用保守、委託先監督、特権アクセス、大量取得、リムーバブルメディア、ログ検証、調査ガバナンスという別の統制面が長期間破られていた。

# 2026年時点の予後

事故そのものの持ち出しは停止しているが、再発防止策は2026年度末までの完了計画を含み、2026年9月にも進捗が更新されている。さらに2026年7月にはNTTビジネスソリューションズの事業運営体制自体が再編された。

これは「漏えい件数を確定して本人通知したら終了」ではなく、**組織・システム・権限設計・文化を数年かけて改修する長期予後**の代表例である。

# 防御上の教訓

- 内部不正ではMFAだけでなく、正当権限の最小化・大量取得制限・持ち出し経路遮断が必要。
- 特権ユーザーの長期固定配置をリスクとして管理する。
- 委託元と委託先の責任分界・エスカレーション経路を明文化する。
- 顧客からの漏えい兆候を「苦情対応」ではなく独立性あるインシデント調査へ昇格させる。
- ログを持つだけでなく、改変・誤読・選択的解釈を防ぐ調査手続きが必要。
- AIによる監視高度化は事故後施策の一つだが、人間の組織文化・利益相反を置き換えない。

# 不明点・限界

- 不正に販売された全データの最終流通先。
- 個々のデータ主体に生じた二次被害の総数。
- 事故前の各保守システムで有効だった全統制の詳細。
- 本件はローカルLLM時代以前から継続した内部不正であり、LLM利用との関連はない。

[^ntt-initial]: NTT西日本「お客さま情報の不正流出に関するお詫びとお知らせ」2023-10-17.
[^ntt-investigation]: NTT西日本グループ「お客さま情報の不正持ち出しを踏まえた情報セキュリティ強化に向けた取組みについて」2024-02-29.
[^ppc-ntt]: 個人情報保護委員会「NTTマーケティングアクトProCX及びNTTビジネスソリューションズに対する行政上の対応」2024-01-24.
[^ntt-progress]: NTT西日本「情報セキュリティ強化に向けた取り組みの進捗状況」2026-09-30.