---
type: Cybersecurity Incident
title: 両毛システムズ — VPNアカウント悪用によるランサムウェア侵害と委託元へのサプライチェーン波及
description: 2026年8月のVPNアカウント悪用による侵入、ランサムウェア確認、受託データの漏えい可能性、大東ガス約12.4万件・伊勢崎市3,789件等の下流影響を追跡する記録。
resource: https://www.ryomo.co.jp/news/202609_02.html
tags: [japan, ransomware, vpn, managed-services, supply-chain, entrusted-data, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 株式会社両毛システムズ
  sector: information-services-and-systems-integration
  jurisdiction: JP
  incident_status: investigation_and_downstream_notification
  attack_type: ransomware
  earliest_known_activity: "2026-08-12"
  detected_at: "2026-08-14 early morning"
  first_disclosed_at: "2026-08-15"
  latest_public_update: "2026-09-30 downstream disclosure"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: "abuse of a VPN account to enter the internal network; how that account was obtained is not publicly established"
  affected_services: "internal network and servers, including files/data retained for customer and delegated operations"
  data_exposure: possible
  availability_impact: confirmed
  restoration_state: "containment and recovery progressed; forensic investigation and downstream scope/notifications continue"
  secondary_abuse: not_observed_in_reviewed_downstream_disclosures
  downstream_impact: "multiple entrusted organizations, including Daito Gas and Isesaki City, identified potentially affected copies held by Ryomo"
  regulatory_response: "affected downstream organizations have issued notifications and protective actions"
  notification_state: "provider and downstream customers continue identifying and notifying affected populations"
  business_continuity: "downstream organizations applied protective actions without evidence that their own production systems were directly breached"
  data_sensitivity: "business/transaction data and personal information of customer organizations, their customers, employees and students depending on entrusted dataset"
sources:
  - id: ryomo-third
    resource: https://www.ryomo.co.jp/news/202609_02.html
    title: 当社への不正アクセスに関する調査結果等について（第3報）
    author: organization:株式会社両毛システムズ
  - id: daito
    resource: https://www.daitogas.co.jp/info/170
    title: 両毛システムズのサイバー攻撃に伴う当社顧客情報の漏えい可能性について
    author: organization:大東ガス株式会社
---

# 概要

両毛システムズは2026年8月12日、外部第三者にVPNアカウントを悪用され社内ネットワークへ侵入された。8月14日未明に異常を検知してネットワークを遮断し、外部専門機関による調査を開始した。9月25日の第3報で、本件がランサムウェア攻撃だったこと、複数サーバーに不正アクセス痕跡があり、営業・取引・個人情報が漏えいした可能性があることを公表した。[^ryomo-third]

本件の重要性は、両毛システムズ自身の情報だけでなく、業務委託・システム作業等で同社環境に保持されていた下流組織のデータへ影響が波及した点にある。大東ガスは過去顧客情報を含む約12.4万件のファイルが漏えいした可能性を公表し、伊勢崎市では児童生徒3,789件のアカウント情報が影響対象になった。これらは下流組織自身の本番システムが直接侵害されたことを意味しない。[^daito][^ryomo-third]

外部の攻撃者集団による犯行声明は存在するが、両毛システムズは攻撃主体を公式認定していないため、本記録では帰属しない。

# 公開情報で確認できる時系列

| 日付 | 公開情報で確認できる出来事 |
| --- | --- |
| 2026-08-12 | VPNアカウントを悪用した第三者が社内ネットワークへ侵入。後の調査で特定。[^ryomo-third] |
| 2026-08-14 early morning | 社内監視で異常を検知し、ネットワーク遮断。 |
| 2026-08-15 | 第1報、外部専門機関によるフォレンジック開始。 |
| 2026-09-25 | 第3報。ランサムウェア攻撃であったこと、VPNアカウント悪用、不正アクセス痕跡、情報漏えい可能性を公表。[^ryomo-third] |
| 2026-09-25 onward | 委託元が自組織への影響を公表。大東ガスは約12.4万件、伊勢崎市は児童生徒3,789件等を対象として保護措置・通知。[^daito] |
| 2026-09-30 | 追加の委託元公表が続き、サプライチェーン影響範囲が拡大。 |

# 影響

## 提供事業者-side impact

一部サーバーで第三者不正アクセス痕跡が確認され、営業情報・取引情報、取引先顧客や従業員等の個人情報に漏えい可能性がある。全体の確定漏えい件数は公表されていない。[^ryomo-third]

## Downstream entrusted data

大東ガスは、両毛システムズ側に保持されていた過去顧客情報を含むファイル約12.4万件について漏えい可能性を公表した。含まれる情報として氏名、住所、電話番号、料金番号、顧客番号、ガスメーター、ガス使用量・料金等が示されている。[^daito]

伊勢崎市については児童生徒3,789件のアカウント情報（学校・学年・氏名・ふりがな・アカウント名・端末パスワード等）が影響対象となり、市は対象パスワード変更や端末利用の一時中断等を実施したと公表されている。

件数の単位・母集団が異なるため、複数委託元の値を「両毛システムズの総被害人数」として単純合算しない。

# 技術的に確認できた事項

公式に確認された初期侵入はVPNアカウントの悪用。VPNアカウントが攻撃者へ渡った方法、MFA状態、VPN機器脆弱性の利用有無、権限範囲は公開されていない。後続調査でランサムウェア攻撃と確定したが、ファミリ名・攻撃主体は会社から公表されていない。[^ryomo-third]

# 対応と復旧

- 8月14日の異常検知後、ネットワークを遮断。[^ryomo-third]
- 外部専門機関によるフォレンジックと復旧調査。[^ryomo-third]
- 委託元ごとに保持コピーを照合し、影響対象を通知。[^daito]
- 下流組織はパスワード変更や端末利用制限など、直接侵害されていなくても予防的保護措置を実施。

# 現在の状況と予後

9月末時点でも下流組織から追加影響公表が続き、プロバイダー横断の最終母集団は確定していない。したがって `investigation_and_downstream_notification` とする。

# 防御上の教訓

- **委託先の「作業用コピー」を資産台帳に含める。** 本番システムが無傷でも、保守・移行・受託作業用に残ったデータが漏えい対象になる。
- **VPNアカウントは機器ではなく資格情報ライフサイクルまで監査する。** 公式に確認された侵入経路はアカウント悪用であり、製品脆弱性と同一視しない。
- **供給者侵害の影響は下流公表で増える。** プロバイダーの初報だけで被害範囲を固定しない。
- **下流件数を無条件に合算しない。** データ集合・時点・単位が異なり重複も未確定である。

# 不明点・未公表事項

- VPNアカウント取得の具体的方法とMFA状態
- VPN機器脆弱性利用の有無
- ランサムウェアファミリ/攻撃主体
- 両毛システムズ全体の最終漏えい対象件数
- 全委託元・全保持コピーの最終範囲
- 二次被害の最終評価

[^ryomo-third]: 両毛システムズ「当社への不正アクセスに関する調査結果等について（第3報）」2026-09-25.
[^daito]: 大東ガス「両毛システムズのサイバー攻撃に伴う当社顧客情報の漏えい可能性について」2026-09-25以降の公表.
