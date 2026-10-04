---
type: Analysis Log
title: インシデント公表の品質・透明性 — 速さだけでなく訂正可能性と行動可能性を評価する
description: サイバー事故の公表を、初報速度、未確定事項、件数単位、訂正履歴、復旧状態、本人行動、規制・市場開示、長期追補などの観点から評価するための枠組み。
tags: [analysis, disclosure, transparency, communication, incident-response, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: nichirei-initial
    resource: https://www.nichirei.co.jp/ir/news/2026/t_in226.html
    title: 当社グループでのシステム障害発生について
    author: organization:株式会社ニチレイ
  - id: nichirei-update7
    resource: https://www.nichirei.co.jp/news/2026/524.html
    title: 当社グループでのシステム障害発生について（第7報）
    author: organization:株式会社ニチレイ
  - id: aflac-faq
    resource: https://www.aflac.co.jp/info/yorisou_faq.html
    title: 当社システムに対する不正アクセスの発生および情報漏えいに関するFAQ
    author: organization:アフラック生命保険株式会社
  - id: ppc-leak-action
    resource: https://www.ppc.go.jp/personalinfo/legal/leakAction/
    title: 漏えい等の対応とお役立ち資料
    author: organization:個人情報保護委員会
  - id: jpx-disclosure
    resource: https://www.jpx.co.jp/equities/listing/disclosure/info/
    title: 適時開示が求められる会社情報
    author: organization:日本取引所グループ
  - id: sec-cyber
    resource: https://www.sec.gov/newsroom/press-releases/2023-139
    title: SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies
    author: organization:U.S. Securities and Exchange Commission
---

# 目的

インシデント公表の品質は、「事故発生から何時間で出したか」だけでは測れない。

初報を早く出せば未確定事項が多くなる。一方、完全調査を待って公表を遅らせれば、顧客・取引先が自衛できない。重要なのは、**未確定であることを明示した早い初報を、その後の確度上昇・訂正・復旧・本人対応へ一貫して接続できるか**である。

本資料は組織のランキングを目的としない。公開情報を防御知識として再利用できる品質か、何がまだ分からないかを評価する。

# 公表品質の十の軸

| 軸 | 主な質問 |
| --- | --- |
| 1. 初報の適時性 | 事故を認識した後、利害関係者が必要な時点で公表されたか |
| 2. 不確実性の明示 | 未確認・調査中・可能性・確認済みを分けているか |
| 3. 件数と単位 | 人数、アカウント、レコード、ファイル等を正しく区別しているか |
| 4. 時系列 | 発生、検知、遮断、公表、復旧、通知を区別できるか |
| 5. 復旧状態 | 「サービス再開」と「調査完了」を混同していないか |
| 6. 訂正可能性 | 初期値の訂正・確度変化が履歴として追えるか |
| 7. 利用者の行動可能性 | パスワード変更、詐欺警戒、問い合わせ先等を具体化しているか |
| 8. 下流影響 | 委託元、顧客、取引先へどの範囲が波及したかを分離しているか |
| 9. 制度・市場対応 | 当局報告、本人通知、市場開示等を必要に応じて明示しているか |
| 10. 長期追補 | 原因、再発防止、財務、二次悪用等を後日更新しているか |

この十軸は数値ランキングより、欠落項目を発見するチェックリストとして使う。

# 1. 初報は「完全さ」ではなく最低限の行動可能性を見る

早い初報では、原因や件数が分からなくてもよい場合がある。最低限、次が重要になる。

- 何が起きているか。
- どのサービス・業務が影響しているか。
- 利用者が今すぐ取るべき行動があるか。
- 組織が何を止めたか。
- 次回更新を行う意思があるか。

原因不明の段階で攻撃手法を推定して書くより、「調査中」と明示する方が情報品質は高い。

# 2. 不確実性を文法として固定する

公表文からDenno Watchへ取り込む際は、次を区別する。

```text
確認した
可能性がある / 否定できない
現時点で確認していない
公表していない
調査中
不明
```

たとえば「現時点で情報漏えいは確認していない」は、`not_observed` に近いが、`confirmed_absent` ではない。その後に漏えい確認へ変化する可能性を残す。

# 3. 件数の訂正は品質劣化ではなく、調査進展の場合がある

初報の最大対象数が大きく、後日調査で確認済み対象が縮小することは不自然ではない。

質の高い履歴では、次を残す。

- 初報時の母集団。
- 後日の確認済み件数。
- 重複排除の有無。
- 通知対象数。
- 訂正理由。

最新値だけへ上書きすると、調査がどう進んだか分からなくなる。

# 4. 技術復旧・業務復旧・調査完了を分ける

「復旧しました」という一文だけでは、何が終わったか判断できない。

少なくとも次を分ける。

1. システムが起動した。
2. 顧客向けサービスを再開した。
3. 受発注・物流等の業務が通常水準へ戻った。
4. 侵入経路・影響範囲を確定した。
5. 本人通知を終えた。
6. 再発防止策を実装した。

OTではさらに、安全確認と通常操業を分離する。

# 国内例: ニチレイの段階公表から読み取れること

ニチレイは2026年7月の事故について、サイバー攻撃の確認、影響業務、個人情報漏えい可能性、順次復旧予定、業績影響は判明次第開示すると公表した。[^nichirei-initial]

その後、複数の続報を経て、9月18日の第7報で、7月24日に全拠点が通常稼働へ移行したこと、個人情報漏えいを確認したこと、9月11日に個人情報保護委員会へ報告したこと、通知と原因・影響範囲調査を継続していることを公表した。[^nichirei-update7]

このような事例は、一つの最終報だけを保存するより、**事実状態がどう変化したか**を時系列で保持する価値を示す。

# 国内例: アフラックの技術FAQから得られる情報粒度

アフラックは2026年の不正アクセスに関するFAQで、最初の不正アクセス日、CPU高負荷の検知時刻、不正アクセスとデータ照会の制御不足、通常利用と同様の形式だったため直ちに不正と判断できなかったこと、短時間の大量照会を監視・制御する機能が不足していたこと等を説明している。[^aflac-faq]

これは「不正アクセスがあった」だけでは得られない防御知識である。

一方、詳細な技術公表が常に正しいとは限らない。未修正の弱点、シークレット、再現手順等、悪用を容易にする情報は公開しない方がよい。透明性は攻撃再現性の最大化ではない。

# 利用者にとっての行動可能性

データ漏えい公表では、利用者は「何件漏れたか」より、自分が何をすべきかを必要とする。

有用な内容:

- 対象者への連絡方法。
- 組織が正規に使用する送信元・ドメイン等の確認方法。
- パスワード変更が必要か。
- 同じパスワードを他サービスで使用している場合の対応。
- 本人確認書類流出時の詐欺・なりすまし警戒。
- 不審な請求・連絡の報告先。
- 組織側がパスワード・トークンを既に無効化したか。
- 問い合わせ窓口の期限。

ただし、必要な行動はデータ種別によって異なるため、定型文だけで済ませない。

# 規制報告と一般公表を混同しない

個人情報保護委員会への報告、所管省庁への報告、警察相談、本人通知、Web公表、TDnet等の市場開示は別経路である。

個人情報保護委員会は一定の漏えい等について速報・確報と本人通知の枠組みを示している。[^ppc-leak-action]

上場会社について、東京証券取引所は投資判断上重要な会社情報の適時開示を求めている。[^jpx-disclosure]

したがって、公表品質の評価では「企業サイトに一報が出た」だけで全ステークホルダーへの対応完了としない。

# 海外比較: 重要性判断と市場開示

米国SECのサイバー開示規則では、上場会社は重要なサイバーインシデントについて、原則として重要性判断後4営業日以内にForm 8-Kで開示する。[^sec-cyber]

日本の期限へ直接読み替えてはならないが、比較軸として次が有用である。

- 検知から重要性判断まで。
- 重要性判断から市場開示まで。
- 初回開示時の不明点。
- 後続10-Q/10-Kで何が追加されたか。

# 公表を一つの「状態機械」として扱う

```text
INITIAL
  ↓
INCIDENT_CONFIRMED
  ↓
SCOPE_UNDER_INVESTIGATION
  ├─ SERVICE_RESTORING
  ├─ DATA_IMPACT_POSSIBLE
  └─ REGULATORY_REPORTING
        ↓
SCOPE_PARTIALLY_CONFIRMED
        ↓
DATA_IMPACT_CONFIRMED_OR_CLOSED
        ↓
NOTIFICATION_IN_PROGRESS
        ↓
ROOT_CAUSE_AND_REMEDIATION
        ↓
LONG_TAIL_MONITORING
```

全事例がこの順序になるわけではない。目的は、現在どの不確実性が残っているかを明示することである。

# 公表履歴のメタデータ候補

```yaml
disclosure_quality:
  initial_disclosure_at: null
  next_update_commitment: unknown
  uncertainty_explicit: unknown
  count_units_clear: unknown
  restoration_distinguished: unknown
  correction_history_preserved: unknown
  user_actions_provided: unknown
  regulatory_channels_disclosed: unknown
  market_disclosure_present: unknown
  long_tail_updates_present: unknown
```

これを単純に10点満点へ合算しない。たとえば利用者行動が不要な事故では `not_applicable` が適切である。

# 公表履歴で避けるべき評価

## 「遅い = 隠蔽」と断定しない

検知日時・事故認識日時が非公表なら、外部から公表所要時間を計算できない。

## 「詳細 = 高品質」と単純化しない

悪用可能な情報を伏せる正当な理由がある。重要なのは、防御・本人保護・投資判断に必要な影響と不確実性が分かること。

## 「訂正 = 信頼性低下」と単純化しない

大規模事故は調査が進めば件数・原因が変わる。訂正を明示し履歴を残すこと自体が透明性である。

## 「更新が止まった = 終了」としない

訴訟、保険、規制、財務、二次悪用は数年続く可能性がある。

# 情報公開の安全性

公表品質を上げるためでも、次は公開すべきではない場合がある。

- 未修正弱点の再現手順。
- 有効な認証情報、トークン、鍵。
- 内部ホスト名・ネットワーク構成の過剰な詳細。
- 個人情報の実例。
- 捜査を阻害する情報。

「なぜ詳細を非公表にするか」を説明できる場合、単なる沈黙より利用者が状態を理解しやすい。

# Denno Watchでの利用法

公表品質は、事故の深刻度や組織のセキュリティ成熟度そのものではない。

Denno Watchでは次に使う。

- 次回調査で何を探すべきか判断する。
- 初報と確報の差を保存する。
- 件数・原因・復旧状態の訂正を追う。
- 利用者保護に必要な情報が公開されたか確認する。
- 比較ケースから良い更新構造を抽出する。

# 関連資料

- [サイバーインシデントの報告・通知・公表マップ](regulatory-reporting-and-disclosure-map-2026-10-04.md)
- [サイバーインシデントの財務・事業影響](incident-financial-and-business-impact-knowledge-base-2026-10-04.md)
- [情報源の監視・鮮度・再確認基準](../methodology/source-monitoring-and-freshness-standard.md)
- [インシデント記録基準](../methodology/reporting-standard.md)
- [データ被害・感度・保持期間](data-harm-sensitivity-and-retention-taxonomy-2026-10-04.md)

[^nichirei-initial]: 株式会社ニチレイ「当社グループでのシステム障害発生について」2026-07-16. https://www.nichirei.co.jp/ir/news/2026/t_in226.html
[^nichirei-update7]: 株式会社ニチレイ「当社グループでのシステム障害発生について（第7報）」2026-09-18. https://www.nichirei.co.jp/news/2026/524.html
[^aflac-faq]: アフラック生命保険株式会社「当社システムに対する不正アクセスの発生および情報漏えいに関するFAQ」 https://www.aflac.co.jp/info/yorisou_faq.html
[^ppc-leak-action]: 個人情報保護委員会「漏えい等の対応とお役立ち資料」 https://www.ppc.go.jp/personalinfo/legal/leakAction/
[^jpx-disclosure]: 日本取引所グループ「適時開示が求められる会社情報」 https://www.jpx.co.jp/equities/listing/disclosure/info/
[^sec-cyber]: U.S. SEC, “SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure by Public Companies” https://www.sec.gov/newsroom/press-releases/2023-139
