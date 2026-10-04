---
type: Analysis Log
title: 2026 Japan major cyber incidents — patterns, realistic countermeasures and defense-budget model
description: Cross-incident analysis of the 42-report Denno Watch corpus, mapping observable attack patterns to realistic preventive/detective/recovery controls, maximum credible loss bands and risk-adjusted security-budget ranges.
tags: [analysis, japan, cybersecurity, controls, risk, budget, resilience, 2026]
status: draft
stale_after: 2027-01-01T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T08:43:00+09:00 }
sources:
  - id: denno-corpus
    resource: ../incidents/index.md
    title: Denno Watch 2026 incident corpus
    author: project:Denno-Watch
  - id: denno-audit
    resource: ../methodology/corpus-audit-2026-10-04.md
    title: 2026 major-incident corpus audit — 2026-10-04
    author: project:Denno-Watch
  - id: verizon-dbir-2026
    resource: https://www.verizon.com/business/resources/reports/dbir/
    title: Verizon 2026 Data Breach Investigations Report
    author: organization:Verizon
  - id: ibm-cost-2025-jp
    resource: https://jp.newsroom.ibm.com/2025-09-02-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications-97-of-which-reported-lacking-proper-ai-access-controls
    title: IBM 2025 Cost of a Data Breach — Japan release
    author: organization:IBM Japan
  - id: ians-budget-2025
    resource: https://www.ians.com/press/ians-research-and-artico-search-release-security-budget-benchmark-report
    title: 2025 Security Budget Benchmark Report
    author: organization:IANS Research and Artico Search
  - id: ipa-sme-2025
    resource: https://www.ipa.go.jp/pressrelease/2025/press20250527.html
    title: 2024年度 中小企業における情報セキュリティ対策に関する実態調査
    author: organization:IPA
  - id: askul-cost
    resource: https://www.lycorp.co.jp/en/ir/news/auto_20260204546714/pdfFile.pdf
    title: LY Corporation financial disclosure — ASKUL system failure response costs
    author: organization:LY Corporation
---

# Purpose and boundary

本ログは、Denno Watch に収録した2026年の日本企業・組織に関する42件の重大インシデントを横断し、**何が繰り返し起きているか、どの防御なら現実的に防止または被害縮小できたか、どの程度の予算を事前に積む合理性があったか**を整理する。

個別企業に対して「この金額を払えば必ず事故を防げた」と断定するものではない。公開情報では事故前のIT予算、人員、既存統制、契約単価、内部アーキテクチャが完全には分からないため、予算値は次の3つを分離する。

1. **全社セキュリティ予算ベースライン** — IT予算に対して通常確保すべき規模。
2. **control-gap closure budget** — 当該攻撃類型を現実的に抑止・検知・復旧するために追加投入する費用帯。
3. **maximum credible loss (MCL)** — 公開事例から見て、事故が悪化した場合に経営上想定すべき損失帯。実損の予測ではなく、予算決定用のストレスケースである。

# Executive synthesis

42件から最も強く見えるのは、「高度な未知技術だけが企業を破る」のではなく、**外部公開資産、認証、データ配置、委託先、復旧設計という基礎統制の穴が、脆弱性悪用・認証情報悪用・ランサムウェアと組み合わさって被害を巨大化している**ことである。

2026 DBIRでも、侵害の初期侵入として脆弱性悪用が世界全体で31%へ上昇し、APACでは42%、credential abuse は25%、third-party involvement は69%とされる。Denno Watch の日本事例でも、分析/BIツール、VPN、ネットワーク機器、SaaS、共有メール基盤、クラウド共有領域など「本体サービスの周辺」と考えられがちな場所が繰り返し入口またはblast radius増幅器になった。[^verizon-dbir-2026]

一方、被害を実際に小さくした統制も観測できる。データを保持していなかったこと、機能/データを別領域に分けていたこと、バックアップから即日復旧できたこと、クリーンネットワークを再構築したこと、代替チャネルで物流・配車・医薬品供給を維持したことなどである。つまり最も費用対効果が高いのは「侵入を100%防ぐ」発想ではなく、**侵入前提でblast radiusと復旧時間を縮める構造的投資**である。

# Observed recurring patterns

## 1. Internet-facing and adjacent-tool vulnerability exploitation

代表例: KDDI、LEAN BODY、VOISING、ApplyNow、メディア4u、OZmall 等。

特徴:

- 顧客向け本体だけでなく、BI/分析、メール基盤、管理画面、周辺ツールが侵入口になる。
- 既知脆弱性だけでなく、KDDIのようにベンダー未認知の脆弱性でも侵害は成立する。
- 2026 DBIRでは脆弱性悪用が初期侵入の最大カテゴリになっており、「月例パッチだけ」の運用では追いつかない。[^verizon-dbir-2026]

現実的な対抗策:

- internet-facing asset inventory / external attack-surface management を常時運用。
- KEV・実悪用情報・ベンダー緊急情報を監視し、公開系は**時間単位〜24時間単位の隔離判断**を可能にする。
- WAFだけで終わらず、API/管理画面/BIへのrate limit、行動異常検知、管理面のIP/identity制約を追加。
- 補助ツールも本番データ境界として扱い、patch owner とSLAを明示。
- 未知脆弱性用にEDR/NDR、egress監視、異常プロセス/通信、権限昇格検知を用意。

防止可能性: **中〜高**。既知脆弱性なら高い。ゼロデイは完全防止困難だが、露出縮小と挙動検知で滞留時間・取得量を抑えられる。

## 2. Credential / session / remote-access abuse

代表例: 両毛システムズのVPNアカウント、扶桑電通のクラウド認証情報、日本資産総研、イノベーションのGitHub資格情報、マルタケの不正作成アカウント等。

特徴:

- 「認証情報が悪用された」ことと「どう取得されたか」は別問題で、後者が不明な事故が多い。
- 単一資格情報がVPN、クラウド、GitHub、共有フォルダへの強い権限を持つと被害が直線的に拡大する。

現実的な対抗策:

- phishing-resistant MFA/FIDO2 を外部アクセス・管理者・クラウド共有へ優先導入。
- legacy authentication を廃止し、条件付きアクセス・端末準拠・地理/ASN/Impossible Travel等を組み合わせる。
- PAM/JIT/JEAで恒久管理者権限を削減。
- PAT/API key/tokenは短寿命・最小権限・自動rotation。コード/設定ファイル直書きを禁止。
- dormant/contractor/vendor account を定期自動失効。
- 認証成功後も大量列挙・異常ダウンロード・深夜アクセスを監視。

防止可能性: **高**。資格情報単独で侵入可能な構成は、MFA・権限制御・監視で大幅にリスク低下可能。

## 3. Ransomware + data theft + operational shutdown

少なくとも9件の収録事例でランサムウェアが明示され、Five Foxesは初報で疑いとして記録されている。代表例: 京王、REXT、CEC、両毛システムズ、ハンズ、フェース、日本資産総研、日本テレネット、マルタケ。

特徴:

- 暗号化だけでなく、事前探索・情報持ち出し・リークサイト公開が組み合わさる。
- 復旧後に機密性評価が悪化する。マルタケ、日本資産総研、REXT等では初期「未確認」から後続情報で外部公開が判明した。
- サーバーを戻すだけでは信頼回復にならず、日本テレネットのようなクリーンネットワーク再構築が強い回復策となる。

現実的な対抗策:

- EDR + 24/365 MDR/SOC、サーバー・端末・identityの相関監視。
- network segmentation と管理経路分離。バックアップ管理面を本番AD/SSOから切り離す。
- immutable/offline backup、復元演習、RTO/RPO測定。
- 管理者資格情報のtiering、LAPS/PAM、横展開に使われるプロトコル・共有を最小化。
- egress異常、圧縮/大量読出し、クラウドストレージ転送を検知。
- IR retainer と「全停止」「部分隔離」「クリーン再構築」の意思決定手順を事前契約。

防止可能性: **中**、被害縮小可能性: **非常に高い**。侵入自体を完全阻止できなくても、暗号化範囲・持出し量・停止期間は設計で大きく変わる。

## 4. Provider / SaaS / entrusted-data concentration

代表例: ApplyNow、KDDI、両毛システムズ、日本テレネット、メディア4u。

特徴:

- 侵害企業自身より、委託元・顧客側データが大きな母集団になる。
- 1プロバイダー侵害が複数ブランド・自治体・顧客企業へ同時波及する。
- 2026 DBIRでもthird-party involvementは全体48%、APACで69%と高い。[^verizon-dbir-2026]

現実的な対抗策:

- 受託データを customer/tenant 単位で論理・暗号鍵・権限・ログ上分離。
- 作業用コピー、移行用コピー、analytics copy にexpirationを設定。
- 契約終了時の削除証跡を委託元へ返す。
- ベンダー評価を質問票だけで終わらせず、MFA、EDR、backup isolation、log retention、incident SLA、subprocessorを証跡確認。
- 下流へ迅速に影響判定できるdata lineage / ownership mapを維持。

防止可能性: **中**、blast-radius縮小: **高**。

## 5. Analytics / BI as a hidden production boundary

代表例: LEAN BODY、ApplyNow、VOISING。

特徴:

- 顧客向けシステムが正常でも、内部分析環境から大量データが抜ける。
- 本番から派生したデータが分析用途で広く・長く・弱い管理下に置かれやすい。

現実的な対抗策:

- BIをproduction-class assetとしてpatch/SAST/secret/IAM監査対象にする。
- 分析DBへ生データを丸ごと複製せず、列削減・tokenize・pseudonymize。
- BIのInternet公開を避け、ZTNA/VPN + MFA + device trustへ限定。
- service accountの読み取り範囲をdataset/column単位へ縮小。
- query volume / export volume / unusual dashboard APIを監視。

防止可能性: **高**。

## 6. Business-logic / legitimate-looking mass query abuse

代表例: アフラック。

特徴:

- リクエスト形式は正規利用に見え、従来WAFや侵入テストを通過する。
- CPU高負荷や大量照会という**業務量の異常**が検知点になる。

現実的な対抗策:

- user/session/device単位の取得量上限、pagination cap、export privilege分離。
- IDOR/BOLAだけでなく「正規権限で何件まで取得できるか」をabuse caseとして脅威モデリング。
- per-account velocity、unique-object access count、深夜・長時間列挙をUEBAへ投入。
- high-value APIはstep-up authenticationとrisk scoringを適用。

防止可能性: **高**。機能要件にrate/volume boundaryを組み込めば大規模化をかなり抑えられる。

## 7. Destructive integrity attacks and database deletion

代表例: コープやまぐち、PeakManager、ランサムウェア群。

特徴:

- 「盗まれたか」だけでなく「消された・暗号化された」が同時に発生する。
- コープやまぐちはDB全削除から同日復旧したが、外部取得有無は別に未解決だった。

現実的な対抗策:

- DB production roleからbackup削除権限を分離。
- point-in-time recovery、immutable snapshot、cross-account/cross-subscription backup。
- deletion / truncate / mass updateを高重要イベントとして即時通知。
- restore testを四半期以上の頻度で実施し、RTO/RPOを実測。

防止可能性: 完全性破壊 **中**、事業停止の縮小 **非常に高い**。

## 8. Source-code / secrets / development-data leakage

代表例: イノベーション。

特徴:

- 認証情報管理不備と、個人情報をrepoに置いたデータ配置不備が重なって被害になった。
- secret scanningだけではPII混入は防げない。

現実的な対抗策:

- GitHub/OIDC等で短寿命tokenを使い、静的長寿命tokenを削減。
- secret scanning + push protection + repository data classification/DLP。
- production/customer dataをdevelopmentへ直接持ち込まない。synthetic/masked dataを標準化。
- org-level audit logをSIEMへ送り、token/repo clone/download異常を監視。

防止可能性: **高**。

## 9. Communications control-plane abuse

代表例: メディア4u。

特徴:

- エンドユーザーDBが大量流出しなくても、正規SMS送信権限を奪われるとフィッシング・詐欺の信頼チャネルとして悪用される。

現実的な対抗策:

- outbound message quota、template allowlist、high-risk URL/domain検査。
- 新規送信元・異常送信量・普段と異なる宛先分布でautomatic pause。
- 管理者操作と配信実行を別権限に分け、重要変更はstep-up MFA/4-eyes。
- emergency credential rotation と顧客単位kill switchを用意。

防止可能性: **高**。

## 10. Large-scale shared infrastructure / DNS / mail platform failures

代表例: JCOM、KDDI。

特徴:

- 単一基盤の障害・侵害が数百万〜千万単位の利用者へ波及する。
- availabilityとcredential compromiseの両方を考える必要がある。

現実的な対抗策:

- DNS anycast / multi-provider / capacity headroom / rate control。
- shared platformをtenant partitionし、credential store/keysを分離。
- failure domainを明示し、顧客ブランドごとの「見かけの分離」ではなく物理・論理依存関係を管理。
- platform-wide emergency credential rotation / notification pipelineを事前実装。

防止可能性: **中**、波及縮小: **高**。

## 11. Historical, dormant and unnecessary data accumulation

代表例: 第一生命、東京メトロ、ApplyNow、PeakManager、両毛システムズ、日本テレネット。

特徴:

- 退会者、過去応募者、休眠メール、旧作業コピーなど、現在サービスに不要なデータが被害母数を増幅する。

現実的な対抗策:

- retention scheduleをDB/backup/analytics/export/委託コピーまで実装。
- 「契約終了=削除済み」と見なさず、削除jobと証跡を監査。
- 年次で保有理由を再承認し、owner不明データを隔離・削除。

防止可能性: 侵入 **なし**、被害規模縮小 **非常に高い**。

## 12. Business continuity and service retirement

代表例: 日本トレクス、日本交通、マルタケ、ドットマネー/ドットギフト、ニチレイ。

特徴:

- ITが止まってもFAX、電話、別予約経路、仮サーバー、手作業で本業を維持できた例がある。
- DotGiftのように復旧せず廃止することも合理的な終端状態になり得る。

現実的な対抗策:

- critical business processごとに非IT/別系統 fallbackを設計。
- 年2回以上のtabletopと実運用切替演習。
- legacy serviceについて「復旧コスト > 残存価値」ならretirementへ移れる計画を事前作成。

# Defense budget model

## External benchmark

IANS / Artico Search の2025 benchmarkでは、security budget は平均で**IT spendの10.9%**。2024年の11.9%から低下し、十分なstaffingと回答したCISOは11%のみだった。[^ians-budget-2025]

IBMの2025日本調査では、データ侵害の平均コストは**5億5,000万円**。[^ibm-cost-2025-jp]

一方、ASKULのランサムウェア関連では、LY Corporationの開示上、2025年度第3四半期累計で**52.62億円**のシステム障害対応費が計上されている。これは調査・復旧だけでなく物流インフラ維持、復旧費、期限切れ商品の評価損等を含む。[^askul-cost]

したがって、数千万円〜数億円規模の予防投資は、重大事故の期待損失と比較して必ずしも過大ではない。

## Denno Watch risk-adjusted annual floor

以下は外部benchmarkそのものではなく、42件の日本事例を踏まえた**Denno Watchの予算モデル**である。

| Environment | Suggested annual security budget | Rationale |
| --- | ---: | --- |
| 一般的な企業IT | IT予算の10〜12% | IANS 10.9%を基準 |
| Internet-facing + 10万件超PII / SaaS / EC | IT予算の12〜15% | application abuse、data concentration、incident responseを上乗せ |
| 金融・通信・物流・医療供給・100万件超データ・multi-tenant provider | IT予算の15〜18% | 大規模下流波及と事業停止を前提 |
| breach後の2年間 / 大規模legacy是正期間 | IT予算の18〜22%も許容 | accumulated debt、clean rebuild、監視増強、人員補強の時限措置 |

この比率は「高いほど安全」という意味ではない。asset ownership、identity、patch、logging、restore testが回っていない組織では、製品購入を増やしても効果は低い。

### Example conversion

| Annual IT spend | 10.9% benchmark | High-risk 15% | Very-high-risk 18% |
| ---: | ---: | ---: | ---: |
| ¥200M | ¥21.8M | ¥30M | ¥36M |
| ¥500M | ¥54.5M | ¥75M | ¥90M |
| ¥1B | ¥109M | ¥150M | ¥180M |
| ¥5B | ¥545M | ¥750M | ¥900M |
| ¥10B | ¥1.09B | ¥1.50B | ¥1.80B |

## Incremental control-gap budget by attack method

以下は**中規模組織 / 大規模組織の年間または初年度オーダー**を示す。公開市場価格の見積書ではなく、人員・導入・運用を含む現実的な予算枠を置くためのモデル値である。

| Attack / failure mode | Core control bundle | Mid-size envelope | Large / critical envelope |
| --- | --- | ---: | ---: |
| Internet-facing vulnerability | EASM + VM + emergency patch + WAF/API controls | ¥10–40M/yr | ¥40–200M/yr |
| Credential / VPN / cloud abuse | SSO/MFA/FIDO2 + PAM/JIT + conditional access | ¥5–30M/yr | ¥30–150M/yr |
| Ransomware/system intrusion | EDR + MDR/SOC + segmentation + IR retainer | ¥30–120M/yr | ¥150–800M/yr |
| Immutable backup / clean recovery | isolated backup + restore drill + recovery environment | ¥10–50M initial, ¥5–30M/yr | ¥50–300M initial, ¥20–150M/yr |
| SaaS / entrusted-data blast radius | tenant isolation + TPRM + data lineage + deletion evidence | ¥5–30M/yr | ¥30–150M/yr |
| BI / analytics compromise | restricted access + patch + data minimization + export monitoring | ¥5–25M/yr | ¥20–100M/yr |
| API/business-logic scraping | API gateway + behavioral analytics + per-session limits | ¥5–30M/yr | ¥30–150M/yr |
| Dev/GitHub secrets and PII | secret scanning + OIDC + DLP + masked test data | ¥3–15M/yr | ¥15–80M/yr |
| Communication control-plane abuse | strong admin auth + send anomaly detection + kill switch | ¥5–20M/yr | ¥20–100M/yr |
| DNS/high-volume availability | managed authoritative DNS + DDoS protection + multi-provider | ¥5–30M/yr | ¥30–200M/yr |
| Data-retention reduction | inventory + deletion automation + archive governance | ¥5–20M/yr | ¥20–100M/yr |
| IR/tabletop/forensics readiness | retainer + twice-yearly exercise + legal/comms playbook | ¥3–15M/yr | ¥15–60M/yr |

# Maximum credible loss model

「最大被害」は件数だけでは決まらない。Denno Watchでは次の合計でストレステストする。

`MCL = business interruption + incident response/rebuild + customer remediation + fraud/abuse + downstream contractual exposure + regulatory/legal cost + lost inventory + churn/reputation + service retirement value`

42件と外部実例から、経営会議で最低限置くべきレンジは次の通り。

| Archetype | Maximum credible loss band | Main loss drivers |
| --- | ---: | --- |
| 限定的なWeb/クラウド侵害、停止小 | ¥0.1–1B | IR、通知、再構築、顧客対応 |
| 10万〜100万規模のPII/credential breach | ¥0.5–5B | 調査、通知、認証変更、fraud対策、churn |
| 100万〜数千万規模 / 高感度データ | ¥2–15B | 長期顧客保護、金融/ID悪用対策、ブランド毀損 |
| Ransomware + 数日〜数週の業務停止 | ¥3–30B+ | 売上/粗利停止、物流、復旧、在庫、再構築 |
| multi-tenant / supplier / shared infrastructure | 自社¥1–10B + downstream aggregate ¥10B超も想定 | 複数顧客同時波及、契約責任、通知・復旧並列化 |
| critical supply / finance / telecom / logistics | ¥5–30B+ | 社会的供給影響、代替運用、長期停止、規制対応 |
| service retirement | 残存サービス価値全額 + 顧客救済 | 復旧不能/非合理、残高・契約・移行負担 |

これらは実損認定ではない。IBMの日本平均5.5億円と、ASKULで観測された52.62億円の対応費の間に、重大事案が容易に数十億円級へ拡大し得る現実的な幅があることを予算判断へ反映するためのモデルである。[^ibm-cost-2025-jp][^askul-cost]

# What should have been funded first

予算が限られる場合、42件から見る優先順位は次の通り。

## Priority 0 — ¥10Mを新しい製品10個へ分散するより先に行う

1. 全Internet-facing assetとownerを確定。
2. 管理者・VPN・クラウド・GitHubへMFA/FIDO2。
3. EDR coverageをサーバーまで100%に近づけ、未導入資産を毎日可視化。
4. backupを本番identityから分離し、復元試験。
5. Critical/KEV patch emergency laneを作る。
6. 重要ログを90日以上オンライン、長期保管を別層に保持。
7. customer/employee/entrusted dataの保有場所と保持期限を可視化。

## Priority 1 — 侵入後の1時間を強くする

- 24/365 MDRまたはオンコール監視。
- kill switch: VPN、外部共有、SMS配信、API export、tenant単位停止。
- credential mass rotation手順。
- network isolationとclean-room recovery手順。
- 法務、広報、個人情報保護、顧客通知まで含むIR playbook。

## Priority 2 — blast radiusを構造的に縮める

- data minimization / retention deletion。
- tenant segmentation。
- analytics copy削減。
- privileged identityのJIT化。
- manual/alternate business process。

# Budget allocation recommendation

全社security budgetを100とした場合、Denno Watchの事例群からは次の配分が妥当な出発点となる。

| Area | Suggested share |
| --- | ---: |
| Security staff / SecOps / IR capability | 25–30% |
| Identity / endpoint / detection & response | 20–25% |
| Vulnerability / application / cloud security | 15–20% |
| Resilience / backup / recovery / segmentation | 15–20% |
| Data governance / DLP / retention | 5–10% |
| Third-party risk / assurance | 5–8% |
| Exercises / training / external IR retainer | 3–7% |

IANSではsecurity softwareが平均security budgetの約30%を占めるとされる。ツール費だけが膨らみ、staffing・運用・復元演習が不足しないようにする必要がある。[^ians-budget-2025]

# Control-to-incident mapping examples

| Incident pattern | Most relevant missing/valuable controls |
| --- | --- |
| LEAN BODY / VOISING / ApplyNow | BI patch ownership、private access、data minimization、export anomaly detection |
| 両毛システムズ / 扶桑電通 | phishing-resistant MFA、PAM、vendor account lifecycle、post-auth anomaly detection |
| 日本テレネット / マルタケ / CEC / 京王 | EDR/MDR、segmentation、immutable backup、clean rebuild、IR retainer |
| アフラック | business-logic abuse detection、query volume cap、risk-based step-up auth |
| KDDI | zero-day-ready detection、shared-platform segmentation、rapid credential reset across downstream providers |
| コープやまぐち | immutable PITR backup、DB destructive-action alert、data minimization |
| メディア4u | send-control plane MFA、quota/anomaly detection、per-customer kill switch |
| イノベーション | short-lived credentials、secret scanning、PII-in-repo prevention、synthetic test data |
| 東京メトロ / 第一生命 | retention reduction and dormant-data deletion |
| ドットマネー / ドットギフト | secure rebuild + business decision gate for restore vs retirement |

# The strongest finding

最大の共通点は、**侵入口そのものより「1回入られた後にどこまで行ける設計だったか」が最終被害を決めている**ことにある。

- MFAがあれば資格情報単独侵入を止められる。
- tenant/data separationがあれば1侵害で数社・数百万人へ広がりにくい。
- retentionを削れば盗まれる母数そのものが減る。
- rate limitがあれば正規操作に見える大量取得を止められる。
- immutable backupがあれば削除・暗号化から戻れる。
- clean rebuildがあれば侵害済み環境を信用せず復旧できる。
- alternate operationsがあれば物流・交通・医薬品供給を維持できる。

したがって、防衛予算の中心は「最新の検知製品」だけではなく、**identity、segmentation、data minimization、patch velocity、observability、recovery engineering、business continuity**へ置くべきである。

# Budget decision rule

経営判断では次のルールを推奨する。

1. 年間security budgetがIT予算の10%未満なら、例外理由を明文化する。
2. 100万件超の個人/認証データ、multi-tenant SaaS、通信、金融、物流、医薬品供給を扱うなら15%前後を開始点にする。
3. 予防controlへの追加投資が、想定MCLの**5〜15%以下**なら原則として優先検討する。
4. 同じ事故類型が同業他社で公開された時点で、翌年度予算ではなく**緊急是正予算**を使える仕組みにする。
5. 防御費は「侵入確率低減」だけでなく「停止時間・漏えい母数・下流件数を減らす投資」としてROI評価する。

# Limits

- Denno Watch corpusは重大事案を意図的に選んでおり、日本企業全体の無作為標本ではない。
- 企業別の実IT予算・既存control費用が非公開なため、本ログの予算額は個別企業の適正額を確定するものではない。
- MCLは公開事例と経営ストレステスト用のレンジであり、会計上の損失予測ではない。
- 事故原因が未公表のケースでは、対策は原因断定ではなく観測されたfailure modeへ対応する。

[^verizon-dbir-2026]: Verizon, 2026 Data Breach Investigations Report. 2026年版では脆弱性悪用が世界全体の初期侵入31%。APAC summaryでは脆弱性悪用42%、credential abuse 25%、third-party involvement 69%、human element 71%と報告。
[^ibm-cost-2025-jp]: 日本IBM「2025年データ侵害のコストに関する調査レポート」日本語版、2025-09-02。日本の平均侵害コスト5億5,000万円。
[^ians-budget-2025]: IANS Research / Artico Search, 2025 Security Budget Benchmark Report. Security budget平均はIT spendの10.9%、security softwareは別調査でsecurity budgetのおよそ30%を占める。
[^ipa-sme-2025]: IPA「2024年度 中小企業における情報セキュリティ対策に関する実態調査」。対策実施企業ではインシデント被害低減が観測され、サプライチェーン対策の重要性を指摘。
[^askul-cost]: LY Corporation, FY2026 Q3 disclosure. ASKULランサムウェアに関連するsystem failure response costsとして累計5,262百万円を計上。
