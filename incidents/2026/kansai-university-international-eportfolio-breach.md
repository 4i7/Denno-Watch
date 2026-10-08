---
type: Cybersecurity Incident
title: 関西国際大学 — eポートフォリオ外部取得／個人識別情報は調査中
description: eポートフォリオ外部取得／個人識別情報は調査中
resource: https://www.kuins.ac.jp/news/2026/10/post_1450.html
tags: [japan, 2026, university, education, exfiltration, outage]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 関西国際大学
  sector: higher-education
  jurisdiction: JP
  incident_status: investigating_and_staged_recovery
  attack_type: unauthorized-access-and-file-exfiltration
  detected_at: "2026-09-30"
  first_disclosed_at: "2026-09-30"
  latest_public_update: "2026-10-06"
  public_record_checked_at: "2026-10-08T14:54:00+09:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "eポートフォリオ外部取得／個人識別情報は調査中"
  data_exposure: possible
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.kuins.ac.jp/news/2026/10/post_1450.html
    title: 発表資料／本文
    author: organization:関西国際大学 
  - id: source-1
    resource: https://www.kuins.ac.jp/news/2026/09/post_1448.html
    title: 2026年9月30日初報
    author: organization:公開資料 
---

# 関西国際大学 — eポートフォリオ外部取得／個人識別情報は調査中

## 初報からの重要なステータス変動

9月30日初報は不正アクセスと学内インターネット接続停止、漏えい有無調査のみを表明。**10月6日第2報**ではアクセス記録の解析により、eポートフォリオシステムの複数ファイルの**繰り返しの外部取得**を確認。2023年3月以前に在籍した学生の在学中の経験・振り返りの**文字情報の流出を確定**した。[^source-0][^source-1]

ただし、流出した文章内に氏名・学籍番号があるか、個人と結び付くかは調査中。そのためデータの**ファイル外部取得はconfirmed、個人情報漏えいはpossible**と分ける。人数・件数は未確定。

## 復旧

ネットワーク・学内Wi-Fiの停止により課題、履修・成績、授業連絡、就職支援等に支障。10月中旬以降、WebClassやUniversal Passportを学内から**段階的に再開する目標**を公表しており、復旧済みとは扱わない。警察等と連携し、外部専門調査を予定。[^source-0]

[^source-0]: 発表資料／本文 — https://www.kuins.ac.jp/news/2026/10/post_1450.html （2026-10-08確認）。
[^source-1]: 2026年9月30日初報 — https://www.kuins.ac.jp/news/2026/09/post_1448.html （2026-10-08確認）。
