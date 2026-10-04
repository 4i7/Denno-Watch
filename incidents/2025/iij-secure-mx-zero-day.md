---
type: Cybersecurity Incident
title: IIJセキュアMXサービス — 2024〜2025年未公知脆弱性悪用と通信の秘密の漏えい
description: 2024年8月3日以降の不正アクセスが2025年4月に発覚。未公知脆弱性の悪用、長期潜伏、認証情報・メール情報の漏えい、総務省行政指導まで追跡する。
resource: https://www.iij.ad.jp/news/pressrelease/2025/0422-2.html
tags: [japan, cloud, email-security, zero-day, vulnerability, credential-exposure, regulatory, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T08:17:31+09:00 }
incident:
  organization: 株式会社インターネットイニシアティブ（IIJ）
  sector: internet-cloud-security-services
  jurisdiction: JP
  incident_status: public_report_closed_with_regulatory_followup
  attack_type: exploitation of previously undisclosed third-party software vulnerability
  earliest_known_activity: "2024-08-03以降"
  detected_at: "2025-04-10"
  first_disclosed_at: "2025-04-15"
  latest_public_update: "2025-07-18"
  public_record_checked_at: "2026-10-05T08:17:31+09:00"
  intrusion_vector: "IIJセキュアMXサービスで利用していた第三者製ソフトウェアの当時未公知の脆弱性。後にJVN#22348866として公開"
  affected_services: "IIJセキュアMXサービスの一部設備、メールアカウント・パスワード、送受信メール本文・ヘッダ、連携クラウド認証情報"
  data_exposure: confirmed
  availability_impact: "公表上は長期全面停止ではなく、侵入経路切り離し後にサービスを安全に利用可能と説明"
  restoration_state: "侵入経路を特定・切り離し。対象ソフトウェア機能は2025年2月に提供終了済み。監視・再発防止を強化"
  regulatory_response: "通信の秘密の漏えい事案として2025-07-18に総務省から書面による行政指導"
  downstream_impact: "法人顧客のメール認証情報、メール内容、連携クラウド認証情報に下流リスク"
  ai_relation: era_context_only
  response_latency:
    detection_latency: "最も早い確認済み不正アクセス日2024-08-03から2025-04-10の発覚まで8か月超"
    containment_latency: "4月10日の可能性確認後、侵入経路を特定して切り離し。正確な所要時間は非公表"
    public_disclosure_latency: "発覚2025-04-10から第一報2025-04-15まで5日"
sources:
  - id: iij-first
    resource: https://www.iij.ad.jp/news/pressrelease/2025/0415.html
    title: IIJセキュアMXサービスにおけるお客様情報の漏えいについて
  - id: iij-second
    resource: https://www.iij.ad.jp/news/pressrelease/2025/0422-2.html
    title: IIJセキュアMXサービスにおけるお客様情報の漏えいについてのお詫びとご報告
  - id: iij-second-pdf
    resource: https://www.iij.ad.jp/news/pressrelease/2025/pdf/20250422_SMX_2.pdf
    title: IIJセキュアMXサービスにおけるお客様情報の漏えいについてのお詫びとご報告 PDF
  - id: iij-guidance
    resource: https://www.iij.ad.jp/news/pressrelease/2025/0718.html
    title: 当社に対する総務省からの行政指導について
  - id: iij-guidance-pdf
    resource: https://www.iij.ad.jp/news/pressrelease/2025/pdf/20250718_SMX3.pdf
    title: 当社に対する総務省からの行政指導について PDF
---

# 概要

IIJは2025年4月10日、法人向けメールセキュリティサービス「IIJセキュアMXサービス」で顧客情報が外部へ漏えいした可能性を確認した。調査の結果、サービス設備は**2024年8月3日以降**に不正アクセスを受け、不正プログラムが実行されていた。[^iij-first]

発覚時点での最大影響候補は6,493契約、4,072,650メールアカウントだったが、4月22日の続報で確認済み影響は絞り込まれた。メールアカウント・パスワードは132契約、311,288アカウント、メール本文・ヘッダは6契約、連携クラウドサービスの認証情報は488契約、重複除外後586契約だった。[^iij-second]

# 発生環境と原因

原因は、IIJセキュアMXサービスで利用していた第三者製ソフトウェアの脆弱性悪用だった。この脆弱性は不正アクセスの発生から発覚まで未発見で、本件を通じて明らかになった後、製造元が修正し、2025年4月18日にJVN#22348866「Active! mail におけるスタックベースのバッファオーバーフロー」として緊急度の高い脆弱性情報が公開された。[^iij-second]

当該ソフトウェアを使うオプション機能は2025年2月で提供終了しており、4月時点では利用していなかった。終了済み機能でも、過去の侵害が後から判明し得ることを示す。

# 検知・封じ込め速度

確認できる最初の不正アクセス日である2024年8月3日から、漏えい可能性を確認した2025年4月10日まで8か月を超える。これはゼロデイだったという背景と分離せず評価する必要がある。既知脆弱性の未修正期間とは性質が異なる。[^iij-first][^iij-second]

4月10日に可能性を確認した後、IIJは侵入経路を特定して切り離し、第一報時点でサービスは安全に利用可能な状態と説明した。封じ込めの正確な時刻・所要時間は公開されていないため、時間単位の値を作らない。

# 情報影響の質

単なるメールアドレス一覧ではなく、アカウント・パスワード、送受信メール本文・ヘッダ、他社クラウドサービスの認証情報が含まれた。特に連携クラウド認証情報は、IIJのサービス境界を越えた二次侵害へつながり得るため、下流影響として別に扱う。[^iij-second]

ただし、公開資料から各連携先で実際に二次侵害が発生したとは確認できないため、可能性と実害を混同しない。

# 規制対応と予後

2025年7月18日、IIJは本件が通信の秘密の漏えい事案に当たり、総務省から書面による行政指導を受けたと公表した。[^iij-guidance] 事故後はセキュリティ対策と監視体制の強化を検討・実施するとしている。

本件は、セキュリティサービス事業者自体が未公知脆弱性の影響を受け、顧客の認証・通信内容へ下流影響が及ぶ「共有責任・集中リスク」の比較事例でもある。

# 株主・開示資料

IIJは第一報・第二報・行政指導についてWeb本文とPDFを併せて公開しており、発生から発覚、対象件数の精査、原因特定、規制対応を追跡可能である。[^iij-second-pdf][^iij-guidance-pdf]

今回の調査では、事故前の一般的なセキュリティ方針を本件の脆弱な第三者ソフトウェアへ直接結び付けられる一次資料までは確認していない。セキュリティ企業であること自体を「具体的統制を公表していた」証拠へ置き換えない。

# AI/LLMとの関係

攻撃者がAI/LLMを利用したことを示す公開証拠は確認していない。`era_context_only` とする。

# 防御上の教訓

- ゼロデイはパッチ速度だけでは防げないため、実行挙動、Web公開面、異常通信、侵害後活動の検知を重ねる。
- 廃止済み機能でも、過去に侵害されていた可能性を考慮し、廃止時にログ・認証情報・侵害痕跡を確認する。
- メールセキュリティ基盤は認証情報と通信内容が集中するため、侵害時の下流リスクが大きい。
- 初報の最大影響範囲と、後日確認された実影響を分離して保存する。
- 通信の秘密など、一般の個人情報保護とは異なる制度上の予後も追跡する。

[^iij-first]: IIJ「IIJセキュアMXサービスにおけるお客様情報の漏えいについて」2025-04-15.
[^iij-second]: IIJ「IIJセキュアMXサービスにおけるお客様情報の漏えいについてのお詫びとご報告」2025-04-22.
[^iij-second-pdf]: IIJ「IIJセキュアMXサービスにおけるお客様情報の漏えいについてのお詫びとご報告」PDF, 2025-04-22.
[^iij-guidance]: IIJ「当社に対する総務省からの行政指導について」2025-07-18.
[^iij-guidance-pdf]: IIJ「当社に対する総務省からの行政指導について」PDF, 2025-07-18.
