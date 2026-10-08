---
type: Cybersecurity Incident
title: "埼玉県 渋沢MIX — 約2,200人の閲覧・3人の詳細閲覧・情報改ざんとメール送信"
resource: https://www.pref.saitama.lg.jp/a0803/news/page/news2026100702.html
tags: [japan, 2026, public-sector, integrity, email-abuse]
status: draft
stale_after: 2026-10-12T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
incident:
  organization: "埼玉県／渋沢MIX"
  sector: "public-sector"
  jurisdiction: "JP"
  incident_status: "investigating"
  attack_type: "unauthorized-access-and-data-modification"
  first_disclosed_at: "2026-10-07"
  latest_public_update: "2026-10-07"
  public_record_checked_at: "2026-10-08T09:54:43.887+00:00"
  data_exposure: "possible"
  detected_at: "2026-10-06"
  earliest_known_activity: "2026-10-06 18:30 JST"
  intrusion_vector: "管理システム脆弱性の悪用が疑われる、詳細は調査中"
  affected_services: "会員申請・施設予約と管理メール"
  availability_impact: "会員申請と施設予約を停止"
  restoration_state: "外部接続遮断とアップデート、調査中"
  secondary_abuse: "不正なメール送信は確定。金銭被害や二次被害は未確認"
  regulatory_response: "PPC報告を予定、完了は未公表"
  notification_state: "対象者に通知、詳細閲覧3名へ個別説明予定"
sources:
  - id: saitama
    resource: https://www.pref.saitama.lg.jp/a0803/news/page/news2026100702.html
    title: "渋沢MIXの管理システムへの不正アクセスについて"
    author: "organization:埼玉県"
---

# 埼玉県 渋沢MIX — 約2,200人の閲覧・3人の詳細閲覧・情報改ざんとメール送信

## 確認済みの機密性と完全性への影響

10月6日18:30頃、管理システムから第三者が関与したメール送信を確認。調査で約2,200名の会員等の氏名・メール一覧の**不正閲覧**と、うち3名の追加詳細閲覧、登録情報の一部**改ざん**、これに伴うメール送信を確認した。システム脆弱性が悪用された可能性があるが侵入手順の詳細は未公表。[^saitama]

閲覧・改ざん・メール送信は観測済みだが、埼玉県は外部へのデータ**窃取や二次被害を確認していない**。情報閲覧をファイル持ち出し確定と同義に扱わない。[^saitama]

## 封じ込めと行政対応

同日中にインターネットから遮断し、施設利用予約と新規会員登録申請を停止。システムを最新バージョンに更新。対象者へ通知し、3人は個別説明予定。PPC報告は実施予定の記述で、報告済みとは扱わない。復旧完了、メール送信件数、侵入経路、外部持ち出し有無を追跡する。[^saitama]


## 3つの独立した確定事実

| 侵害範囲 | 根拠に基づく認定 | 未確定事項 |
| --- | --- | --- |
| 約2,200名の氏名・メール等一覧 | **第三者の不正閲覧を確認** | 各人の全項目、外部データ窃取 |
| 3名の詳細情報 | **追加の不正閲覧を確認** | 詳細項目の内訳、再利用・悪用 |
| 登録情報と通知機能 | **一部改ざんと不正メール送信を確認** | 改ざん対象数、送信メールの通数、受信者への影響 |

**閲覧**と**サーバ外へのコピー**は異なる証拠。埼玉県は10月7日時点でデータの窃取、不正利用、二次被害を確認していないと明示している。ただし、改ざんと不正メール送信まで「未確認」と書き換えてはならない。[^saitama]

## インシデントが及んだ業務

管理システムをインターネットから遮断したため、施設利用予約と新規会員申請を停止。アップデート実施済みだが、予約再開や本人通知完了を意味しない。原因は脆弱性への攻撃と考えられるとの説明にとどまり、CVE・公開状態・具体的な不正操作は非公表。[^saitama]

PPCへの報告は個人情報保護法68条1項に基づき**行う予定**とされており、完了日を創作しない。確認すべき点は、約2,200名への通知、3名への詳細説明、改ざん前データとの整合、異常メール送信の遮断証明、最終復旧である。[^saitama]

[^saitama]: 埼玉県「渋沢MIXの管理システムへの不正アクセスについて」. https://www.pref.saitama.lg.jp/a0803/news/page/news2026100702.html
