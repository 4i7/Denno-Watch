---
type: Cybersecurity Incident
title: 戸田建設 — 支払管理システム等から取引先・従業員情報流出
description: 支払管理システム等から取引先・従業員情報流出
resource: https://www.toda.co.jp/news/2026/20261007_006350.html
tags: [japan, 2026, construction, personal-data, vendor-impact, confirmed-leak]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 戸田建設株式会社
  sector: construction
  jurisdiction: JP
  incident_status: contained_and_investigating
  attack_type: unauthorized-access
  detected_at: "2026-10-05"
  first_disclosed_at: "2026-10-07"
  latest_public_update: "2026-10-07"
  public_record_checked_at: "2026-10-08T14:54:00+09:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "支払管理システム等から取引先・従業員情報流出"
  data_exposure: confirmed
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.toda.co.jp/news/2026/20261007_006350.html
    title: 発表資料／本文
    author: organization:戸田建設株式会社 
  - id: source-1
    resource: https://www.toda.co.jp/toda_webservice/toda_webservice.html
    title: 戸田建設WEBサービス停止案内
    author: organization:公開資料 
---

# 戸田建設 — 支払管理システム等から取引先・従業員情報流出

## 時系列・被害

10月5日に支払管理システム等への不正アクセスを検知。**10月1〜5日**に情報漏えいした痕跡を調査で確認し、当該システムをネットワークから隔離した。10月7日に公表し、個人情報保護委員会への報告を完了。[^source-0]

| 情報 | 最大対象 | 単位 |
| --- | ---: | --- |
| 取引先担当者のメールアドレス | 7,200 | アドレス件数 |
| 取引先の取引データ | 6,000 | 取引データ件数 |
| 従業員氏名・住所・電話・メール・部署 | 4,778 | 人数 |

これらは異なる単位なので足し算しない。漏えい情報の一般公開・不正利用は公表時点で未確認。影響対象者へ順次連絡する予定。[^source-0]

## 業務の停止

出来高請求、協力会社ユーザー管理、請求方法検索、作業所電話帳の各Webサービスを対処のため停止と案内。復旧完了や攻撃の侵入口について確定公表を確認できない。[^source-1]

[^source-0]: 発表資料／本文 — https://www.toda.co.jp/news/2026/20261007_006350.html （2026-10-08確認）。
[^source-1]: 戸田建設WEBサービス停止案内 — https://www.toda.co.jp/toda_webservice/toda_webservice.html （2026-10-08確認）。
