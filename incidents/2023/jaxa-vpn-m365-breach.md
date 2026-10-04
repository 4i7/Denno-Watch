---
type: Cybersecurity Incident
title: JAXA — VPN脆弱性から横展開・Microsoft 365への正規利用者偽装アクセス
description: 2023年10月に外部機関通報で認知したJAXA侵害について、VPN脆弱性、未知マルウェア、資格情報窃取、Microsoft 365、不正アクセス再発、恒久対策まで追跡する。
resource: https://www.jaxa.jp/press/2024/07/20240705-2_j.html
tags: [japan, government, space, vpn, identity, m365, zero-day-like, credential-theft, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: 国立研究開発法人宇宙航空研究開発機構（JAXA）
  sector: aerospace-and-government-research
  jurisdiction: JP
  incident_status: remediation_and_monitoring
  attack_type: vulnerability-exploitation-and-credential-abuse
  earliest_known_activity: "2023"
  detected_at: "2023-10 external-organization notification"
  first_disclosed_at: "2024-07-05 detailed public report"
  latest_public_update: "2024-07 detailed report and subsequent security strengthening"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "VPN appliance vulnerability; likely exploitation of a recently disclosed vulnerability"
  affected_services: "internal servers/endpoints and Microsoft 365 environment"
  data_exposure: confirmed_and_possible_mixed
  availability_impact: "servers disconnected for containment; rocket/satellite operations not reported as affected"
  restoration_state: "malware removed, emergency controls implemented, permanent measures being rolled out"
  downstream_impact: "information shared with external partner organizations and personal information"
  regulatory_response: "coordinated with police, JPCERT/CC, IPA and Microsoft"
  notification_state: "affected external parties were individually informed and apologized to"
sources:
  - id: jaxa-report
    resource: https://www.jaxa.jp/press/2024/07/20240705-2_j.html
    title: JAXAにおいて発生した不正アクセスによる情報漏洩について
    author: organization:JAXA
  - id: jaxa-president
    resource: https://www.jaxa.jp/about/president/presslec/202407_j.html
    title: 2024年7月理事長定例記者会見
    author: organization:JAXA
---

# 概要

JAXAは2023年10月、外部機関からの通報により業務用イントラネットの一部サーバーに対する不正アクセスを認知した。調査では、第三者がVPN装置の脆弱性を起点にサーバー・端末へ侵入し、内部で侵害を広げてアカウント情報等を窃取、その資格情報を用いてMicrosoft 365へ**正規ユーザーを装って不正アクセス**したことが確認された。[^jaxa-report]

MS365上で管理していた外部機関との業務情報・個人情報の一部が漏えいした。一方、侵害を受けた情報システム・ネットワークではロケットや衛星の運用等の機微情報を扱っておらず、そこへの影響は確認されていない。[^jaxa-report]

# インシデント発生時の環境

2023年はVPN・境界装置がランサムウェアや標的型侵入の主要な攻撃面として既に問題化していた。本件でもVPN装置の脆弱性が侵入起点となった。

JAXAは高度な技術組織であり、警察・JPCERT/CC・IPA・Microsoft等と連携可能な体制を持っていた。それでも、未知のマルウェアが複数使われ、侵害検知を困難にしたと自ら説明している。[^jaxa-report]

本件は「高度組織なら未知脅威を即時検知できる」という前提が成立しない例であり、**外部情報共有と独立通報が重要な検知チャネル**だった。

# 時系列

| 時期 | 出来事 |
| --- | --- |
| 2023年 | VPN装置の脆弱性を起点とする侵入が発生。詳細日時は非公表。 |
| 2023-10 | 外部機関からの通報で侵害を認知。[^jaxa-report] |
| 認知直後 | 攻撃元との通信遮断、対象サーバ等をJAXAネットワークから切断。 |
| 調査期 | セキュリティベンダーによる侵害痕跡・端末・サーバーのフォレンジック、未知マルウェア発見・除去。 |
| 調査期 | MS365への不正アクセス可能性を認識しMicrosoft専門チームが調査。追加侵害なしを確認。 |
| 2024年 | VPN機器を狙った複数の追加不正アクセスを確認したが、これらによる情報漏えいは確認されず。 |
| 2024-07-05 | 詳細な侵害範囲・対応状況を公表。[^jaxa-report] |
| 2024-07-12 | 理事長会見でVPN→横展開→資格情報→MS365の流れを改めて説明。[^jaxa-president] |

# 即応性

自社監視による初期検知ではなく外部機関通報が起点だった点は重要である。認知後は、通信遮断・サーバ切断・専門機関調査・マルウェア除去・緊急防御を並行実施した。

またMS365への侵害可能性が出た段階でMicrosoft専門チームを投入して追加侵害の有無を調査した。SaaS側証拠を自社ログだけで完結させず、提供者側の調査能力を利用した点は、クラウド共有責任・証拠境界の代表例である。

# 技術的に確認できた事項

JAXAの公開報告は侵害経路を比較的具体的に示す。[^jaxa-report]

1. VPN装置の脆弱性を起点に一部サーバー・端末へ侵入。
2. サーバーから横展開し、アカウント情報等を窃取。
3. 窃取資格情報を使い、MS365へ正規ユーザーを装ってアクセス。

VPN脆弱性は「先だって公表された脆弱性が悪用された可能性が高い」とされるが、具体的CVE・製品名は公表資料で明記されていないため推定しない。

複数の未知マルウェアも利用され、検知困難性を高めた。

# 影響

- JAXA職員等の個人情報を含む、一部端末・サーバー上の情報に漏えい可能性。
- MS365上の外部機関との業務情報・個人情報の一部は漏えいを確認。
- ロケット・衛星運用等の機微情報は侵害対象システムで扱っておらず、影響なしと説明。
- 影響先には個別説明・謝罪を実施。

件数が公開されていないため、独自推計を行わない。

# 追加攻撃と再発防止

JAXAは2024年にも複数回、VPN機器を狙った不正アクセスを確認したが、情報漏えいはないとした。これは「最初の事故後も同じ攻撃面が攻撃され続ける」ことを示す。

短期的対策として脆弱性へ迅速対応する体制を整え、恒久対策も策定した。恒久対策の詳細すべては公開していない。

# 事故前のセキュリティ取り組みとの比較

JAXAは国家的研究開発機関として情報セキュリティ管理・外部専門機関との連携能力を持っていたが、本件の初期認知は外部通報だった。したがって評価すべきは「体制があるか」だけではなく、**境界装置での新規脆弱性悪用を何時間・何日で検知できるか、資格情報窃取後のクラウドアクセスを行動分析で止められるか**である。

# 2026年までの予後

2026年10月4日の再確認時点で、2024年7月報告を置き換える大規模な追加漏えい公表は確認していない。恒久対策の具体化・実装は継続課題として公表されており、追加攻撃があったことから再発防止は「一度パッチを当てて終了」とは扱えない。

# 防御上の教訓

- VPN・境界機器は「社内へ入る門」ではなく直接インターネットへ晒された高価値資産として監視する。
- 新規脆弱性公開後の対応速度を日単位で測る。
- 資格情報窃取を前提に、クラウド側で異常ログイン・セッションを検知する。
- 外部機関からの通報チャネルを正式なインシデント検知系へ組み込む。
- 自社ログにないSaaS証拠は提供者と共同調査できる契約・手順を持つ。
- 未知マルウェア前提で、シグネチャ以外の振る舞い監視・フォレンジックを準備する。

# 不明点

- VPN製品名・CVE。
- 初期侵入の厳密な日時。
- 漏えいデータの総件数。
- 攻撃者の帰属。
- 2024年追加攻撃と2023年侵害の攻撃主体同一性。
- LLM/生成AI利用を示す公開証拠はない。

[^jaxa-report]: JAXA「JAXAにおいて発生した不正アクセスによる情報漏洩について」2024-07-05.
[^jaxa-president]: JAXA「2024年7月理事長定例記者会見」2024-07-12.