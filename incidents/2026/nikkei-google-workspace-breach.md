---
type: Cybersecurity Incident
title: 日本経済新聞社 Workspace — Google Workspace不正ログイン／1646人に漏えい疑い
description: Google Workspace不正ログイン／1646人に漏えい疑い
resource: https://www.nikkei.co.jp/nikkeiinfo/news/information/1547.html
tags: [japan, 2026, google-workspace, cloud-identity, personal-data]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 株式会社日本経済新聞社
  sector: media
  jurisdiction: JP
  incident_status: contained_and_investigating
  attack_type: google-workspace-account-compromise
  detected_at: "2026-08 上旬にGoogleから通知"
  first_disclosed_at: "2026-10-04"
  latest_public_update: "2026-10-04"
  public_record_checked_at: "2026-10-08T09:53:59.257+00:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "Google Workspace不正ログイン／1646人に漏えい疑い"
  data_exposure: possible
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.nikkei.co.jp/nikkeiinfo/news/information/1547.html
    title: 発表資料／本文
    author: organization:株式会社日本経済新聞社 
  - id: source-1
    resource: https://internet.watch.impress.co.jp/docs/news/2145512.html
    title: INTERNET Watch 2026年10月5日
    author: organization:公開資料 
---

# 日本経済新聞社 Workspace — Google Workspace不正ログイン／1646人に漏えい疑い

## 事実とMicrosoft 365の別件との区別

日経社員のGoogle Workspaceアカウントが**7月下旬以降不正ログイン**され、8月上旬のGoogleからの通知で発覚。**1,646人**の社員・取引先等の氏名、メールアドレスなどに漏えいの疑いがあり、10月4日に公表した。読者や取材先に関する情報を含まないと報じられている。パスワード変更後の追加不正ログインは確認されていない。[^source-0][^source-1]

同社Microsoft 365の9月30日付なりすましメール送信とは、プラットフォームと時期・影響が異なる別件として収録。同一侵入起点、攻撃者、攻撃キャンペーンを断定しない。

## 出典上の制限

公式URLは確認したが調査環境では直接取得できず、報道による交差確認を利用した。最終確定件数・認証情報の入手元・二次被害は未確定。


## 侵害の時間軸と確認範囲

| 事象 | 確認された情報 | 確定していない情報 |
| --- | --- | --- |
| 7月下旬以降 | 社員Google Workspaceアカウントに不正ログイン | 初期認証情報取得元・認証突破方法 |
| 8月上旬 | Googleからの通知により認識 | 具体的な攻撃継続日数 |
| 10月4日 | 1,646人分（社員、取引先等）の氏名・メール等に漏えい**疑い**を公表 | 実際に取得された件数、個々のデータ種別 |
| パスワード変更後 | 追加不正ログインは確認されず | 侵害全体の長期的終息、他サービスへの影響 |

取材先の情報が対象外と報じられる一方、公開根拠で最終影響人数の確定やフォレンジック手法の詳細までは確認できない。本文が利用している情報源は**公式告知URLに直接アクセスできない環境での独立報道**であり、組織一次情報の全文との照合が必要という制限を維持する。[^source-0][^source-1]

## Microsoft 365と同一事故だと断定しない理由

9月30日のMicrosoft 365アカウント悪用は、偽装メール**約9,000通の送信**と取引先を巻き込むフィッシングを含む。一方Google Workspace侵害の判明は8月上旬、約1,646人のデータ影響の疑いという別の対象である。原因、取得された認証情報の共通性、同一人物・攻撃者の関与は公表されておらず、攻撃者帰属を機械的に統合しない。[^source-1]

## 続報の確認条件

Google Workspaceの最終個人データ取得数、認証方式・端末の安全確認、各アカウントのセッション無効化、本人通知の完了、二次メール詐欺の確認。これらは調査項目であり、未公表の統制欠落を会社へ帰属するものではない。

[^source-0]: 発表資料／本文 — https://www.nikkei.co.jp/nikkeiinfo/news/information/1547.html （2026-10-08確認）。
[^source-1]: INTERNET Watch 2026年10月5日 — https://internet.watch.impress.co.jp/docs/news/2145512.html （2026-10-08確認）。
