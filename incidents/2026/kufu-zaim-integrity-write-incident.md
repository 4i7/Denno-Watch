---
type: Cybersecurity Incident
title: "くふう Zaim — 14名の登録情報書き換え確定、漏えい・不正ログインは未観測"
resource: https://kufu.co.jp/2026/09/22/zaim-announce/
tags: [japan, 2026, consumer-finance, integrity, repaired]
status: draft
stale_after: 2026-10-12T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
incident:
  organization: "くふうカンパニー／くふう Zaim"
  sector: "finance-app"
  jurisdiction: "JP"
  incident_status: "investigating"
  attack_type: "unauthorized-data-write"
  first_disclosed_at: "2026-09-22"
  latest_public_update: "2026-09-22"
  public_record_checked_at: "2026-10-08T06:48:28.488+00:00"
  data_exposure: "not_observed"
  earliest_known_activity: "2026-09-18 20:09 JST"
  detected_at: "2026-09-21 15:47 JST"
  affected_services: "登録情報と新規ユーザーの一部保存操作"
  intrusion_vector: "一部処理不具合を悪用したデータ書込み"
  availability_impact: "9月19〜21日の一部保存エラー、復旧済み"
  restoration_state: "2026-09-21中に修正・14人のデータ復元完了"
  secondary_abuse: "メールの第三者送信は未確認"
  regulatory_response: "監督官庁報告済"
  notification_state: "対象者へ個別連絡"
sources:
  - id: zaim
    resource: https://kufu.co.jp/2026/09/22/zaim-announce/
    title: "くふう Zaimへの不正アクセスによる登録情報書き換えについて"
    author: "organization:くふうカンパニー"
---

# くふう Zaim — 14名の登録情報書き換え確定、漏えい・不正ログインは未観測

## 外部からの書込みと復元

9月18日20:09〜19日01:42、外部者が処理不具合を悪用し**14人**のニックネーム、メールアドレス、旧認証方式のパスワード関連情報を改ざんした。新規ユーザーの一部で9月19〜21日に家計簿保存エラーが発生。21日15:47頃に検知し同日修正・復元完了。[^zaim]

## 漏えいではない完全性被害

情報改ざんは**confirmed**。一方、運営者は元の登録情報・家計簿データの外部読み取りを防ぐ仕組みだったとし、**漏えい、不正ログイン、第三者へのメール送信を確認していない**。現行ログインは別のくふうアカウントであり、旧認証関連値を現行パスワードの漏えいと誤認しない。収支・金融連携・予算データは書き換えられていないと公表。[^zaim]

9月21日に復旧し、対象者へ連絡・監督官庁へ報告。長期監視強化の実装は別途確認する。同じ運営者の10月「まちトークβ版」事件とは別系統で、共通攻撃者の証拠はない。[^zaim]

[^zaim]: くふうカンパニー「くふう Zaimへの不正アクセスによる登録情報書き換えについて」. https://kufu.co.jp/2026/09/22/zaim-announce/
