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
  public_record_checked_at: "2026-10-08T14:54:00+09:00"
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

[^source-0]: 発表資料／本文 — https://www.nikkei.co.jp/nikkeiinfo/news/information/1554.html （2026-10-08確認）。
[^source-1]: INTERNET Watch 2026年10月5日 — https://internet.watch.impress.co.jp/docs/news/2145512.html （2026-10-08確認）。
[^source-2]: 日経BPへのフィッシング波及を報じたINTERNET Watch 2026年10月6日 — https://internet.watch.impress.co.jp/docs/news/2146104.html （2026-10-08確認）。
