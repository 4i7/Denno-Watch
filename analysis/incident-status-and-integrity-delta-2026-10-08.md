---
type: Analysis
title: 2026年10月8日 第二次調査 — 情報漏えい・完全性・可用性・下流被害の差分
resource: https://github.com/4i7/Denno-Watch
tags: [japan, 2026, status-delta, integrity, availability, downstream-impact]
status: draft
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
sources:
  - id: fuji
    resource: https://www.city.fuji.shizuoka.jp/1005250000/p007783.html
    title: 富士市職員採用試験個人情報の不正流出続報
    author: organization:静岡県富士市
  - id: nissui
    resource: https://www.nissui.co.jp/news/2026100702.html
    title: 日水物流システム障害
    author: organization:ニッスイ
  - id: his
    resource: https://www.his.co.jp/assets/20261007.pdf
    title: HISタイ法人侵害報告PDF
    author: organization:エイチ・アイ・エス
---

# 証拠の確度と新しい被害軸

2026年10月8日、国内収録83件から6件を追加、89件となった。特に、**外部へのファイル取得**、**不正閲覧のみ**、**登録改ざん**、**正規メール機能の悪用**、**事業継続障害**を区別する。

| 新規事例 | 情報被害の確度 | 別軸の実害 | 現在の対応 |
| --- | --- | --- | --- |
| [ABAHOUSE INTERNATIONAL](../incidents/2026/abahouse-international-order-data-breach.md) | 会員・注文DBはpossible | 実注文に合致する不審な返金メールの受信報告は確認済み。攻撃者との同一性は未確定 | 遮断、通知、調査 |
| [HISタイ法人](../incidents/2026/his-thailand-passport-file-server-breach.md) | 最大627人の旅券・アレルギー情報possible | 2025年12月検知から全ファイル照合、2026年10月公表 | 精査完了、通知中 |
| [埼玉県渋沢MIX](../incidents/2026/saitama-shibusawa-mix-integrity-breach.md) | 約2,200名の一覧閲覧は確認、データ外部取得は未確認 | **改ざんと不正メール送信がconfirmed** | 会員申請・予約停止 |
| [セレス・ポイントインカム](../incidents/2026/ceres-point-income-breach.md) | 195件の閲覧possible（会員88、従業員等107） | サービス緊急停止 | 10月7日21時再開**予定**、実際の完了は未確認 |
| [くふう Zaim](../incidents/2026/kufu-zaim-integrity-write-incident.md) | 漏えい・不正ログインはnot_observed | 14名の登録情報改ざんconfirmed／保存エラー | 修正・復旧完了と公表 |
| [くふう まちトークβ](../incidents/2026/kufu-machi-talk-beta-breach.md) | 少なくとも1名のメール漏えいconfirmed、生年月日等possible | サービス停止 | 範囲調査と通知 |

## 既存レコードの差分（顧客別確定情報と事業停止）

- [ApplyNow](../incidents/2026/applynow-recruitment-platform-breach.md)：富士市は採用試験応募情報**815件の外部流出を確認**。氏名・メール・電話・受験番号のデータと動画の別保存を明示した。既報所沢市1,701件に無条件加算して全顧客人数にはしない。[^fuji]
- [IDCフロンティア](../incidents/2026/idc-frontier-cloud-ransomware.md)：ファイバーゲートは公式にIDCF基盤依存と攻撃に伴うサービス影響を明示。日水物流は**商品の入出荷ができない**と公表したが、ニッスイ公式資料には委託先の固有名がなく、IDCとの帰属は一次資料だけでは確定しない。データ持ち出しもunknownを維持。[^nissui]

## 方法論上の再確認

1. **外部閲覧 ≠ 外部持ち出し確定**。改ざん・送信の確定も、情報持ち出しとは別の事実である。
2. **不審メールの受信 ≠ 攻撃者への自動帰属**。ABAHOUSEは注文情報が一致したという観測事実を重視しつつ、侵入と送信の因果は留保。
3. **最初の検知 ≠ 最初の公表**。HISの2025年12月検知・PPC報告と2026年10月公開を分離。調査対象サーバ内に不要な混在データがあると、対象抽出と通知が数か月単位で長期化し得る。[^his]
4. **封じ込め ≠ 復旧 ≠ 通知完了**。クラウド供給者のネットワーク隔離と下流企業の物流再開を別々に追跡。サービス再開予定を実績とみなさない。
5. **同一事業者の複数事故 ≠ 同一の侵入者**。くふうZaimとまちトークを独立した記録として保持する。

## 今後必要な資料

HISの通知・旅券悪用・国外子会社モニタリング、ABAHOUSEの最終人数と返金詐欺の関係、渋沢MIXの窃取検証・メール件数・予約復旧、セレスの実再開、IDCFとファイバーゲート／日水物流の復旧、富士市以外のApplyNow下流顧客の確定対象数。追加候補：日本エネルギー経済研究所、日本化粧品工業会、らしんばん、富山県立大学、ニッポンレンタカー、日経BPの独立下流被害。

全件の最新性を再調査したとの主張はしない。未確認事例の状態は無変更で、確認済みの時点・範囲を維持する。

[^fuji]: 静岡県富士市「本市職員採用試験（プレゼンテーション動画試験）を受験された方の個人情報の不正流出ついて【続報】」2026-10-07. https://www.city.fuji.shizuoka.jp/1005250000/p007783.html
[^nissui]: ニッスイ「日水物流株式会社におけるシステム障害について（第1報）」2026-10-07. https://www.nissui.co.jp/news/2026100702.html
[^his]: エイチ・アイ・エス「子会社ファイルサーバへの不正アクセスによる個人情報流出の可能性に関するお詫びとお知らせ」2026-10-07. https://www.his.co.jp/assets/20261007.pdf
