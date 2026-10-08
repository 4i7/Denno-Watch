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
  public_record_checked_at: "2026-10-08T09:53:59.257+00:00"
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


## 支払・工事協力会社への業務影響

会社の協力会社向けサービスページでは、事故対処のため**出来高請求システム、協力会社ユーザー管理、請求方法検索、作業所電話帳**を停止している。情報の機密性被害だけでなく、協力会社の出来高請求・照会・担当者連絡の業務継続にも影響する。代替運用・手動請求・支払期日変更・各サービスの復旧完了はこの公表では未確定である。[^source-1]

## 流出量と確度の整理

| 分類 | 公表数 | 意味 |
| --- | ---: | --- |
| 取引先の担当者メールアドレス | 最大7,200件 | アドレスの件数。会社数や人数とは限らない |
| 取引データ | 最大6,000件 | 取引・支払に関連するデータ件数 |
| 従業員の連絡先・所属 | 4,778人分 | 氏名・住所・電話番号・メール・所属部署 |

10月1〜5日の**情報漏えい痕跡**が調査で確認されたため、第三者による単なる閲覧可能性より強い事実として扱う。一方、漏えい情報の公開や不正利用については、10月7日時点で会社は**確認していない**とする。対象者への連絡は順次実施予定であり通知完了ではない。[^source-0]

取引先と従業員には同社名・請求書・担当者名を悪用した偽装メール等のリスクがあるため、会社は不審なメールやSMSのリンク・添付を開かないよう注意喚起している。**実際の詐欺発生が本件に帰属したとの公表はない**。[^source-0]

## 続報で確かめる事実

最初の侵入経路と侵入日時、外部へ持ち出された実ファイル数、最終対象人数、出来高請求等の再開と未処理データの照合、取引先への連絡完了、業績・IR影響。事故前の一般的な施工・ガバナンス方針を侵害時の統制の実装証拠と混同しない。

[^source-0]: 発表資料／本文 — https://www.toda.co.jp/news/2026/20261007_006350.html （2026-10-08確認）。
[^source-1]: 戸田建設WEBサービス停止案内 — https://www.toda.co.jp/toda_webservice/toda_webservice.html （2026-10-08確認）。
