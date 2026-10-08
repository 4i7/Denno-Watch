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
  public_record_checked_at: "2026-10-08T09:53:59.257+00:00"
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


## 個人情報の認定に必要な追加確認

確認されたのは、**eポートフォリオ上の複数ファイルの反復外部取得**と、2023年3月以前に在籍した学生の経験・振り返り等の**文章情報の流出**である。氏名や学籍番号が含まれるか、他のデータと結合して本人識別が可能かは依然調査中である。よって機密情報としての文章の流出は確定するが、個人データ対象人数は未確定とする。[^source-0]

本文が自由記述のため、定型フォームに氏名欄がなくても、学生生活、実習先、個別相談、個人の経験などを文章から特定可能な場合がある。これはデータ構造からみた**検証対象**であり、流出文章の具体的な内容や機微情報を公表事実として捏造しない。

## 学生の学修継続と復旧ゲート

| 機能 | 公表上の状態 | 復旧と誤認しないための条件 |
| --- | --- | --- |
| 学内ネットワーク・Wi-Fi | 被害拡大防止で停止 | 端末・経路の安全確認後の再接続 |
| WebClass・Universal Passport | 10月中旬以降に**学内からの段階的再開を目標** | 実際の再開日時と利用可能者の確認 |
| 学外からの利用 | 安全性と対策進捗を踏まえて判断 | 学内での再開を学外利用可能としない |
| 課題・履修・成績・就職支援 | 代替手段・提出期限等を調整中 | 代替手段での継続と通常システム復旧を分離 |

大学は、警察等との連携、外部専門機関の調査手配、PPCへの必要な報告、対象者への通知を**今後の対応**として挙げる。予定と実施済みを混同しない。学生には大学を装うメールや認証コードの問い合わせへの警戒、パスワード再利用先の変更を促している。[^source-0]

## 調査上の未確定事項

初期侵入手段、ダウンロードファイルの件数・内容、学籍番号等の存否、本人識別の可否、2023年度以降の在学生への影響、復旧完了・通知完了時刻。

[^source-0]: 発表資料／本文 — https://www.kuins.ac.jp/news/2026/10/post_1450.html （2026-10-08確認）。
[^source-1]: 2026年9月30日初報 — https://www.kuins.ac.jp/news/2026/09/post_1448.html （2026-10-08確認）。
