---
type: Cybersecurity Incident
title: DMM Bitcoin / Ginco — 開発者標的型侵害から4,502.9 BTC窃取・事業終了へ
description: 2024年のDMM Bitcoin暗号資産流出について、Ginco開発者への標的型ソーシャルエンジニアリング、認証・セッション悪用、正規取引指示の改変、約482億円相当の窃取、顧客資産移管まで追跡する。
resource: https://www.npa.go.jp/bureau/cyber/koho/caution/caution20241224.html
tags: [japan, cryptocurrency, supply-chain, social-engineering, developer, credential-theft, integrity, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
incident:
  organization: DMM Bitcoin / Ginco
  sector: crypto-asset
  jurisdiction: JP
  incident_status: DMM_Bitcoin_business_closed_and_customer_assets_transferred
  attack_type: targeted-social-engineering-and-transaction-integrity-compromise
  earliest_known_activity: "2024-03"
  detected_at: "2024-05-31"
  first_disclosed_at: "2024-05-31"
  latest_public_update: "2025-03-12 transfer-related issues resolved"
  public_record_checked_at: "2026-10-04T22:14:00+09:00"
  intrusion_vector: "Ginco developer targeted through social engineering and malware/session compromise; legitimate transaction flow subsequently manipulated"
  affected_services: "Ginco Enterprise Wallet infrastructure used for DMM Bitcoin wallet operations"
  data_exposure: not_the_primary_publicly_confirmed_impact
  integrity_impact: "4,502.9 BTC transferred to attacker-controlled wallet through tampered transaction process"
  financial_impact: "approximately JPY 48.2 billion at the time, approximately USD 308 million in joint attribution notice"
  restoration_state: "customer asset protection and service wind-down; accounts and entrusted assets transferred to SBI VC Trade in March 2025"
  regulatory_response: "joint NPA/FBI/DC3 attribution; financial-sector supervisory response and industry-wide mitigation guidance"
sources:
  - id: npa-attribution
    resource: https://www.npa.go.jp/bureau/cyber/koho/caution/caution20241224.html
    title: 北朝鮮を背景とするサイバー攻撃グループTraderTraitorによる暗号資産関連事業者を標的としたサイバー攻撃について
    author: organization:警察庁
  - id: ginco-report
    resource: https://www.ginco.co.jp/news/20250128_pressrelease
    title: 当社サービスへのサイバー攻撃に関するご報告
    author: organization:Ginco
  - id: sbi-transfer
    resource: https://www.sbivc.co.jp/dmm_vct
    title: DMM Bitcoinからの移管 特設サイト
    author: organization:SBI VCトレード
---

# 概要

2024年5月31日、DMM Bitcoinから4,502.9 BTCが不正流出した。警察庁、FBI、米国防総省サイバー犯罪センターは同年12月、北朝鮮を背景とするTraderTraitorが本件を実行したと共同で特定し、当時約482億円、約3億800万ドル相当の暗号資産窃取と公表した。[^npa]

公開調査では、直接DMM Bitcoinの利用者を騙した単純なフィッシングではなく、ウォレット業務を支えるGincoの開発者が標的になった。攻撃者はソーシャルエンジニアリングとマルウェアを用いて開発者環境・セッションへ到達し、Ginco Enterprise Walletを構成するインフラストラクチャの特定部分へ不正アクセスした。[^ginco]

本件の本質は機密情報流出だけではなく、**正規の暗号資産移転業務の完全性を破壊し、正しい送金指示を攻撃者のアドレスへ向ける取引へ改変したこと**にある。

# 事故発生時の環境

2024年は、ローカルLLM・生成AIによる調査、文書生成、コード理解が一般化しつつあったが、本件について公的帰属資料はAI利用を原因としていない。確認されているのは、暗号資産関連企業の開発者を長期に狙う北朝鮮系攻撃グループの標的型ソーシャルエンジニアリングである。

暗号資産ウォレットでは、秘密鍵保護だけでなく次の全体が完全性境界になる。

- 開発者端末。
- Git・CI/CD・開発アカウント。
- セッション・認証情報。
- ウォレットAPI・通信経路。
- 出庫指示の生成・承認。
- 署名前後のアドレス・金額照合。

秘密鍵そのものが直接盗まれたかどうかだけで安全性を評価してはいけない。

# 公開情報から確認できる攻撃系列

警察庁/FBIとGinco公表を組み合わせると、次の因果系列が確認できる。[^npa][^ginco]

1. 2024年3月頃、攻撃者がGincoの開発者を採用活動等を装って標的化。
2. 開発者へ悪意あるスクリプト等を実行させ、環境へ侵入。
3. 開発者のセッション・認証を足場としてGinco Enterprise Wallet関連環境へ到達。
4. DMM BitcoinからGinco側へ送られる正規の取引要求を観測・操作可能な状態を形成。
5. 2024年5月31日、DMM Bitcoinの正規取引要求の内容が改変され、4,502.9 BTCが攻撃者管理アドレスへ送付された。

ここで「DMM Bitcoinの秘密鍵が盗まれた」「ブロックチェーンが破られた」とは書かない。公開根拠が示しているのは、委託先を含む取引処理系の完全性侵害である。

# 即応性

DMM Bitcoinは5月31日に流出を公表し、顧客預かりBTCについて全量保証する方針を示した。出庫等に制限を掛けながら、流出相当分のBTC調達を進めた。

一方、攻撃の侵入準備は3月頃まで遡る。5月31日の資産流出まで攻撃者が開発者・業務セッションを利用できたことから、**認証成功を正当利用とみなさず、開発者行動・業務取引・送金完全性を横断監視する必要性**が分かる。

# 財務・事業への影響

窃取額は約482億円相当。単なる一時的なシステム停止ではなく、DMM Bitcoinは最終的に自社で事業継続せず、顧客口座・預かり資産をSBI VCトレードへ移管する方針となった。

SBI VCトレードは2025年3月8日に対象口座・預かり資産の移管を実施した。移管当日から翌日にかけ、一部顧客でパスワード再設定や資産反映の遅延が生じたが解消し、3月12日までに一部JPY出金障害も解消された。[^sbi]

したがって本件の予後は「暗号資産を補填した」で終わらず、**被害企業の暗号資産交換業そのものの終了と顧客基盤移管**に達した。

# 第三者・委託先境界

GincoはDMM Bitcoinのウォレット業務を支える重要な第三者だった。攻撃者は最終被害組織の最外周ではなく、専門ベンダーの開発者・業務経路を狙った。

これは2026年のSaaS・共有基盤事故と同じく、次の原則を示す。

- 「専門業者へ委託した」はリスク移転ではない。
- 委託先の開発者端末・認証・セッションも自社資産の信頼境界になる。
- 高価値操作は、上流システムから届いた要求が正しいことだけで承認しない。
- 送金直前に宛先、金額、要求元、承認者を独立経路で照合する。

# 事故前セキュリティ開示との比較

暗号資産交換業者・ウォレット事業者は制度上も厳しい資産管理・システムリスク管理を要求されるが、本件は規制対象組織の内部統制だけではなく、**業務委託先の開発環境と正規取引プロトコルの完全性**が破られた。

「コールドウォレット比率」「MFA」「秘密鍵管理」だけを事故前安全性の指標とせず、サプライチェーン開発者、セッション保護、トランザクション検証を別項目で評価する必要がある。

# 2026年までの予後

2025年3月にDMM Bitcoin顧客の口座・預かり資産はSBI VCトレードへ移管された。警察庁/FBIの帰属公表は国際的な北朝鮮サイバー活動の代表事例として継続利用されている。

2026年の金融庁資料でも、北朝鮮関係者によるDMM Bitcoinからの約3億800万ドル相当窃取が金融機関向けサイバーリスクの参考事例として取り上げられている。

# 防御上の教訓

- 開発者は高価値の特権主体としてフィッシング・採用詐称・コード実行を想定する。
- 認証情報だけでなくブラウザ/開発セッション窃取を前提とする。
- 正規API通信でも内容改変を検出できる取引完全性検証を行う。
- 高額送金は独立経路・複数主体で最終宛先を再確認する。
- 委託先インシデントが自社の事業廃止にまで波及し得ることをBCPへ含める。
- 被害額だけでなく、顧客資産補償、事業移管、監督対応を長期予後として追う。

# 不明点

- Ginco開発者端末で利用された全マルウェア・永続化手法。
- 取引改変の実装詳細。
- DMM Bitcoin側で事故前に稼働していた全検知・承認統制。
- LLM/生成AIが攻撃に使われた証拠は公表されていない。

[^npa]: 警察庁「北朝鮮を背景とするサイバー攻撃グループTraderTraitorによる暗号資産関連事業者を標的としたサイバー攻撃について」2024-12-24.
[^ginco]: Ginco「当社サービスへのサイバー攻撃に関するご報告」2025-01-28.
[^sbi]: SBI VCトレード「DMM Bitcoinからの移管 特設サイト」および2025-03-03〜12の移管関連公表。