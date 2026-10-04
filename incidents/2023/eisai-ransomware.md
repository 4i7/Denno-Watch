---
type: Cybersecurity Incident
title: エーザイ — 2023年ランサムウェア／国内外サーバー・物流関連システムの隔離
description: 2023年6月のエーザイグループランサムウェアについて、即時の全社対策本部、国内外システム隔離、IR開示、同年4月の別クラウド不正アクセス、事故後の情報セキュリティ組織強化まで追跡する。
resource: https://www.eisai.com/news/2023/news202341.html
tags: [japan, pharmaceutical, ransomware, logistics, governance, ir, eisai, 2023]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: エーザイ株式会社
  sector: pharmaceutical
  jurisdiction: JP
  incident_status: public_detail_limited_after_initial_response
  attack_type: ransomware
  earliest_known_activity: "2023-06-03 late night"
  detected_at: "2023-06-03 late night"
  first_disclosed_at: "2023-06-06"
  latest_public_update: "2023-06-06 incident disclosure; later governance materials discuss cybersecurity strengthening"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "multiple group servers and selected internal systems in and outside Japan including logistics-related systems"
  data_exposure: unknown_in_public_final_record
  availability_impact: "selected internal/logistics systems disconnected; corporate websites and email remained operational"
  restoration_state: "recovery initiated with external experts; detailed final technical report not found in reviewed public record"
  regulatory_response: "law enforcement consulted; incident disclosed as TSE Prime listed-company release"
  notification_state: unknown
sources:
  - id: eisai-ransom
    resource: https://www.eisai.com/news/2023/news202341.html
    title: Notification of Ransomware Incident
    author: organization:Eisai Co., Ltd.
  - id: eisai-ransom-pdf
    resource: https://www.eisai.co.jp/news/2023/pdf/news202341pdf.pdf
    title: ランサムウェア被害の発生について
    author: organization:エーザイ株式会社
  - id: eisai-april
    resource: https://www.eisai.co.jp/information/2023/pdf/20230519.pdf
    title: 2023年4月28日のクラウドプラットフォーム不正アクセスに関する公表
    author: organization:エーザイ株式会社ほか
  - id: eisai-governance
    resource: https://www.eisai.co.jp/company/governance/cgregulations/pdf/cgovernance20241223.pdf
    title: コーポレートガバナンス報告書（2024年12月）
    author: organization:エーザイ株式会社
---

# 概要

エーザイは2023年6月3日深夜、グループの複数サーバーがランサムウェアにより暗号化されていることを確認した。直ちにインシデント対応計画を実行し、外部専門家と調査を開始、全社対策本部を立ち上げた。[^eisai-ransom]

被害対応のため、物流関連を含む国内外の一部社内システムをサーバーから切り離した。一方、Webサイト・メールは通常稼働していた。初報時点では情報流出の有無と業績影響を調査中とした。[^eisai-ransom]

# 発生直前の別インシデント

エーザイグループはランサムウェアの約1か月前、2023年4月28日に**海外法人社員のアカウントを不正利用した外部者がクラウドプラットフォーム上の一部情報へアクセスした別事案**も確認していた。5月19日の公表では、取引先関係者の氏名・メールアドレスが漏えいした可能性を示し、不正アクセス遮断、ネットワーク監視強化、各国規制への対応を行った。[^eisai-april]

公開情報から4月事案と6月ランサムウェアの攻撃主体・侵入経路が同一だと結び付ける根拠はない。Denno Watchでは別事案として扱いながら、**同一企業で短期間に異なる認証/クラウド侵害とランサムウェアが発生した時代背景**として相互参照する。

# 事故発生時の環境

2023年は製薬業界においてもグローバルIT、クラウド、物流・研究・本社機能のデジタル依存が高まっていた。エーザイのランサムウェア対応では、被害サーバーだけでなく物流関連を含む国内外の一部システムを切り離したため、**侵害拡大防止と医薬品供給継続のトレードオフ**が重要となった。

また、エーザイはコーポレートガバナンス上、秘密情報セキュリティポリシー、情報セキュリティ規程、継続研修、リスクマネジメント体制を持っていた。2023年度には取締役会の課題としてサイバーセキュリティを扱い、後のガバナンス報告ではITセキュリティ強化策の報告・議論、外部有識者による知見習得等が記録されている。[^eisai-governance]

# 時系列

| 日付 | 出来事 |
| --- | --- |
| 2023-04-28 | 別事案として海外法人社員アカウントの不正利用によるクラウド情報アクセスを確認。 |
| 2023-05-19 | 4月事案を公表。関係者通知、PPC等規制対応、監視強化。[^eisai-april] |
| 2023-06-03深夜 | 複数サーバー暗号化を確認。ランサムウェアと認識。[^eisai-ransom] |
| 直後 | 外部専門家と調査開始、インシデント対応計画を実行、全社対策本部を設置。 |
| 2023-06-06 | TSEプライム上場会社の開示として事故を公表。物流関連を含む国内外一部システム隔離、情報流出・業績影響調査中と説明。 |
| 2023-06-21 | 有価証券報告書の後発事象にもランサムウェア被害と調査・復旧中である旨を記載。 |
| 2023-10-16 | IT組織再編で情報セキュリティ部を新設し、グローバルセキュリティオペレーションセンター等の責任を明示。 |
| 2024年以降 | 取締役会・ガバナンス資料でITセキュリティ強化策の監督・議論を継続。[^eisai-governance] |

# 即応性

会社の初報によれば、暗号化を確認後**直ちに**外部専門家との調査、インシデント対応計画、全社対策本部設置を行った。国内外の一部システムを切り離し、警察等関係機関にも相談した。[^eisai-ransom]

Web・メールを維持しながら物流等の一部システムを隔離した点は、全ネットワーク停止ではなく被害範囲と業務継続を分けた対応である。ただし公表情報では、検知時刻から隔離までの時間、復旧完了日、RTO/RPO等は確認できない。

# IR・株主向け開示

6月6日の公表は会社名、代表執行役CEO、証券コード4523（東証プライム）、問い合わせ先を付した投資家向け形式のPDFでも公開された。

- IR/公表PDF: `https://www.eisai.co.jp/news/2023/pdf/news202341pdf.pdf`

さらに有価証券報告書の後発事象にも6月3日のランサムウェア、影響範囲調査、システム保護・復旧、業績影響精査を記載した。事故を単なるITニュースではなく財務報告上の事象として扱っていたことが分かる。

# 公開情報上の限界

2026年10月4日まで再調査した範囲では、6月6日の初報を置き換えるような**詳細な最終フォレンジック報告、情報流出確定件数、侵入経路、復旧完了時刻**を示すエーザイ本体の公開事故報告は確認できなかった。

したがって、初報時点の「情報流出は調査中」を後から「流出なし」と読み替えない。逆に流出があったとも断定しない。

# 事故後の組織対応

2023年10月の組織改編では、IT統括本部に情報セキュリティ部を新設し、グローバルサイバーセキュリティ＆ITコンプライアンス、グローバルSOC等の責任を明示した。後のコーポレートガバナンス資料でも、取締役会がサイバーセキュリティ強化策を監督対象として扱っている。[^eisai-governance]

これは事故との直接因果を会社が明示したものではないため、「ランサムウェアのため組織改編した」と断定せず、**事故後同年度に観測されたガバナンス強化**として記録する。

# 防御上の教訓

- 医薬品企業ではサーバー暗号化と物流・供給継続を同時評価する。
- グローバルシステムは必要に応じ迅速にセグメント分離できる設計にする。
- 1か月前に別のクラウド認証インシデントがあっても、その対策がランサムウェア侵入面を自動的に閉じるとは限らない。
- 取締役会レベルのセキュリティ監督と、実際の端末・サーバ・認証・バックアップ実効性は別軸で測る。
- 初報後に詳細を公開しない場合、外部ナレッジ側では「不明」を維持して推測で埋めない。

# 不明点

- 初期侵入経路。
- 攻撃者・ランサムウェア系統。
- 外部持ち出しの有無・件数。
- 暗号化されたサーバー数。
- 物流への実測影響と復旧完了日。
- 身代金要求・支払の有無。
- 本件でLLM/生成AIが用いられた公開証拠はない。

[^eisai-ransom]: Eisai Co., Ltd., “Notification of Ransomware Incident,” 2023-06-06.
[^eisai-april]: エーザイ株式会社ほか「海外法人社員アカウントを不正利用したクラウドプラットフォームへの不正アクセス」2023-05-19.
[^eisai-governance]: エーザイ株式会社「コーポレートガバナンス報告書」2024-12-23.