---
type: Cybersecurity Incident
title: 日本原子力研究開発機構 — JRR-3研究支援サイト／175人の身分証・健診情報流出
description: JRR-3研究支援サイト／175人の身分証・健診情報流出
resource: https://www.jaea.go.jp/02/press2026/p26100105/
tags: [japan, 2026, research, identity-documents, health-data, confirmed-exfiltration]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 国立研究開発法人日本原子力研究開発機構
  sector: nuclear-research
  jurisdiction: JP
  incident_status: contained_and_investigating
  attack_type: unauthorized-file-download
  detected_at: "2026-09-25"
  first_disclosed_at: "2026-10-01"
  latest_public_update: "2026-10-01"
  public_record_checked_at: "2026-10-08T14:54:00+09:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "JRR-3研究支援サイト／175人の身分証・健診情報流出"
  data_exposure: confirmed
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.jaea.go.jp/02/press2026/p26100105/
    title: 発表資料／本文
    author: organization:国立研究開発法人日本原子力研究開発機構 
---

# 日本原子力研究開発機構 — JRR-3研究支援サイト／175人の身分証・健診情報流出

## 確定したファイル流出

研究用原子炉JRR-3の外部利用者向け研究支援サイトで、9月25日に**2,419ファイルの不正ダウンロード**を確認し、外部接続を停止。9月29日にそのうち**367ファイル・175人分**に個人情報が含まれると判明し、10月1日に公表。[^source-0]

- 顔写真付き公的身分証明書（免許証・マイナンバーカード・旅券・在留カード）200件。**うち6人のマイナンバー**を含む。
- 放射線業務の特殊健康診断結果146件。
- 放射線業務従事者証明書21件。

ファイル数と人数を合算しない。ID・パスワード・登録フォームに入力した氏名は流出していないと説明。研究支援サイトは業務ネットワークから分離されており、他システムの影響はないと公表。対象者への個別通知、個人情報保護委員会・関係官庁・警察への報告・相談を実施した。[^source-0]

## 評価・未解明

原子炉運転制御系への侵害が生じたという根拠はない。流出規模は175人だが、特定個人情報と健康診断結果は不可逆的な個人被害が大きくなり得る。侵入経路、二次利用、最終復旧は未確定。

[^source-0]: 発表資料／本文 — https://www.jaea.go.jp/02/press2026/p26100105/ （2026-10-08確認）。
