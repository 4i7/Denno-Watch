---
type: Cybersecurity Incident
title: "GMO お名前.comデスクトップクラウド — 26,739サーバー影響・取引口座不正操作の報告"
description: "不正プログラムを顧客仮想サーバーで確認して全プラン停止。10月22日には取引ツールを使う顧客からの不正口座操作報告を受け、認証情報失効を緊急要請。"
resource: https://www.onamae.com/news/article/11584/
tags: [japan, 2026, VPS, malware, financial-integrity, cloud, identity, service-outage]
status: draft
stale_after: 2026-10-26T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:42:15.916+00:00 }
incident:
  organization: "GMOインターネット株式会社／お名前.comデスクトップクラウド"
  sector: "cloud-VPS"
  jurisdiction: "JP"
  incident_status: "investigating_service_suspended"
  attack_type: "unauthorized-server-access-and-malicious-program"
  detected_at: "2026-10-20"
  first_disclosed_at: "2026-10-21"
  latest_public_update: "2026-10-22 16:59 JST"
  intrusion_vector: "一部の利用者サーバーで不正プログラム設置確認。初期侵入口不明"
  affected_services: "お名前.comデスクトップクラウド全プラン、最大26,739サーバー環境"
  data_exposure: "possible"
  availability_impact: "2026-10-21 04:00以降全プラン停止、FX・証券取引ツールの常時運用にも影響"
  restoration_state: "全プラン停止継続、全面再開日不明、外部専門家調査中"
  secondary_abuse: "2026-10-22顧客から証券/FX取引口座で第三者による不正操作の報告。会社が本件との因果や金額を最終確定したわけではない"
  notification_state: "顧客へ取引ツール口座の認証情報変更・セッション切断を至急要請"
  data_sensitivity: "仮想サーバーに保存されたID・パスワードやMT4/MT5など取引ツールの認証情報。運営会社が保持するカード情報は別"
  public_record_checked_at: "2026-10-23T09:42:15.916+00:00"
sources:
  - id: first
    resource: https://www.onamae.com/news/article/11584/
    title: "デスクトップクラウド第三者不正アクセス第一報"
    author: "organization:GMOインターネット"
  - id: second
    resource: https://group.gmo/info/alert/20261022/
    title: "お名前.comデスクトップクラウド不正アクセス第2報"
    author: "organization:GMOインターネットグループ"
  - id: stop
    resource: https://www.onamae.com/news/article/11583/
    title: "緊急メンテナンス（全プラン停止）"
    author: "organization:GMOインターネット"
---

# GMO お名前.comデスクトップクラウド — 26,739サーバー影響・取引口座不正操作の報告

## 攻撃の公表事実

2026年10月20日に顧客サーバーの一部で**第三者が設置した不正プログラム**を確認。影響可能性があるサーバー環境は**26,739件**。この数字は利用者人数でも感染確定台数でもない。10月21日4時以降、全プランのサーバーを順次停止。実際の外部取得件数、侵入入口、再開日時は調査中。[^first][^stop]

## 10月22日の重大な下流変化

GMOは一部顧客から、当該VPS上で使用していた取引ツールに関連し、**証券会社・FX会社等の取引口座が第三者によって不正操作されたという報告があった**と公表した。MT4/MT5などを含むツールと口座のパスワード等がサーバーに保存されていた場合、閲覧された可能性がある。GMOは顧客に至急、パスワード変更と**ログオフ・セッション切断**を要請した。[^second]

| 対象 | 確度 | 数値と解釈 |
| --- | --- | --- |
| 不正プログラムの設置 | confirmed | 一部の顧客サーバー |
| 影響し得る環境 | possible | **26,739サーバー**。アカウント数ではない |
| 顧客データ・口座認証情報の閲覧 | possible | 外部取得件数未確定 |
| 第三者による不正な金融取引操作 | **顧客から報告あり** | GMO側が因果・損失・実行額を最終確定した証拠はない |
| サーバーの利用停止 | confirmed | 全プラン。再開日は未公表 |

## 金銭被害とデータ漏えいを混同しない

顧客による「不正操作の報告」は観測済みだが、その全てが本件侵入に起因したとフォレンジックで確定したわけではない。金銭損失・件数を推定していない。**VPSへの侵入**と**顧客の取引口座側の操作**を独立した証拠とし、顧客の認証・注文ログで両者を照合する必要がある。[^second]

## 緊急対応と長期予後

VPS内の認証情報変更だけでは、すでに有効な外部サービスのAPIキーや取引セッションが失効しないことがある。証券・FX事業者側でのセッション無効化、ツール連携先の鍵失効、注文履歴の照合、停止中の代替取引手段を確認する。これらは防御側の作業論点であり、当該全顧客の被害を示す証拠ではない。

未公表：侵入口、実際のプログラム設置台数、外部取得量、口座不正操作の確定件数・金銭損失、全プランの復旧日、セキュリティ統制の独立検証。

[^first]: GMOインターネット「デスクトップクラウド第三者不正アクセス第一報」. https://www.onamae.com/news/article/11584/
[^second]: GMOインターネットグループ「お名前.comデスクトップクラウド不正アクセス第2報」. https://group.gmo/info/alert/20261022/
[^stop]: GMOインターネット「緊急メンテナンス（全プラン停止）」. https://www.onamae.com/news/article/11583/
