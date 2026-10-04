---
type: Cybersecurity Incident
title: Helpfeel / Gyazo — 2026年9月の不正アクセスと大規模情報流出
description: Gyazoへの不正アクセス、約2,362万ユーザー分のデータと大規模な画像メタデータ流出、サービス停止・段階的再開までを追跡する記録。
resource: https://corp.helpfeel.com/news/news-20260925-01
tags: [japan, saas, image-sharing, unauthorized-access, data-breach, credentials, metadata, 2026]
status: draft
stale_after: 2026-10-17T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T20:20:00Z }
incident:
  organization: 株式会社Helpfeel / Gyazo
  sector: software-as-a-service
  jurisdiction: JP
  incident_status: service_restored_investigation_continues
  earliest_known_activity: "2026-09-11"
  detected_at: "2026-09-11 night JST"
  first_disclosed_at: "2026-09-16"
  latest_public_update: "2026-09-29"
  affected_services: Gyazo
  data_exposure: confirmed
  availability_impact: "service temporarily suspended; legacy image delivery and viewing remain deliberately restricted after restart"
  restoration_state: "service resumed 2026-09-27; pre-incident images defaulted to owner-only, with Gyazo Teams access partially relaxed on 2026-09-29"
  secondary_abuse: "not observed as of 2026-09-25"
sources:
  - id: helpfeel-first
    resource: https://corp.helpfeel.com/news/news-20260916-1
    title: 「Gyazo」への不正アクセスによる情報漏えいに関するお知らせとお詫び
    author: organization:Helpfeel
  - id: helpfeel-second
    resource: https://corp.helpfeel.com/news/news-20260925-01
    title: 「Gyazo」への不正アクセスによる情報漏えいに関するお知らせとお詫び（第二報）
    author: organization:Helpfeel
  - id: helpfeel-recovery
    resource: https://corp.helpfeel.com/news/news-20260927-01
    title: 「Gyazo」サービス再開のお知らせ
    author: organization:Helpfeel
---

# 概要

2026年9月11日、Gyazoの画像アップロードサーバーに存在した脆弱性を利用した第三者による不正アクセスが発生した。Helpfeelは同日夜に不正な挙動を検知し、9月12日未明までに確認済みの侵入経路を遮断して原因となった脆弱性を修正した。[^helpfeel-first]

その後の調査でGyazoのデータベースへの不正アクセスと情報流出が確認された。9月16日の第一報ではユーザー関連データ約2,362万件、主に2019年1月以前の画像メタデータ約4.9億件、別条件で取得された画像メタデータ約240万件の流出を公表した。9月25日の第二報では、主に2023年2月以前に削除された画像に関するメタデータ約1.74億件の流出も追加確認された。[^helpfeel-first][^helpfeel-second]

二次被害防止のためGyazoは一時停止し、9月27日にサービスを再開した。再開時には侵害発生前にアップロードされた画像を原則として所有者本人のみ閲覧可能な状態へ変更した。9月29日にはGyazo Teamsについて、配信停止中でも同一チームのメンバーが一部画像を閲覧できるよう仕様を調整した。[^helpfeel-復旧]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-09-11 | 不正アクセス発生。同日夜に不正挙動を検知し調査開始。[^helpfeel-first] |
| 2026-09-12 未明まで | 確認済み侵入経路を遮断し、原因脆弱性の修正を完了。[^helpfeel-first] |
| 2026-09-14 | Gyazo内情報の外部流出を確認。画像配信停止等の予防措置を実施。[^helpfeel-first] |
| 2026-09-15 | 追加の二次被害防止措置。個人情報保護委員会へ速報を提出。[^helpfeel-first] |
| 2026-09-16 | 第一報を公表。[^helpfeel-first] |
| 2026-09-24 | サービス全体を一時停止。[^helpfeel-first] |
| 2026-09-25 | 第二報。削除済み画像メタデータ約1.74億件の追加流出を公表。[^helpfeel-second] |
| 2026-09-27 | サービス再開。侵害前画像は原則owner-onlyで再開。[^helpfeel-復旧] |
| 2026-09-29 21:30 | Gyazo Teamsについて、配信停止中の侵害前画像も同一チームメンバーが閲覧できるよう一部仕様変更。「自分のみ」設定とパスワード保護画像には従来の制約を維持。[^helpfeel-復旧] |

# 影響

## 利用者データ

約2,362万件のユーザー関連データが流出した。第二報時点の内訳は、メールアドレス未登録の匿名ユーザー約1,801万件（約76%）、メールアドレス登録済みユーザー約562万件（約24%）。全ユーザーで同じ項目が流出したわけではない。[^helpfeel-second]

対象には、ユーザーごとに氏名・ニックネーム、メールアドレス、パスワードのハッシュ値、利用者ID、端末ID、ログインセッションID、X連携用トークン、Google SSOメールアドレス、プロフィール、登録・最終ログイン日時、契約プラン、課金ステータス等が含まれ得る。クレジットカード番号等の決済情報は流出していない。[^helpfeel-first]

X連携用トークンは、後続調査で単体ではXアカウントへのログインや操作ができないことが確認され、関連するOAuth認証情報は予防的に無効化された。[^helpfeel-second]

## 画像メタデータ

| Data set | Confirmed scale | Public scope |
| --- | ---: | --- |
| 画像メタデータ | 約4.9億件 | 主に2019年1月以前にアップロード、総画像数の約14.4% |
| 条件を絞って取得された画像メタデータ | 約240万件 | 対象範囲は調査中、総画像数の約0.07% |
| 削除済み画像のメタデータ | 約1.74億件 | 主に2023年2月以前に削除、総画像数の約5.1% |

メタデータには画像ID、アップロード元IPアドレス、User-Agent、EXIF位置情報、OCRテキスト、画像タイトル、取得元URL、非公開画像のパスフレーズのハッシュ値等が含まれ得る。画像ファイルそのものの一括流出件数を示す数字ではない一方、画像ID等から対象画像へアクセスされる可能性と、非公開画像のファイル一覧が取得されていたことが公表されている。[^helpfeel-first][^helpfeel-second]

## 可用性と段階的復旧

保存済み画像の消失は確認されていないが、二次被害防止のため画像配信・閲覧が制限され、Gyazo全体が一時停止した。9月27日の再開時には、侵害前の画像を一律に所有者本人のみ閲覧可能とし、ユーザーが内容と閲覧範囲を確認してから従来の共有状態へ戻す安全側の復旧方式が採用された。[^helpfeel-復旧]

9月29日には業務利用への影響を緩和するため、Gyazo Teamsのみ、配信停止中であっても同一チーム内では侵害前画像を閲覧できるよう段階的に制約を緩和した。「自分のみ」設定は除外され、パスワード保護画像ではパスワード入力が引き続き必要とされた。配信を再開した画像は元の公開範囲へ戻る。[^helpfeel-復旧]

この経過は「サービス再開=事故前の公開状態へ即時復帰」ではなく、安全側の初期状態から機能ごとに段階復旧した事例として記録する。

HelpfeelとCosenseは別システムで、9月25日時点では両サービスからの情報流出、不正アクセス、攻撃痕跡は確認されていない。ただしGyazo画像を利用していた箇所では画像配信停止の影響を受け得た。[^helpfeel-second]

# 対応

公表済みの対応には、侵入経路の遮断、原因脆弱性の修正、認証関連情報の無効化・制限、画像閲覧制限、外部専門機関による調査、個人情報保護委員会・総務省・海外当局との連携、サービス全体の追加セキュリティ検証、認証・認可・アクセス制御の見直し、監視・監査体制と開発・レビュー体制の強化が含まれる。[^helpfeel-first][^helpfeel-second]

# 現在の状況と予後

9月27日にサービス自体は再開したが、事故前の画像公開状態は一括復元されていない。9月29日時点でも段階的な閲覧制御が継続し、外部専門機関を含む調査・検証と必要な追加対策が継続している。[^helpfeel-復旧]

したがって「復旧済み」と「調査完了」を分離し、`service_restored_investigation_continues` を維持する。

# 防御上の観察事項

- 封じ込め完了と影響範囲確定は別フェーズであり、後続調査で対象データが大幅に増えた。
- 画像本体だけでなく、URL構成情報、OCR、EXIF、IPアドレス等のメタデータ集合も高い機密性を持ち得る。
- 削除済みコンテンツでもメタデータの保持期間が長ければ別の露出面となる。
- サービス復旧時に旧公開状態を自動復元せず、共有範囲を安全側へリセットした点は再利用可能な復旧設計として重要。
- 機能制限を一括解除せず、Teams内共有のように対象と境界を限定して段階的に緩和する方式は、可用性と二次被害防止を両立する復旧パターンとして観測価値がある。[^helpfeel-復旧]

# 不明点・未解決事項

2026-10-04時点で公表情報から確定できない事項:

- 原因脆弱性の具体的な識別情報
- 不正アクセスの全活動期間と全操作内容
- 非公開画像が実際に第三者閲覧された件数
- 約240万件の追加メタデータの完全な対象範囲
- 外部専門機関による最終調査結果
- 個別通知の完了状況
- 侵害前画像の通常配信への全面復旧時期
- 本件に起因する後続の二次被害

未公表事項は「発生していない」とは扱わない。

[^helpfeel-first]: 株式会社Helpfeel「『Gyazo』への不正アクセスによる情報漏えいに関するお知らせとお詫び」
[^helpfeel-second]: 株式会社Helpfeel「『Gyazo』への不正アクセスによる情報漏えいに関するお知らせとお詫び（第二報）」
[^helpfeel-recovery]: 株式会社Helpfeel「『Gyazo』サービス再開のお知らせ」2026-09-29追記まで確認。
