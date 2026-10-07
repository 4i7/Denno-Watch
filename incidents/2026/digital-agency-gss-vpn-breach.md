---
type: Cybersecurity Incident
title: デジタル庁 / GSS — 既知VPN脆弱性悪用・保守運用アカウント経由／約24.6万件の個人情報に漏えい可能性
description: ガバメントソリューションサービスで既知のVPN脆弱性が修正前に悪用され、保守運用担当者アカウントを利用した大量ファイルアクセスを経て約24.6万件の個人情報に漏えい可能性が生じた事案。
resource: https://www.digital.go.jp/news/2026-0911-01
tags: [japan, government, vpn, known-vulnerability, privileged-account, personal-data, 2026]
status: draft
stale_after: 2026-11-07T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-07T08:39:00+09:00 }
incident:
  organization: デジタル庁
  sector: government
  jurisdiction: JP
  incident_status: contained_and_monitoring
  attack_type: known-vulnerability-exploitation
  earliest_known_activity: unknown
  detected_at: "2026-06-25"
  first_disclosed_at: "2026-09-11"
  latest_public_update: "2026-09-12"
  public_record_checked_at: "2026-10-07T08:39:00+09:00"
  intrusion_vector: "publicly known vulnerability in a network connection device (VPN), exploited before patch application"
  affected_services: "ガバメントソリューションサービス（GSS）"
  data_exposure: possible
  availability_impact: "侵害機器を封じ込めつつGSS利用機関向け業務を継続"
  restoration_state: "VPNパッチ適用、関係アカウント認証情報変更、外部通信遮断後、新たな不正アクセス・不審通信は未確認"
  secondary_abuse: not_publicly_disclosed
  downstream_impact: "GSS利用機関の職員・公務員等約18.9万件、関係事業者・個人約5.7万件"
  regulatory_response: "デジタル庁が公表・本人等への対応を進行"
  notification_state: "影響対象の特定と対応を進行"
  data_sensitivity: "氏名、メールアドレス、電話番号、住所等。マイナンバー、金融機関口座情報、年金番号は対象外"
sources:
  - id: digital-gss-primary
    resource: https://www.digital.go.jp/news/2026-0911-01
    title: ガバメントソリューションサービスへの不正アクセスによる職員等の個人情報の漏えいの可能性について
    author: organization:デジタル庁
  - id: digital-gss-qa
    resource: https://www.digital.go.jp/press/5fc99139-a4e2-4b7b-8b0c-d475e926143f
    title: 「ガバメントソリューションサービスへの不正アクセスによる職員等の個人情報の漏えいの可能性について」に関するQ&A
    author: organization:デジタル庁
---

# 概要

デジタル庁は2026年6月25日、ガバメントソリューションサービス（GSS）で保守運用担当者のアカウントを利用した大量ファイルアクセスを検知した。7月9日、第三者がネットワーク接続機器（VPN）の脆弱性を利用して侵入していたことが判明し、当該アカウント停止と侵害機器の外部通信遮断を実施した。[^digital-gss-primary]

外部専門事業者による調査の結果、個人情報を含むファイルの一部が外部へ漏えいした可能性があると判断し、9月11日に公表した。対象となる個人情報は約**24.6万件**である。[^digital-gss-primary]

# 影響

内訳は、GSS利用機関の職員および同機関の業務に携わった公務員等が約18.9万件、GSS利用機関の業務に携わった事業者・個人が約5.7万件である。一般国民の個人情報は含まれない。[^digital-gss-primary][^digital-gss-qa]

属性別では氏名約23.6万件、メールアドレス約23.1万件、電話番号約9.4万件、住所約0.1万件等で、重複を含む。マイナンバー、金融機関口座情報、年金番号等は対象外である。[^digital-gss-primary][^digital-gss-qa]

# 技術的に確認できた事項

Q&Aによれば、悪用されたVPN脆弱性は攻撃前から公表されていた既知脆弱性で、当初の深刻度評価はMediumだった。デジタル庁は一般的な対応より早く対処を進めていたものの、修正プログラム適用前に悪用されたとしている。具体的な脆弱性識別子は、今後のセキュリティ確保への支障を理由に非公表である。[^digital-gss-qa]

これは「パッチ未計画」ではなく、**対応中の既知脆弱性が適用完了前に実際に悪用された**ケースとして区別して記録する。

# 対応と復旧

- 侵害された保守運用担当者アカウントを停止。[^digital-gss-primary]
- 侵害機器の外部通信を遮断。[^digital-gss-primary]
- VPNへ修正プログラムを適用。[^digital-gss-qa]
- 関係アカウントの認証情報を変更。[^digital-gss-qa]
- 監視を強化し、封じ込め後の新たな不正アクセス・不審通信は未確認。[^digital-gss-qa]
- 脆弱性管理方法と外部接続方法の見直しを再発防止へ反映。[^digital-gss-primary]

# 現在の状況と予後

2026年9月12日時点で封じ込め措置後の再侵入は確認されていない。一方、公開情報上のデータ影響は「漏えいした可能性」の状態であり、confirmedへ引き上げない。

# 防御上の教訓

- **CVSSの公表値だけでパッチ優先順位を決めない。** 政府共通基盤や外部公開VPNでは資産重要度・到達性・悪用可能性を含む実質リスクで優先度を上げる必要がある。
- **VPN侵害と保守運用アカウントの利用は連鎖として監視する。** 境界機器から特権・運用アカウントへ到達した後の大量アクセス検知が重要になる。
- **大量ファイルアクセスは高価値な検知シグナルになり得る。** 本件では保守運用アカウントによる異常な大量アクセスが調査の起点となった。
- **パッチ適用中という状態自体がリスク窓である。** 公表から修正完了までの暫定緩和策を別途持つ必要がある。

# 不明点・未公表事項

- 悪用された具体的なVPN製品とCVE
- 攻撃者の初回侵入日時
- 外部へ実際に取得されたファイルの確定範囲
- 攻撃者帰属
- 長期的な本人影響・二次悪用評価

[^digital-gss-primary]: デジタル庁「ガバメントソリューションサービスへの不正アクセスによる職員等の個人情報の漏えいの可能性について」2026-09-11.
[^digital-gss-qa]: デジタル庁「『ガバメントソリューションサービスへの不正アクセスによる職員等の個人情報の漏えいの可能性について』に関するQ&A」2026-09-12確認.
