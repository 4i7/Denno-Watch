---
type: Executive Threat Analysis
title: AIで攻撃コストが崩れた時代の企業サイバーリスク — 経営層と情報システム部門のための調査報告
summary: 前半を非専門家向け約2ページの経営サマリー、後半を経営・情シス・セキュリティ部門向けの詳細調査として構成し、日本の重大インシデント、AIによる攻撃経済性の変化、本人確認書類流出の長期リスク、業種別最大被害、現実的な多層防御を整理する。
tags: [executive, ai, cyber-risk, japan, defense, resilience, economics, automation, local-ai, identity, 2026]
status: draft
stale_after: 2027-01-01T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T10:20:00+09:00 }
sources:
  - id: denno-corpus
    resource: ../incidents/index.md
    title: Denno Watch 2026 incident corpus — 42 reports
    author: project:Denno-Watch
  - id: denno-audit
    resource: ../methodology/corpus-audit-2026-10-04.md
    title: 2026 major-incident corpus audit
    author: project:Denno-Watch
  - id: denno-budget
    resource: incident-defense-budget-analysis-2026-10-04.md
    title: Patterns, realistic countermeasures and defense-budget model
    author: project:Denno-Watch
  - id: denno-sector
    resource: sector-worst-case-impact-matrix-2026-10-04.md
    title: 全業種サイバー侵害・最大被害ストレスマトリクス
    author: project:Denno-Watch
  - id: denno-evidence
    resource: evidence-ledger-ai-cyber-risk-2026-10-04.md
    title: AI時代の企業サイバーリスク — 根拠資料台帳
    author: project:Denno-Watch
  - id: ipa-2026
    resource: https://www.ipa.go.jp/security/10threats/10threats2026.html
    title: 情報セキュリティ10大脅威 2026
    author: organization:IPA
  - id: microsoft-mddr
    resource: https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
    title: 2026 Digital Defense Report
    author: organization:Microsoft
  - id: google-gtig
    resource: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai
    title: GTIG AI Threat Tracker — From Prompting to Autonomy
    author: organization:Google Threat Intelligence Group
  - id: anthropic-navigator
    resource: https://www.anthropic.com/research/attack-navigator
    title: Mapping AI-enabled cyber threats
    author: organization:Anthropic
  - id: verizon-dbir
    resource: https://www.verizon.com/business/ja-jp/resources/reports/dbir/
    title: 2026 Data Breach Investigations Report
    author: organization:Verizon
  - id: ibm-2026
    resource: https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled%2C-costing-companies-6-million-on-average
    title: Cost of a Data Breach 2026
    author: organization:IBM
  - id: mistral-offline
    resource: https://docs.mistral.ai/vibe/code/cli/offline-models
    title: Using offline models
    author: organization:Mistral AI
  - id: times-third
    resource: https://www.park24.co.jp/news/2026/09/20260929-1.html
    title: タイムズカーWebシステムへの不正アクセスに関する調査結果および今後の対応について（第3報）
    author: organization:Park24
---

# PART I — 約2ページで把握する経営サマリー

## まず知ってほしいこと

企業が直面している変化は、突然まったく新しい種類の攻撃が生まれたことではない。

これまでにも、パスワードの窃取、古いシステムの弱点、委託先からの侵入、身代金要求型の攻撃、顧客データの持ち出し、偽メールやなりすましは存在した。

変わったのは、**それらを探し、試し、失敗を整理し、次の候補へ移り、得られた情報を分析するために必要だった「人間の時間」が急速に安くなっていること**である。

AIは、調査、文章作成、翻訳、コード作成の補助、大量情報の整理、優先順位付け、長時間の監視などを高速に処理できる。攻撃者が全工程をAIだけに任せられるわけではないが、機械に任せやすい仕事を24時間365日続け、人間は重要な判断だけを行う形が現実になりつつある。

その結果、企業側は「自社が有名だから狙われる」「一度防げば相手は諦める」「攻撃者も平日の日中に人手で調査している」といった前提を置けなくなった。

**攻撃側は、1000社を浅く調べて1社の弱点を見つければよい。防御側は、自社の全ての入口を毎日守らなければならない。**

この非対称性が、AIによってさらに大きくなっている。

## 高性能なAIを使うために巨大設備を所有する必要もない

高性能なAIは、大規模な計算設備を自社で建設しなくても、外部の計算資源やAIサービスを必要な時間だけ借りられる。

もう一つの経路もある。十分な性能のGPU等を一度確保すれば、公開・配布されている高性能モデルを自己管理環境で動かすことができる。公式ドキュメントでも、高性能なコード・agent用途のmodelを一般に入手可能なGPU級でlocal実行し、外部通信を切ったoffline運用が可能な例が示されている。[^mistral]

したがって、防御側は「危険な命令ならAI会社が拒否する」「大量に使えば利用上限で止まる」「異常ならaccountが停止される」ことを、自社の防衛策として期待してはいけない。

攻撃者の能力を判断するときに見るべきなのは、相手が巨大なdata centerを所有しているかではない。**どれだけの計算資源、人員、自動化、時間を組み合わせられるか**である。

## 小さな費用でも、人間一人の処理量はすでに大きく増幅できる

実利用の一例として、月数千円規模のAI利用料で、単独の開発者がGitHub上で15万行を超える規模の開発を扱えたケースがある。

コードの行数は品質や攻撃能力そのものを示す尺度ではない。しかし、従来は複数人の時間を必要とした調査、設計、実装、修正、レビュー、文書化を、一人で大規模に処理できるようになったという点は重要である。

ここから企業が考えるべき問いは単純である。

> **月数千円でも一人の知識労働を大きく増幅できるなら、悪意ある複数人が数百万円、数千万円という資金を投じ、外部の高性能計算資源、自己管理AI、多数の実行環境、24時間365日の自動化を組み合わせた場合、従来の攻撃者像のままで十分か。**

これは「AIなら何でも侵入できる」という意味ではない。むしろ逆である。**今まで放置されていた普通の弱点を、より多く、より速く、より粘り強く探される**と考えるべきである。

## 日本では、すでに「一度の侵害で数百万人」が珍しくない

Denno Watchが2026年の公開情報から整理した42件には、数百万から数千万record規模の情報影響、身代金要求型攻撃、物流・交通・小売・医療に近い業務停止、委託先から複数企業へ広がる被害が含まれる。[42件のincident corpus](../incidents/index.md)

代表例だけでも、次の規模が確認されている。

- タイムズカー: 約660万accountの情報取得。うち約160万accountで運転免許証画像等の本人確認書類が漏えい。[^times]
- EPARK / PeakManager: 約2,218万recordsの外部転送を確認。
- Helpfeel / Gyazo: 2,000万を超えるuser規模の情報影響。
- KDDIの共有mail基盤: 約1,223万mail addressと約762万passwordが影響。
- ムラウチドットコム: 約771万customer records。

金額だけを見ても、大規模ランサムウェア事案では、ASKULのsystem outage対応費としてLY Corporationが**52.62億円**を計上している。これは最終的な全損失ではなく、物流設備維持、調査・復旧、期限切れ商品損失等を含む特定費用項目である。[^askul]

また、過去の国内事例では、大阪急性期・総合医療センターがランサムウェア被害後、基幹system再稼働まで43日、全体の診療system復旧まで73日を要し、調査・復旧費用は数億円以上、診療制限に伴う逸失利益は十数億円以上と見込んだ。[^osaka]

名古屋港ではランサムウェアにより全container terminalの作業が停止した。これは、IT障害が画面上の問題ではなく、**物理物流、診療、製造、交通、社会機能の停止に変わる**ことを示す。[^nagoya]

## タイムズカーの160万件は「パスワード流出」と同じ種類の問題ではない

2026年9月29日、Park24は、タイムズカーの約160万accountで本人確認書類が漏えいしたと公表した。対象には運転免許証画像、現住所確認書類、学生証、家族確認書類が含まれる。[^times]

ここで重要なのは、本人確認書類はpasswordのように単純に変更できる情報ではないことである。氏名、生年月日、顔、住所等の組合せは長期に本人と結び付く。

一方、**2026年10月4日時点で、Times Carから漏えいした情報を使った不正loan、不正credit契約等が実際に発生したという一次公表は確認できない。** 「160万人の信用情報がすでに毀損した」と書くことは事実を超える。

しかし、リスクが抽象的なものでもない。

JICCは、運転免許証画像等が流出し現物が手元にある場合でも「名義の悪用防止」の本人申告を登録できるとしている。全国銀行個人信用情報センターも、本人確認書類の漏えいにより名義冒用のおそれがある場合、本人申告情報を金融機関の与信判断の参考にできるとしている。CICにも同種の制度がある。[^jicc][^ksc][^cic]

そしてPark24の第3報直後、JICCでは本人申告・本人開示の申込みが集中し、2026年10月1日にsmartphone app受付を一時休止した。CICも9月30日、本人申告や信用情報開示の受付番号、call centerへの申込み・問い合わせが通常より増え、つながりにくい状態を公表した。各機関は原因をTimes Carと断定していないため因果関係は断定できないが、**本人確認情報流出後に信用取引上の自己防衛行動が大規模に発生していること自体は確認できる。**[^jicc-load][^cic-load]

本人確認書類が悪用されれば、条件次第で名義を使ったcredit/loan申込み、通信契約、account recovery、より精密なphishing等へ利用される可能性がある。警察庁も、偽造本人確認書類や本人になりすました契約により不正取得された携帯電話が特殊詐欺等へ悪用される事例を記録している。[^npa]

ただし、現代の本人確認には顔照合、liveness、IC、既登録電話番号、追加認証、不正検知等もあるため、**画像を持つだけであらゆる契約が成立するわけではない。**

経営上の教訓は、本人確認書類を「普通の個人情報」と同じ保存期間・同じ場所・同じ権限で扱わないことである。

## 経営層が今すぐ確認すべき7項目

専門製品名を知らなくても、次の7問に答えられればよい。

1. **自社がInternetへ公開しているsystemを、今この瞬間に全部列挙できるか。**
2. **管理者、VPN、cloud、開発環境へpasswordだけで入れる場所が残っていないか。**
3. **重大な弱点が今日見つかった場合、夜中でも1日以内に塞ぐか外部から切り離せるか。**
4. **正しいaccountを盗まれた場合でも、数十万件を一気に読む・送る・変更する異常を止められるか。**
5. **本当に必要な期間を超えて、本人確認画像、退会者情報、元従業員情報、古いexportを保存していないか。**
6. **全serverやdatabaseを破壊されても、攻撃者が触れた認証情報を使わずにbackupから戻せるか。実際に復旧試験をしたか。**
7. **夜間・休日、委託先の事故を含めて、誰が止める権限を持っているか。**

一つでも答えられない場合、問題は「AIそのもの」ではない。**AIによって繰り返し探されやすくなった既存の管理不備**である。

---

# PART II — 経営・情シス・セキュリティ部門向け詳細調査

# 1. 調査範囲と読み方

本報告は、Denno Watchの2026年日本重大incident 42件、被害企業・公的機関の一次公表、Microsoft、Google Threat Intelligence Group、Anthropic、Verizon、IBM、IPA等の2026年脅威資料を横断している。

強い警告を出す一方、次を混同しない。

- `confirmed`: 被害組織、公的機関、調査主体が確認した事実。
- `supported inference`: 確認事実から合理的に導けるが、その事件で発生確認されていない二次risk。
- `stress scenario`: 経営上の備えとして想定する最大被害。
- `unknown`: 公開情報では分からないこと。

根拠のclaim-by-claim対応は[根拠資料台帳](evidence-ledger-ai-cyber-risk-2026-10-04.md)、全業種の最大被害は[全業種最大被害ストレスマトリクス](sector-worst-case-impact-matrix-2026-10-04.md)に分離した。

# 2. AIが変えたのは「攻撃の目的」ではなく「経済性」

攻撃者の目的は大きく変わっていない。侵入、情報窃取、金銭詐取、恐喝、諜報、妨害である。

変化しているのは、そのために必要なexpert timeである。

Microsoftは2026 Digital Defense Reportで、AIがvulnerability discovery、reconnaissance、phishing、malware/exploit development、data analysis、post-compromise activityに利用され、attack speed、scale、consistencyを高めていると報告した。また、実環境でのvulnerability discoveryからweaponizationまでのmedianが24時間を大きく下回るとする。[^microsoft]

GTIGは2026年Q2、侵害したcloud resourceからagent-enabled mass credential-harvesting campaignを6時間未満で計画、構築、実行した活動を観測した。[^google]

Anthropicは2025年3月から2026年3月までの悪用accountのうち詳細を分析できた832件について、13,873 actions、MITRE ATT&CK全14 tactics、482 techniques/sub-techniquesにAI利用をmapした。中risk以上のactor比率は研究期間前半33%から後半56%へ増えた。ただし、この832件はAnthropicが調査・停止したaccountのsubsetで、全攻撃者の母集団ではない。[^anthropic]

Verizon 2026 DBIRでは、software vulnerability exploitationがbreachの31%で侵入経路となり、stolen credentialsを上回る主要vectorになった。[^verizon]

日本でもIPA「情報セキュリティ10大脅威 2026」は、組織向け1位をランサム、2位をサプライチェーン・委託先、3位を初選出の「AIの利用をめぐるサイバーリスク」、4位を脆弱性悪用としている。[^ipa]

これらを合わせると、企業にとって重要なのは「AIだけの新攻撃」を探すことではない。

**既存の入口が、以前より高速・大量・長時間に探索される世界へ防御速度を合わせること**である。

# 3. 攻撃者の計算資源を「所有設備」で評価してはいけない

## 3.1 外部の超高性能計算資源を借りる

高性能GPU、cloud inference、AI API等は、設備を購入せず必要な時間だけ利用できる。

これにより、攻撃者の見た目の規模と利用可能な計算能力は一致しない。小規模なgroupでも、短時間だけ大きな計算能力を利用できる。

## 3.2 高性能AIを自己管理環境へ置く

open-weight modelは自己管理環境でlocal inferenceできる。Mistralのofficial documentationは、agentic/code task向け24B modelについて、24GB VRAM GPUを含むlocal deployment例を示し、fully offline運用も説明している。[^mistral]

Metaもdownloaded Llamaについて、利用者が入力・出力をMetaへ送らない限り、Meta側はそれらへアクセスしないとFAQで説明している。[^meta]

これは特定providerの問題ではない。一般論として、自己管理modelではexternal providerのcentral moderation、API refusal、quota、account suspension、usage monitoringを防御側が期待できない。

ローカル環境は無限ではない。GPU throughput、memory、電力、冷却、故障、network等の制約がある。しかしhardware取得後は、処理ごとのAPI料金ではなく、電力・冷却・保守を中心とする継続費で反復運用できる。

**防御計画は「悪意ある利用ならAI providerが止めてくれる」ことをcontrolとして数えてはいけない。**

# 4. 24時間365日型の攻撃とは何か

「AIが全自動で企業を侵害する」という極端な絵ではない。

より現実的なのは、次のような人間時間を消費する仕事を常時回し、重要な判断だけ人間へ上げることだ。

- 公開assetやservice変更の継続監視
- 新しい脆弱性と利用technologyの照合
- 大量候補のpriority付け
- 公開文書、技術情報、code等の整理
- 長期campaignの状態保持
- 失敗対象の再評価
- 取得した大量情報の分類・検索
- 多言語での文章処理

この構造では、1回防いだことは「終了」を意味しない。新しい公開asset、設定変更、credential exposure、supplier connection、software vulnerabilityが現れれば、同じ企業が再び候補になる。

防御側も、発見、triage、isolation、credential revoke、restoreを人手の営業時間だけに依存できない。

# 5. 生産性増幅を経営上のcapacity problemとして見る

AIのriskは、個別modelのbenchmarkだけでは理解しにくい。

実利用では、月数千円規模のAI利用で一人の開発者がGitHub上の15万行を超える開発規模を扱えた事例がある。LOCはqualityやoffensive capabilityの尺度ではなく、これ自体が攻撃能力を証明するものではない。

しかし、調査、設計、実装、debug、review、documentationのthroughputを一人でも大きく増幅できることは、組織capacityの変化を示す。

悪意あるgroupについても、防御側は「高度技術者一人が一件ずつ手作業する」モデルを置くべきではない。

資金が数百万円、数千万円へ増え、複数operator、外部compute、local AI、worker node、automationを組み合わせれば、**対象数、監視時間、再試行頻度、分析量を同時に増やせる**。

このときの防御指標は「攻撃者がどれほど賢いか」だけではなく、**何件を同時に追跡できるか、何時間休まず再評価できるか**になる。

# 6. 42件の日本事例から見える反復パターン

Denno Watch corpusからは、少なくとも次の反復が見える。

1. Internet-facing / adjacent toolの脆弱性悪用
2. credential / VPN / cloud account悪用
3. ransomware + data theft +業務停止
4. SaaS / provider / entrusted-data concentration
5. BI / analyticsを経由したproduction data侵害
6. 正規API・正常accountを使った大量照会
7. database deletion等のintegrity破壊
8. source code / secret / development data漏えい
9. communications control-planeの悪用
10. shared infrastructureの大規模failure domain
11. 退会者・過去data等の長期保持によるblast radius拡大
12. 復旧不能時のservice retirement

詳細なcontrol mappingとbudget modelは[攻撃類型・防衛予算分析](incident-defense-budget-analysis-2026-10-04.md)を参照する。

ここで最も重要な共通点は、**侵入そのものより、侵入後にどこまで一つの権限で届くかが最終被害を決めている**ことである。

# 7. Case study — Times Car本人確認書類流出をどう評価するか

## 7.1 確認された事実

Park24は2026年9月、Times Car Web systemへの不正accessにより約660万accountの情報が第三者に取得されたと公表した。9月29日の第3報で、そのうち約160万accountに本人確認書類の漏えいがあると確認した。[^times]

公表された本人確認書類は、

- 運転免許証画像
- 現住所確認書類画像
- 学生証画像
- 家族確認書類画像

である。

「160万件すべてが運転免許証画像」とは公表されていないため、そのようには集計しない。

## 7.2 なぜ長期riskなのか

passwordは変更できる。card numberも再発行できる。

一方、氏名、生年月日、顔、過去・現在の住所、家族関係等は簡単には変更できない。本人確認画像を他の漏えいdataと組み合わせれば、target-specificなidentity fraudやsocial engineeringの材料が増える。

JICCは、運転免許証等の現物が手元にあっても、画像などの情報が漏えいした場合に「名義の悪用防止」の本人申告を利用できると明示している。JICC加盟会員はloanやcash advanceの審査時に本人申告commentを確認し、より慎重な与信判断を行える。[^jicc]

全国銀行個人信用情報センターも、本人確認書類の紛失、盗難、**漏えい**により名義冒用の可能性がある場合、本人申告情報を登録し、member financial institutionsの与信判断の参考にできるとしている。ただし判断を拘束せず、悪用防止を保証するものでもなく、預金口座開設時の照会対象ではない。[^ksc]

CICも本人確認書類の紛失・盗難、名義悪用のおそれについて本人申告制度を提供し、credit/loan審査時の参考情報として扱う。[^cic]

したがって、「本人確認書類画像がcredit riskと無関係」という見方は公的な信用情報制度と整合しない。

## 7.3 すでに確認できる二次影響

Times Car由来の不正契約そのものは、10月4日時点の一次情報で確認できない。

一方、Park24第3報の翌日である9月30日、JICCはsmartphone appへのaccessと本人申告・本人開示の申込み集中、処理遅延を公表した。10月1日にはsystem maintenanceのため本人申告・本人開示のapp受付を一時休止した。[^jicc-load]

CICも9月30日、internet開示、internet本人申告等の受付番号取得とcall centerへの問い合わせ・申込みが通常より増え、つながりにくい状態を公表した。[^cic-load]

JICC/CICは原因をTimes Carだと公式には明示していないため、因果関係は`confirmed`としない。しかし時系列上、**大規模な本人確認書類漏えいの直後に、信用情報の確認・名義悪用防止に関する社会的対応負荷が現実に増大した**ことは、企業が二次被害対応costを考えるうえで重要である。

## 7.4 想定すべき二次被害

Times Car incidentで発生確認済みとはしないが、本人確認書類と個人属性の漏えいでは次をstress scenarioへ含めるべきである。

- credit / loan申込みでの名義冒用
- communication service等の不正契約
- account recovery / 本人確認を狙う試行
- 正確な氏名、住所、契約関係を使うphishing / voice fraud
- 別の漏えいdataとの照合によるidentity profile精密化
- 不正契約が成立した場合のcredit record調査、異議申立て、訂正、長期monitoring cost

警察庁は、偽造本人確認書類を提示したり本人になりすましたりして不正取得された他人・架空名義の携帯電話が特殊詐欺等に悪用される事例を記録している。[^npa]

金融庁は、Timesとは独立した金融犯罪統計として、令和7年度のinternet banking不正送金3,946件、平均被害額360万円を公表している。[^fsa]

これらをTimes被害額へ足し合わせてはいけない。意味するのは、**identity compromiseが接続し得る後段の犯罪・金融riskが現実の制度設計上も無視できない**ということだけである。

## 7.5 企業が本人確認書類に適用すべき設計

- 本人確認完了後、本当に画像を保持し続ける必要があるかを定期再評価する。
- 法定・契約上必要な証跡と、画像原本の長期保存を分ける。
- identity document storeを通常customer DBから分離する。
- access権を極小化し、bulk read / exportを強く監視する。
- data retentionをaccount lifecycleと連動させる。
- incident時には顧客への「漏えい通知」だけでなく、credit bureau、通信、不正契約monitoring等の長期支援をplanする。

# 8. 業種別の最大被害 — 最悪時は「情報漏えい」で終わらない

詳細は[全業種最大被害ストレスマトリクス](sector-worst-case-impact-matrix-2026-10-04.md)に、日本標準産業分類A〜Sを基礎として整理した。

重要な上限だけを抜き出す。

| 業種 | 最大被害の中心 |
| --- | --- |
| 医療・福祉 | 電子カルテ、検査、処方、手術、救急の制限。最悪時は生命・健康riskへ到達 |
| 電力・gas・水道 | 広域供給停止が医療、通信、交通、決済へ連鎖。設備条件次第で物理安全・環境risk |
| 通信・cloud | 自社障害が多数業種へ同時波及する増幅点 |
| 金融・保険 | 顧客資産、不正送金、credit、決済、市場functionへの直接影響 |
| 物流・港湾・航空・鉄道 | 人・物の移動停止。工場、食品、医薬品、輸出入へ連鎖 |
| 製造 | 工場停止、quality data改ざん、設計・製法流出。supplier一社から多数工場へ連鎖 |
| 小売・EC | 受注、倉庫、配送、POS停止と大規模customer data流出 |
| 建設 | BIM/設計・工程喪失、支払先改ざん、工期・安全・巨大projectへ影響 |
| 教育 | 未成年data、成績、研究知財の長期漏えいと授業・学務停止 |
| 不動産・賃貸・mobility | 本人確認書類、住所、契約、物理accessが同時にrisk化 |
| 行政 | 住民記録、給付、税、災害、消防・警察等のservice continuityと国民の権利へ波及 |
| SaaS/BPO/MSP等 | 一社の侵害が多数企業へ同時波及するため、所属業種以上のsystemic risk |

過去のKDDI大規模通信障害はcyberattackではないが、音声約2,278万人、data765万人以上に影響し、物流、自動車、行政、銀行、交通等へ波及した。これは通信基盤が停止した場合のdependency impactを示す実例である。[^kddi]

名古屋港ではcyberattackにより全container terminalが停止し、IT停止が物理物流停止へ直結した。[^nagoya]

大阪急性期・総合医療センターでは、system復旧が数週間〜数か月規模となり、診療実績も大きく低下した。[^osaka]

**重要インフラやphysical operationを持つ企業では、最大被害を「個人情報漏えい人数」だけで測定してはいけない。**

# 9. 最大被害を作る10の構造

業種を問わず、次の条件が重なるほどdamage ceilingが急上昇する。

1. 一つのadministrator credentialでproduction、cloud、backup、tenantへ到達できる。
2. 退会者、元従業員、旧customer等のhistorical dataを大量保持する。
3. identity document、medical、free-text等の高感度dataを通常PIIと同じ場所へ置く。
4. internet-facing asset inventoryが不完全。
5. critical vulnerabilityを塞ぐのに数日〜数週間かかる。
6. supplier / maintenance remote accessが常設される。
7. 異常なbulk read/exportが正規accountなら通る。
8. backupがproduction identityと同じ管理planeにある。
9. restore testをしていない。
10. 夜間休日にcontainment decisionを出せない。

# 10. 現実的な多層防御

AI時代でも、中心は「AI対AI製品」を買うことではない。

## Layer 1 — 公開面を完全に把握する

- Internet-facing asset inventoryとownerを持つ。
- certificate、domain、cloud endpoint、remote admin、BI/dev surfaceの変化をcontinuous discoveryする。
- 不明assetを0へ近づける。

**経営KPI:** unknown internet-facing assets、critical exposure MTTR。

## Layer 2 — Identityを最優先で固める

- admin、VPN、cloud、GitHub、SaaSをphishing-resistant MFAへ。
- legacy/password-only authを廃止。
- permanent adminを減らし、必要時だけ権限を与える。
- service account/tokenを短寿命化する。

**経営KPI:** phishing-resistant MFA coverage、standing privileged account数。

## Layer 3 — patch対応を「週次作業」から「hours単位のrisk control」へ

Microsoftが示すように、vulnerability discoveryからweaponizationまでが24時間を大きく下回り得るなら、重要なInternet-facing assetに30〜60日の通常change cycleを適用できない。[^microsoft]

- active exploitation / KEVとの自動照合
- emergency isolation / feature disable / temporary mitigation
- VPN、mail gateway、BI、network applianceもproduction-equivalent SLA

**経営KPI:** exploit-known external exposureのmitigation time。

## Layer 4 — 「正しいcredentialによる異常」を止める

malware signatureだけではvalid account abuseを止められない。

- account/session/APIごとのread/write volume baseline
- bulk export、mass query、mass sendの制限
- high-value operationのstep-up authentication
- account/tenant/function単位のkill switch

**経営KPI:** abnormal bulk action detect-to-block。

## Layer 5 — 盗まれるdataそのものを減らす

- retention期限をDB、backup、analytics、export、vendor copyまで適用。
- production PIIをdev/test/BIへ無制限複製しない。
- identity documentsは別classとして短期化・分離。
- 委託終了時のdeletion proofを残す。

**経営KPI:** expired sensitive data volume、ownerless stores、production PII copies。

## Layer 6 — blast radiusを分割する

- endpoint、server、backup、management plane、tenantを分離。
- shared credentials / shared keysを減らす。
- admin pathを通常business networkから分離。

**経営KPI:** credential一つで到達可能なcritical systems数。

## Layer 7 — 防御も24時間365日へ

選択肢はinternal SOCでもMDR/MSSPでもよい。

必要なのは、夜間休日にhigh-confidence signalを見つけ、account revoke、endpoint isolation、network block等へ移れること。

**経営KPI:** MTTD、mean time to contain、off-hours containment coverage。

## Layer 8 — backupを「存在」ではなく「復旧能力」で評価する

- production identityからbackup control planeを分離。
- immutable/offline copy。
- restore drill。
- clean recovery environment。
- RTO/RPOの実測。

**経営KPI:** restore success rate、tested RTO/RPO。

## Layer 9 — supplierを自社riskとして扱う

- supplierが持つ自社dataをinventory化。
- remote admin pathを把握。
- tenant/data separationを契約・技術両面で確認。
- breach notification SLA、credential rotation、exit/deletion planを持つ。

**経営KPI:** critical vendor data/IR mapping completeness。

## Layer 10 — 人間系high-risk operationを別経路で確認する

AIで文章・音声等の社会工学が増幅されても、employeeの見抜く能力だけに依存しない。

- 振込先変更
- admin追加
- credential reset
- large export
- supplier bank account変更

等をsingle-person / single-channelで完結させない。

# 11. 防御側もAIを使うべき領域

攻撃側の速度だけが上がる状態を避ける。

比較的安全に自動化しやすい領域:

- threat intelligenceと自社assetの照合
- alert triageと関連log収集
- asset owner特定
- vulnerability priority付け
- identity anomaly enrichment
- incident timeline作成
- configuration drift検出
- detection rule候補作成

人間承認を残すべき領域:

- 広域production isolation
- 全顧客credential reset
- destructive remediation
- regulatory/legal notification
- public attribution
- service shutdown / retirement

# 12. 30日・90日・365日の実行計画

## 最初の30日

1. Internet-facing assetとownerを確定。
2. admin/VPN/cloud/GitHubのMFA gapを閉じる。
3. backupがproduction identityと分離されているか確認。
4. top 20 critical systemsのrestore可否を確認。
5. exploited vulnerabilityのemergency processを文書化。
6. critical vendor / remote access一覧を作る。
7. identity document、medical、payment、credential等の高感度data所在を把握。

## 90日以内

1. 24/365 detection / MDR / on-call containmentを成立。
2. privileged accessをJIT/PAMへ移行開始。
3. bulk read/export/send anomalyを主要systemへ実装。
4. immutable backup restore exerciseを実施。
5. historical data deletionを実行。
6. supplier compromise tabletopを実施。
7. CISO/情シスだけでなく法務、広報、経営、現場を含むincident commandを訓練。

## 365日以内

1. network / tenant / management-plane segmentationをarchitectureとして完成。
2. business-critical processごとにnon-IT fallbackまたはalternate pathを確立。
3. clean-room recoveryを実地訓練。
4. third-party data lineageを契約・technical evidenceまで追跡。
5. security metricを取締役会の定例KPIにする。

# 13. 予算判断

「何円なら安全」という金額は存在しない。

Denno Watchのplanning modelでは、security budgetをIT spendの比率で考える場合、一般企業10〜12%、Internet-facingかつ大量PII/SaaS/EC 12〜15%、金融・通信・物流・医療供給・100万件超data・multi-tenant provider等は15〜18%を一つのstarting rangeとしている。重大incident後のlegacy remediation期には18〜22%を許容する場合もある。[予算モデル](incident-defense-budget-analysis-2026-10-04.md)

これはvendor quoteでも「使えば安全」の保証でもない。

優先順位は、

1. asset ownership
2. identity
3. patch velocity
4. logging/detection
5. segmentation
6. recovery
7. data minimization
8. supplier governance

のgapを閉じることであり、tool数を増やすことではない。

IBM 2026では、AI-enabled malicious breachesは平均$6Mでglobal breach average $4.99Mより高く、security operationsにAI/automationを使う組織は使わない組織よりbreach costが平均で約$2M低かったと報告した。[^ibm]

# 14. 経営が毎月見るべき10指標

| 指標 | 目標方向 |
| --- | --- |
| unknown Internet-facing assets | 0 |
| exploit-known critical external exposure MTTR | hours〜1 day |
| phishing-resistant MFA coverage | 100% |
| standing privileged accounts | 最小化 |
| serverを含むEDR coverage | 100% |
| critical log coverage | 100% |
| abnormal bulk access detect-to-block | 分単位 |
| immutable backup restore success | 毎回成功 |
| expired/unowned sensitive data | 0 |
| critical vendor data/IR mapping | 100% |

# 15. 取締役会で問うべき5問

1. **今夜Internetに公開されている自社assetを全部言えるか。**
2. **明日0-day/critical vulnerabilityが出たら、営業時間外でも隔離できるか。**
3. **admin credential一つを失ったら、何system・何人分のdataへ届くか。**
4. **productionとbackupの両方を破壊されても、cleanに復旧できるか。**
5. **最大supplierが侵害された瞬間、自社dataがどこに何件あり、誰がcredentialを止めるか即答できるか。**

# 16. 最終評価

企業が恐れるべきなのは「万能AI」ではない。

より現実的な脅威は、**従来は高価だった専門家の注意力、調査時間、反復作業が安価になり、弱点を探し続ける能力が広く利用可能になったこと**である。

日本企業の公開事例だけでも、一回の侵害から数百万人・数千万recordへ到達し、本人確認書類が大量に失われ、物流や医療に近い業務が止まり、数十億円級の直接費用が発生し得ることは既に示されている。

AIは、これらの被害を生み出す既存の弱点を新しく作る必要すらない。見つけ、整理し、優先順位を付け、再試行するcostを下げるだけで十分に脅威を増幅できる。

したがって、防御の目標は「侵入を一度も許さない」だけでは不十分である。

> **侵入されても横へ広がらない。盗めるdataが少ない。正規accountでも大量操作を止める。backupは別のidentityで守る。夜中でも封じ込める。委託先が落ちても続けられる。そして復旧を実際に試してある。**

この状態を構造として作ることが、AI時代の企業防衛の中心になる。

# Related analysis

- [2026年42件incident corpus](../incidents/index.md)
- [根拠資料台帳](evidence-ledger-ai-cyber-risk-2026-10-04.md)
- [全業種サイバー侵害・最大被害ストレスマトリクス](sector-worst-case-impact-matrix-2026-10-04.md)
- [攻撃類型・最大被害・防衛予算model](incident-defense-budget-analysis-2026-10-04.md)
- [2026 corpus audit](../methodology/corpus-audit-2026-10-04.md)

[^ipa]: IPA「情報セキュリティ10大脅威 2026」2026-01-29 / updated 2026-05-21. https://www.ipa.go.jp/security/10threats/10threats2026.html
[^microsoft]: Microsoft, “2026 Digital Defense Report — AI is changing the physics of cybersecurity,” 2026-10-01. https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
[^google]: Google Threat Intelligence Group, “From Prompting to Autonomy — The Evolution of Adversarial AI,” 2026-09-08. https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai
[^anthropic]: Anthropic, “Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK Navigator,” 2026-06-03. https://www.anthropic.com/research/attack-navigator
[^verizon]: Verizon, 2026 DBIR. https://www.verizon.com/business/ja-jp/resources/reports/dbir/
[^ibm]: IBM, “Cost of a Data Breach Report 2026,” 2026-07-29. https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled%2C-costing-companies-6-million-on-average
[^mistral]: Mistral AI, “Using offline models.” https://docs.mistral.ai/vibe/code/cli/offline-models
[^meta]: Meta, “Llama FAQs.” https://ai.meta.com/llama/faq/
[^times]: Park24「タイムズカーWebシステムへの不正アクセスに関する調査結果および今後の対応について（第3報）」2026-09-29. https://www.park24.co.jp/news/2026/09/20260929-1.html
[^jicc]: JICC「不正利用防止の届け出」およびFAQ「運転免許証等の現物は手元にあるが画像など情報が流出してしまった場合…」. https://www.jicc.co.jp/comment/ ; https://www.jicc.co.jp/faq/detail/a095i000000LtgMAAS
[^ksc]: 全国銀行個人信用情報センター「本人申告の手続き」. https://www.zenginkyo.or.jp/pcic/return/
[^cic]: CIC「本人申告とは」. https://www.cic.co.jp/mydata/declaration/index.html
[^jicc-load]: JICC「スマホアプリのご利用について（アクセス集中のお知らせ）」2026-09-30、および「本人申告コメントおよび本人開示のスマホアプリ一時休止について」2026-10-01. https://www.jicc.co.jp/news/a04TL00001VXvGUYA1 ; https://www.jicc.co.jp/notes/a04TL00001VnQBtYAN
[^cic-load]: CIC「インターネット開示・本人申告などの受付番号の取得およびコールセンターへのお電話がつながりにくい状況について」2026-09-30. https://www.cic.co.jp/news/info/2026/09/3d8511719448f94d3c888099a326c14a77855800.html
[^npa]: 警察庁「警察白書 第1項 犯罪捜査に関する各種取組」— 偽造本人確認書類やなりすましにより取得された携帯電話が特殊詐欺等へ悪用される実態を記載. https://www.npa.go.jp/hakusyo/r05/honbun/html/z2221000.html
[^fsa]: 金融庁「預貯金の不正送金被害等の発生状況（令和8年3月末）」2026-06-30. https://www.fsa.go.jp/news/r7/ginkou/20260630.html
[^osaka]: 大阪急性期・総合医療センター「情報セキュリティインシデント調査報告書 概要」2023-03-28. https://www.gh.opho.jp/incident/1.html
[^nagoya]: NISC「名古屋港コンテナターミナルのサイバー攻撃におけるインシデント対応について」2024-07-26. https://www.nisc.go.jp/pdf/policy/infra/shiryo2.pdf
[^kddi]: KDDI「7月2日に発生した通信障害について」2022-07-29. https://news.kddi.com/kddi/corporate/newsrelease/2022/07/29/6200.html
[^askul]: LY Corporation, FY2025 Q3 Results, Note 12 System Failure Response Costs — JPY 5,262 million. https://www.lycorp.co.jp/en/ir/news/auto_20260204546714/pdfFile.pdf
