---
type: Cybersecurity Incident
title: Snowflake顧客アカウント侵害 — 窃取認証情報とMFA未適用が多数組織へ波及した2024年キャンペーン
summary: 2024年、UNC5537が過去に窃取された顧客側認証情報を使って複数のSnowflake顧客インスタンスへ侵入し、データ窃取と恐喝を行った。提供基盤自体の侵害が確認されないまま、共有責任、委託先端末、長寿命資格情報、集中SaaSの法的・評判リスクが顕在化した比較ケース。
resource: https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
tags: [international, global, saas, credential-theft, infostealer, identity, shared-responsibility, 2024]
status: draft
stale_after: 2027-01-04T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T13:08:00+09:00 }
comparative_case: true
included_in_japan_corpus: false
incident:
  organization: Snowflake customer organizations / Snowflake Inc.
  sector: cloud-data-platform
  jurisdiction: global
  incident_status: long_tail_monitoring
  attack_type: credential-abuse-data-theft-and-extortion
  earliest_known_activity: "2024-04"
  detected_at: varies-by-customer
  first_disclosed_at: "2024-05"
  latest_public_update: "2026-09-04"
  public_record_checked_at: "2026-10-04T13:08:00+09:00"
  intrusion_vector: "stolen customer credentials, commonly originating from historical infostealer infections"
  affected_services: "customer Snowflake database instances"
  data_exposure: confirmed-across-multiple-customers
  availability_impact: not_primary
  restoration_state: "customer-specific containment completed in many cases; litigation, regulatory and reputational tail remained in 2026"
  secondary_abuse: "extortion and attempted sale of stolen customer data were observed"
sources:
  - id: mandiant
    resource: https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
    title: UNC5537 Targets Snowflake Customer Instances for Data Theft and Extortion
  - id: snowflake-2026q2
    resource: https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm
    title: Snowflake Form 10-Q for quarter ended 2026-07-31, filed 2026-09-04
  - id: snowflake-filing-index
    resource: https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/0001640147-26-000037-index.htm
    title: Snowflake 2026-09-04 filing index
---

# 概要

2024年、MandiantがUNC5537として追跡する攻撃者は、複数組織のSnowflake顧客インスタンスへ不正アクセスし、データを窃取して恐喝や犯罪フォーラム上での販売を試みた。Mandiantが対応した事例では、Snowflakeの企業環境そのものの侵害ではなく、**顧客側の窃取済み認証情報**が初期侵入原因だった。[^mandiant]

被害を大きくした主因は、MFA未適用、長期間ローテーションされていない認証情報、接続元を限定するネットワーク許可リストの未使用である。MandiantとSnowflakeは約165組織へ潜在的な露出を通知した。[^mandiant]

本件の比較価値は、SaaS提供事業者の基盤自体が侵害されていなくても、顧客の認証設計、委託先端末、共有責任モデル、データ集中によって、多数組織の事故が同じサービス名の下で同時に発生し得る点にある。

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2020-11以降 | 後に攻撃へ使われた資格情報の一部について、情報窃取型マルウェアによる過去の露出が確認された。最古の関連感染は2020年11月まで遡る。[^mandiant] |
| 2024-04 | Mandiantが、後に被害組織のSnowflakeインスタンス由来と判明するデータに関する脅威情報を取得し、調査を開始。[^mandiant] |
| 2024-05-22 | Mandiantがより広いキャンペーンを認識しSnowflakeへ連絡、潜在的被害組織への通知を開始。[^mandiant] |
| 2024-05-30 | Snowflakeが検知・堅牢化ガイダンスを顧客へ公開。[^mandiant] |
| 2024-06-10 | MandiantがUNC5537キャンペーンの詳細を公開。約165組織へ潜在的露出を通知済みと説明。[^mandiant] |
| 2024-10-04 | 米国の関連集団訴訟がMontana地区の多地区訴訟へ統合されたことをSnowflakeが後続開示。 |
| 2025-2026 | 消費者・金融機関原告による訴訟、カナダの集団訴訟、規制当局調査、議会関係者からの照会が継続。 |
| 2026-09-04 | Snowflakeの10-Qで、顧客アカウント侵害に関連する多数の訴訟、規制調査、議会照会、評判・顧客喪失・保険回収リスクを継続開示。[^snowflake-2026q2][^snowflake-filing-index] |

# 技術的に確認できた事項

Mandiantは、対応した全事例でSnowflake顧客の侵害原因を窃取済み認証情報へ遡った。[^mandiant]

少なくとも次の条件が繰り返し確認された。

- 影響アカウントでMFAが有効化されていなかった。
- 情報窃取型マルウェアに出力された認証情報が、窃取から数年後も有効なまま残っていた。
- 被害インスタンスで信頼済み接続元だけに限定するネットワーク許可リストが使われていなかった。
- MandiantとSnowflakeの分析では、攻撃者が使ったアカウントの少なくとも79.7%で過去の認証情報露出が確認された。[^mandiant]

またMandiantは、一部調査で、個人利用にも使われた委託先端末が情報窃取型マルウェアへ感染していたことを確認している。同じ委託先端末から複数組織のSnowflake環境へアクセスできる場合、一台の感染が複数顧客へ波及し得る。[^mandiant]

# 影響

## データ窃取と恐喝

UNC5537は、侵害した顧客インスタンスから大量のデータを取得し、被害組織への恐喝や犯罪フォーラムでの販売を行った。[^mandiant]

これは主に機密性の事故であり、サービス停止が中心ではない。したがって「可用性に影響がなかった」ことを低リスクと解釈してはならない。

## 集中SaaSの評判・法的波及

Snowflakeは2026年の10-Qで、自社システムの脆弱性・設定不備・企業環境侵害に起因する証拠を確認していないとしつつ、顧客事案に関連して多数の訴訟、規制調査、議会関係者からの照会を受けていると開示している。[^snowflake-2026q2]

さらに、事故原因についての誤認も含む否定的な評判、顧客喪失、顧客からの請求、保険で損失を完全に回収できない可能性をリスクとしている。[^snowflake-2026q2]

これは、**技術的な侵害責任と、集中サービス事業者として負う法務・評判・顧客支援上の負担が一致しない**ことを示す。

# 対応と復旧

MandiantとSnowflakeは潜在的な被害組織への通知、共同調査、検知・堅牢化ガイダンスの公開を行った。[^mandiant]

個々の顧客では、認証情報の失効、MFA導入、ネットワーク制約、ログ調査、流出データの特定が必要となる。提供事業者だけが一括して「復旧」できる事故ではなく、**各顧客テナントが独立したインシデント対応主体**になる。

# 現在の状況と予後

2026年9月4日提出のSnowflake 10-Qでも、米国の多地区訴訟、カナダの集団訴訟、規制・議会照会、評判リスクが継続している。[^snowflake-2026q2]

技術的なキャンペーンが2024年に発覚した後も、法的・規制・評判面の予後は2年以上続いている。

# 防御上の教訓

- **MFAを顧客任意設定にしない重要性。** 高価値データ基盤では、MFA未設定アカウントを例外として可視化し、可能なら強制する。
- **長寿命認証情報を廃止する。** パスワードやトークンは、盗まれてから数年後でも使える状態を作らない。
- **認証情報漏えい監視と利用制限を組み合わせる。** 漏えい監視だけでなく、FIDO2等の強い認証、端末信頼、接続元制限、短寿命トークンを使う。
- **委託先端末を顧客境界として扱う。** 一台の委託先PCから複数顧客へ管理接続できる構造は、集中リスクとして棚卸しする。
- **SaaS内の大量取得を業務ロジックとして監視する。** 正常認証後でも、異常な列挙・読み出し・エクスポートを検知する。
- **共有責任モデルを責任分界表だけで終わらせない。** 危険な顧客設定を提供側がどこまで強制・警告・監視するかまで評価する。

# 日本の事例へ読み替える際の注意

本件はSnowflake自体の基盤侵害と確認された事故ではない。日本のSaaS・クラウド事故へ適用する際も、「提供事業者が侵害された」「顧客テナントだけが侵害された」「委託先端末が入口だった」を分離する。

国内のApplyNow、BI基盤侵害、GitHub認証情報、クラウドストレージ認証情報悪用等を評価する際に、**認証情報の寿命、MFA、接続元制約、委託先端末、集中データ**という比較軸が有用である。

# 不明点・未公表事項

- 約165組織は潜在的露出通知の規模であり、すべてが同一水準の侵害・流出を受けたことを意味しない。
- 各顧客の最終的な流出件数や二次被害は顧客ごとに異なる。
- Snowflakeと各顧客の法的責任は訴訟・規制手続の結果と分離して扱う。

[^mandiant]: Mandiant, “UNC5537 Targets Snowflake Customer Instances for Data Theft and Extortion,” 2024-06-10, updated 2024-06-17.
[^snowflake-2026q2]: Snowflake Inc., Form 10-Q for quarter ended 2026-07-31. 顧客アカウント侵害に関する訴訟、規制調査、議会照会、評判・保険リスクを継続開示。
[^snowflake-filing-index]: SEC EDGAR, Snowflake Form 10-Q filing detail, filed 2026-09-04.
