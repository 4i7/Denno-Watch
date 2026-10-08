---
type: Corpus Audit
title: Denno-Watch 2026-10-08 第二次差分監査
resource: https://github.com/4i7/Denno-Watch
tags: [audit, japan, 2026, new-records, status-transitions]
status: draft
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
---

# 基準と結果

基準コミットは 5a3ceb110d065cf7442c6661944d63f120517e67。前回国内83件（2026年57件）から、新規6件を収録して**89件（2026年63件、2025年12件、2024年7件、2023年7件）**とした。これは全国全件の網羅数ではない。

## 新規6件

- [ABAHOUSE](../../incidents/2026/abahouse-international-order-data-breach.md)：漏えいpossible、不審な返金案内受信を観測、利用データと悪用の因果は未確定。
- [HISタイ法人](../../incidents/2026/his-thailand-passport-file-server-breach.md)：2025年12月検知、旅券等最大627人possible、2026年10月公表。
- [埼玉県渋沢MIX](../../incidents/2026/saitama-shibusawa-mix-integrity-breach.md)：約2,200名一覧の閲覧、3名の詳細閲覧、改ざん・メール送信を確認。データ窃取は未確認。
- [セレス](../../incidents/2026/ceres-point-income-breach.md)：195件（88会員、107従業員等）閲覧possible。再開予定と実績を区別。
- [くふうZaim](../../incidents/2026/kufu-zaim-integrity-write-incident.md)：14名の情報改ざんconfirmed。漏えいnot_observed、復旧済み。
- [くふうまちトークβ](../../incidents/2026/kufu-machi-talk-beta-breach.md)：メール漏えい少なくとも1人confirmed、他情報possible。停止中。

## 既存記録2件の更新

- **ApplyNow／富士市**：2026年10月7日公式続報で応募者情報815件の外部漏えいを確認。所沢市1,701件とは別の下流単位。動画は別領域で対象外。データ流出のメタ確度 confirmed は以前からのまま。https://www.city.fuji.shizuoka.jp/1005250000/p007783.html
- **IDCフロンティア**：ファイバーゲート公式に直接の基盤依存を確認。日水物流は入出荷停止を公式公表、委託先の名指しはなし。IDCへの確定帰属とせず二次資料との境界を保持。データ漏えいはunknown。https://www.fibergate.co.jp/news/14742/ https://www.nissui.co.jp/news/2026100702.html

## 事実確度・件数単位・調査日

- 閲覧／持ち出し、改ざん／漏えい、封じ込め／全面復旧／顧客業務再開を別の結論とする。
- 627は旅券情報対象者の上限、2,200は一覧閲覧対象者の概数、195は情報**件数**、14は改ざんされた**人数**。単純合算しない。
- 最新公表日を調査実施日で上書きしない。確認した対象文書のみ public_record_checked_at を 2026-10-08T06:48:28.488+00:00 に更新した。
- 全国収録89件全件の新しい金融IR・行政・復旧情報を再調査した意味ではない。
- 公的な複数類型の注意喚起だけから攻撃者同一性・AI利用・特定CVEを個別組織へ帰属しない。

## 残課題

日本エネルギー経済研究所・日本化粧品工業会・ニッポンレンタカー・らしんばん・富山県立大学・日経BP・ちばぎん商店の追加採否、セレス実再開、IDCF下流復旧、ABAHOUSE最終人数・金銭詐欺、HIS旅券悪用・通知、2023〜2025年の予後再評価。
