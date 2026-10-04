---
type: Analysis Log
title: サイバーインシデントの報告・通知・公表マップ — 日本の制度と実務を事故対応へ接続する
description: 個人情報保護、マイナンバー、金融、重要インフラ、上場会社の適時開示、国家サイバー統括室の共通様式を、インシデントの時間軸と証拠管理へ対応付ける。
tags: [analysis, regulation, incident-reporting, disclosure, privacy, critical-infrastructure, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: ppc-leak-action
    resource: https://www.ppc.go.jp/personalinfo/legal/leakAction/
    title: 漏えい等の対応とお役立ち資料
    author: organization:個人情報保護委員会
  - id: ppc-guideline
    resource: https://www.ppc.go.jp/personalinfo/legal/guidelines_tsusoku/
    title: 個人情報の保護に関する法律についてのガイドライン（通則編）
    author: organization:個人情報保護委員会
  - id: ppc-mynumber
    resource: https://www.ppc.go.jp/legal/rouei/
    title: 特定個人情報の漏えい等事案が発生した場合の対応について
    author: organization:個人情報保護委員会
  - id: nco-unified-reporting
    resource: https://www.cyber.go.jp/policy/group/cyber/policy.html
    title: サイバー攻撃時の報告様式の統一について
    author: organization:国家サイバー統括室
  - id: nco-critical-infra
    resource: https://www.cyber.go.jp/policy/group/infra/policy.html
    title: 重要インフラ対策関連
    author: organization:国家サイバー統括室
  - id: fsa-cyber
    resource: https://www.fsa.go.jp/policy/cybersecurity/
    title: 金融分野におけるサイバーセキュリティ対策について
    author: organization:金融庁
  - id: jpx-disclosure
    resource: https://www.jpx.co.jp/equities/listing/disclosure/info/
    title: 適時開示が求められる会社情報
    author: organization:日本取引所グループ
  - id: sec-cyber-disclosure
    resource: https://www.sec.gov/newsroom/press-releases/2023-139
    title: SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies
    author: organization:U.S. Securities and Exchange Commission
---

# 目的

サイバーインシデントでは、技術対応と同時に「誰へ、何を、いつまでに、どの確度で報告するか」が進行する。Denno Watch の既存資料は、検知、封じ込め、復旧、本人通知、規制対応を個別事例で記録しているが、複数制度を横断して事故対応へ接続する独立した地図はなかった。

本資料は、日本の公開制度を中心に、事故の発覚から速報、調査、本人通知、所管当局への報告、投資家向け公表、長期更新までを一つの時間軸で整理する。これは法的助言ではなく、公開資料を調査・記録するときの観測軸である。実際の報告義務は、組織の業種、法的地位、影響データ、契約、事故の内容によって変わる。

# 最初に分離すべき五つの報告経路

一つの事故で、次の経路が同時に存在し得る。相互に代替できるとは限らない。

| 経路 | 主な相手 | 主な目的 | Denno Watchで分けて記録する事項 |
| --- | --- | --- | --- |
| 個人情報保護 | 個人情報保護委員会等、本人 | 権利利益の保護、法定報告・本人通知 | 報告対象事態、発覚日、速報、確報、本人通知 |
| 業法・監督 | 所管省庁・監督当局 | 業務継続、健全性、利用者保護 | 業種固有の報告、監督当局との連携 |
| 国家サイバー対応 | 国家サイバー統括室、警察、所管省庁等 | 被害把握、官民連携、捜査・対処 | 共通様式の利用、共有同意、相談・連携 |
| 市場開示 | 取引所、投資家 | 投資判断上重要な情報の公平・迅速な開示 | 適時開示の有無、業績影響、重要性判断 |
| 契約・下流通知 | 委託元、顧客、取引先、保険者等 | 契約上の通知、下流被害対応 | 通知開始、対象確定、契約上の期限・要件 |

「当局へ報告済み」と「本人通知済み」、「所管省庁へ報告済み」と「市場へ開示済み」は別の事実として扱う。

# 個人情報保護法上の漏えい等報告

個人情報保護委員会は、一定の漏えい等について報告を義務付けている。公開ガイドラインでは、要配慮個人情報、財産的被害のおそれがある個人データ、不正目的による行為に起因する漏えい等、本人の数が1,000人を超える漏えい等などを報告対象として示している。[^ppc-guideline]

報告期限は、発覚後の**速報がおおむね3〜5日以内**、確報が原則**30日以内**、不正な目的で行われたおそれがある場合は**60日以内**と案内されている。[^ppc-leak-action]

Denno Watchでは最低限、次を分ける。

- `detected_at`: 技術的な検知日時。
- `incident_known_at`: 組織が「漏えい等又はそのおそれ」を認識した基準日。公開されていなければ推定しない。
- `regulatory_initial_reported_at`: 速報を行った日。
- `regulatory_final_reported_at`: 確報を行った日。
- `notification_started_at`: 本人通知を開始した日。
- `notification_completed_at`: 完了が公表された場合のみ記録。

事故発生日と発覚日は同一とは限らない。侵入開始から数か月後に発覚した事例でも、法定期限の起点を公開情報なしに侵入日に置き換えない。

# マイナンバー・特定個人情報

特定個人情報については、個人情報保護委員会が専用の漏えい等対応経路を案内している。2026年10月1日以降、ランサムウェア事案とその他サイバー攻撃等事案では、関係省庁申合せに基づく共通様式を利用できる場合がある。[^ppc-mynumber]

したがって、個別事例でマイナンバーが含まれる場合は単なる「高感度個人情報」とせず、少なくとも以下を独立記録する。

- マイナンバー又は特定個人情報が対象に含まれるか。
- 「含まれる可能性」と「確認済み」を分ける。
- 共通様式を用いたかは、公表がある場合だけ記録する。
- 番号そのものと、本人確認書類画像、給与・税務情報等を混同しない。

# 2026年の重要変更: サイバー攻撃時の共通報告様式

国家サイバー統括室は、複数官公署へ異なる様式で報告する負担を軽減するため、報告様式の統一を進めている。2025年10月からDDoS攻撃とランサムウェア事案の共通様式が運用され、2026年9月15日の改定で既存様式を更新するとともに、**「その他サイバー攻撃等事案」共通様式が新設**された。国家サイバー統括室の案内では、DDoS、ランサムウェア、その他サイバー攻撃等の共通様式が示されている。[^nco-unified-reporting]

これは「すべての報告先が一つになった」という意味ではない。共通様式は報告内容の重複を減らす仕組みであり、実際の提出先、報告義務、本人通知、業法上の手続、警察相談等は事故と組織によって異なる。

Denno Watchでは、今後次を観測対象にする。

1. 被害組織が共通様式の利用を公表したか。
2. 所管省庁、個人情報保護委員会、警察、国家サイバー統括室のどこへ報告・相談したか。
3. 同じ事故について複数の報告経路が存在したか。
4. 共通様式導入後、初報・確報の情報粒度が改善したか。
5. 公表文から、報告負担軽減が初動速度へ寄与したかを確認できるか。確認できなければ不明とする。

# 金融分野

金融庁は「金融分野におけるサイバーセキュリティに関するガイドライン」を公開し、管理態勢、リスク特定、防御、検知、インシデント対応・復旧、サードパーティリスク管理を一体で扱っている。2026年9月には、監督指針等のサイバー事案報告様式を関係省庁申合せの共通様式へ移行する改正も公表された。[^fsa-cyber]

金融事例では、個人情報報告だけでなく次を別軸として追う価値が高い。

- 監督当局への障害・サイバー事案報告。
- 顧客資産、決済、認証、取引継続への影響。
- サードパーティ障害が金融機関の業務へ波及したか。
- 技術復旧と、利用者保護・照合・補償等の完了が同時か。

# 重要インフラ

2026年10月1日、「重要インフラのサイバーセキュリティ対策のための統一基準」が施行された。国家サイバー統括室は、重要インフラ分野間で対策水準にばらつきがあったことを背景に、分野横断の統一基準を整備したと説明している。併せて安全基準等策定ガイドラインも施行され、従来の一部指針・ガイダンスは廃止された。[^nco-critical-infra]

Denno Watchで重要インフラ事故を扱う場合、単なるIT障害としてではなく次を追加観測する。

- 社会機能・人命・安全への影響。
- 他の重要インフラ分野への相互依存。
- 代替運転、手動運転、縮退運転の有無。
- 復旧判断に安全確認が含まれていたか。
- 監督・所管機関への報告と一般公表の時間差。

詳細は [OT・重要インフラの安全・復旧リスク](ot-critical-infrastructure-safety-and-recovery-2026-10-04.md) で扱う。

# 上場会社の適時開示

東京証券取引所は、投資判断に重要な影響を与える会社の業務、運営又は業績等に関する情報を適時開示の対象としている。「災害に起因する損害又は業務遂行の過程で生じた損害」等も発生事実として整理されている。サイバー事故という名称だけで一律に開示義務を判断するのではなく、投資判断上の重要性を確認する必要がある。[^jpx-disclosure]

そのため上場会社の事例では、企業サイト上の「お知らせ」だけでなく、TDnet・決算資料・有価証券報告書等も確認する価値が高い。

観測項目:

- 初回の顧客向け公表日時。
- TDnet等の市場向け公表日時。
- 業績影響額、特別損失、売上影響等が明示されたか。
- 「影響は軽微」「精査中」「業績予想へ織り込み済み」等の経営判断が後日変化したか。
- 復旧費、調査費、補償費、再発防止投資を区別できるか。

# 海外比較: 米国SECの「重要性判断後4営業日」

米国SECは上場会社に対し、重要なサイバーインシデントと判断した場合、原則としてその重要性判断から4営業日以内のForm 8-K開示を求めている。事故発生日や検知日から4日ではなく、重要性を判断した後が起点である。[^sec-cyber-disclosure]

これは日本の法的期限として流用してはならない。ただし、Denno Watchの比較軸として次が有用である。

- 検知から重要性判断までの時間。
- 重要性判断から市場開示までの時間。
- 初回開示時点で未確定だった事項と、その後の訂正・追補。
- 技術詳細を過度に公開せず、投資家に必要な影響情報をどこまで提供したか。

# 報告・通知の時間軸

事故対応では、次の順序が必ずしも一直線ではない。

```text
侵入・異常発生
    ↓
技術的検知
    ↓
事故として認識
    ├─ 封じ込め・証拠保全
    ├─ 個人情報等の速報
    ├─ 所管省庁・監督当局への報告
    ├─ 警察・国家サイバー統括室等への相談・連携
    ├─ 顧客・委託元への契約通知
    └─ 投資家向け重要性判断
           ↓
       必要な市場開示
    ↓
影響範囲の追加調査
    ↓
確報・本人通知・下流通知
    ↓
業績影響・再発防止・長期予後の追補
```

このため、「初報が早い組織ほど調査が完了している」とは限らない。初報の早さと、内容の確度・訂正履歴は別々に評価する。

# 個別インシデントへ追加すると有用なフィールド

公開根拠がある場合に限り、次のフィールドを追加できる。

| フィールド | 意味 |
| --- | --- |
| `incident_known_at` | 組織が報告対象となり得る事故として認識した日時・日付。 |
| `regulatory_initial_reported_at` | 速報・初回報告を行った日。 |
| `regulatory_final_reported_at` | 確報・最終報告を行った日。 |
| `regulatory_channels` | 個人情報保護委員会、所管省庁、監督当局等、公表された報告先。 |
| `law_enforcement_contact` | 警察等への相談・届出・連携。 |
| `market_disclosure` | TDnet等の市場向け開示。 |
| `contractual_notifications` | 委託元・顧客等への契約上の通知。 |
| `notification_started_at` | 本人・顧客等への通知開始。 |
| `notification_completed_at` | 完了が明示された場合のみ。 |
| `disclosure_corrections` | 件数、対象、原因、影響の訂正履歴。 |

# 公開情報の評価で避けるべき誤り

1. **「報告済み」を「法令違反なし」と読み替えない。** 公開情報だけでは適法性を評価できない場合が多い。
2. **「本人通知」を「流出確認人数」と同義にしない。** 予防的に広い母集団へ通知する場合がある。
3. **「警察へ相談」を「犯人特定」と同義にしない。**
4. **「共通様式」を「窓口完全一元化」と書かない。**
5. **「適時開示なし」を「重要性がない」と断定しない。** 判断根拠が公開されない場合がある。
6. **後日の確報で初報が訂正された場合、初報を削除しない。** 証拠状態の変化として残す。

# Denno Watchでの横断分析候補

今後42件の国内事例へ共通項目が十分蓄積すれば、次を横断分析できる。

- 検知から初回公表までの時間。
- 初回公表から影響対象確定までの時間。
- 技術復旧から本人通知完了までの時間差。
- 上場会社の市場開示と顧客向け公表の順序。
- 第三者サービス侵害で、サービス提供者とデータ管理者のどちらが通知主体になったか。
- 共通様式導入前後で、公表される報告先・事実項目に変化があるか。

ただし、公開されていない内部報告時刻を補完推定して統計化してはならない。

# 関連資料

- [サイバーインシデントのライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md)
- [インシデント対応指標と経営判断トリガー](incident-response-metrics-and-decision-triggers-2026-10-04.md)
- [インシデント後の長期予後](post-incident-long-tail-prognosis-2026-10-04.md)
- [データ被害・感度・保持期間の評価](data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md)
- [公開情報の鮮度・監視・再確認基準](../methodology/source-monitoring-and-freshness-standard.md)

[^ppc-guideline]: 個人情報保護委員会「個人情報の保護に関する法律についてのガイドライン（通則編）」 https://www.ppc.go.jp/personalinfo/legal/guidelines_tsusoku/
[^ppc-leak-action]: 個人情報保護委員会「漏えい等の対応とお役立ち資料」 https://www.ppc.go.jp/personalinfo/legal/leakAction/
[^ppc-mynumber]: 個人情報保護委員会「特定個人情報の漏えい等事案が発生した場合の対応について」 https://www.ppc.go.jp/legal/rouei/
[^nco-unified-reporting]: 国家サイバー統括室「サイバー攻撃時の報告様式の統一について」 https://www.cyber.go.jp/policy/group/cyber/policy.html
[^fsa-cyber]: 金融庁「金融分野におけるサイバーセキュリティ対策について」 https://www.fsa.go.jp/policy/cybersecurity/
[^nco-critical-infra]: 国家サイバー統括室「重要インフラ対策関連」 https://www.cyber.go.jp/policy/group/infra/policy.html
[^jpx-disclosure]: 日本取引所グループ「適時開示が求められる会社情報」 https://www.jpx.co.jp/equities/listing/disclosure/info/
[^sec-cyber-disclosure]: U.S. SEC, “SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies” https://www.sec.gov/newsroom/press-releases/2023-139
