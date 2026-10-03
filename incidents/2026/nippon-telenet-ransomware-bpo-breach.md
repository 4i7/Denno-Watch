---
type: Cybersecurity Incident
title: 日本テレネット — ネットワーク機器経由のランサムウェア侵害と受託データの広範な潜在影響
description: 2026年3月の侵入・暗号化から、約60.2万件のCSS/L-net受託情報、約40.4万件のBPO受託情報を含む潜在影響、クリーンネットワーク再構築までを追跡する記録。
resource: https://www.nippon-tele.net/release/20260612_4659/
tags: [japan, ransomware, bpo, managed-services, supply-chain, network-appliance, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
incident:
  organization: 日本テレネット株式会社
  sector: information-services-and-bpo
  jurisdiction: JP
  incident_status: investigation_complete_monitoring_continues
  attack_type: ransomware
  earliest_known_activity: "2026-03-09"
  detected_at: "2026-03-09"
  first_disclosed_at: "2026-03-17"
  latest_public_update: "2026-06-12"
  public_record_checked_at: "2026-10-04T05:25:00+09:00"
  intrusion_vector: "external attacker entered the internal network via network equipment; specific weakness or credential path not publicly disclosed"
  affected_services: "internal network, file servers, CSS/L-net and BPO entrusted-data environments"
  data_exposure: possible
  availability_impact: confirmed
  restoration_state: "clean network built independently from the old environment; business PCs reimaged; monitoring and hardening continue"
  secondary_abuse: not_observed
  downstream_impact: "entrusted client data formed the largest potentially affected populations"
  regulatory_response: "reported to the Personal Information Protection Commission; consulted Kyoto Prefectural Police and relevant authorities"
  notification_state: "individual notification to be performed if later investigation establishes leakage risk"
  business_continuity: "recovery performed through a clean-network rebuild rather than simple reuse of the affected environment"
  data_sensitivity: "entrusted customer/contact data, business contacts, employee/former-employee/family information"
sources:
  - id: nippon-telenet-final
    resource: https://www.nippon-tele.net/release/20260612_4659/
    title: サイバー攻撃によるシステム障害発生に関する調査結果および再発防止策について
    author: organization:日本テレネット株式会社
  - id: nippon-telenet-index
    resource: https://www.nippon-tele.net/release/
    title: 日本テレネット株式会社 リリース一覧
    author: organization:日本テレネット株式会社
---

# Executive summary

日本テレネットでは2026年3月9日、外部攻撃者がネットワーク機器を経由して社内ネットワークへ侵入し、ファイルサーバ等がマルウェアによって暗号化された。外部専門家によるフォレンジック調査ではランサムウェア被害と確認された一方、データを外部へ転送した痕跡は検出されず、6月12日時点で情報の外部流通・公開・不正利用などの二次被害も確認されていない。[^nippon-telenet-final]

ただし「漏えいが確認されていない」ことと「侵害された環境に何が存在したか」は分けて扱う必要がある。潜在的に影響を受け得る保有情報として、CSS/L-net受託業務の個人情報約60.2万件、BPO受託業務の個人情報約40.4万件、営業・取引関係者情報約3.3万件、従業員・退職者・家族情報2,044件が公表された。これらは異なるデータ集合であり、ユニーク人数として合算しない。[^nippon-telenet-final]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-03-09 | サイバー攻撃によるシステム障害が発生。後の調査でネットワーク機器経由の侵入とランサムウェアによるファイルサーバ等の暗号化を確認。[^nippon-telenet-final] |
| 2026-03-17 | 初回の対外公表。[^nippon-telenet-index] |
| 2026-03 – 06 | 外部専門家によるフォレンジック、ダークウェブ調査、復旧対応、当局連携を継続。[^nippon-telenet-final] |
| 2026-06-12 | 調査結果・潜在影響範囲・復旧状況・再発防止策を公表。外部転送痕跡、公開、不正利用等は確認されていないと報告。[^nippon-telenet-final] |
| 2026-10-04 review | 公式リリース一覧を再確認し、6月12日より後の本件固有の公表は確認できなかった。[^nippon-telenet-index] |

# Impact

## Potentially affected information

| Population / data set | Public count | Evidence state |
| --- | ---: | --- |
| CSSサービス / L-net受託情報 | 約602,000件 | potentially affected; exfiltration not observed |
| BPO受託業務情報 | 約404,000件 | potentially affected; exfiltration not observed |
| 営業・取引先関係者情報 | 約33,000件 | potentially affected; exfiltration not observed |
| 従業員・退職者・家族情報 | 2,044件 | potentially affected; exfiltration not observed |

CSS/L-netには会社名、氏名、FAX番号等、BPOには氏名、住所、電話番号、メールアドレス、問い合わせ内容等が含まれ得る。営業・取引関係情報には会社・所属・役職・連絡先等、人事情報には家族情報等が含まれる。クレジットカード情報は対象情報に含まれないとされた。[^nippon-telenet-final]

件数はデータ集合の規模であり、重複関係が公表されていないため総人数へ変換しない。

## Availability and integrity

ファイルサーバ等で暗号化被害が確認され、既存環境をそのまま信頼して復旧するのではなく、独立したクリーンネットワークを新設し、全業務用PCを初期化・再キッティングした。これは可用性だけでなく、復旧後の環境完全性を再確立する対応として重要である。[^nippon-telenet-final]

# Technical findings

公開された初期侵入事実は「ネットワーク機器を経由して内部ネットワークへ侵入」までである。製品名、脆弱性、認証情報悪用の有無、ランサムウェアファミリ、横展開手法は公開されていないため推測しない。[^nippon-telenet-final]

# Response and recovery

- 既存環境から独立したクリーンネットワークを構築。[^nippon-telenet-final]
- ファイアウォール設定を見直し、ネットワーク分離を再構成。[^nippon-telenet-final]
- 全業務用PCを初期化し、安全確認済み端末のみ利用する運用へ変更。[^nippon-telenet-final]
- 旧環境とクリーン環境の混在を避ける端末・接続・データ移行時の検疫ルールを整備。[^nippon-telenet-final]
- アカウント管理・ログイン認証の統一、MFA、EDR、24時間365日のSOC、IT資産・脆弱性管理、教育・統制を強化。[^nippon-telenet-final]
- 個人情報保護委員会へ報告し、京都府警察等と連携。[^nippon-telenet-final]

# Prognosis / current state

6月12日時点で外部転送痕跡・公開・不正利用は確認されず、クリーン環境への再構築と主要な強化策が進んでいる。公開調査は成熟しているが、同社は外部専門業者によるダークウェブ調査を継続するとしているため、`investigation_complete_monitoring_continues` とする。[^nippon-telenet-final]

# Defensive lessons

- **委託先の保有コピーをサプライチェーン資産として棚卸しする。** 最大の潜在影響集合は自社営業情報ではなく受託データだった。
- **復旧時に信頼境界を再構築する。** 独立クリーンネットワーク、PC再キッティング、データ検疫を組み合わせた点は、侵害環境の単純復元より強い回復モデルである。[^nippon-telenet-final]
- **「流出痕跡なし」と「影響対象なし」を同義にしない。** 漏えい未確認でも、侵害環境内の受託データ母集団は明示して追跡する必要がある。

# Unknowns / withheld details

- ネットワーク機器の製品・バージョン
- 脆弱性悪用か認証情報悪用かを含む具体的初期侵入方法
- ランサムウェアファミリと攻撃主体
- 暗号化対象の正確なサーバー・ファイル数
- 公表されたデータ集合間の重複関係

[^nippon-telenet-final]: 日本テレネット株式会社「サイバー攻撃によるシステム障害発生に関する調査結果および再発防止策について」2026-06-12.
[^nippon-telenet-index]: 日本テレネット株式会社「リリース」一覧、2026-10-04確認。
