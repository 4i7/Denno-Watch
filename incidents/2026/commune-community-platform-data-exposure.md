---
type: Cybersecurity Incident
title: "Commune / Commune for Work — 約30.7万人の会員データ流出と144アカウントの仮パスワード変更"
description: "コミュニティ運営SaaSを通じた複数顧客会員への流出。会員約30.7万人分の情報と144アカウントの非本人操作の仮パスワード変更を確認。"
resource: https://communeinc.com/ja/news/2026oct09
tags: [japan, 2026, community, SaaS, supply-chain, integrity, personal-data, multi-tenant]
status: draft
stale_after: 2026-10-27T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-23T09:44:16.131+00:00 }
incident:
  organization: "コミューン株式会社"
  sector: "community-software-as-a-service"
  jurisdiction: "JP"
  incident_status: "investigating_customer_notification"
  attack_type: "unauthorized-access-and-account-modification"
  earliest_known_activity: "2026-10-05 18:00 JST"
  detected_at: "2026-10-06 to 2026-10-07 (public chronology)"
  first_disclosed_at: "2026-10-09"
  latest_public_update: "2026-10-09"
  intrusion_vector: "CommuneおよびCommune for Workに第三者の不正アクセス。入口の具体技術詳細は非公表"
  affected_services: "一部顧客企業のCommuneとCommune for Workのコミュニティ"
  data_exposure: "confirmed"
  availability_impact: "詳細な全顧客停止範囲は公表から未確定"
  restoration_state: "影響顧客・会員への通知・調査と再発防止を継続"
  secondary_abuse: "144会員の仮パスワードが本人以外の操作により変更されたと会社が確認。元パスワード漏えいは未確認"
  downstream_impact: "会員約30.7万人（重複・攻撃者作成ID除外の会社推計）、うちメールあり約12.6万人・メールなし約18.1万人"
  notification_state: "顧客企業との連携で会員通知"
  data_sensitivity: "メール、表示名、自己紹介、非公開グループ所属など。会員144名の仮パスワード非本人変更"
  public_record_checked_at: "2026-10-23T09:44:16.131+00:00"
sources:
  - id: commune
    resource: https://communeinc.com/ja/news/2026oct09
    title: "当社サービスCommune、Commune for Workへの不正アクセスによる個人情報漏えいのお知らせ"
    author: "organization:コミューン株式会社"
---

# Commune / Commune for Work — 約30.7万人の会員データ流出と144アカウントの仮パスワード変更

## 数値を読み違えない

コミューンは複数顧客企業のコミュニティについて、10月5日18時頃〜6日21時頃、および10月7日13時17分〜14時36分に会員情報が外部へ漏えいしたと公表した。会社推計で**約30.7万人**、内訳はメールアドレスを含む約12.6万人（うち同社従業員・デモアカウント約4.2万人）と、メールなし約18.1万人。会社は同一会員IDの重複と攻撃者作成アカウントを除いた推計値としている。[^commune]

| 単位 | 数値 | 根拠と注意 |
| --- | ---: | --- |
| 漏えいした会員 | 約307,000人 | 会社推計、同一IDの重複除外 |
| メールアドレスを含む会員 | 約126,000人 | うち従業員・デモ用約42,000人を含む |
| メールを含まない会員 | 約181,000人 | 表示名、プロフィール、非公開グループ所属等 |
| 不正な仮パスワード変更 | **144人** | 30.7万人の一部であり別途人数へ加えない |

**144人の仮パスワードは本人操作によらず変更された**ことが確認されている。これは単純な情報持ち出しだけでなく、アカウント状態への**完全性侵害**を含む。元のログインパスワードそのものが外部へ漏えいした事実は確認されていない。[^commune]

## マルチテナントに特有の被害境界

顧客企業の会員が異なるコミュニティに加入していても、供給者システムの侵害によって連鎖的に影響し得る。**実人数の会社推計**と、各ブランドが後で発表する顧客向け件数は重複し得るため、後者を総数へ足さない。非公開コミュニティへの参加事実は、単なるメールの有無より利用者にとって機微となり得る。

## 防御・復旧の検証

仮パスワードの更新を伴う正規機能の呼出経路、認可・監査ログ、影響会員の既存セッション失効、会員への通知、第三者による後続アカウント変更の有無、顧客企業別の調査完了を確認する。侵入技術・CVE・攻撃者帰属・財務影響は未公表として留保する。[^commune]

[^commune]: コミューン株式会社「当社サービスCommune、Commune for Workへの不正アクセスによる個人情報漏えいのお知らせ」. https://communeinc.com/ja/news/2026oct09
