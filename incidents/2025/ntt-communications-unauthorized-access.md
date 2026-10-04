---
type: Cybersecurity Incident
title: NTTコミュニケーションズ — 2025年社内システム不正アクセスと検知後の影響範囲拡大
description: 2025年2月5日に不審ログを検知し初動措置を行った後、10日後に別装置への不正アクセスを特定。事故前にEDR/NDR/UEBA等を公表していた環境での検知・スコープ確定を比較する。
resource: https://www.ntt.com/about-us/press-releases/news/article/2025/0305_2.html
tags: [japan, telecommunications, unauthorized-access, monitoring, edr, ndr, ueba, corporate-data, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: NTTコミュニケーションズ株式会社
  sector: telecommunications
  jurisdiction: JP
  incident_status: monitoring
  attack_type: unauthorized access
  earliest_known_activity: unknown
  detected_at: "2025-02-05"
  first_disclosed_at: "2025-03-05"
  latest_public_update: "2025-03-05"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "社内オーダ情報流通システム。一部法人顧客のサービス開通・変更関連情報"
  data_exposure: possible
  availability_impact: "公表資料では大規模な顧客向けサービス停止を主影響としていない"
  restoration_state: "装置Aへ初動制限、装置Bをネットワークから隔離。監視・再発防止強化"
  notification_state: "影響可能性のある17,891社へ営業担当または封書で順次通知"
  ai_relation: era_context_only
  response_latency:
    detection_latency: unknown
    containment_latency: "装置Aは2月5日の検知当日に入口を制限。調査継続で装置Bの侵害を2月15日に特定し同日隔離"
    public_disclosure_latency: "検知2025-02-05から対外公表2025-03-05まで28日"
  pre_incident_control_disclosure:
    state: confirmed
    published_at: "2024"
    sources: [nttcom-sustainability-2024]
    declared_controls: ["社内ネットワークのEDR/NDR", "UEBA導入", "セキュリティ運用の自動化・効率化", "セキュリティ委員会", "IT/OT資産管理・ガバナンス強化"]
    applicability_to_failure_surface: direct_but_scope_unknown
sources:
  - id: nttcom-incident
    resource: https://www.ntt.com/about-us/press-releases/news/article/2025/0305_2.html
    title: 当社への不正アクセスによる情報流出の可能性について
  - id: nttcom-sustainability-2024
    resource: https://www.ntt.com/content/dam/nttcom/hq/jp/about-us/csr/report/pdf/nttcom_sr2024.pdf
    title: NTTコミュニケーションズグループのサステナビリティ 2024
---

# 概要

2025年2月5日、NTTコミュニケーションズの情報セキュリティ部が、社内オーダ情報流通システム内の装置Aに対する通信で不審なログを検知した。同日、装置Aへの入口を制限し、翌6日には一部情報が流出した可能性を確認した。調査を続けた結果、2月15日に別の装置Bにも不正アクセスがあったことを特定し、同日ネットワークから遮断した。[^nttcom-incident]

本件は「検知できた／できなかった」の二値ではなく、最初の検知から侵害範囲全体の把握までに時間を要した事例として扱う。

# データ影響

流出した可能性があるのは17,891社の法人顧客に関する、契約番号、契約名義、担当者名、電話番号、メールアドレス、住所、サービス利用に係る情報等である。個人向けサービスの情報は対象外と公表された。2025年3月5日時点では情報の不正利用は確認されていなかった。[^nttcom-incident]

公開資料は「流出した可能性」であり、確認済み流出へ格上げしない。

# 即応性

装置Aでは検知当日にアクセス制限を実施している。一方、装置Bの不正アクセス特定と隔離は10日後だった。この10日を単純に「何もしていなかった期間」とは評価しない。装置Aと周辺システムの通信ログを解析し、影響範囲の調査を進めた結果として別装置の侵害が判明したためである。[^nttcom-incident]

重要なのは、初動の速さとは別に、**隣接システムを含む侵害範囲の確定速度**を測ることである。

# 事故前の公表統制との比較

Sustainability Report 2024では、2023年度の情報セキュリティ強化として、社内ネットワークの不正アクセス対策にEDR/NDRに加えてUEBAの導入を完了し、セキュリティオペレーションの自動化・効率化、セキュリティ委員会を通じたIT/OT資産管理・ガバナンス強化等を公表していた。2024年度KPIとして重大なサイバー攻撃・重大な情報漏えい0件を掲げていた。[^nttcom-sustainability-2024]

この事故だけから「EDR/NDR/UEBAが機能しなかった」とは断定できない。実際、最初の発見は不審ログの検知だった。しかし、事故前に監視統制を公表していた環境でも、侵害全体のスコープ確定には追加調査と時間が必要だった。

比較上確認したいのは、製品導入の有無ではなく、対象装置が各監視のカバレッジに含まれていたか、ログ保持が十分だったか、相関分析で隣接侵害をどれだけ早く特定できたかである。これらの詳細は公開されていない。

# 公表・通知と予後

2025年3月5日に対外公表し、影響を受けた可能性がある顧客へ営業担当または封書で順次連絡した。同社は再発防止のためセキュリティ対策と監視体制を強化するとした。[^nttcom-incident]

2026年10月5日の再確認で、本件について上記公表内容を大きく変更する後続一次公表は確認できなかった。これは「追加影響が存在しない」ことの証明ではなく、公開記録上の状態である。

# AI/LLMとの関係

本件にAI/LLMが利用されたことを示す公開証拠は確認していない。`era_context_only` とする。

# 防御上の教訓

- 最初のIOC・不審ログへの対応時間と、全侵害範囲を確定する時間を別々に測る。
- EDR/NDR/UEBAの導入状況だけでなく、資産カバレッジ、ログ保持、隣接システム相関の運用品質を確認する。
- 「重大インシデント0件」というKPIは、将来の侵害耐性や検知能力の証明ではない。
- 情報流出の可能性と確認済み流出を分離する。

[^nttcom-incident]: NTTコミュニケーションズ「当社への不正アクセスによる情報流出の可能性について」2025-03-05.
[^nttcom-sustainability-2024]: NTTコミュニケーションズ「NTTコミュニケーションズグループのサステナビリティ 2024」.
