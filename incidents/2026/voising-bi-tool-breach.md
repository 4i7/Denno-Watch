---
type: Cybersecurity Incident
title: VOISING — BIツール既知脆弱性悪用による約17万件の個人情報漏えい
description: 2026年8月のBIツール侵害、個人情報ダウンロード、外部公開検知、9月30日の最終調査と侵害環境廃棄・再発防止策までを追跡する記録。
resource: https://voising-official.com/news/1015
tags: [japan, entertainment, bi, analytics, vulnerability, data-breach, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 株式会社VOISING
  sector: entertainment
  jurisdiction: JP
  incident_status: public_investigation_complete_monitoring_continues
  attack_type: "exploitation of a known vulnerability in a BI tool before the security fix was applied"
  earliest_known_activity: "2026-08-10 01:02 JST"
  detected_at: "2026-08-16 23:55 JST"
  first_disclosed_at: "2026-08-18"
  latest_public_update: "2026-09-30"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: "known BI-tool vulnerability; product/CVE not publicly identified"
  affected_services: "internal BI/analytics environment containing customer and service-usage data"
  data_exposure: confirmed
  availability_impact: "BI tool stopped; customer-facing service outage not established as the primary impact"
  restoration_state: "compromised environment discarded rather than restored; credentials invalidated/rotated and controls rebuilt"
  secondary_abuse: not_observed_as_of_final_report
  downstream_impact: "registered users, including service history and preference data"
  regulatory_response: "police consultation/report and Personal Information Protection Commission reporting completed"
  notification_state: "affected customers notified by email"
  business_continuity: "affected BI tool was stopped and isolated; compromised environment was not returned to service"
  data_sensitivity: "identity/contact data, purchase history, payment amounts, subscription status and selected favorite talent; no card data or login passwords held in the affected data"
sources:
  - id: voising-final
    resource: https://voising-official.com/news/1015
    title: 〖第四報〗当社が利用するBIツールへの不正アクセスおよび個人情報漏えいに関する調査結果と再発防止策について
    author: organization:株式会社VOISING
  - id: voising-news
    resource: https://voising-official.com/news
    title: VOISING News
    author: organization:株式会社VOISING
---

# 概要

VOISINGは2026年8月、社内で利用していたBIツールの既知脆弱性を悪用され、顧客データを含む分析環境へ侵入された。9月30日の最終調査では約17万件の個人情報漏えいを確認し、原因を「修正プログラム適用前に既知脆弱性を悪用されたこと」と公表した。[^voising-final]

漏えい項目には氏名・住所・電話番号・メールアドレス・生年月日・性別、購買履歴、決済金額記録、サービス加入状況、応援対象タレント（推し）の選択情報が含まれる。クレジットカード番号・有効期限・セキュリティコード・ログインパスワードは当該環境で保持しておらず漏えい対象外とされた。[^voising-final]

本件では侵害環境を復旧せず廃棄し、その環境にあった資格情報を全て失効・更新した。BI/分析環境を「社内補助ツール」ではなく、本番個人データを扱う重要境界として再設計した点が重要である。[^voising-final]

# 公開情報で確認できる時系列

| Date / time | Observable event |
| --- | --- |
| 2026-08-10 01:02 | 後の調査で不正アクセス開始時刻として特定。 |
| 2026-08-16 18:47–20:21 | 個人情報の不正ダウンロードが観測された時間帯。 |
| 2026-08-16 23:55 | 異常を検知。 |
| 2026-08-17 | BIツール停止。攻撃者作成アカウント/APIキー無効化、ネットワーク隔離等を実施。[^voising-final] |
| 2026-08-18 | 第1報を公表。 |
| 2026-08-24 | 第3報。関連情報の一部がSNS等の外部で公開されていることを確認。[^voising-news] |
| 2026-09-30 | 第4報/最終調査。約17万件の漏えい、既知脆弱性悪用、実施済み対策と再発防止策を公表。[^voising-final] |

# 影響

## Confirmed leaked data

最終公表値は約17万件。これは初期の可能性評価ではなく最終調査で確認された漏えい件数である。[^voising-final]

対象データは連絡先PIIだけでなく、購買履歴、支払金額、加入状況、推し選択のような嗜好・行動情報を含む。これらは単独では認証秘密でなくても、対象者に合わせたなりすましや詐欺の説得力を上げ得る。

## Excluded high-リスク data

VOISINGはカード番号、有効期限、セキュリティコード、ログインパスワードに相当する情報を当該環境で保持していなかったため、漏えい対象外と公表した。データ最小化/非保持が観測可能な被害縮小要因となった。[^voising-final]

# 技術的に確認できた事項

直接原因はBIツールの既知脆弱性に対する修正適用が、脆弱性公開から攻撃までの時間軸に間に合わなかったこと。製品名とCVEは公表されていないため、外部の脆弱性候補を結びつけない。[^voising-final]

# 対応と復旧

- 8月17日に対象BIツールを停止。[^voising-final]
- 攻撃者作成アカウント/APIキーを無効化。[^voising-final]
- 侵害環境を復旧せず廃棄し、保持資格情報を全失効・更新。[^voising-final]
- データ基盤へのアクセス経路を限定し、監査ログを有効化。[^voising-final]
- 資格情報を棚卸しし最小権限化。[^voising-final]
- 修正プログラム適用と関連パスワード/アクセスキー変更を完了。[^voising-final]
- 個人情報の仮名化・最小化、インターネット直接公開構成の見直し、大量取得/管理操作監視、ログ集約・保持延長を進める。[^voising-final]
- 警察・個人情報保護委員会への必要な対応を完了。[^voising-final]

# 現在の状況と予後

専門機関の最終調査と社内精査は完了し、主要封じ込め・再構築も完了している。一方でダークウェブ監視等は継続するため `public_investigation_complete_monitoring_continues` とする。[^voising-final]

# 防御上の教訓

- **BI/分析ツールを本番データ境界として管理する。** 分析環境の脆弱性が直接大規模漏えいへつながった。
- **パッチ公開から攻撃までの時間をSLA化する。** 脆弱性の深刻度ごとの対応期限と責任者を決める必要がある。[^voising-final]
- **侵害環境は必要なら廃棄する。** 復旧より再構築を選び、資格情報を全失効することで信頼状態を再確立した。
- **非保持は最も強い漏えい対策になり得る。** カード情報・ログインパスワードを保持しなかったことで影響範囲から外れた。

# 不明点・未公表事項

- BIツール製品名・CVE
- 攻撃主体
- 約17万件をユニーク人数へ変換した場合の人数
- 外部公開された全データの範囲と再拡散状況

[^voising-final]: 株式会社VOISING「〖第四報〗当社が利用するBIツールへの不正アクセスおよび個人情報漏えいに関する調査結果と再発防止策について」2026-09-30.
[^voising-news]: VOISING公式 News一覧、2026-10-04確認。
