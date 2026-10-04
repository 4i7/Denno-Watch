---
type: Executive Threat Analysis
title: AIで攻撃コストが崩れた時代の企業サイバーリスク — 42件の日本事例から見る被害、攻撃経済性、防衛
summary: Denno Watchの2026年日本重大インシデント42件と2026年の主要脅威インテリジェンスを統合し、経営層が一目で被害構造、AIによる攻撃コスト低下、24/365型の継続攻撃、現実的な多層防御を理解するためのエグゼクティブレポート。
tags: [executive, ai, cyber-risk, japan, defense, resilience, economics, automation, 2026]
status: draft
stale_after: 2027-01-01T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T08:43:00+09:00 }
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
  - id: microsoft-mddr
    resource: https://www.microsoft.com/en-us/security/security-insider/threat-landscape/2026-digital-defense-report
    title: Microsoft Digital Defense Report 2026 — AI is changing the physics of cybersecurity
    author: organization:Microsoft
  - id: google-gtig-autonomy
    resource: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai
    title: GTIG AI Threat Tracker — From Prompting to Autonomy
    author: organization:Google Threat Intelligence Group
  - id: google-gtig-may
    resource: https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access/
    title: GTIG AI Threat Tracker — Vulnerability exploitation, augmented operations and initial access
    author: organization:Google Threat Intelligence Group
  - id: google-risk-resilience
    resource: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
    title: AI risk and resilience in 2026 — Mandiant special report
    author: organization:Google Cloud / Mandiant
  - id: anthropic-navigator
    resource: https://www.anthropic.com/research/attack-navigator
    title: Mapping AI-enabled cyber threats — LLM ATT&CK Navigator
    author: organization:Anthropic
  - id: verizon-dbir
    resource: https://www.verizon.com/business/ja-jp/resources/reports/dbir/
    title: Verizon 2026 Data Breach Investigations Report
    author: organization:Verizon
  - id: gemini-pricing
    resource: https://ai.google.dev/gemini-api/docs/pricing
    title: Gemini Developer API pricing
    author: organization:Google
---

# 30秒で分かる結論

> **企業が向き合うべき変化は「攻撃者が突然超人になった」ことではない。攻撃に必要だった人間の時間・専門知識・調査コストがAIで圧縮され、同じ人数・同じ資金で、より多くの企業を、より長時間、より粘り強く狙えるようになったことである。**

2026年のDenno Watch corpusには、日本企業・組織の重大インシデント42件が含まれる。そこでは、ランサムウェア、脆弱性悪用、VPN/認証情報悪用、クラウド・SaaS、BI/分析基盤、API/業務ロジック、大規模共有基盤、委託先・サプライチェーン、データ破壊、開発基盤の秘密情報管理不備などが繰り返し観測されている。[Denno Watch incident index](../incidents/index.md)

AIはこれらの「古い攻撃経路」を消してはいない。むしろ、**探索、優先順位付け、文章生成、コード生成、脆弱性調査、対象別の適応、ログや盗取データの分析、複数作業の並列化**を安価にし、攻撃者側の限界だった人手を取り除きつつある。

Microsoftは2026年10月、AIが脆弱性探索、偵察、フィッシング、マルウェア/エクスプロイト開発、データ分析、侵害後活動に使われ、攻撃の速度・規模・一貫性を高めていると報告した。また、実環境での脆弱性発見からweaponizationまでの中央値が24時間を大きく下回る一方、企業のcritical external vulnerability修正は30〜60日を要する場合があると指摘している。[^microsoft]

Google Threat Intelligence Groupは2026年Q2、侵害したクラウド資源を起点に、攻撃者がagent-enabled mass credential harvesting campaignを**6時間未満**で計画・構築・実行した事例を報告している。[^gtig-autonomy]

Anthropicは2025年3月〜2026年3月に悪用で停止した832アカウントを分析し、AI利用がMITRE ATT&CK全14 tactic、482 sub-techniqueへ広がっていたと報告した。中〜高リスクに分類されたactor比率は期間前半33%から後半56%へ上昇し、従来は高度な技術者に偏っていた活動へ低〜中スキルactorも進出している。[^anthropic]

ただし、**「完全自律型の高度侵害がすでに一般化した」とは言わない**。Microsoftも複雑な実世界侵害の多くには現在も意味のある人間の指示が必要と明記している。変化の本質は、全工程の無人化ではなく、従来人間が数十分〜数時間かけていた作業の一部をAIへ継続的に委譲できることである。[^microsoft]

# 経営層向けワンページ

| 企業が知るべきこと | 2026年時点の意味 |
| --- | --- |
| **攻撃者は大規模GPU設備を所有する必要がない** | モデル推論はAPI/クラウドとして借りられる。ローカル側は制御・中継・ブラウザ/ネットワーク処理を担えばよく、DGX SuperPODのような設備投資は前提ではない。 |
| **安価なノードを並列化できる** | 数百〜数千円級の低価格/中古端末が「制御・中継ノード」として使われ得る。重要なのは各ノードで巨大LLMを動かすことではなく、外部推論、ネットワーク、認証、automationを組み合わせられること。 |
| **24時間365日、休まない作業が可能** | reconnaissance、公開資産監視、候補の再評価、文章生成、キャンペーン分類、失敗対象の再試行などは自動化しやすい。複雑な侵害判断は人間が残っていても、監視・準備・反復部分は常時稼働できる。 |
| **1社を深く狙う前に1000社を浅く調べられる** | LLMがWeb情報、公開コード、技術スタック、求人情報、漏えい資格情報などを整理するため、対象選定の限界が「分析担当者の人数」ではなくなる。 |
| **攻撃の入口は古典的なまま** | exposed vulnerability、valid account、VPN、SaaS、API、委託先、GitHub、メール/SMSなど。AIは入口を魔法のように増やすというより、既存入口の探索と悪用を速くする。 |
| **被害は侵入の巧妙さよりblast radiusで決まる** | 侵入後に数百万件のPII、共有認証、バックアップ、委託データ、複数tenantへ届く設計だと損失が跳ね上がる。 |
| **防衛側も人間速度のままでは負ける** | exposure discovery、patch判断、identity anomaly、rate limit、isolation、credential rotation、restoreをできるだけ機械速度へ近づける必要がある。 |

# 「高価な攻撃設備が必要」という前提は崩れた

## DGX SuperPODは攻撃者の必須条件ではない

企業はAI攻撃を「巨大GPUクラスタを持つ国家級actorの問題」と誤認してはいけない。

攻撃者が必要とする機能は大きく二つに分かれる。

1. **推論・判断** — LLMに文章、コード、分類、次行動候補を生成させる。
2. **実行・観測** — 通信、ブラウザ、API、ジョブ管理、ログ保存、対象の状態監視を行う。

前者は商用API、クラウド推論、レンタルGPU、open-weight model等へ外部化できる。後者は必ずしもGPUを必要とせず、一般的なCPU、低価格VPS、古いPC、SBC、ルータ/ゲートウェイ相当の機器などで成立する。

2026年10月時点で、商用LLM APIには100万token単位で数ドル以下の入力価格帯やbatch/flex価格が存在する。これは「攻撃が無料」という意味ではないが、**高度な言語・コード処理を行うためのCAPEXが、巨大なGPU設備購入から従量課金へ移った**ことを意味する。[^gemini-pricing]

したがって、数百円級の端末を数十台並べる構成を考える場合も、それらの役割は**巨大モデルのローカル推論ではなく、分散した制御・観測・中継・ジョブ実行**であると理解するのが正確である。実際の知的処理は外部APIや別の共有計算資源へ送れる。

重要なのは機器単価ではなく、次の非対称性である。

> **防御側は自社の全資産を24/365守る必要がある。攻撃側は大量の候補から一つでも守りの薄い資産を見つければよい。AIはその候補探索と反復コストを急速に下げている。**

# 24/365型攻撃で何が変わるか

24/365型とは「AIが完全自律で365日侵入し続ける」という意味ではない。企業が想定すべきなのは、**攻撃ライフサイクルのうち機械化しやすい部分が常時回り、人間は価値の高い判断だけへ集中できる状態**である。

## 常時自動化しやすい部分

- 公開資産・サブドメイン・証明書・サービス変更の継続監視
- 新しく公開された脆弱性と対象技術スタックの照合
- 大量候補の危険度分類と優先順位付け
- 公開文書・求人・技術ブログ・GitHub等からの環境推定
- 多言語メール/SMS/問い合わせ文の大量生成と対象別調整
- 認証異常・失敗結果の分類と再試行候補管理
- 取得した大量ファイル/ログ/データの検索・要約・価値分類
- 長期キャンペーンの状態管理、重複排除、再訪問
- 防御変更を検知した後の別候補探索

このため、企業側から見ると「攻撃者が一度諦める」という期待が成立しにくくなる。今日閉じた入口があっても、明日新しい資産、設定ミス、認証情報、委託先、SaaS連携が出れば再評価される。

# AIが攻撃者に与える5つの経済的効果

## 1. 調査単価の低下

以前は技術者が検索結果、ドキュメント、コード、脆弱性情報を読んで対象ごとに整理していた。LLMはこの前処理を大量並列化できる。

**企業への影響:** 「有名企業だから狙われる」から、「機械的に弱点が見つかった企業が狙われる」へ重心が移る。

## 2. スキル格差の縮小

Anthropicの2026年分析では、actorの技術的sophisticationとAIによるrisk upliftの相関は弱く、低〜中スキルactorでも従来よりoperationalな活動へ進む傾向が観測された。[^anthropic]

**企業への影響:** 高度な攻撃グループだけを想定した脅威モデルでは不足する。

## 3. 並列性の向上

人間1人は同時に数十件の調査を精密に処理できないが、automation + LLMでは大量targetの状態を保持し、優先度の高いものだけ人間へ返せる。

**企業への影響:** 攻撃者側の「対象選定コスト」が下がる。

## 4. 反復コストの低下

失敗した対象を記録し、数日後の設定変更、patch遅延、新しい脆弱性、新しいcredential exposureを契機に再評価できる。

**企業への影響:** 一度防いだ攻撃が終戦ではなく、継続的pressureになる。

## 5. 言語・業種知識の障壁低下

日本語、業界用語、顧客対応文、採用情報、技術文書等を自動処理できる。

**企業への影響:** 日本企業であること、国内中心であることが攻撃の摩擦になりにくい。

# 42件の日本事例が示す「実際に起きる被害」

Denno Watch corpusは、AIそのものが直接原因ではない事例を含む。しかし、これは重要である。AI時代の攻撃者が拡大するのは、まさに**すでに成功している既存経路**だからである。

## 被害1 — 数百万〜数千万件の情報漏えい

- KDDI: 共有ISPメール基盤で約1,223万メールアドレス、約762万パスワード。
- Helpfeel/Gyazo: 2,362万ユーザー規模の情報影響。
- EPARK/PeakManager: 約2,218万recordsの外部転送確認。
- Murauchi.com: 約771万customer records。
- アフラック: 約440万人規模の顧客情報、約22万人には口座関連情報。

**経営上の意味:** 一つの認証・一つの共有基盤・一つの分析環境の侵害が、会社の顧客母数そのものへ達し得る。

## 被害2 — 業務停止と売上/供給への波及

- ニチレイ: 冷蔵倉庫入出庫・冷凍食品出荷への影響。
- 日本交通: 配車/予約への影響。
- マルタケ: 医薬品卸システム障害、代替手段・仮サーバーで供給継続。
- DotMoney/DotGift: 全面停止、片方は復旧せずサービス終了。

**経営上の意味:** cyber incidentはIT部門の問題ではなく、物流、売上、在庫、顧客資産、サービス継続の問題になる。

## 被害3 — 下流企業へ連鎖

- KDDI: 6 ISPへ同時波及。
- 両毛システムズ: 委託データを介し複数組織へ影響。
- 日本テレネット: BPO/CSS受託データが大きなpotential impact population。
- ApplyNow: recruitment SaaSを介して複数顧客へ波及。
- メディア4u: OEM/代理店を含むSMS基盤のdownstream handling。

**経営上の意味:** 自社のsecurity postureだけでなく、データを預けた相手、共有platform、保守先の守りが自社損失へ直結する。

## 被害4 — 正規機能そのものの悪用

- アフラック: 正常利用に見える形式の大量照会を従来検知が捉えにくかった。
- メディア4u: 正規SMS送信権限を使った280件の不正送信。

**経営上の意味:** 「malwareを見つければ守れる」ではなく、valid account/valid session/valid APIの**異常な使い方**を見る必要がある。

## 被害5 — 破壊と復旧

- コープやまぐち: DB全データ削除。ただしbackupから同日復元。
- 日本テレネット: clean network rebuildと全PC reimage。

**経営上の意味:** intrusion preventionに失敗しても、immutable/isolated backupとclean recoveryが企業存続を左右する。

# AI時代に最大化しやすい被害シナリオ

以下は「必ず起きる」予測ではなく、42件と2026年のAI threat intelligenceから導くstress scenarioである。

## Scenario A — 外部公開脆弱性のmass exploitation

新規脆弱性公開後、AIが大量の候補企業を自動分類し、露出している資産へ優先順位を付ける。攻撃者は少人数でも、多数の組織を短期間に評価できる。

**最大化要因:** patch SLAが週〜月、asset owner不明、internet-facing inventory欠落。

**防衛:** 外部surface continuous discovery、KEV/active exploitation連動、24時間以内のisolation/mitigation lane、virtual patch/WAF、egress monitoring。

## Scenario B — credential reuse / valid-account scaling

漏えいした資格情報や取得済みsession等をAIが大量分類し、価値の高いアカウントとサービスを絞る。

**最大化要因:** password-only、VPN/M365/cloud/adminにMFAなし、legacy auth、長寿命token。

**防衛:** phishing-resistant MFA/FIDO2、conditional access、device binding、PAM/JIT、short-lived token、impossible-travelだけに頼らないbehavior analytics。

## Scenario C — hyper-personalized social engineering

公開情報から役職、業務、取引関係、製品、イベントを理解し、対象ごとに自然な日本語で文面を大量生成する。

**最大化要因:** 高権限者がメール/SMSだけで重要操作を承認、payment/account changeにout-of-band確認なし。

**防衛:** high-risk transactionの二経路承認、known-number callback、FIDO2、DMARC/SPF/DKIM、SMS/voiceを単独本人確認へ使わない。

## Scenario D — low-and-slow API / business-logic extraction

「攻撃らしいpayload」ではなく、正規操作を大量に繰り返す。AIが取得結果を分類しながらrateを調整し、価値の高いデータだけを狙う。

**最大化要因:** user/session/account単位の取得量制限なし、export API無制限、異常量監視なし。

**防衛:** per-identity/session/object rate limit、bulk-read budget、behavior baseline、sensitive-action step-up auth、server-side authorization、data egress quota。

## Scenario E — SaaS/委託先一社から多数企業へ波及

AIは一社のprovider compromiseから得たデータを自動分類し、顧客ごとの価値、credential、次の標的を抽出できる。

**最大化要因:** entrusted copyの長期保持、tenant isolation不十分、shared administrator、downstream data owner不明。

**防衛:** tenant boundary、data lineage、contractual deletion proof、customer-specific encryption/key separation、vendor IR SLA、provider compromise tabletop。

## Scenario F — ransomware + data theft + operational targeting

侵害後にAIがファイル、共有、database、業務dependencyを分類し、停止効果や情報価値が高い箇所の判断を補助する。

**最大化要因:** flat network、backup identity共用、domain-wide admin、recovery plan未検証。

**防衛:** segmentation、tiered admin、EDR/MDR、immutable backup、clean-room restore、restore drill、非IT fallback。

# 「数百円の機器数十台」の意味を正確に理解する

この表現は、**数百円の機器だけでfrontier LLMをローカル実行できる**という意味ではない。

重要なのは、現代の攻撃automationでは各nodeが高度な知能を持つ必要がない点にある。nodeは次のような軽量役割だけでもよい。

- queueからjobを受け取る
- targetの状態を観測する
- 結果をcentral controllerへ返す
- browser/network taskを実行する
- time scheduleで再試行する
- logやartifactを保存する

知的処理は外部LLM/APIへ委譲できる。この構造では、**GPU設備ではなく「安価な実行点を多数持てること」と「クラウド推論を従量課金で借りられること」の組合せ**が脅威になる。

また、攻撃側は必ずしも自前の物理機器を買う必要もない。クラウド/VPS、既存PC、侵害済み機器等を利用し得るため、「敵が高価な設備を購入できるか」は防衛判断にほとんど使えない。

# 現実的な多層防御

AI時代でも、防御の中心は奇抜な「AI対AI製品」ではない。42件の実例と2026年threat intelligenceから、優先順位は以下になる。

## Layer 1 — 見えていないInternet-facing assetをゼロへ近づける

必須:

- asset inventory / owner / business criticality
- external attack surface continuous discovery
- certificate/subdomain/cloud endpoint change monitoring
- exposed admin/BI/dev interfaceの原則非公開化
- emergency mitigation ownerと24h SLA

**KPI:** unknown internet-facing asset数、Critical exposure MTTR。

## Layer 2 — Identityを最優先の防壁にする

必須:

- admin/VPN/cloud/GitHub/SaaSにphishing-resistant MFA/FIDO2
- legacy/password-only auth廃止
- JIT/JEA/PAM、権限常設を減らす
- service account/tokenの短寿命化
- impossible travelだけでなくsession behavior、device trust、bulk accessを評価

**KPI:** phishing-resistant MFA coverage、standing privileged account数、token最大有効期間。

## Layer 3 — 脆弱性対応を人間の週次作業から機械速度へ寄せる

必須:

- KEV/active exploitation feedとの自動照合
- internet-facing critical findingをhours単位でtriage
- patchできない場合のisolation、feature disable、WAF/ACL等のtemporary mitigation
- BI、VPN、mail gateway、network appliance、管理画面もproduction-equivalent patch SLA

**KPI:** exploit-known external vulnの平均mitigation時間。

## Layer 4 — 「正規に見える異常」を検知する

必須:

- account/session/API単位のread/write volume baseline
- bulk export、high-rate query、異常な対象分布の検知
- value-transfer、SMS send、credential change等へのstep-up auth
- kill switchを機能/tenant/account単位で用意

**KPI:** abnormal bulk actionのdetect-to-block時間。

## Layer 5 — データを減らす

必須:

- historical/dormant/customer/employee/entrusted dataのretention期限
- analytics/export/dev環境への本番PII複製制限
- free-text/attachmentにもDLP/retentionを適用
- 委託終了時のdelete evidence
- payment/identity document等を必要システム以外へ置かない

**KPI:** owner不明data store、期限切れdata volume、production PII copy数。

## Layer 6 — Network / tenant / workload blast radiusを切る

必須:

- user endpoint、server、backup、management plane、tenantを分離
- shared platformのcredential/keyをtenantごとに分割
- east-west movementを監視・制限
- admin pathを通常業務networkから分離

**KPI:** 一つのcredentialで到達できるcritical systems数。

## Layer 7 — 24/365検知へ移行する

攻撃が24/365で準備・反復されるなら、防御が「平日9〜17時のalert確認」では不十分になる。

選択肢:

- internal SOC
- MDR/MSSP
- on-call rotation + automated containment
- AI-assisted triage + human approval

重要なのはSOC製品を買うことではなく、**high-confidence signalからisolation/credential revokeまでの時間**を短くすること。

**KPI:** MTTD、MTTC (mean time to contain)、夜間休日のcontainment capability。

## Layer 8 — Backupを「ある」から「戻せる」へ

必須:

- production identityからbackup control planeを分離
- immutable/offline copy
- 定期restore test
- clean-room recovery
- ransomware/DB deletionを想定したRTO/RPO検証

コープやまぐちではDB全削除後に同日backup restoreが機能した。日本テレネットではclean network rebuildと全PC reimageまで実施した。こうした復旧能力は、侵入を完全に防げない環境で企業生存率を大きく左右する。

## Layer 9 — サプライチェーンを自社資産として扱う

必須:

- vendorが保持する自社data copyを台帳化
- tenant/data isolation requirements
- provider breach時の通知SLA
- credential rotation権限・手順
- termination時のdelete proof
- critical provider代替/exit plan

**KPI:** critical vendorごとのdata inventory completeness、breach notification SLA、exit test status。

## Layer 10 — 人間系の高リスク操作を別経路で確認する

AIで日本語social engineeringの質と量が上がるほど、「社員が見抜く」だけを最後の砦にしてはいけない。

必須:

- 振込先変更、認証情報変更、権限追加、重要データexportは二者承認
- known channel / known numberでout-of-band確認
- executive/VIP workflowの例外廃止
- helpdesk resetへ強い本人確認

**KPI:** high-risk business actionのsingle-person approval率。

# 経営が毎月見るべき10指標

| 指標 | 目標の方向 |
| --- | --- |
| unknown internet-facing assets | 0へ |
| exploit-known critical external exposure MTTR | hours〜1 dayへ |
| phishing-resistant MFA coverage | 100%へ |
| standing privileged accounts | 最小化 |
| EDR coverage（server含む） | 100%へ |
| critical log coverage | 100%へ |
| abnormal bulk access detect-to-block | 分単位へ |
| immutable backup restore success | 毎回成功 |
| expired/unowned sensitive data | 0へ |
| critical vendor data/IR mapping | 100%へ |

# 企業規模別の最低防衛モデル

## 小〜中規模企業

自前SOCや高価なSIEMをフル構築するより、以下を先に完成させる。

1. FIDO2/MFA
2. managed EDR/MDR
3. asset inventory + vulnerability management
4. managed backup + restore drill
5. cloud/SaaS access governance
6. external incident-response retainer
7. critical vendor inventory

**重要:** 製品数を増やすより、coverageと運用責任を100%へ近づける。

## 中堅〜大企業

上記に加えて、

- 24/365 SOC/MDR
- EASM
- PAM/JIT
- NDR/egress analytics
- API behavior analytics
- tenant/data segmentation
- enterprise DLP/data lineage
- clean recovery environment
- provider compromise exercise

を組み合わせる。

## 金融・通信・物流・医療供給・multi-tenant provider

防御目標を「侵入防止」から**社会的サービス継続**へ引き上げる。

- multi-region / multi-provider failover
- independent recovery control plane
- service-specific kill switch
- high-risk operationのhuman + machine dual control
- customer-specific credential/key rotation
- downstream mass-notification pipeline
- annual full-scale cyber recovery exercise

# 防御側もAIを使うべき領域

AIが攻撃者へ速度を与える以上、防御側だけが全判断を手作業にすると時間差が広がる。

安全に自動化しやすい領域:

- vulnerability / exploit intelligenceの自社asset照合
- alert triageと関連ログの収集
- phishing/SMS/voice contentの分類
- identity anomalyのcontext enrichment
- incident timeline生成
- asset owner特定
- configuration drift検出
- detection rule候補生成
- public threat intelligence要約

人間承認を残すべき領域:

- production isolationの大規模実行
- customer-wide credential reset
- delete/destructive remediation
- legal/regulatory notification
- attribution
- public statement
- business shutdown / service retirement

# 何を買うかではなく、何秒で反応できるか

AI時代に重要なのは「AI security productを導入したか」ではない。

経営層が問うべきは次の5問である。

1. **自社のInternet-facing assetを今この瞬間に全部言えるか。**
2. **今日critical vulnerabilityが出たら、夜中でも24時間以内に隔離できるか。**
3. **1つのvalid accountが盗まれた時、何万人/何systemへ届くか。**
4. **全DBを消されても、攻撃者のidentityを使わずcleanに復旧できるか。**
5. **委託先が侵害された時、自社dataがどこに何件あるか即答できるか。**

5つのうち1つでも答えられない場合、AI時代の最大リスクは「AIそのもの」ではなく、**AIが高速に見つけられる既存の管理不備**である。

# 最終メッセージ

AIは攻撃者へ、かつて大規模組織だけが持っていたような**継続性・並列性・言語能力・コード支援・分析能力**を低コストで提供し始めている。

その結果、攻撃者がDGX SuperPODのような大規模計算基盤を所有しているかどうかは重要ではなくなった。外部推論を利用できるなら、現場のcontroller/workerは安価な汎用機器でもよい。数十nodeを24/365動かし、人間は高価値判断だけを行う構成は経済的に現実的である。

ただし、これは「防衛不能」という意味ではない。

42件の日本事例が示す防御側の勝ち筋は明確である。

> **Identityを強くする。公開面を減らす。patchを速くする。正規操作の異常量を見る。データを持ちすぎない。ネットワークとtenantを分ける。24/365で検知する。backupを隔離し、実際に戻す。委託先を含めて守る。そして、止まっても事業を続ける。**

攻撃者の1回あたりのコストが下がるほど、防御側は「一件ずつ人が対応する」モデルから脱却しなければならない。

これからの企業防衛は、**machine-speed pressureに対して、machine-assisted defenseと構造的resilienceで応えること**が中心になる。

# Related Denno Watch analysis

- [42件のincident corpus](../incidents/index.md)
- [2026 corpus audit](../methodology/corpus-audit-2026-10-04.md)
- [攻撃類型・最大被害・防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md)

[^microsoft]: Microsoft, “2026 Digital Defense Report — AI is changing the physics of cybersecurity,” 2026-10-01. Microsoft reports AI use across reconnaissance, vulnerability discovery, phishing, malware/exploit development, data analysis and post-compromise activity; it also notes that most complex real-world intrusions still require meaningful human direction.
[^gtig-autonomy]: Google Threat Intelligence Group, “From Prompting to Autonomy — The Evolution of Adversarial AI,” 2026-09-08. GTIG reports a Q2 2026 case in which a compromised cloud resource was used to plan, build and execute an agent-enabled mass credential-harvesting campaign in under six hours.
[^anthropic]: Anthropic, “Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK Navigator,” 2026-06-03. Analysis of 832 malicious cyber accounts found AI use across all 14 MITRE ATT&CK tactics and 482 sub-techniques, with medium-or-higher-risk actors increasing from about 33% to 56% across the study halves.
[^gemini-pricing]: Google AI for Developers, Gemini Developer API pricing, checked 2026-10-04. The cited pricing page documents free tiers and paid inference priced per one million tokens, including discounted batch/flex modes; exact prices are time-dependent and should not be treated as permanent.
