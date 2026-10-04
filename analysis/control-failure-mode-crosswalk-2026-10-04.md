---
type: Analysis Log
title: 失敗モードと防御統制の対応表 — 個別事故を再発防止策へ接続する
description: 国内事例で観測される侵入・拡大・復旧失敗の型を、NIST CSF 2.0、NIST SP 800-61r3、CISA CPG、経済産業省・金融庁の公開指針へ対応付ける。
tags: [analysis, controls, failure-modes, defense, nist-csf, incident-response, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: nist-csf
    resource: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1299.pdf
    title: NIST Cybersecurity Framework 2.0 Resource & Overview Guide
    author: organization:NIST
  - id: nist-ir
    resource: https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations
    title: NIST Revises SP 800-61: Incident Response Recommendations and Considerations for Cybersecurity Risk Management
    author: organization:NIST
  - id: cisa-cpg
    resource: https://www.cisa.gov/cybersecurity-performance-goals
    title: Cross-Sector Cybersecurity Performance Goals
    author: organization:CISA
  - id: meti-management
    resource: https://www.meti.go.jp/policy/netsecurity/mng_guide.html
    title: サイバーセキュリティ経営ガイドラインと支援ツール
    author: organization:経済産業省
  - id: fsa-cyber
    resource: https://www.fsa.go.jp/policy/cybersecurity/
    title: 金融分野におけるサイバーセキュリティ対策について
    author: organization:金融庁
---

# 目的

個別インシデントから「MFAを入れる」「バックアップを取る」といった一般論だけを抽出すると、実際に壊れた境界と対策が対応しない。逆に、公開情報から侵入経路が確定していない事故へ特定製品や設定を原因として割り当てると推測になる。

本資料では、Denno Watchの国内事例で反復して観測できる**失敗モード**を単位にし、そこから防御側が確認すべき統制、証拠、運用指標を整理する。NIST CSF 2.0は統治・識別・防御・検知・対応・復旧の六機能でリスク管理を整理し、SP 800-61r3はインシデント対応を組織全体のリスク管理へ統合している。CISA CPGは高いリスク低減効果が期待できる基礎的実践を優先している。[^nist-csf][^nist-ir][^cisa-cpg]

本資料の対応表は「この対策があれば事故を確実に防げた」という反実仮想の断定ではない。

# 証拠の三層

| 層 | 意味 | 書き方 |
| --- | --- | --- |
| A: 事故で確認済み | 公開資料が原因・経路・欠陥を明示 | 「VPNアカウント悪用が公表された」等 |
| B: 事故から直接導ける防御要件 | 影響事実から必要な境界を論理的に確認可能 | 「共有基盤の侵害が複数顧客へ波及したため、顧客単位の分離と下流通知能力が重要」 |
| C: 一般的な推奨統制 | 公的フレームワークが推奨するが、当該事故との因果は未確認 | 「耐フィッシングMFAを優先候補とする」等 |

個別事故レポートへはAとBを中心に書き、Cは横断分析へ置く。

# 失敗モード別の対応表

| 失敗モード | 公開事例で観測し得る兆候 | 優先する統制 | CSF 2.0上の主領域 | 測るべき指標 |
| --- | --- | --- | --- | --- |
| 認証情報の侵害 | VPN、クラウド、メール、管理アカウントの悪用 | 強固なMFA、資格情報のローテーション、条件付きアクセス、特権分離 | Protect / Detect | MFA適用率、特権アカウント数、異常ログイン検知時間 |
| 既知・未知脆弱性の悪用 | 公開サーバー、BI、API、VPN等への侵入 | 資産把握、露出面管理、脆弱性優先順位付け、緊急修正手順 | Identify / Protect | インターネット公開資産の把握率、重大修正の所要時間 |
| 過大な到達権限 | 一つの認証・管理面から広いデータや複数顧客へ到達 | 最小権限、管理面分離、顧客分離、短命資格情報 | Protect | 管理者権限保有者、横断アクセス可能範囲、権限レビュー周期 |
| サードパーティ集中 | 一社の侵害で複数顧客・委託元へ波及 | 契約・技術両面の分離、下流通知、出口計画、監査可能性 | Govern / Identify | 重要委託先依存数、代替不能サービス数、通知SLA |
| データ集中・長期保持 | 大量の本人情報、退職者情報、本人確認書類等が一か所へ蓄積 | 収集最小化、保持期限、分割、暗号化、アクセス監査 | Govern / Protect | 保持年数、削除対象残存率、1資格情報あたり到達データ量 |
| ログ不足・検知遅延 | 侵入時点が長期間不明、後日調査で発覚 | 重要ログ集中、時刻同期、検知ルール、保全期間 | Detect | 検知までの時間、重要ログ取得率、保全期間 |
| セグメント不十分 | 業務系・グループ・顧客基盤へ影響拡大 | ネットワーク・ID・管理面の分離、経路制限 | Protect | セグメント間許可経路数、管理面共用率 |
| バックアップ不足・同時侵害 | 復旧長期化、データ削除、暗号化 | オフライン/分離バックアップ、復元試験、構成バックアップ | Protect / Recover | 復元試験成功率、RPO/RTO実測、バックアップ分離状態 |
| クリーン復旧の証明不足 | サービス再開後も再侵入条件が不明 | 根絶確認、資格情報全面更新、既知良好状態から再構築 | Respond / Recover | 再構築範囲、再発監視期間、再認証完了率 |
| 通知・報告準備不足 | 影響範囲確定や本人通知が長期化 | データ所在台帳、連絡先整備、報告テンプレート、法務連携 | Govern / Respond | 対象特定時間、速報準備時間、通知不能率 |
| OT遠隔アクセスの脆弱性 | 制御系へ外部から到達、安全・操業へ影響 | 強固な遠隔アクセス、分離、ジャンプ経路、手動代替 | Protect / Recover | 外部到達可能OT資産、遠隔セッション監査率 |

# 1. 認証情報の侵害

Denno Watchでは、[両毛システムズ](../incidents/2026/ryomo-systems-ransomware-supply-chain.md)、[扶桑電通](../incidents/2026/fuso-dentsu-cloud-storage-breach.md)、[日本資産総研](../incidents/2026/nihon-shisan-souken-ransomware-leak.md)など、公開資料で認証情報・アカウント悪用が重要な文脈となる事例を収録している。

ここで見るべきなのは「MFAの有無」だけではない。

- 人間のログインだけでなく、APIキー、サービスアカウント、同期資格情報を含むか。
- 認証成功後に一つのアカウントでどこまで到達できたか。
- 管理者・通常利用者・委託先の権限境界が分離されていたか。
- 資格情報失効後、既存セッションやトークンも無効化できたか。
- 退職者・異動者・委託終了者の権限が残っていないか。

「MFA導入率100%」でも、回復コード、セッショントークン、サービスアカウント、管理APIが例外なら実際の境界は残る。指標は例外を含めて測る。

# 2. 脆弱性管理はCVSSだけで優先しない

[LEAN BODY](../incidents/2026/lean-body-metabase-breach.md)、[VOISING](../incidents/2026/voising-bi-tool-breach.md)、[KDDI](../incidents/2026/kddi-isp-mail-breach.md)など、脆弱性が事故文脈に現れる事例では、公開された深刻度だけでなく実際の露出・到達範囲が重要になる。

優先順位は少なくとも次を組み合わせる。

1. インターネットから到達可能か。
2. 実際に悪用が観測されているか。
3. 認証なし又は低権限から悪用可能か。
4. 管理面・認証基盤・大量データへ到達するか。
5. 代替緩和策があるか。
6. 修正適用に停止リスクがあるか。

CISAのKnown Exploited Vulnerabilities Catalogのような「実悪用」を優先する外部情報は、CVSSと別軸で使う価値がある。

# 3. サードパーティと共有基盤

[ApplyNow](../incidents/2026/applynow-recruitment-platform-breach.md)、[両毛システムズ](../incidents/2026/ryomo-systems-ransomware-supply-chain.md)、[日本テレネット](../incidents/2026/nippon-telenet-ransomware-bpo-breach.md)、[KDDI](../incidents/2026/kddi-isp-mail-breach.md)のような事例では、被害組織数だけでなく**共有されていた権限・データ・復旧経路**が重要である。

委託先評価では次の質問を優先する。

- 一つの管理者資格情報で複数顧客へ到達できるか。
- 顧客ごとの暗号鍵、DB、テナント、バックアップが分離されているか。
- 委託先停止時に自社だけで最低限の業務を継続できるか。
- 事故時に「どの顧客のどのデータへアクセスされたか」をログで切り分けられるか。
- サービス提供者とデータ管理者の通知責任が契約で明確か。

詳細は [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md) を参照する。

# 4. データ保持そのものを攻撃面として扱う

第一生命の事例では長期間にわたる退職者情報、タイムズカーでは本人確認書類、KDDIでは大規模な認証情報というように、データの「量」だけではなく、**変更できるか、失効できるか、何年悪用可能か**が事故後リスクを決める。

防御統制として、保存時暗号化だけでは不十分である。

- そもそも保持する必要があるか。
- 保持期限を超えたデータを自動削除できるか。
- 本番処理に不要な原本画像を分離できるか。
- 一つのアカウントから過去全期間へ到達できないよう時間・用途で分割できるか。
- 分析・バックアップ・ログへ複製されたデータも削除方針の対象か。

詳細は [データ被害・感度・保持期間の評価](data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md) で扱う。

# 5. ログと検知の設計

インシデント後に「侵入経路不明」「影響範囲を調査中」が長く続く場合、必ずしもログ不足が原因とは限らない。しかし、防御側では調査に必要な証拠を平時から保持できるかを測る必要がある。

最低限の観測点:

- ID基盤の認証・トークン発行・権限変更。
- VPN、リモートアクセス、管理コンソール。
- クラウド監査ログ。
- EDR等の端末イベント。
- 大量データ読み出し・エクスポート。
- API管理操作。
- バックアップ削除・設定変更。
- ログ設定そのものの変更。

`ログ取得率`は「何台が送信しているか」だけでなく、事故調査に必要なイベントが保持され、改ざんされにくく、必要期間を遡れるかで評価する。

# 6. 復旧統制

[コープやまぐち](../incidents/2026/coop-yamaguchi-line-miniapp-breach.md)のようにバックアップから早期復旧できた事例と、長期停止・クリーン再構築が必要だった事例を同じ「バックアップあり」でまとめてはならない。

復旧能力は次の積で決まる。

```text
復旧能力
= 復元可能なデータ
× 信頼できる構成
× 利用可能な資格情報
× 分離された復旧環境
× 復元手順の実測
× 業務側の受入確認
```

バックアップが存在しても、同じ管理面から削除可能、暗号化済み、構成情報がない、復元試験をしていない、必要な外部SaaSが停止している場合は実効的な復旧能力が低い。

# 7. 経営統制

経済産業省のサイバーセキュリティ経営ガイドラインVer.3.0は、サイバーリスクを経営課題として扱い、体制、人材、サプライチェーン、インシデント対応を経営側の責務へ接続する。[^meti-management]

経営会議へ報告すべき指標は製品導入数よりも、次のような残存リスクへ寄せる。

- インターネット公開資産の未把握数。
- MFA例外となる特権アカウント。
- 復元試験に失敗した重要サービス。
- 単一委託先停止で継続不能になる業務。
- 保持期限を超えた高感度データ。
- ログ保持期間より長い潜在侵入期間。
- 事故時に連絡不能な重要委託先・顧客。

# 統制の優先順位を決める方法

「重要だから全部やる」では予算配分にならない。Denno Watchでは次の順で優先度を決める。

1. **一つの失敗で多数の事故型を止められる統制** — 例: 強固なID境界、資産把握、分離バックアップ。
2. **復旧不能を避ける統制** — バックアップ、構成保存、代替業務、連絡網。
3. **被害範囲を制限する統制** — 最小権限、テナント分離、ネットワーク分離。
4. **調査不能を避ける統制** — ログ、時刻同期、保全。
5. **事故後の尾部を短くする統制** — データ最小化、通知準備、契約・保険・法務連携。

# 個別事例へ追加すると有用な統制評価

公開情報だけで記録できる場合、次の形で残す。

```yaml
control_evidence:
  confirmed_existing:
    - "公表資料で実施済みと確認できた統制"
  confirmed_gap:
    - "組織自身が不足・不備として公表した事項"
  post_incident_changes:
    - "事故後に導入・強化を公表した統制"
  defensive_inference:
    - "事故事実から一般化した防御上の示唆。因果は断定しない"
```

「事故が起きたのでEDRがなかった」「MFAがなかった」と推定してはならない。未公表なら `unknown` のまま保持する。

# 関連する公的フレームワークの使い分け

| 資料 | Denno Watchでの用途 |
| --- | --- |
| NIST CSF 2.0 | 統治から復旧までを一貫した分類に使う。製品チェックリストにはしない。 |
| NIST SP 800-61r3 | インシデント対応を平時のリスク管理・改善へ戻す循環の設計に使う。 |
| CISA CPG | 人員・予算が限られる組織で、高効果の基礎統制を優先する参考にする。 |
| 経産省 サイバーセキュリティ経営ガイドライン | 日本企業の経営責任、体制、人材、サプライチェーンへ接続する。 |
| 金融庁ガイドライン | 金融分野の管理態勢、検知、対応・復旧、サードパーティ管理を補う。 |

# 次に深掘りすべき領域

- 各国内42事例に対する失敗モードの機械可読タグ付け。
- 「確認済み原因」と「推定される防御策」を別カラムにした比較表。
- 事故前に存在した統制と、事故後に追加された統制の差分。
- 再発した組織で、過去の是正策がどこまで有効だったかの長期追跡。
- 防御予算モデルと本対応表を接続し、1円当たりの複数失敗モード低減効果を評価する。

# 関連資料

- [2026年 日本の重大サイバーインシデント — 攻撃パターン、現実的対抗策、防衛予算モデル](incident-defense-budget-analysis-2026-10-04.md)
- [第三者・認証・集中リスク](third-party-identity-concentration-risk-2026-10-04.md)
- [サイバーインシデントのライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md)
- [インシデント対応指標と経営判断トリガー](incident-response-metrics-and-decision-triggers-2026-10-04.md)

[^nist-csf]: NIST, “Cybersecurity Framework 2.0: Resource & Overview Guide” https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1299.pdf
[^nist-ir]: NIST, “NIST Revises SP 800-61: Incident Response Recommendations and Considerations for Cybersecurity Risk Management” https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations
[^cisa-cpg]: CISA, “Cross-Sector Cybersecurity Performance Goals” https://www.cisa.gov/cybersecurity-performance-goals
[^meti-management]: 経済産業省「サイバーセキュリティ経営ガイドラインと支援ツール」 https://www.meti.go.jp/policy/netsecurity/mng_guide.html
