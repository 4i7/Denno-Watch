---
type: Evidence Ledger
title: 2023〜2025年 事故前セキュリティ・株主／規制向けPDF台帳
description: 重大インシデントについて、事故前に企業が公開していたセキュリティ・統合報告資料と、事故後の調査・株主・財務・規制資料を分離して記録し、宣言された統制と実際の失敗面の比較可否を示す。
tags: [evidence-ledger, pdf, pre-incident-controls, ir, shareholder, regulatory, cybersecurity, 2023, 2024, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
---

# 目的

インシデント後の「再発防止策」を事故前から存在していた統制と誤認しないため、資料を次の4種類に分離する。

1. **事故前の統制資料** — 統合報告書、サステナビリティ報告書、情報セキュリティ報告等。
2. **事故そのものの調査資料** — 初報、フォレンジック結果、最終報告。
3. **株主・財務資料** — 適時開示、決算、株主総会、有価証券報告、内部統制報告等。
4. **規制・下流資料** — 行政指導、委託元・顧客組織の通知等。

事故前資料に書かれた統制は、**文書上の方針・施策・認証の存在**を示す。全資産・全拠点への実装、例外の不存在、運用品質、有効性までは証明しない。

# 重点比較 — 事故前の統制公表が明確な企業

| 組織 | 事故前資料 | 事故前に公表していた主な統制 | 事故後に確認された失敗面 | 比較評価 |
| --- | --- | --- | --- | --- |
| カシオ計算機 | [サステナビリティレポート2023](https://www.casio.co.jp/content/dam/casio/global/corporate/csr/report/2023/sustainability-report-2023-10.pdf) | 国内外の定期教育、標的型攻撃メール訓練、不審通信監視強化、ゼロトラストネットワーク、クラウドチェックリスト、ISO 27001範囲拡大 | 2024年事故後、フィッシング対策と海外拠点を含むグローバルネットワークセキュリティ体制の一部不備を公表 | **直接比較価値が高い**。施策の存在と海外拠点までの適用・運用品質を分離する必要 |
| ASKUL | [ASKUL Report 2024](https://www.askul.co.jp/corp/assets/pdf/ASKUL_Report_2024E.pdf) / [日本語IR資料室](https://www.askul.co.jp/corp/investor/library/ir/) | 情報セキュリティを重要な経営課題、ISMS、システム冗長化、バックアップ、セキュリティ強化 | MFA例外の管理アカウント、一部サーバーEDR未導入、24時間監視対象外、オンラインバックアップのランサムウェア耐性不足 | **直接比較価値が高い**。高位統制より実カバレッジ・例外管理が失敗面 |
| アサヒグループHD | [Integrated Report 2024](https://s3-ap-northeast-1.amazonaws.com/asahigroup-doc/company/policies-and-report/pdf/en/2024_all.pdf) | グループ共通サイバーセキュリティ基準、対策評価、セキュリティシステム維持・強化、インシデント情報集約 | 拠点ネットワーク機器経由の侵入、パスワード上の弱点、ゼロトラスト移行前PC、後に一部ITインフラのアクセス権限管理等の重要な不備 | **直接比較価値が高い**。共通基準と実装・移行・権限運用を分離 |
| NTTコミュニケーションズ | [サステナビリティレポート2024](https://www.ntt.com/content/dam/nttcom/hq/jp/about-us/csr/report/pdf/nttcom_sr2024.pdf) | EDR/NDRに加えUEBA導入完了、セキュリティ運用自動化、セキュリティ委員会、IT/OT資産管理・ガバナンス | 不審ログを実際に検知し装置Aを制限したが、装置Bの侵害特定・隔離は10日後 | **直接比較価値が高いが「製品が無効」とは言えない**。検知後の相関・スコープ確定能力を評価 |
| 富士通 | [Fujitsu Group Sustainability Data Book 2023 — Information Security](https://www.fujitsu.com/jp/documents/about/resources/reports/sustainabilityreport/2023-report/fujitsudatabook2023-06.pdf) | 専任CISO、リージョンCISO、グローバル一貫ポリシー、情報セキュリティ責任者、脆弱性管理等 | 2024年、検知回避・偽装型マルウェアが社内業務PC49台へ横展開。事故後に固有挙動を監視ルールへ反映 | **比較価値あり**。高位ガバナンスと未知・回避型挙動への検知適応速度を分離 |

# 事故後・株主・財務・規制資料

## ASKUL — 技術事故が経営・市場開示へ直結

- [ランサムウェア攻撃の影響調査結果および安全性強化に向けた取り組みのご報告（PDF）](https://pdf.irpocket.com/C0032/PDLX/O3bg/N4O3.pdf)
- [IRニュース一覧](https://www.askul.co.jp/corp/investor/release/) — 決算発表延期、半期報告書提出期限延長、特別損失、業績予想取り下げ、配当予想修正、役員報酬減額等を時系列で追跡可能。
- [アスクルのサイバーセキュリティ](https://www.askul.co.jp/corp/security/) — 事故後の時系列とSOC・EDR・ログ監視・BCP等の継続強化。

評価上は、10月19日の物理遮断だけでなく、10月22日の外部クラウド不正アクセス、10月23〜24日の認証情報・MFA・EDR対応までを一つの封じ込め過程として扱う。

## アサヒグループHD — 株主・有報・内部統制まで長期化

- [2026-02-18 再発防止策とガバナンス体制の強化](https://www.asahigroup-holdings.com/newsroom/detail/20260218-0101.html)
- [2026-03-24 有価証券報告書の提出期限延長申請](https://www.asahigroup-holdings.com/newsroom/detail/20260324-0105.html)
- [第102回定時株主総会招集通知（PDF）](https://www.asahigroup-holdings.com/pdf/en/ir/event/shareholders/260220_1.pdf)
- [2026-07-27 財務報告に係る内部統制の重要な不備](https://www.asahigroup-holdings.com/en/newsroom/detail/20260727-0204.html)

本件は、ランサムウェアが物流だけでなく会計・監査・法定開示・株主説明・内部統制評価へ波及した基準例である。

## IIJ — 事故調査から行政指導まで

- [2025-04-22 第2報（PDF）](https://www.iij.ad.jp/news/pressrelease/2025/pdf/20250422_SMX_2.pdf)
- [2025-07-18 総務省行政指導について（PDF）](https://www.iij.ad.jp/news/pressrelease/2025/pdf/20250718_SMX3.pdf)

未公知脆弱性、認証情報・メール本文・連携クラウド認証情報、通信の秘密という複数の制度・技術面を同じ記録で追える。

## サンリオエンターテイメント — 初期最大影響から最終調査への証拠状態変化

- [2025-08-12 最終調査結果（PDF）](https://www.sanrio-entertainment.co.jp/wp-content/uploads/2025/08/%E3%80%90%E3%82%B5%E3%83%B3%E3%83%AA%E3%82%AA%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%86%E3%82%A4%E3%83%A1%E3%83%B3%E3%83%88%E3%80%91%E5%BD%93%E7%A4%BE%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AA%E3%82%89%E3%81%B3%E3%81%AB%E6%83%85%E5%A0%B1%E6%BC%8F%E6%B4%A9%E3%81%AE%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E8%AA%BF%E6%9F%BB%E7%B5%90%E6%9E%9C%E3%81%AE%E3%81%94%E5%A0%B1%E5%91%8A20250812.pdf)

初期には最大約200万件の漏えい可能性を公表したが、最終フォレンジックでは漏えいを確認しなかった。この変化を上書きせず保持する。

## 保険見直し本舗グループ — 委託元への下流通知

- [2025-02-25 第一報（PDF）](https://hoken.mhompo.co.jp/news/20250225/pdf/ac183dcf.pdf)
- [2025-04-30 第2報（PDF）](https://www.mhompo.co.jp/news/20250430/pdf/20250430.pdf)
- [2025-08-29 最終調査・再発防止（PDF）](https://hoken.mhompo.co.jp/whokenp/wp-content/uploads/2025/08/Release_20250829.pdf)
- [明治安田生命 — 委託先保険代理店における漏えい等のおそれ](https://www.meijiyasuda.co.jp/profile/news/topics/20250430.html)

事故主体の調査と、各保険会社がデータ保有・委託責任の観点から行う顧客通知を分離する。

## NTT西日本グループ — 長期是正を追える事後PDF

- [2024-02-29 情報セキュリティ強化に向けた取組み（PDF）](https://www.ntt-west.co.jp/news/2402/pdf/240229a_1.pdf)
- [情報セキュリティ強化に向けた取り組みの進捗状況](https://www.ntt-west.co.jp/corporate/security/)

2023年7月の初期調査が事実を見抜けなかったことを含め、技術統制だけでなく調査能力・エスカレーション・長期組織是正を追跡する。

## KADOKAWA / ドワンゴ — 翌年度損益まで追えるIR

- [システム障害関連・時系列](https://group.kadokawa.co.jp/system_failure/)
- [当社サービスへのサイバー攻撃に関するご報告とお詫び](https://group.kadokawa.co.jp/information/media-download/1360/73b7af68478b8a51/)
- [ランサムウェア攻撃による情報漏洩に関するお知らせ](https://group.kadokawa.co.jp/information/media-download/1356/d3f77b589c58d083/)
- [2025年3月期 通期決算](https://group.kadokawa.co.jp/information/promotional_topics/article-12287.html)

2025年3月期ではWebサービス部門の売上・営業利益影響と、サイバー攻撃関連特別損失まで追跡できる。

# 「資料がある」だけでは強い比較にしないケース

HOYA、セイコー等にも統合報告書・企業セキュリティ資料は存在するが、今回の公開調査で事故の具体的失敗面へ直接対応する事故前記述を十分に確認できない場合は、単にPDFが存在するという理由だけで「対策を明記していたのに破られた」と評価しない。

同様に、事故後に作られたセキュリティ報告・再発防止資料を、事故前から存在していた統制の証拠として利用しない。

# 今後の更新ルール

各PDFについて次を保持する。

- 発行主体
- 発行日・対象年度
- 事故前／事故後の区分
- URLと、可能なら固定版
- 宣言された統制
- 事故の失敗面への適用性（直接／部分的／間接／不明）
- 後日差し替え・削除の有無
- 再発防止策なら `announced / implemented / tested / independently_assessed / operationally_observed` の状態

これにより「セキュリティ報告書を出していた企業が侵害された」という見出し比較ではなく、**宣言・実装範囲・例外・運用・検知・復旧を証拠単位で比較**する。
