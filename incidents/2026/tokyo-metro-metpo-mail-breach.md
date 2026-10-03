---
type: Cybersecurity Incident
title: 東京メトロ / メトポ — メール配信サービス不正アクセスと約5万9000件のメールアドレス閲覧・取得可能性
description: 2026年9月にメトポ会員向けメール配信サービスで発生した不正アクセス、約59,000件の配信停止中メールアドレスへの影響、データ分離によるblast radius限定を追跡する記録。
resource: https://www.to-me-card.jp/important/202609-01/index.html
tags: [japan, transportation, loyalty-program, email, unauthorized-access, data-separation, 2026]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T19:54:53Z }
incident:
  organization: 東京地下鉄株式会社 / メトロポイントクラブ（メトポ）
  sector: transportation-and-loyalty-services
  jurisdiction: JP
  incident_status: investigating
  attack_type: unauthorized-access
  earliest_known_activity: unknown
  detected_at: "2026-09-25 (investigation triggered by 2026-09-20 mail-service malfunction)"
  first_disclosed_at: "2026-09-27"
  latest_public_update: "2026-09-27"
  public_record_checked_at: "2026-10-04T04:54:53+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "Metpo member mail-delivery service server holding addresses whose delivery had been suspended"
  data_exposure: possible_viewing_or_acquisition
  availability_impact: "mail-delivery service malfunction observed; rail operations not implicated"
  restoration_state: "suspected access point identified and technical blocking measures implemented; impact and root-cause investigation ongoing"
  secondary_abuse: unknown
sources:
  - id: metro-primary
    resource: https://www.to-me-card.jp/important/202609-01/index.html
    title: メトポ会員向けサービスにおける不正アクセス事案の発生について
    author: organization:Tokyo Metro
---

# Executive summary

東京地下鉄は2026年9月27日、メトロポイントクラブ（メトポ）の会員向けサービスで第三者による不正アクセスが行われ、**約59,000件のメールアドレス**が閲覧または取得された可能性があると公表した。[^metro-primary]

対象は、メール送信不能のため東京メトロ側で配信を停止していたメールアドレスを格納するサーバーである。同社は、当該サーバーにはメールアドレス以外の会員情報が含まれていないことを確認した。[^metro-primary]

9月20日にメトポのメール配信サービスで不具合が発生し、その調査中の9月25日に通常とは異なる利用記録を発見。詳細確認により、国外からと思われる第三者の不正アクセスが判明した。[^metro-primary]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-09-20 | メトポのメール配信サービスで不具合が発生し、調査開始。[^metro-primary] |
| 2026-09-25 | 通常と異なる利用記録を発見。詳細確認により国外からと思われる第三者の不正アクセスを確認。[^metro-primary] |
| 2026-09-27 | 約59,000件の配信停止中メールアドレスに閲覧・取得可能性があることを公表。被疑箇所特定と技術的防御措置、ログ保全、影響調査、関係機関連携を公表。[^metro-primary] |

# Impact

## Potentially affected data

対象は**メール配信を停止した顧客のメールアドレス約59,000件**。これは公表時点の値であり、今後の調査結果で変更される可能性がある。[^metro-primary]

会社は当該サーバーにメールアドレス以外の会員情報が含まれていないことを確認している。一方、その他の会員情報が別経路で閲覧・取得されていないかは引き続き調査中としている。[^metro-primary]

## Data separation

被害対象サーバーが「配信停止中メールアドレス」という限定された用途だったため、氏名、住所、ポイント情報、決済情報等が同じサーバーから漏えいする構造ではなかったことが公開情報から確認できる。[^metro-primary]

これは被害の小ささを意味するものではないが、サービス機能ごとのデータ分離がblast radiusを限定した観測例である。

## Service impact

9月20日にメール配信サービスの不具合が発生したことは公表されているが、鉄道運行や他の東京メトロ事業への障害は本公表では示されていない。したがって鉄道運行への影響を推測しない。[^metro-primary]

# Technical findings

公開情報で確認できる技術的事実は以下。

- 国外からと思われる第三者による不正アクセス。[^metro-primary]
- メール配信停止中アドレスを格納するサーバーへのアクセスを確認。[^metro-primary]
- 通常とは異なる利用記録が検知端緒。[^metro-primary]
- 不正アクセスされた被疑箇所を特定し技術的防御措置を実施。[^metro-primary]

初期侵入経路、脆弱性、認証情報悪用の有無、攻撃元、滞在期間、実際の取得操作は公表されていない。

# Response and recovery

緊急対策として以下が公表された。[^metro-primary]

- 被疑箇所の特定と技術的防御措置
- 利用記録の保全
- 影響範囲調査
- 委託先を含む原因調査
- 関係機関への報告・連携
- 影響対象の可能性がある顧客へのメール通知

恒久対策は公表時点では検討中。

東京メトロは、本件案内メールから別途手続きや外部サイト遷移を求めることはないと明示し、便乗フィッシングへの注意を呼びかけた。[^metro-primary]

# Prognosis / current state

2026年10月4日時点で確認できる本件の一次公表は9月27日の初報であり、影響範囲・原因・恒久対策の調査が継続しているため `investigating` とする。

# Defensive lessons

- **機能ごとにデータを分離する。** 配信停止中メールアドレス用サーバーに他の会員情報を置いていなかったことが、確認された直接の影響範囲を限定した。
- **可用性異常をセキュリティ調査へ接続する。** 9月20日のメール配信不具合の調査が、9月25日の異常利用記録発見と侵害確認につながった。
- **停止済み・休眠データも攻撃対象になる。** 現役配信先ではなく「送信不能で配信停止中」のアドレス集合が影響を受けたため、休眠データの保存必要性・隔離・削除期限も管理対象とすべきである。
- **通知チャネルの真正性を明示する。** 事故後の便乗詐欺を想定し、公式通知が外部サイト遷移を要求しないことを事前に示した。

# Unknowns / follow-up required

- 初期侵入経路・悪用された弱点
- 約59,000件のうち実際に取得された件数
- 攻撃開始時刻・滞在期間
- 委託先を含む原因調査結果
- その他の会員情報への影響有無の最終確認
- 恒久対策
- 二次被害の有無

[^metro-primary]: 東京地下鉄「メトポ会員向けサービスにおける不正アクセス事案の発生について」2026-09-27.
