---
type: Reference
title: Denno Watch 情報源の監視・鮮度・再確認基準
description: インシデント記録と横断分析を継続更新するため、情報源の優先順位、確認時刻、更新検知、鮮度、差分、上書き禁止、長期追跡のルールを定義する。
tags: [methodology, sources, freshness, monitoring, provenance, maintenance]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: ppc-leak-action
    resource: https://www.ppc.go.jp/personalinfo/legal/leakAction/
    title: 漏えい等の対応とお役立ち資料
    author: organization:個人情報保護委員会
  - id: nco-unified-reporting
    resource: https://www.cyber.go.jp/policy/group/cyber/policy.html
    title: サイバー攻撃時の報告様式の統一について
    author: organization:国家サイバー統括室
  - id: npa-cyber
    resource: https://www.npa.go.jp/publications/statistics/cybersecurity/
    title: サイバー空間をめぐる脅威の情勢等
    author: organization:警察庁
  - id: ipa-top10
    resource: https://www.ipa.go.jp/security/10threats/10threats2026.html
    title: 情報セキュリティ10大脅威 2026
    author: organization:情報処理推進機構
  - id: jpcert-reports
    resource: https://www.jpcert.or.jp/pr/
    title: JPCERT/CC 活動報告・インシデント報告・インターネット定点観測レポート
    author: organization:JPCERT/CC
  - id: jvn
    resource: https://jvn.jp/
    title: Japan Vulnerability Notes
    author: organization:JVN
  - id: cisa-kev
    resource: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
    title: Known Exploited Vulnerabilities Catalog
    author: organization:CISA
  - id: jpx-tdnet
    resource: https://www.jpx.co.jp/equities/listing/disclosure/tdnet/index.html
    title: TDnetの概要
    author: organization:日本取引所グループ
---

# 目的

インシデント記録は、公開時点では未確定の情報を多く含む。初報では「影響を調査中」、後日「流出確認」、さらに数か月後に「件数訂正」「本人通知完了」「業績影響確定」と変化することがある。

Denno Watchでは、**最後に公表された日**と**最後に新情報がないか確認した日**を同じものとして扱わない。本基準は、公開情報をいつ、どこで、どの優先順位で再確認し、何が変わったときにレコードを更新するかを定義する。

# 時刻を四種類に分ける

| 項目 | 意味 | 更新条件 |
| --- | --- | --- |
| `source_published_at` | 情報源が公表された日時・日付 | 情報源ごとに固定 |
| `latest_public_update` | 当該事故について反映した最新の一次公表日 | 新しい一次公表を反映したときだけ |
| `public_record_checked_at` | より新しい公開情報がないか能動確認した時刻 | 確認するたび更新可能 |
| `retrieved_at` | 特定の出典を取得・保存した時刻 | 出典取得ごと |

新しい公表が見つからなかった場合、`latest_public_update` は変えず、`public_record_checked_at` のみ更新する。

# 情報源の階層

## 第1層: 事故主体・責任主体の一次情報

- 被害組織。
- 親会社・子会社。
- サービス運営事業者。
- 事故調査結果として組織が公表した資料。
- 上場会社のTDnet等の正式開示。

事故の件数、影響、復旧、原因、通知については最優先する。

## 第2層: 権限ある公的機関

- 個人情報保護委員会。
- 国家サイバー統括室。
- 警察庁・都道府県警察。
- 金融庁、総務省、経済産業省等の所管・監督機関。
- その他の規制当局・自治体等。

制度、法定報告、統計、捜査上公表された事実、分野別指針に使う。

## 第3層: 直接影響を受けた顧客・委託元・取引先

サービス提供者が詳細を公表していない場合でも、顧客側通知から下流影響が確認できることがある。ただし、顧客の通知をサービス提供者自身の侵害範囲へ無制限に一般化しない。

## 第4層: 脅威・脆弱性の公的／準公的観測

- JPCERT/CC。
- JVN。
- IPA。
- 警察庁の情勢・統計。
- 海外比較ではCISA KEV等。

これらは「当該組織がその手法で侵害された」と証明する資料ではない。事故で確認済みの製品・脆弱性・攻撃型を、外部の悪用状況や一般的傾向へ接続するために使う。

## 第5層: 信頼できる二次報道・研究

一次情報に存在しない独立観測、決算・裁判・長期予後等を補完する。後日の一次情報と矛盾した場合は、一次情報を優先して訂正履歴を保持する。

# 情報源別の監視対象

| 情報源 | 主に確認する内容 | 推奨する確認契機 |
| --- | --- | --- |
| 被害組織のニュース・障害情報 | 初報、件数、原因、復旧、通知、再発防止 | 活動中事故は高頻度、安定後は段階的に間隔を延ばす |
| 個人情報保護委員会 | 漏えい報告制度、ガイドライン、本人通知 | 制度改定時、個人情報事例の方法論更新時 |
| 国家サイバー統括室 | 共通報告様式、重要インフラ、政府方針 | 制度・様式改定時 |
| 金融庁等の監督機関 | 業種固有の監督・レジリエンス | 該当業種の事例、制度改定時 |
| 警察庁 | 半期・年次の脅威情勢、統計 | 新しい半期・年次資料公表時 |
| IPA | 年次の10大脅威、注意喚起 | 年次更新・重要追補時 |
| JPCERT/CC | 四半期の活動・インシデント・定点観測 | 四半期更新時、特定脅威の背景確認時 |
| JVN | 国内製品を含む脆弱性情報 | CVE/JVNが事故で公表された場合、重要脆弱性の背景確認時 |
| CISA KEV | 実悪用が確認された脆弱性 | 脆弱性優先順位の背景情報が必要なとき |
| TDnet・決算資料 | 業績影響、適時開示、損失、復旧 | 上場会社事故の初報後、四半期・年度決算時 |

2026年度からJPCERT/CCは、活動四半期報告、インシデント報告対応レポート、インターネット定点観測レポートを統合した形で四半期情報を提供している。[^jpcert-reports]

# 事故の状態に応じて確認間隔を変える

固定の「毎日確認」を全事例へ適用すると、古い事故に監視資源を消費し、新しい重大更新を見落としやすい。次はDenno Watchの**保守優先順位**であり、法的期限ではない。

| 状態 | 例 | 推奨再確認 |
| --- | --- | --- |
| P0 活動中 | サービス停止中、原因・影響調査中、重大下流影響 | 24〜72時間を目安に、新規公表の有無を確認 |
| P1 収束中 | サービス復旧済みだが件数・通知・原因未確定 | 約1週間ごと、重要公表があれば即時 |
| P2 経過観察 | 調査・通知まで概ね完了、長期予後待ち | 1〜3か月ごと、決算・当局公表等の節目 |
| P3 長期追跡 | 訴訟、保険、二次悪用、再発、是正効果 | 半年〜1年ごとの節目調査 |

公開情報が極端に少ない事例では、確認頻度を上げても新情報が増えるとは限らない。重要度と更新可能性の両方で資源を配分する。

# 更新を発生させる差分

次のいずれかが変わった場合は、単なる再確認ではなく実質更新として扱う。

1. 原因・侵入経路・攻撃型が新たに確定又は訂正された。
2. 最大対象数、確認済み取得数、通知対象数が変わった。
3. 新しいデータ種別、特に認証・本人確認・医療・金融・マイナンバー等が判明した。
4. サービス又は業務の復旧段階が変わった。
5. 外部流出・攻撃者サイト掲載・二次悪用が新たに確認された。
6. 本人通知・顧客通知・監督当局報告の状態が変わった。
7. 決算・適時開示で費用・業績影響が明らかになった。
8. 再発防止策又はシステム再構築方針が具体化した。
9. 公表済み内容が訂正・撤回された。
10. 後続インシデントが過去事故の是正効果を評価する材料になった。

文面変更だけで事実状態が変わらない場合は、不要な更新履歴を増やさない。

# 「新情報なし」を証拠として過大評価しない

`public_record_checked_at` が新しいことは、「公開情報を確認した」ことを示すだけである。

次を意味しない。

- 事故が完全に終息した。
- 二次悪用が存在しない。
- 規制・捜査が終了した。
- 非公表の追加被害がない。
- 侵入経路が存在しない。

したがって、「2026-10-04時点で新しい公表を確認できなかった」と「2026-10-04時点で問題が存在しない」を明確に分ける。

# 情報源自体の状態を記録する

外部ページは移動、置換、削除される。可能な場合、出典ごとに次を保持する。

```yaml
source_status:
  published_at: 2026-09-30
  last_modified_at: null
  retrieved_at: 2026-10-04T20:57:00+09:00
  state: active
  supersedes: null
  superseded_by: null
  immutable_revision: null
```

`state` の候補:

- `active`: 現行の公開ページ。
- `superseded`: 後続資料に置き換えられた。
- `withdrawn`: 発行主体が撤回・廃止した。
- `moved`: URLが変更された。
- `unavailable`: 以前は確認できたが現在取得不能。
- `archived`: 公式アーカイブ等から参照している。

同じURLの本文が静かに差し替えられる場合があるため、日付・題名・発行主体をURLだけに依存せず保持する。

# 仕様・標準は版を固定する

OKFのように同じ版番号のまま本文が変化し得る仕様は、版番号だけでなく参照コミット等の不変識別子を保持する。Denno Watchの `index.md` が `okf_version` と `okf_spec_revision` を分離しているのはこのためである。

同様に、次を区別する。

- 確定版とドラフト。
- 現行版と廃止版。
- ガイドライン本体とFAQ・補足資料。
- 制度の決定日と施行日。

# 脆弱性情報を事故へ結び付ける条件

JVN、CISA KEV、ベンダーアドバイザリ等で重大脆弱性が公開されていても、当該事故の侵入経路とは限らない。

個別事例へCVE/JVNを結び付けるのは、原則として次のいずれかがある場合に限る。

- 被害組織が脆弱性を明示した。
- 調査主体・監督当局が当該事故との関連を明示した。
- 信頼できる一次技術報告が当該侵害との関連を示した。

外部で実悪用が確認されているだけの場合は、「背景情報」として分離する。CISA KEVは実際に悪用された脆弱性の優先順位付けに有用だが、個別事故の原因証明ではない。[^cisa-kev]

# 市場・財務情報の長期確認

上場会社の事故は、技術復旧後の四半期・年度決算で初めて費用や業績影響が明らかになる場合がある。TDnetは上場会社の適時開示情報を伝達・公開する仕組みとして用いられる。[^jpx-tdnet]

確認対象:

- 事故関連損失・特別損失。
- 売上・出荷・受注への影響。
- 調査、復旧、補償、外部専門家、再構築の費用。
- 保険金収入。
- 業績予想の変更。
- 後続決算での追加費用又は見積変更。

事故直後に「業績影響は精査中」とされている場合は、精査中という状態自体を保持し、推計値で埋めない。

# 長期予後の再確認

技術復旧後も次を追う価値がある。

- 本人確認情報等の二次悪用。
- 訴訟・和解・行政措置。
- 保険・求償。
- 顧客・取引先への補償。
- サービス廃止又は事業撤退。
- 再発。
- 公表した再発防止策の後続結果。

長期追跡では、事故直後の一次ページだけでなく、決算、統合報告書、裁判・当局資料、後続事故の公表も調べる。

# 調査キューを機械可読にする場合

今後、規模が大きくなった場合は、次のような保守キューを別ファイル又は自動処理で持てる。

```yaml
research_queue:
  - incident: times-car-web-breach
    priority: P2
    next_check_after: 2027-01-04
    watch_for:
      - secondary_abuse
      - regulatory_update
      - financial_impact
    last_checked_at: 2026-10-04T20:57:00+09:00
```

`next_check_after` は「この日まで新情報が存在しない」という意味ではなく、通常の再確認予定である。重大公表を別経路で検知した場合は前倒しする。

# 公開脅威情報の定期基準点

Denno Watchの個別事例から一般傾向を論じる場合、母集団がDenno Watchの収録基準に偏っていることを明示する。外部基準点として、少なくとも次を使い分ける。

- 警察庁: 国内のサイバー脅威情勢・統計。[^npa-cyber]
- IPA: 組織・個人が注目すべき脅威の年次整理。[^ipa-top10]
- JPCERT/CC: インシデント報告対応とインターネット観測の四半期情報。[^jpcert-reports]
- JVN: 国内向け脆弱性情報。[^jvn]

外部統計とDenno Watch事例集の件数を同じ母集団として合算しない。

# 更新時の最小チェックリスト

1. 既存レコードの `latest_public_update` と `public_record_checked_at` を確認する。
2. 被害組織の一次ページを確認する。
3. 必要に応じて規制当局・顧客・市場開示を確認する。
4. 新しい事実と単なる再掲を分ける。
5. 旧値を消さず、訂正・確度変化を時系列へ残す。
6. 件数の単位と母集団を維持する。
7. 新しい主張へ出典を結び付ける。
8. 新情報がなくても、能動確認を行った場合だけ `public_record_checked_at` を更新する。
9. 索引・横断分析へ影響する変更なら関連資料も更新する。
10. `log.md` に実質的な変更を記録する。

# 関連資料

- [インシデント記録基準](reporting-standard.md)
- [2026年 重大インシデント事例集監査](corpus-audit-2026-10-04.md)
- [報告・通知・公表マップ](../analysis/regulatory-reporting-and-disclosure-map-2026-10-04.md)
- [インシデント後の長期予後](../analysis/post-incident-long-tail-prognosis-2026-10-04.md)
- [失敗モードと防御統制の対応表](../analysis/control-failure-mode-crosswalk-2026-10-04.md)

[^ppc-leak-action]: 個人情報保護委員会「漏えい等の対応とお役立ち資料」 https://www.ppc.go.jp/personalinfo/legal/leakAction/
[^nco-unified-reporting]: 国家サイバー統括室「サイバー攻撃時の報告様式の統一について」 https://www.cyber.go.jp/policy/group/cyber/policy.html
[^npa-cyber]: 警察庁「サイバー空間をめぐる脅威の情勢等」 https://www.npa.go.jp/publications/statistics/cybersecurity/
[^ipa-top10]: 情報処理推進機構「情報セキュリティ10大脅威 2026」 https://www.ipa.go.jp/security/10threats/10threats2026.html
[^jpcert-reports]: JPCERT/CC「活動報告・インシデント報告対応レポート・インターネット定点観測レポート」 https://www.jpcert.or.jp/pr/
[^jvn]: JVN https://jvn.jp/
[^cisa-kev]: CISA “Known Exploited Vulnerabilities Catalog” https://www.cisa.gov/known-exploited-vulnerabilities-catalog
[^jpx-tdnet]: 日本取引所グループ「TDnetの概要」 https://www.jpx.co.jp/equities/listing/disclosure/tdnet/index.html
