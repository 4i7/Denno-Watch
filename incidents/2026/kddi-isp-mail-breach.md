---
type: Cybersecurity Incident
title: KDDI — ISP向け共通メール基盤へのゼロデイ悪用と大規模認証情報漏えい
description: 2026年5月から発生したISP向けメールシステムへの不正アクセスと、約1,223万人のメールアドレス・約762万人のパスワード漏えい、6事業者への波及を追跡する記録。
resource: https://newsroom.kddi.com/news/assets/2026/kddi_nr_s-73_4619/kddi_nr_s-73_4619_pdf_01.pdf
tags: [japan, telecom, supply-chain, zero-day, email, credentials, data-breach, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: KDDI株式会社
  sector: telecommunications
  jurisdiction: JP
  incident_status: public_report_closed_with_regulatory_followup
  attack_type: "exploitation of a then-vendor-unknown vulnerability in third-party software"
  earliest_known_activity: "2026-05-16"
  detected_at: "2026-06-17"
  first_disclosed_at: "2026-06-23"
  latest_public_update: "2026-08-19 regulatory follow-up"
  intrusion_vector: "third-party software vulnerability in shared ISP mail platform"
  affected_services: "KDDI ISP mail platform used by six providers"
  data_exposure: confirmed
  availability_impact: "no broad mail-service outage established in KDDI report; account-protection actions required"
  restoration_state: "vulnerability remediated 2026-06-17; EDR rollout and forced password changes conducted"
  secondary_abuse: unknown
sources:
  - id: kddi-first
    resource: https://newsroom.kddi.com/news/assets/2026/kddi_nr_s-71_4593/kddi_nr_s-71_4593_pdf_01.pdf
    title: ISP事業者向けメールシステムに対する不正アクセスの発生について
  - id: kddi-final
    resource: https://newsroom.kddi.com/news/assets/2026/kddi_nr_s-73_4619/kddi_nr_s-73_4619_pdf_01.pdf
    title: ISP事業者向けメールシステムに対する不正アクセスについてのお詫びとご報告
  - id: ppc-kddi
    resource: https://www.ppc.go.jp/news/careful_information/260819_mailservice/
    title: KDDI株式会社及びインターネットサービスプロバイダに対する行政上の対応並びに注意喚起
    author: organization:Personal Information Protection Commission Japan
---

# 概要

KDDIが6社のISP事業者向けに提供していた共通メール基盤で、2026年5月16日から一部事業者環境に不正アクセスが発生した。原因は、基盤に導入されていた第三者製ソフトウェアの脆弱性悪用で、KDDIが6月17日に侵害を確認した時点ではソフトウェアベンダー自身も認識していない脆弱性だった。KDDIは同日にシステムを改修し対処した。[^kddi-final]

7月6日の調査報告（7月21日人数訂正）では、同システムで作成された電子メールアドレス **12,231,954名分** と、その内数であるパスワード **7,616,173名分** の漏えいを確認した。初報時点の「最大1,422万件の可能性」から、調査により確定対象へ更新された。[^kddi-first][^kddi-final]

影響はSTNet、KDDIウェブコミュニケーションズ、JCOM、中部テレコミュニケーション、ニフティ、ビッグローブの6社に波及した。auメール、UQ mobileメール、au one netメールは別設備で、本件の影響対象外とされた。[^kddi-first][^kddi-final]

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-05-16 | 一部ISP事業者の環境で不正アクセス開始。後の調査で特定。[^kddi-final] |
| 2026-06-17 | KDDIが不正アクセスを確認。同日システムを改修し、脆弱性への対処と技術的防御措置を実施。[^kddi-final] |
| 2026-06-21 | 外部通信を制御する全サーバーへのEDR導入を完了。[^kddi-final] |
| 2026-06-23 | 初報。6 ISPと最大1,422万件のメールアドレス・パスワードに漏えい可能性があると公表。第三者製ソフトウェア脆弱性の悪用を公表。[^kddi-first] |
| 2026-06-23 | 第三者機関によるフォレンジック調査で、当該脆弱性以外の不審痕跡が存在しないことを確認。[^kddi-final] |
| 2026-06-24 | 総務省から電気通信事業法に基づく報告徴収。[^kddi-final] |
| 2026-07-06 | KDDIが報告書提出。漏えい確認件数を電子メールアドレス12,233,087名、パスワード7,616,173名と公表し、原因が検知時点でベンダー未認知の脆弱性だったことを説明。[^kddi-final] |
| 2026-07-21 | メールアドレス漏えい人数を12,231,954名へ訂正。[^kddi-final] |
| 2026-08-19 | 個人情報保護委員会がKDDIおよび関係ISPに対する個人情報保護法上の行政対応と利用者向け注意喚起を公表。[^ppc-kddi] |

# 影響

## Affected 提供事業者 and services

KDDIの初報で対象とされた6事業者は以下。[^kddi-first]

| 提供事業者 | Affected service |
| --- | --- |
| STNet | ピカラ光、ピカラモバイル、お仕事ピカラ関連メール |
| KDDIウェブコミュニケーションズ | レンタルサーバー CPI のメール |
| JCOM | J:COM NET、ケーブルテレビ事業者向けメール |
| 中部テレコミュニケーション | コミュファ光、ビジネスコミュファのメール |
| ニフティ | @niftyメール |
| ビッグローブ | BIGLOBEメール |

単一事業者の侵害ではなく、**共通基盤を介して複数ブランド・複数ISPへ同時に波及したサプライチェーン型の影響**として扱う。

## Confirmed data exposure

最終的に確認された対象は、電子メールアドレス12,231,954名分と、その内数であるパスワード7,616,173名分。[^kddi-final]

初報では、対象に解約済み・一定期間未利用の休眠顧客も含まれ得ること、パスワードにはハッシュ化・暗号化されたものも含むことが説明されている。[^kddi-first]

KDDI本体のauメール、UQ mobileメール、au one netメールは異なる設備で構築され、本件による漏えいはないとされた。[^kddi-final]

## アカウント-security impact

漏えい後の主要な顧客保護措置はパスワード変更で、ISP各社と連携し、利用頻度の低い顧客も含めて強制変更を進めた。[^kddi-final]

メールアカウントは他サービスのパスワード再設定や本人確認の受信点になり得るため、単純なメールアドレス漏えいとは別に、認証基盤としての二次波及リスクを持つ。ただし、本レポートでは公開根拠のない具体的アカウント乗っ取り件数を推定しない。

# 技術的に確認できた事項

侵入の起点は、KDDIが共通メール基盤へ導入していた第三者製ソフトウェアの脆弱性だった。調査によれば、KDDIが侵害を確認した2026年6月17日時点でソフトウェアベンダーはこの脆弱性を認識していなかった。[^kddi-final]

このため、既知CVEを未適用のまま放置した事案と同一視しない。公開情報上は、**ベンダー未認知の脆弱性を実運用環境で先に悪用されたゼロデイ相当の状況**である。[^kddi-final]

KDDIは第三者機関のフォレンジックで当該脆弱性以外の不審痕跡がないことを確認したと公表した。[^kddi-final]

製品名、脆弱性識別子、攻撃コード、攻撃主体、権限昇格・横展開の詳細はKDDI報告書では公開されていない。

# 対応と復旧

- 6月17日に被疑箇所を特定しシステム改修、脆弱性対処。[^kddi-final]
- 6月21日に外部通信を制御する全サーバーへEDR導入完了。[^kddi-final]
- 6月23日に第三者機関フォレンジックを実施し、別経路の不審痕跡なしを確認。[^kddi-final]
- 6 ISPと連携して顧客のパスワード変更を実施し、未変更アカウントへの強制変更を推進。[^kddi-final]
- ソフトウェア設計書・プログラムをAI等も利用して分析し、潜在的欠陥を網羅的に確認する方針を公表。[^kddi-final]
- 従来型メールクライアントへの影響を考慮しつつ、よりセキュリティ強度の高い通信規格へ早期移行する方針。[^kddi-final]
- 個人情報保護委員会・総務省への報告と、その後の行政対応。[^kddi-first][^ppc-kddi]

# 現在の状況と予後

技術的な侵入経路は6月17日に遮断され、調査・顧客保護措置・行政対応まで進んでいるため、公開情報上の主たるインシデント調査は成熟している。8月19日には個人情報保護委員会による行政上の対応と注意喚起が公表された。[^ppc-kddi]

Denno Watchでは `public_report_closed_with_regulatory_followup` とし、後続の行政文書や追加の確定被害が出た場合のみ更新する。

# 防御上の教訓

- **共通基盤のblast radiusを顧客ブランド単位ではなく依存関係グラフで管理する。** 1つのメール基盤の脆弱性が6 ISPへ同時波及した。[^kddi-first]
- **ゼロデイ前提の検知・封じ込めを持つ。** パッチ管理だけでは防げないため、外部通信・挙動監視、EDR、異常検知、侵害時の強制資格情報ローテーションが必要になる。[^kddi-final]
- **休眠・解約アカウントもデータ残存期間を含めてリスク評価する。** 初報では解約者・休眠顧客も対象に含まれ得るとされた。[^kddi-first]
- **共有サービスの事故対応契約には顧客側の強制保護措置まで含める。** ISP各社がパスワード強制変更を行える連携が二次被害抑制に使われた。[^kddi-final]
- **初期最大値と確定値を混同しない。** 1,422万件は初報時点の最大値であり、最終的な確認値はメールアドレス12,231,954名、パスワード7,616,173名である。[^kddi-first][^kddi-final]

# 不明点・未公表事項

- 第三者製ソフトウェアの製品名と脆弱性識別子
- 攻撃主体と攻撃インフラ
- 脆弱性悪用後の具体的な権限・操作経路
- 各ISPごとの全確定件数（KDDI全体値以外）
- 漏えい認証情報に起因する実際のアカウント不正利用の最終集計

[^kddi-first]: KDDI「ISP事業者向けメールシステムに対する不正アクセスの発生について」2026-06-23.
[^kddi-final]: KDDI「ISP事業者向けメールシステムに対する不正アクセスについてのお詫びとご報告」2026-07-06、2026-07-21更新.
[^ppc-kddi]: 個人情報保護委員会「KDDI株式会社及びインターネットサービスプロバイダに対する個人情報の保護に関する法律に基づく行政上の対応並びにメールサービス利用者に対する注意喚起について」2026-08-19.
