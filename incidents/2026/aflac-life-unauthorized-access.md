---
type: Cybersecurity Incident
title: アフラック生命保険 — 顧客ポータル等への不正アクセスと約440万人の個人情報漏えい
description: 2026年6月に発生した不正アクセスにより顧客・代理店情報が漏えいし、一部に保険料振替口座情報を含んだ事案。
resource: https://www.aflac.co.jp/info/yorisou_faq.html
tags: [japan, insurance, unauthorized-access, personal-data, financial-data, 2026]
status: draft
stale_after: 2026-10-15T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: アフラック生命保険株式会社
  sector: insurance
  jurisdiction: JP
  incident_status: monitoring
  attack_type: "unauthorized access resembling legitimate application use and high-volume data queries"
  earliest_known_activity: "2026-06-10"
  detected_at: "2026-06-25 06:30 JST"
  first_disclosed_at: "2026-06-30"
  latest_public_update: "2026-10-01"
  intrusion_vector: "application-level access pattern; exact credential/exploit path not publicly disclosed"
  affected_services: "Aflac Yorisou Net and related systems"
  data_exposure: confirmed
  availability_impact: "Yorisou Net suspended as containment; partially resumed 2026-09-28"
  restoration_state: "major service resumed after countermeasures and validation; some procedures still unavailable as of 2026-09-28"
  secondary_abuse: not_observed
sources:
  - id: aflac-faq
    resource: https://www.aflac.co.jp/info/yorisou_faq.html
    title: 当社システムに対する不正アクセスの発生および情報漏えいに関するFAQ
  - id: aflac-status
    resource: https://www.aflac.co.jp/info/yorisou_maintenance.html
    title: 当社システムに対する不正アクセスの発生および情報漏えいに関するお詫び
  - id: aflac-resume
    resource: https://www.aflac.co.jp/canet/login-guide/
    title: アフラック よりそうネット サービス再開のご案内
  - id: aflac-news
    resource: https://www.aflac.co.jp/corp/profile/news/2026/
    title: アフラック生命保険 ニュースリリース 2026年
---

# 概要

アフラック生命保険では、2026年6月10日から25日にかけて「アフラック よりそうネット」等へ複数回の不正アクセスが行われ、顧客・代理店の個人情報を含む情報が不正閲覧され、漏えいした。6月25日6時30分、CPU高負荷を検知したことを契機に調査が始まった。[^aflac-faq]

最終的に公表された顧客関連の漏えい対象は約440万人で、このうち約22万人には保険料振替口座情報が含まれる。契約者・被保険者・受取人情報、証券番号、保障内容、第二連絡先、口座情報等が対象になり得る一方、マイナンバー、クレジットカード情報、メールアドレス、「よりそうネット」のID・パスワードは漏えい対象外とされた。[^aflac-faq]

原因分析では、今回のアクセス形式が通常利用と同様に見えたため既存の不正アクセス検知・遮断で直ちに識別できず、短時間の大量照会を監視・制御する機能も不足していた。設計時レビューやリリース前侵入テストでも今回の手口に関するリスクを想定できていなかった。[^aflac-faq]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-06-10 | 現在の調査で確認された最初の不正アクセス。[^aflac-faq] |
| 2026-06-10 – 06-25 | 複数回の不正アクセスを確認。[^aflac-faq] |
| 2026-06-25 06:30 | CPU高負荷を検知し調査開始。[^aflac-faq] |
| 2026-06-30 | 初回の対外公表。2026年ニュースリリース一覧に記録。[^aflac-news] |
| 2026-07-10 – 07-30 | 漏えい対象顧客への書面発送を順次実施し、7月30日に完了。[^aflac-faq] |
| 2026-07-31 | 調査結果と再発防止策を公表。[^aflac-news] |
| 2026-09-28 | 再発防止策と安全性検証後、「よりそうネット」を一部機能を除き再開。[^aflac-status][^aflac-resume] |
| 2026-10-01 | FAQ更新。漏えい口座情報を該当金融機関へ提供し、不正取引監視強化等に利用する対応を説明。[^aflac-faq] |

# 影響

## Personal data

顧客関連の漏えいは約440万人。対象者によって項目は異なるが、公開された項目には契約者の氏名、生年月日、性別、住所、電話番号、被保険者の氏名・生年月日・性別、受取人氏名、証券番号、保障内容、第二連絡先等が含まれる。[^aflac-faq]

契約中の顧客だけでなく過去契約者も対象になり得る。[^aflac-faq]

## Financial アカウント data

約22万人では、金融機関名、支店名、預金種類、口座番号、口座名義など保険料振替口座情報も漏えい対象となった。アフラックは対象口座情報を金融機関へ提供し、各金融機関で不正取引監視強化等の対応が実施または検討されている。[^aflac-faq]

口座情報が漏えいしたこと自体を、直ちに預金引き出し可能な状態と同一視しない。ただし、契約情報や本人属性と組み合わせた社会工学・詐欺リスクが高まるため、同社は金融機関・警察・公的機関等を装う電話やSMSへの注意を呼びかけている。[^aflac-faq]

## Data explicitly outside scope

マイナンバー、詳細なクレジットカード情報、メールアドレス、「よりそうネット」のID・パスワードは漏えいしていないと公表された。[^aflac-faq]

## 可用性

情報漏えい拡大防止のため「よりそうネット」は停止された。再発防止策と安全性検証後、9月28日に一部機能を除き再開した。支援金・祝金等の一部手続きや受取人/指定代理請求人の登録・変更は同日時点でWebから利用できず、コールセンター等で代替受付していた。[^aflac-status][^aflac-resume]

# 技術的に確認できた事項

本件で公開された技術的な核心は、明白な異常リクエストではなく**通常利用と同様の形式に見えるアクセスとデータ照会**が悪用された点にある。既存の検知・遮断機能はあったが直ちに不正と識別できず、短時間の大量照会を監視・制御する機能も不足していた。[^aflac-faq]

また、設計時のセキュリティレビューとリリース前侵入テストは実施されていたにもかかわらず、今回の手口に関するリスクを想定できていなかった。[^aflac-faq]

公開資料からは、初期認証の突破方法、セッション取得方法、利用されたアカウント、具体的なAPI/画面、攻撃元インフラは判断できない。そのため認証情報窃取や特定脆弱性の悪用を推測しない。

# 対応と復旧

- 影響拡大防止のため「よりそうネット」等を停止。[^aflac-status]
- 外部専門機関を含む調査を実施し、7月31日に原因・影響範囲・再発防止策を公表。[^aflac-faq][^aflac-news]
- 漏えい対象顧客へ7月10日から30日に書面通知。[^aflac-faq]
- 口座情報が漏えいした対象について、金融犯罪防止目的で金融機関へ必要情報を提供し監視強化に接続。[^aflac-faq]
- 再発防止策実施と安全性検証後、9月28日に主要オンライン機能を再開。[^aflac-status][^aflac-resume]

# 現在の状況と予後

2026年10月1日時点では、情報の不正利用等は確認されていない。主要オンラインサービスは再開したが、一部手続きは未復旧であり、漏えい口座情報に対する金融機関側の監視も継続している。[^aflac-faq][^aflac-status]

したがって、インシデント原因・対象範囲の調査は成熟しているものの、顧客保護とサービス正常化が継続中という意味で `monitoring` とする。

# 防御上の教訓

- **正規に見える操作の異常量を検知する。** WAFや単純なシグネチャだけでなく、短時間の大量照会、通常利用から外れたデータ探索量、セッション単位の取得量を制御する必要がある。[^aflac-faq]
- **ペネトレーションテスト実施済みを安全性の証明にしない。** 想定されなかった業務ロジック/照会パターンは従来レビューを通過し得る。[^aflac-faq]
- **漏えい後の防御を外部機関へつなぐ。** 口座情報が含まれたケースで金融機関へ対象データを渡し、不正取引監視へ接続した対応は、事後の被害抑制策として再利用価値が高い。[^aflac-faq]
- **復旧完了を二値化しない。** サービス再開後も一部機能が代替チャネル運用であり、可用性回復は段階的である。[^aflac-status]

# 不明点・未公表事項

- 最初の認証突破またはセッション取得方法
- 攻撃に使われた具体的エンドポイント/API/アカウント
- 攻撃元・攻撃主体
- 不正アクセスごとの取得量と全活動ログ
- 9月28日時点で未再開だった機能の完全復旧時期
- 7月31日以降に新たな二次被害が確認されたかの継続的な最終評価

[^aflac-faq]: アフラック生命保険「当社システムに対する不正アクセスの発生および情報漏えいに関するFAQ」2026-10-01時点.
[^aflac-status]: アフラック生命保険「当社システムに対する不正アクセスの発生および情報漏えいに関するお詫び」2026-09-28.
[^aflac-resume]: アフラック生命保険「アフラック よりそうネット サービス再開のご案内」.
[^aflac-news]: アフラック生命保険「ニュースリリース 2026年」.
