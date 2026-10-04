---
type: Methodology
title: 過去インシデント・事故前セキュリティ開示の収集基準
description: 2023年以降の過去事例を2026年事例と同じ粒度で収集し、事故前の統合報告・セキュリティ開示と実際の侵害境界を時系列を崩さず比較するための基準。
tags: [methodology, historical-incidents, pre-incident, disclosure, ir, evidence]
status: active
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T22:14:00+09:00 }
---

# 適用範囲

Denno Watchでは、2023年を「ローカルLLMが一般の個人・小規模主体でも現実的な補助道具となり始めた観測開始年」とする。ただしこの区分は**時代背景を切るためのもの**であり、個別インシデントをLLM起因と分類する根拠にはしない。

2023年以降の国内重大事例を2026年コーパスと同じ証拠基準で収録し、必要に応じて海外比較を追加する。

# 収録優先度

次のいずれかを満たす事例を優先する。

1. 長時間・広範な事業停止。
2. 大規模または高感度な個人・機密情報。
3. 重要インフラ・物流・金融・医療等への物理/社会波及。
4. SaaS、クラウド、委託先、共有基盤を通じた多数組織への波及。
5. 大きな財務損失、決算遅延、事業撤退、配当等への影響。
6. 行政指導、認証停止、訴訟、組織再編等の長期予後。
7. 事故前に高度なセキュリティ統制を公表しており、実際の失敗境界と比較価値が高い。
8. 復旧・BCP・クリーンリストア・手作業運用等の教訓が具体的。

# 必須の時間軸

少なくとも次を分ける。

```yaml
earliest_known_activity: null
detected_at: null
incident_known_at: null
first_disclosed_at: null
contained_at: null
service_restored_at: null
business_normalized_at: null
regulatory_final_report_at: null
latest_public_update: null
public_record_checked_at: null
```

不明な時刻を推定で埋めない。最古の確認済み活動と攻撃開始推定も分ける。

# 事故前セキュリティ開示

統合報告書、サステナビリティ報告、ガバナンス報告、セキュリティ方針、有価証券報告書等から、**事故前に既に外部公表されていた統制だけ**を抽出する。

```yaml
pre_incident_security_disclosure:
  - published_at: null
    document_type: integrated_report
    source: null
    stated_controls: []
    rollout_scope: unknown
    quantified_kpis: []
    claim_status: stated
```

## 状態を混ぜない

- `stated`: 文書で方針・体制として記載。
- `planned`: 導入予定。
- `in_progress`: 展開途中。
- `implemented`: 実装済みと会社が説明。
- `tested`: 演習・復旧試験等の証拠あり。
- `independently_assessed`: 第三者審査・監査等あり。
- `operationally_observed`: 実事故で機能したことが観測された。

例: 「ゼロトラストを推進」と「侵害端末へゼロトラスト適用済み」は同じではない。

# PDF資料台帳

株主・投資家・事故前セキュリティ資料は次の形で記録する。

```yaml
disclosure_documents:
  - published_at: null
    title: null
    document_type: shareholder_notice
    temporal_role: pre_incident | incident | post_incident | prognosis
    url: null
    organization: null
    relevant_pages: []
    claims_supported: []
```

優先資料:

- 統合報告書。
- サステナビリティ/ESG報告書。
- コーポレートガバナンス報告書。
- 有価証券報告書・半期報告書。
- 決算短信・決算説明資料。
- 適時開示PDF。
- 株主総会招集通知・臨時株主総会資料。
- 行政機関・規制当局PDF。
- 独立調査委員会報告書。
- ISO/Pマーク等の審査・停止・再開に関する一次資料。

# 「対策していたのに侵害」の評価ルール

次の短絡を禁止する。

- 認証取得済み → 侵害資産も安全だった。
- CISO/SOCがある → 検知可能だった。
- EDR導入 → 全端末へ適用済みだった。
- MFA導入 → 特権/海外/委託先を含む全アカウントで強制されていた。
- ゼロトラスト導入 → 旧端末・旧ネットワークが消えていた。
- 事故後にEDR/MFAを強化 → 事故前には一切なかった。

比較は必ず三列にする。

| 事故前に公表された統制 | 実際に観測された失敗境界 | 事故後に追加・強化された統制 |
| --- | --- | --- |
| 事実のみ | 事実と推定を分離 | 状態（計画/実装/試験）を付与 |

# 即応性

少なくとも次を記録する。

```yaml
response_timeliness:
  detection_source: null
  detection_delay: unknown
  first_containment_action: null
  containment_delay: unknown
  regulator_contact: null
  law_enforcement_contact: null
  external_forensics_engaged: null
  customer_notification_started: null
```

時間が速い/遅いだけで評価せず、初回遮断後の二次侵入、見落とし、追加調査、業務停止コストも併記する。

# 復旧

技術・業務・安全性を分ける。

- `technical_restoration`: システムを動かせた。
- `clean_restoration`: 残存脅威・資格情報・バックアップ整合性を確認した。
- `business_restoration`: 注文・出荷・決算等が通常能力に戻った。
- `regulatory_closure`: 当局報告や行政対応が完了した。
- `long_tail_prognosis`: 訴訟、本人通知、認証、組織再編、再発防止が継続。

# AI/LLM関連性

AI関連性は次の状態のみを使用する。

```yaml
ai_llm_relation:
  era_context: post_local_llm_inflection
  evidence_of_use: none_public | reported | confirmed
  role: unknown
```

公開証拠なしにフィッシング文面、マルウェア、脆弱性探索等を「AI生成」と推定しない。

# 予後の追跡

最低でも次を再確認する。

- 30〜90日: 調査範囲・復旧・本人通知。
- 6か月: 財務影響・行政・再発防止実装。
- 1年: 統合報告・内部統制・訴訟・追加通知。
- 2〜3年: 再発、認証、組織再編、長期財務・評判・規制。

この周期は法定期限ではなくDenno Watchの知識保守目安である。

# 重要な原則

**事故前の自己評価、事故中の実測、事故後の再発防止、現在の状態を同じ時制で書かない。**

これにより、「対策していたのに侵害された企業」を宣伝文句への皮肉ではなく、統制の適用範囲・例外・移行状態・検知実効性を分析する資料として扱う。