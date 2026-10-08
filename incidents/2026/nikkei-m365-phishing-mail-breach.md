---
type: Cybersecurity Incident
title: 日本経済新聞社 M365 — Microsoft 365アカウント侵害／偽装メール約9000通と日経BPへの連鎖
description: Microsoft 365アカウント侵害／偽装メール約9000通と日経BPへの連鎖
resource: https://www.nikkei.co.jp/nikkeiinfo/news/information/1554.html
tags: [japan, 2026, m365, email, credential-abuse, phishing, downstream]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 株式会社日本経済新聞社
  sector: media
  jurisdiction: JP
  incident_status: contained_and_investigating
  attack_type: m365-account-compromise-and-phishing
  detected_at: "2026-09-30"
  first_disclosed_at: "2026-10-04"
  latest_public_update: "2026-10-04"
  public_record_checked_at: "2026-10-08T09:55:51.644+00:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "Microsoft 365アカウント侵害／偽装メール約9000通と日経BPへの連鎖"
  data_exposure: possible
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.nikkei.co.jp/nikkeiinfo/news/information/1554.html
    title: 発表資料／本文
    author: organization:株式会社日本経済新聞社 
  - id: source-1
    resource: https://internet.watch.impress.co.jp/docs/news/2145512.html
    title: INTERNET Watch 2026年10月5日
    author: organization:公開資料 
  - id: source-2
    resource: https://internet.watch.impress.co.jp/docs/news/2146104.html
    title: 日経BPへのフィッシング波及を報じたINTERNET Watch 2026年10月6日
    author: organization:公開資料 
---

# 日本経済新聞社 M365 — Microsoft 365アカウント侵害／偽装メール約9000通と日経BPへの連鎖

## 確定した不正利用と漏えい可能性

日経は10月4日、社員のMicrosoft 365アカウントへの不正ログインが疑われ、9月30日に社内・取材先などへ**約9,000通のなりすましメール**が送信されたと公表。メールには悪性サイトへ誘導する内容があり、送信先の氏名・メールアドレスや一部本文が漏れた可能性がある。パスワード変更後の追加ログインは未確認。[^source-0][^source-1]

**日経BPに実際の二次侵害**が発生した点が重要。日経社員を装うフィッシングメールを受けた日経BP従業員の認証情報が窃取され、同社のメールアカウントへ不正アクセスが発生。氏名・メールアドレス**26件の漏えい可能性**が公表された。BPは当該アカウントを遮断し対象者に連絡した。[^source-2]

実際のメール不正送信と下流アカウント侵害は**confirmed**、メール情報の流出量は**possible/調査中**と区別する。Google Workspaceの別件と共通攻撃者と認定しない。

## 出典上の制限

日本経済新聞社公式ページのURLは確認できたが、調査環境から本文を直接開けなかった。一次公表内容を引用する二つの独立した報道で交差確認した。攻撃者・侵入口・最終のメール漏えい件数は未確定。


## メール送信の確定被害と後続侵入を区別する

| 事象 | 事実の状態 | 人数・件数の注意点 |
| --- | --- | --- |
| 9月30日、日経社員名義のメール | 不審な誘導メール**約9,000通が送信された** | 送信件数であり9,000人の被害ではない |
| Microsoft 365メール・連絡先 | 送信先氏名・アドレスと一部本文に漏えい**可能性** | 外部取得の実量・最終人数は未確定 |
| 日経BP従業員のフィッシング | 当該メールを受けた従業員の認証情報取得とメールアカウント侵害が確認 | 下流の実侵害であり、親会社の全宛先の侵害を意味しない |
| 日経BPメールアカウント | **26件の氏名・アドレス**に漏えい可能性 | 実取得量と二次悪用は別途調査中 |

日経側は当該アカウントのパスワードを変更し、それ以後の追加不正ログインは確認していない。日経BPは侵害アカウントを遮断し、関係者へ個別に連絡した。**1段目のなりすまし送信と、2段目の認証情報取得による別組織アカウント侵害**を、委託先または取引先依存による二次被害の具体例として区別する。[^source-0][^source-1][^source-2]

## 自社メール防御で照合する証拠

受信者のフィッシングサイト到達状況、メール送信ログ、アカウント認証イベント、疑わしいOAuth同意、セッション失効・パスワード変更後のアクセス、送信先への注意喚起の進捗を独立して点検する。ここに列挙したログの有無や設定漏れが今回の組織で確認されたわけではない。Google Workspaceの7月下旬以降の別件とは攻撃開始時期・認証基盤を分離する。

[^source-0]: 発表資料／本文 — https://www.nikkei.co.jp/nikkeiinfo/news/information/1554.html （2026-10-08確認）。
[^source-1]: INTERNET Watch 2026年10月5日 — https://internet.watch.impress.co.jp/docs/news/2145512.html （2026-10-08確認）。
[^source-2]: 日経BPへのフィッシング波及を報じたINTERNET Watch 2026年10月6日 — https://internet.watch.impress.co.jp/docs/news/2146104.html （2026-10-08確認）。
