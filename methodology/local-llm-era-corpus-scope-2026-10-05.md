---
type: Methodology
title: ローカルLLM時代のインシデント補助コーパス — 対象期間と評価基準
description: 2026年中心の事例集を、一般利用者がローカル環境で実用的なLLMを運用できるようになった時期まで遡って補完するための対象期間、AI関与の証拠基準、事故前統制・初動・予後の追加観測項目を定義する。
tags: [methodology, historical-corpus, local-llm, incident-response, governance, provenance, 2023, 2024, 2025]
status: draft
stale_after: 2027-01-05T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
sources:
  - id: meta-llama2
    resource: https://ai.meta.com/blog/llama-2/
    title: Meta and Microsoft Introduce the Next Generation of Llama
    author: organization:Meta
  - id: meta-llama2-license
    resource: https://ai.meta.com/llama/license/
    title: Llama 2 Community License Agreement
    author: organization:Meta
  - id: mistral7b
    resource: https://mistral.ai/news/announcing-mistral-7b/
    title: Mistral 7B
    author: organization:Mistral AI
  - id: reporting-standard
    resource: https://github.com/4i7/Denno-Watch/blob/main/methodology/reporting-standard.md
    title: Denno Watch インシデント記録基準
---

# 目的

Denno Watch の国内個別事例は2026年を主対象として構築されてきた。本資料は、その比較基盤を過去へ拡張し、**一般利用者が自前の計算資源上で実用的な大規模言語モデル（LLM）を継続運用できるようになった時代**以降の重大インシデントを補助コーパスとして収録するための境界を定義する。

この境界は「その日以降の攻撃がLLMを使った」という意味ではない。攻撃者によるAI利用は、被害組織、捜査機関、攻撃基盤の運営者、セキュリティ研究者等による具体的な根拠がある場合だけ記録する。時代的にローカルLLMが利用可能だったという事実と、個別事案の因果関係を分離する。

# 対象期間

## コア期間の起点: 2023年7月18日

Metaは2023年7月18日にLlama 2を公開し、研究・商用利用向けにモデルへのアクセスを開いた。公開物にはモデルコード、学習済み重み、推論・学習・微調整を可能にする構成が含まれる。[^meta-llama2][^meta-llama2-license]

続いてMistral AIは2023年9月27日に7.3BパラメータのMistral 7BをApache 2.0で公開し、公式に「ローカルを含む任意の場所」で利用できることを明示した。[^mistral7b]

このためDenno Watchでは、**2023年7月18日以降**を「ローカルLLM時代」のコア調査期間とする。これは社会・攻撃経済性を比較するための時代区分であり、性能が一夜で閾値を超えたという主張ではない。

## 直前比較ケース

2023年7月4日に発生した名古屋港統一ターミナルシステム（NUTS）のランサムウェア被害は、コア期間のわずか2週間前であり、港湾・物流・VPN・復旧・事業継続の比較基準として価値が高い。そのため、**直前比較ケース**として例外的に収録する。

# AI関与の状態

各事例には、公開根拠が意味を持つ場合に次の `ai_relation` を付与できる。

| 状態 | 意味 |
| --- | --- |
| `ai_use_evidenced` | 個別事案で攻撃者等がAI/LLMを利用したことを具体的根拠が裏付ける。 |
| `ai_use_alleged` | 当事者・研究者等が利用を主張しているが、独立した裏付け又は十分な技術証拠がない。 |
| `era_context_only` | ローカルLLMが実用可能な時代の事案だが、個別攻撃へのAI利用を示す公開証拠はない。 |
| `unknown` | 公開情報だけではAI利用の有無を判断できない。 |
| `not_applicable` | AI関係の評価が事例比較に意味を持たない。 |

`era_context_only` を「AIを使っていない」と読み替えてはならない。これは単に、公開根拠から個別のAI利用を立証できないことを示す。

# 既存記録基準へ追加する観測軸

過去事例を現在の2026年事例と同じ比較面へ載せるため、[インシデント記録基準](reporting-standard.md)の標準フィールドに加え、根拠がある場合は以下を記録する。

## 事故前の環境・統制公表

```yaml
pre_incident_control_disclosure:
  state: confirmed | partial | not_found | unknown
  published_at: null
  sources: []
  declared_controls: []
  applicability_to_failure_surface: direct | partial | indirect | unknown
```

対象とする資料には次を含む。

- 統合報告書、年次報告書、有価証券報告書
- サステナビリティ報告書、ESG資料
- 情報セキュリティ基本方針、CSIRT・SOC・CISO等の体制説明
- BCP、バックアップ、ゼロトラスト、脆弱性管理、認証、監視等の説明
- 株主総会招集通知、決算説明資料、投資家向け説明資料
- ISMS等の認証の公表

公表されていた統制が存在することは、その実装範囲・運用品質・有効性を証明しない。また、事故が起きたことだけを理由に、公表内容が虚偽だったと推定しない。

## 即応性

公開時刻・日付の精度を保ったまま、可能な場合は以下を算出する。

| 指標 | 定義 |
| --- | --- |
| `detection_latency` | `earliest_known_activity` から組織が異常を検知するまで。初期侵入時刻が不明なら算出しない。 |
| `containment_latency` | 検知又は事故認識から、主要な侵入経路遮断・ネットワーク隔離等の封じ込めまで。 |
| `public_disclosure_latency` | 事故認識から最初の対外公表まで。法的な報告期限適合性とは別評価。 |
| `service_restoration_latency` | 業務停止開始から主要サービス再開まで。全面復旧と部分復旧を分離。 |

公表精度が「日付のみ」の場合、時間単位の値を捏造しない。

## 市場・株主向け影響

```yaml
market_ir_effect:
  disclosure_present: confirmed | not_found | unknown
  disclosure_channels: []
  accounting_or_reporting_delay: confirmed | not_observed | unknown
  disclosed_financial_effect: null
  executive_accountability: null
```

技術事故が、決算発表延期、法定開示期限延長、業績予想撤回、特別損失、配当、役員報酬、株主総会説明等へ接続した場合に記録する。

## 予後・再発防止の実効性

`prognosis_checked_at` を用いて、サービス復旧後も次を追う。

- 本人通知・取引先通知の完了
- 規制当局・捜査機関への確報、行政指導、勧告等
- 再発防止策の `announced` / `implemented` / `tested` / `independently_assessed` / `operationally_observed` の区別
- 後続の同型又は近接インシデント
- サービス廃止、事業撤退、事業譲渡
- 訴訟、補償、保険、長期財務影響
- 1年後・2年後等の統合報告書や株主向け資料での総括

# 「事故前に対策を公表していた企業」の比較原則

事故前の資料と事故後の原因を比較する際は、次の順序を守る。

1. `pre_incident_declared_control` — 事故前に何を公表していたか。
2. `observed_failure_surface` — 実際にどの境界・統制・運用で事故が成立したか。
3. `control_applicability` — 公表統制がその失敗面へ直接、部分的、間接的に適用されるか。
4. `response_latency` — 検知・封じ込め・公表・復旧の速度。
5. `operational_ir_tail` — 業務・会計・市場開示への長期影響。
6. `post_incident_change` — 事故後に何を変更し、その実装をどこまで確認できるか。

これにより、「対策を公表していたのに侵害された」という単純な対比ではなく、**宣言された統制の適用範囲と、実際に破られた境界の差**を評価する。

# 調査対象の優先順位

過去事例は全公表を網羅する一覧ではなく、少なくとも次の一つを満たす事例を優先する。

- 大規模又は機微な個人・認証情報
- 長期の事業停止又は社会インフラ影響
- 第三者・SaaS・共有認証・サプライチェーンへの波及
- ランサムウェア、破壊、暗号資産窃取等の重大な完全性・財務被害
- 詳細な初動時系列が公開されている
- 事故前統制資料と事故後原因の比較価値が高い
- 1年以上の長期予後を追跡できる

# 出典管理

既存の[インシデント記録基準](reporting-standard.md)を継承し、一次資料を優先する。特にPDFは、発行主体、発行日、資料名、版を保持し、Web上の要約だけでページ内容を代替しない。事故後に更新・差し替えされた資料の場合は、事故前から存在した統制説明なのか、事故後の回顧説明なのかを区別する。

[^meta-llama2]: Meta, “Meta and Microsoft Introduce the Next Generation of Llama,” 2023-07-18.
[^meta-llama2-license]: Meta, “Llama 2 Community License Agreement,” release date 2023-07-18.
[^mistral7b]: Mistral AI, “Mistral 7B,” 2023-09-27.