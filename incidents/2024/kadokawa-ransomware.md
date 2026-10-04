---
type: Cybersecurity Incident
title: KADOKAWA / ドワンゴ — 2024年ランサムウェア攻撃と大規模事業停止
description: 2024年6月8日にグループデータセンターがランサムウェアを含む攻撃を受け、ニコニコ、社内業務、出版等へ波及。情報漏えいと財務影響まで追跡する。
resource: https://group.kadokawa.co.jp/system_failure/
tags: [japan, media, ransomware, private-cloud, outage, data-leak, financial-impact, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: KADOKAWAグループ / 株式会社ドワンゴ
  sector: media-publishing-internet-education
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: ransomware and data exfiltration
  earliest_known_activity: "2024-06-08 03:30 JST"
  detected_at: "2024-06-08 03:30 JST"
  incident_known_at: "2024-06-08 08:00 JST"
  first_disclosed_at: "2024-06-08"
  latest_public_update: "2025-05-08"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "group data center/private cloud, Niconico and other web services, internal business systems, publishing operations"
  data_exposure: confirmed
  availability_impact: "large-scale web-service and business-system outage with publishing and payment effects"
  restoration_state: "major services and business functions restored; financial impact reflected in FY2025 results"
  market_disclosure: "multiple IR disclosures and financial-result impact"
  ai_relation: era_context_only
sources:
  - id: dwango-jun14
    resource: https://group.kadokawa.co.jp/information/media-download/1360/73b7af68478b8a51/
    title: 当社サービスへのサイバー攻撃に関するご報告とお詫び
  - id: kadokawa-leak
    resource: https://group.kadokawa.co.jp/information/media-download/1356/d3f77b589c58d083/
    title: ランサムウェア攻撃による情報漏洩に関するお知らせ
  - id: system-failure
    resource: https://group.kadokawa.co.jp/system_failure/
    title: システム障害関連
  - id: fy2025
    resource: https://group.kadokawa.co.jp/information/promotional_topics/article-12287.html
    title: KADOKAWA、2025年3月期 通期決算を発表
---

# 概要

2024年6月8日3時30分頃、KADOKAWAグループの複数システムと「ニコニコ」等で障害が発生し、8時頃までにランサムウェアを含むサイバー攻撃と確認された。グループ企業のデータセンター内プライベートクラウドで相当数の仮想マシンが暗号化され、Webサービス、社内業務、出版、取引先支払等へ影響が波及した。[^dwango-jun14]

# 即応と攻撃継続性

攻撃確認後、関連サーバーをシャットダウンし、データセンター内通信を切断、社内ネットワークの一部利用も停止した。特徴的なのは、遠隔シャットダウン後も攻撃者がサーバーを遠隔起動し感染拡大を図る挙動が観測されたことである。単純な「電源断」で侵害を止め切れない管理面の支配を示した。[^dwango-jun14]

6月9日に警察・外部専門機関へ連絡、10日に個人情報保護委員会へ初報、12日に関東財務局へ障害報告を行っている。

# 情報漏えい

6月末以降、攻撃者を称する者がデータを公開し、KADOKAWA/ドワンゴは漏えい情報の調査、拡散抑止、法的措置を進めた。8月5日の公表では、ランサムウェア攻撃に起因する情報漏えいについて対象を整理した。[^kadokawa-leak]

公開データには従業員、取引先、クリエイター、学校関係者等の情報が含まれ、単なるニコニコ利用者のサービス停止より広いグループ影響となった。

# 事業継続と復旧

出版では受発注・製造・物流を代替手段や人手で継続し、Webサービスは段階復旧した。ニコニコは2024年8月5日に新環境で再開した。KADOKAWAは事故専用ページで初報から復旧、漏えい、犯行声明対応まで時系列を保持している。[^system-failure]

# 株主・財務への長期影響

2025年3月期決算で、Webサービス部門はサイバー攻撃により売上高約39.5億円、営業利益約21億円のマイナス影響を受け、グループ全体ではサイバー攻撃関連の特別損失24億円を計上した。[^fy2025]

このため本件は、技術復旧から翌年度の損益まで追える基準例である。

# 事故前公表との比較

KADOKAWAは情報セキュリティポリシー等を公開していたが、事故前の具体的なプライベートクラウドの耐障害性・管理面分離がどこまで実装されていたかを公開資料だけで断定できない。事故後説明を事故前統制の証拠へ遡及利用しない。

# 防御上の教訓

- private cloud/仮想化管理面を侵害された場合、ゲスト単位の復旧だけでなく管理プレーンの信頼再確立が必要。
- 遠隔再起動等の攻撃継続を想定し、ネットワーク遮断と物理/管理経路の封じ込めを組み合わせる。
- 大規模業務停止では手作業・代替経路による事業継続能力を技術復旧とは別に記録する。
- 技術費用だけでなく売上・利益・特別損失まで追跡する。
- AI/LLM利用の公開証拠はない。

[^dwango-jun14]: ドワンゴ「当社サービスへのサイバー攻撃に関するご報告とお詫び」2024-06-14.
[^kadokawa-leak]: KADOKAWA「ランサムウェア攻撃による情報漏洩に関するお知らせ」2024-08-05.
[^system-failure]: KADOKAWAグループ「システム障害関連」.
[^fy2025]: KADOKAWA「2025年3月期 通期決算を発表」2025-05-08.