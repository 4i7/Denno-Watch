---
type: Analysis
title: ローカルLLM実用化以降の重大インシデント比較 — 2023〜2025年
description: ローカル実行可能なLLMが実用段階へ入った2023年7月前後から2025年までの国内重大インシデントを、初動、復旧、長期予後、事故前統制、株主・規制資料の共通軸で比較する。
tags: [analysis, historical-corpus, local-llm, incident-response, governance, disclosure, 2023, 2024, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T14:22:00+09:00 }
sources:
  - id: meta-cse1
    resource: https://ai.meta.com/research/publications/purple-llama-cyberseceval-a-benchmark-for-evaluating-the-cybersecurity-risks-of-large-language-models/
    title: Purple Llama CyberSecEval
  - id: meta-cse2
    resource: https://ai.meta.com/research/publications/cyberseceval-2-a-wide-ranging-cybersecurity-evaluation-suite-for-large-language-models/
    title: CYBERSECEVAL 2
  - id: meta-cse3
    resource: https://ai.meta.com/research/publications/cyberseceval-3-advancing-the-evaluation-of-cybersecurity-risks-and-capabilities-in-large-language-models/
    title: CYBERSECEVAL 3
  - id: anthropic-aug2025
    resource: https://www.anthropic.com/news/detecting-countering-misuse-aug-2025
    title: Detecting and countering misuse of AI — August 2025
  - id: anthropic-espionage
    resource: https://www.anthropic.com/news/disrupting-AI-espionage
    title: Disrupting the first reported AI-orchestrated cyber espionage campaign
  - id: anthropic-sep2026
    resource: https://www.anthropic.com/threat-intelligence-report-september-2026
    title: Detecting and countering misuse of AI — September 2026
  - id: historical-scope
    resource: https://github.com/4i7/Denno-Watch/blob/main/methodology/local-llm-era-corpus-scope-2026-10-05.md
    title: ローカルLLM時代のインシデント補助コーパス — 対象期間と評価基準
---

# 結論

Denno Watchでは、**2023年7月18日以降**をローカルLLM時代のコア比較期間とする。この境界は、一般利用者が実用的なオープンウェイトLLMを自前の計算資源で継続利用できる環境が成立した時代区分であり、「その日から企業侵害にLLMが使われた」という因果境界ではない。

2023〜2024年の公開評価は、LLMがコード生成、調査、攻撃支援、ソーシャルエンジニアリング、自律的な攻撃工程へ意味のある能力を持ち始めたことを示す。2025年には、犯罪・諜報作戦でAIが偵察、脆弱性探索、資格情報収集、データ分析、外部送信等の複数工程へ組み込まれた実運用例が公開された。2026年の脅威インテリジェンスでも悪用形態の継続的な変化が報告されている。[^meta-cse1][^meta-cse2][^meta-cse3][^anthropic-aug2025][^anthropic-espionage][^anthropic-sep2026]

一方、ここで比較する日本国内26件について、公開根拠だけから個別攻撃へのAI/LLM利用を認定できる事例はない。各事例は `era_context_only` として扱い、**攻撃能力を取り巻く時代背景**と**個別事故の原因**を分離する。

# AI攻撃能力の時代区分

## 2023: 攻撃支援能力を脅威モデルへ含める段階

Llama 2、Code Llama等により、個人が自前の計算資源でコード生成・説明・調査補助を継続利用できる環境が一般化した。2023年12月のMeta CyberSecEvalは、安全でないコード生成とサイバー攻撃支援要求への応答を独立した評価対象とし、LLMのサイバーリスクを定量評価の対象にした。[^meta-cse1]

この時点から、偵察、スクリプト生成、翻訳、文面生成、ログ整理、既知技術の組合せ等の作業単価低下を防御側の脅威モデルへ含めることには合理性がある。ただし、企業侵害の原因へLLM利用を自動付与する根拠にはならない。

## 2024: exploit・社会工学・自律攻撃の評価が本格化

CyberSecEval 2はソフトウェア脆弱性の自動exploit生成を評価し、コーディング能力を持つモデルが優位である一方、完全な自動exploit能力には限界があることを示した。CyberSecEval 3では、自動ソーシャルエンジニアリング、人間主導攻撃のスケーリング、自律的な攻撃オペレーションへ評価範囲が広がった。[^meta-cse2][^meta-cse3]

従って2024年は、攻撃工程の自動化可能性を実測する段階へ入った年として扱うが、エンドツーエンドの完全自動侵害が一般化した年とはみなさない。

## 2025: 複数攻撃工程への実運用上の組込み

Anthropicは2025年8月、少なくとも17組織を狙うデータ窃取・恐喝作戦で、攻撃者がClaude Codeを利用して偵察、データ分析、攻撃作業を大きくスケールさせた事例を公表した。[^anthropic-aug2025]

同社が2025年11月に公表した別の諜報作戦では、約30組織が標的となり、AIが偵察、脆弱性発見、exploit、横展開、資格情報収集、データ分析、外部送信等を高い自律度で担い、少数の侵入成功が確認された。[^anthropic-espionage]

これらは「AIが攻撃者の補助ツールである」段階から、「攻撃ワークフローの複数工程を実行する構成要素である」段階への移行を示す。

## 2026: 悪用形態の継続的変化

Anthropicの2026年9月脅威インテリジェンスは、2025年12月から2026年8月までに検知・妨害した悪用事例を取り上げ、2025年の既報以降もAIを組み込んだ攻撃手法が変化していることを報告している。[^anthropic-sep2026]

この事実は2026年の脅威環境を評価する根拠にはなるが、日本国内の特定インシデントでAIが使われたことの証拠にはならない。

| 時点 | 防御側が意味として取るべき変化 | 個別事故への扱い |
| --- | --- | --- |
| 2023-07 | 実用的なローカルLLMを一般利用者が継続運用できる時代へ | 比較コーパスのコア境界 |
| 2023-12 | 攻撃支援・安全でないコード生成が公開ベンチマーク上の明示的リスクへ | 攻撃作業単価低下の背景証拠 |
| 2024-04〜07 | exploit、社会工学、自律攻撃の能力評価が本格化 | 能力拡大の過渡期 |
| 2025 | 犯罪・諜報作戦でAIが複数の攻撃工程へ実運用投入 | 実運用上の転換点 |
| 2026 | 脅威インテリジェンス上で悪用形態の継続的変化を観測 | 現行脅威環境。個別帰属とは分離 |

# 国内26件の比較コーパス

## 2025年

| 事例 | 類型 | 比較上の主題 |
| --- | --- | --- |
| [快活CLUB / FiT24](../incidents/2025/kaikatsu-club-unauthorized-access.md) | 会員システム不正アクセス | 729万件の漏えい可能性、即時隔離、約1か月のアプリ制限、実流出未確認 |
| [NTTコミュニケーションズ](../incidents/2025/ntt-communications-unauthorized-access.md) | 不正アクセス | EDR/NDR/UEBA等の事故前公表、初動と全侵害範囲確定の時間差 |
| [保険見直し本舗グループ](../incidents/2025/hoken-minaoshi-honpo-ransomware.md) | ランサムウェア | ネットワーク機器、即時隔離、保険会社への下流影響、24時間監視・CISO体制 |
| [損保ジャパン](../incidents/2025/sompo-japan-web-system-breach.md) | Webサブシステム不正アクセス | Zero Trust/SASE/SOC等の事故前公表、大規模保険データ、金融庁報告徴求 |
| [PR TIMES](../incidents/2025/pr-times-unauthorized-access.md) | 管理者画面侵害 | IP許可例外、共有アカウント、残存プロセス、発表前情報、段階的な再発防止実装 |
| [IIJ / IIJセキュアMX](../incidents/2025/iij-secure-mx-zero-day.md) | 未公知脆弱性悪用 | 8か月超の潜伏、メール・認証情報、通信の秘密、行政指導 |
| [審調社](../incidents/2025/shinchosa-ransomware.md) | ランサムウェア | ネットワーク機器脆弱性、保護ソフト無効化、医療情報、委託先波及 |
| [ハウステンボス](../incidents/2025/huis-ten-bosch-breach.md) | 不正アクセス・暗号化 | リモートアクセス機器、約150万人規模の顧客情報、機微な従業員情報、BCP |
| [ローレルバンクマシン / Jijilla](../incidents/2025/laurel-bank-machine-jijilla-breach.md) | 身代金要求を伴う不正アクセス | AI-OCR、反復認証攻撃、DB削除・窃取可能性、CSIRT/ISO等の平時公表 |
| [アサヒグループHD](../incidents/2025/asahi-group-ransomware.md) | ランサムウェア | 約10日前の侵入、ゼロトラスト移行前端末、権限管理、物流・会計・内部統制 |
| [ASKUL](../incidents/2025/askul-ransomware.md) | ランサムウェア | 約4か月半の潜伏、MFA例外、EDR/監視カバレッジ、バックアップ、物流・IR |
| [サンリオエンターテイメント](../incidents/2025/sanrio-entertainment-ransomware.md) | ランサムウェア | リモートアクセス機器、初期最大約200万件→最終漏えい未確認、約6か月復旧 |

## 2024年

| 事例 | 類型 | 比較上の主題 |
| --- | --- | --- |
| [富士通](../incidents/2024/fujitsu-stealth-malware.md) | 検知回避型マルウェア | CISO等の事故前ガバナンス、49台、未知・回避型挙動への検知適応 |
| [HOYA](../incidents/2024/hoya-cyberattack.md) | サイバー攻撃・データ流出 | 複数業務停止、復旧後約1年を経た個人データ流出確定 |
| [DMM Bitcoin](../incidents/2024/dmm-bitcoin-tradertraitor.md) | 社会工学・取引完全性侵害 | TraderTraitor、約4,502.9 BTC、事業終了と顧客資産移管 |
| [イセトー](../incidents/2024/iseto-ransomware.md) | ランサムウェア | VPN、便宜保存・削除不徹底、ISO 27001/27017・PrivacyMark停止→再開、経営体制再構築 |
| [ニデックインスツルメンツ](../incidents/2024/nidec-instruments-ransomware.md) | ランサムウェア | 管理者資格情報、EDR即応、翌日バックアップ復旧、国内外グループ波及 |
| [KADOKAWA / ドワンゴ](../incidents/2024/kadokawa-ransomware.md) | ランサムウェア | private cloud、遠隔再起動、出版/Web/教育、翌年度財務影響 |
| [カシオ計算機](../incidents/2024/casio-ransomware.md) | ランサムウェア | 事故前の訓練・監視・ゼロトラスト・ISO 27001と、海外を含む実装不足の比較 |

## 2023年

| 事例 | 類型 | 比較上の主題 |
| --- | --- | --- |
| [エムケイシステム / 社労夢](../incidents/2023/mk-system-sharomu-ransomware.md) | SaaSランサムウェア | 最大約2,242万人管理、弱い認証・パッチ・ログ監視不備、数千の委託元報告・IR影響 |
| [名古屋港NUTS](../incidents/2023/nagoya-port-nuts-ransomware.md) | ランサムウェア | コア境界直前、保守VPN、港湾物流、約60時間の復旧 |
| [セイコーグループ](../incidents/2023/seiko-group-ransomware.md) | ランサムウェア | 約6万人、EDR/MFA等の事故後強化 |
| [LINEヤフー](../incidents/2023/line-yahoo-shared-auth-breach.md) | 委託先・共有認証侵害 | 共通認証・ネットワーク、第三者集中、2026年規制当局向け最終報告 |
| [JAXA](../incidents/2023/jaxa-vpn-m365-breach.md) | VPN装置侵害→Microsoft 365 | 外部通報、未知マルウェア、資格情報窃取、情報分離、2025年度まで恒久対策 |
| [カシオ ClassPad.net](../incidents/2023/casio-classpad-development-environment.md) | 開発環境DB侵害 | 開発環境の設定・運用、翌年の別系統ランサムウェアとの長期比較 |
| [NTT西日本グループ](../incidents/2023/ntt-west-insider-data-exfiltration.md) | 内部不正 | 約10年、特権アクセス、初期調査失敗、2026年までの長期是正 |

# 即応性は一つの時間では測れない

可視障害に対する隔離が速くても、侵入自体を長期間検知できていない場合がある。また、初期遮断後に別経路・別装置・クラウド側資格情報・永続化が残る場合もある。

| 組織 | 最も早い公開上の攻撃活動 | 組織の認知 | 主な初期封じ込め | その後に残った工程 |
| --- | --- | --- | --- | --- |
| アサヒ | 障害の約10日前 | 2025-09-29 07:00頃 | 11:00頃にネットワーク・データセンター隔離 | 侵害範囲、情報影響、物流・会計復旧、内部統制評価 |
| ASKUL | 2025-06-05 | 2025-10-19 | 同日物理遮断 | 外部クラウド不正アクセス、認証情報変更、物流・決算復旧 |
| NTTコミュニケーションズ | 公開上不明 | 2025-02-05 | 装置Aを当日制限 | 装置B侵害を2月15日に特定・隔離、全スコープ確定 |
| IIJ | 2024-08-03以降 | 2025-04-10 | 経路特定後に切り離し | 影響範囲、顧客通知、行政対応 |
| サンリオ | 2025-01-21 | 同日 | 認知後隔離 | サービス復旧、最終フォレンジック、漏えい有無確定 |
| 保険見直し本舗 | 2025-02-16 | 同日 | 関連サーバーを直ちに隔離 | 下流通知、最終調査、再発防止 |
| ニデックインスツルメンツ | 2024-05-26認知時点で活動確認 | 2024-05-26 | 当日EDR等で駆除 | 翌日最低限業務継続、約2か月の情報影響調査・通知 |

比較では最低でも、`detection_latency`、`initial_containment_latency`、`scope_determination_latency`、`credential_reset_latency`、`persistence_eradication_latency`、`service_restoration_latency`、`public_disclosure_latency` を分ける。

# 事故前統制と実際の失敗面

## エムケイシステム

事故発覚時のWebサイトでは強いセキュリティ管理を表示していた一方、個人情報保護委員会は、弱い利用者・管理者パスワード、重大なセキュリティ更新未適用、ログ保管・監視不足等を具体的に認定した。宣言と実装の差を規制当局資料で直接比較できる。

## ASKUL

事故前の統合報告では情報セキュリティを重要な経営課題として扱い、ISMS、冗長化、バックアップ等を説明していた。事故後調査では、MFA例外、一部サーバーへのEDR未導入、24時間監視対象外、オンラインバックアップの耐ランサム性不足が具体的に判明した。

## アサヒグループHD

グループ共通サイバーセキュリティ基準等を事故前に公表していた一方、事故後にはゼロトラスト移行前PC、パスワード上の弱点、権限管理等が論点となった。方針の有無より、移行完了、例外、旧資産、権限運用を評価する必要がある。

## イセトー

ISO/IEC 27001、ISO/IEC 27017、PrivacyMarkを取得していたが、VPN侵入に加えて、本来扱わないサーバーへの受託データ便宜保存と削除不徹底が被害範囲へ影響した。事故後には第三者認証の一時停止と是正後の再開まで観測できる。

## ニデックインスツルメンツ

不正アクセス防御や不正プログラム検知・即時駆除を事故前に公表しており、事故当日のEDR等による駆除と翌日のバックアップ復旧は実際に機能した。一方、管理者資格情報の侵害とグループ波及は防げなかった。統制を「有効／無効」の二値で評価できない例である。

## NTTコミュニケーションズ

EDR/NDR/UEBA等を事故前に公表しており、不審ログの検知自体は機能した。一方、別装置の侵害特定まで10日を要した。製品導入有無ではなく、検知後の相関、隣接資産調査、全侵害範囲確定速度を評価する。

詳細な証拠対応は [事故前統制と実侵害のギャップ](pre-incident-control-gap-comparison-2023-2025-2026-10-05.md) と [事故前セキュリティ・株主／規制向け資料台帳](pre-incident-security-and-ir-pdf-ledger-2023-2025.md) に分離する。

# 株主・規制・経営資料で見える長期予後

サービス復旧だけでは事故は終わらない。公開記録では、次の影響が数か月から数年残る。

- 本人・顧客・委託元への追加通知。
- 規制当局の行政指導、報告徴求、監督対応。
- ISO/PrivacyMark等の第三者認証停止・再開。
- 決算発表延期、有価証券報告書等の提出期限延長。
- 特別損失、売上・利益影響、配当修正、役員報酬。
- 内部統制上の重要な不備。
- 事業撤退、サービス終了、顧客資産移管。
- 事故後に発表した統制の実装・試験・独立評価。

ASKULとアサヒは、事故前の経営向け統制説明から、事故後の技術原因、財務影響、法定開示、統制是正まで連続して追える。エムケイシステムは規制当局による具体的な技術的不備認定と株主向け財務影響を同時に追える。イセトーは第三者認証の停止・再開を含む予後を追える。

# 横断して現れる防御上の失敗面

1. **外部境界機器** — VPN、リモートアクセス機器、ネットワーク装置、メール基盤。
2. **ID・権限** — MFA例外、盗用資格情報、管理者権限、共有アカウント、委託先資格情報。
3. **カバレッジの穴** — EDR未導入サーバー、監視対象外、ゼロトラスト移行前端末、例外資産。
4. **長期潜伏** — ランサムウェア実行日や障害発生日より前からの侵入・探索。
5. **復旧基盤** — オンラインバックアップの同時被害、クリーンな新環境の再構築、復元後照合。
6. **データ配置・保持** — 一時コピー、便宜保存、削除不徹底、削除済みデータの残存。
7. **第三者集中** — SaaS、保険代理店、共通認証、メールセキュリティ等の単一点波及。
8. **検知後のスコープ確定** — 初期遮断後に別装置・別経路・クラウド・永続化が残る問題。
9. **財務・法定開示への波及** — 決算延期、報告書提出期限延長、特別損失、内部統制の重要な不備。

AIが攻撃者の調査、コード生成、並列処理、反復作業のコストを下げても、企業側で繰り返し破られているのはAI固有の脆弱性だけではない。ID、境界機器、例外、監視、バックアップ、データ保持、第三者依存といった既存の弱点を、より高速・低コストに探索・悪用される前提で評価する必要がある。

# 証拠上の限界

- 国内26件で攻撃者のAI/LLM利用を示す公開証拠は確認されていない。
- AI能力の時代区分は、公開モデル、評価、脅威インテリジェンスから設定した背景情報であり、個別事故の因果関係ではない。
- 事故前PDFや認証は文書・認証範囲の存在を示すが、全資産での実装・運用品質を証明しない。
- 事故後の再発防止策は、公表時点で効果が実証されたことを意味しない。
- `not_observed` は不存在の証明ではない。

[^meta-cse1]: Meta, “Purple Llama CyberSecEval,” 2023-12-07.
[^meta-cse2]: Meta, “CYBERSECEVAL 2,” 2024-04-18.
[^meta-cse3]: Meta, “CYBERSECEVAL 3,” 2024-07-23.
[^anthropic-aug2025]: Anthropic, “Detecting and countering misuse of AI: August 2025,” 2025-08-27.
[^anthropic-espionage]: Anthropic, “Disrupting the first reported AI-orchestrated cyber espionage campaign,” 2025-11-13.
[^anthropic-sep2026]: Anthropic, “Detecting and countering misuse of AI: September 2026,” 2026-09.
