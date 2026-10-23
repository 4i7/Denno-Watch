---
type: Cybersecurity Incident
title: IDCフロンティア — IDCFクラウドのランサムウェア／495企業・自治体に障害
description: IDCFクラウドのランサムウェア／495企業・自治体に障害
resource: https://www.idcf.jp/news/topics/20261007002
tags: [japan, 2026, cloud, ransomware, infrastructure, outage, shared-infrastructure]
status: draft
stale_after: 2026-10-11T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
incident:
  organization: 株式会社IDCフロンティア
  sector: cloud-infrastructure
  jurisdiction: JP
  incident_status: partial_backup_recovery_vm_restoration_unresolved
  attack_type: ransomware-confirmed
  detected_at: "2026-10-07 03:40 JST"
  first_disclosed_at: "2026-10-07"
  latest_public_update: "2026-10-18"
  public_record_checked_at: "2026-10-23T09:48:30.992+00:00"
  intrusion_vector: "specific initial vector not confirmed by public sources"
  affected_services: "IDCFクラウドのランサムウェア／495企業・自治体に障害"
  data_exposure: "VM-data-exfiltration-not_observed; portal-data-access-confirmed; personally-identifying-email-possible"
  availability_impact: "東日本リージョン1遮断と他リージョンの管理コンソール停止、契約495組織への影響"
  restoration_state: "2026-10-18非影響ゾーン向けバックアップサービス再開。スナップショット機能は停止、影響4ゾーンの全面VM復旧は未確認"
  downstream_impact: "ファイバーゲートはIDCF基盤利用を明示、ニッスイは日水物流の入出荷停止を公表するが一次資料には委託先名なし"
  secondary_abuse: not_publicly_disclosed
sources:
  - id: source-0
    resource: https://www.idcf.jp/news/topics/20261007002
    title: 発表資料／本文
    author: organization:株式会社IDCフロンティア 
  - id: source-1
    resource: https://www.idcf.jp/news/topics/20261007001
    title: 10月7日初報
    author: organization:公開資料 
  - id: fibergate
    resource: https://www.fibergate.co.jp/news/14742/
    title: クラウドサーバー停止に伴うサービス影響について
    author: organization:株式会社ファイバーゲート
  - id: nissui
    resource: https://www.nissui.co.jp/news/2026100702.html
    title: 日水物流株式会社におけるシステム障害について（第1報）
    author: organization:株式会社ニッスイ
  - id: idcf-fifth
    resource: https://www.idcf.jp/news/topics/20261014001/
    title: 〖第5報〗不正アクセスによる障害に関する調査の進捗について
    author: organization:IDCフロンティア
  - id: idcf-sixth
    resource: https://www.idcf.jp/news/topics/20261018001/
    title: 〖第6報〗バックアップサービスの提供再開について
    author: organization:IDCフロンティア
  - id: source-2
    resource: https://www.idcf.jp/pdf/cloud/pdf/IDCFCloud_security_WP.pdf
    title: 2026年4月1日発行IDCFクラウドセキュリティホワイトペーパー第13版
    author: organization:公開資料 
---

# IDCフロンティア — IDCFクラウドのランサムウェア／495企業・自治体に障害

## 事実・経過

2026年10月7日午前3時40分頃からIDCFクラウドの東日本リージョン1に障害が発生。初報では不正アクセスとされ、第2報において**ランサムウェア攻撃**と判明した。影響範囲はサービスを契約する**495の企業・自治体**。[^source-0]

10月7日の初報では外部からのアクセス検知とサービス障害が先に公表され、第2報でランサムウェア攻撃が確認された。[^source-1] 被害拡大・漏えい防止のため対象リージョンのネットワークを遮断しシステムを停止した。他リージョンの外部公開管理コンソールも安全確認の間停止している。侵入経路、復旧時期、データ持ち出しの有無は調査中である。495は**影響顧客の組織数**であり、漏えい件数でも人数でもない。[^source-0]

## 10月7日 下流のサービス・物流影響

**ファイバーゲート**は、自社のサービス・関連システムがIDCフロンティアのクラウド基盤に依存しており、IDCF側のランサムウェア攻撃による遮断・仮想マシン停止の影響を受けたと明示。顧客別復旧の実績・日時は別途確認する。[^fibergate]

**ニッスイ**は日水物流のシステム障害により、取り扱う商品の**入出荷ができない**と公表。委託先データセンターへの不正アクセスが原因とみられるが、ニッスイの一次公表は**IDCフロンティアという事業者名を示していない**。外部報道による関連付けとは明確に分離し、公式公表だけで同一インシデントだと確定しない。ニッスイ側の個人情報・顧客データ流出も調査中。[^nissui]

495は顧客組織数であり、すべての組織が商品入出荷停止を経験した数ではない。供給者の隔離・復旧と利用者の業務再開を別々に追跡する。

## 事故前に公表された統制の比較

同社の2026年4月のセキュリティホワイトペーパー8〜9ページは、クラウド管理コンソールでの二段階認証の提供、管理者による適用強制、接続元IP制限、定期的な脆弱性診断、24時間監視体制、検知から30分以内の顧客通知を**目標**として記載する。[^source-2]

これは平時の**制度・機能の説明**であって、今回の侵害経路が管理コンソールだった証明でも、当該対策が破られた証明でも、通知目標の遵守実績でもない。後続の調査と通知実測値で対照する必要がある。

## 10月14日第5報：顧客VMと運営ポータルの被害は別

外部の専門企業と協力してアクセスログ、認証・操作ログ、不正プログラム、外部持ち出しの痕跡を調査した結果、影響を受けた東日本リージョン1のtesla／henry／pascal／joule各ゾーンにおいて、**顧客VM内データの不正照会・外部持ち出し痕跡は確認されず、会社は外部流出なしと判断**した。これは**調査対象と期間についての会社判断**であり、ランサムウェアによる可用性侵害まで否定するものではない。[^idcf-fifth]

一方、**IDCFクラウドポータルでは48社の登録情報に対する不正照会を確認**。企業名、ログインID、強いランダムハッシュ化済みのログインパスワード、通知先、月額料金合計等を含み、**2社の各1メールアドレスは担当者の個人名を含む可能性**がある。不正照会は確定するが、外部への持ち出し痕跡は確認されていない。[^idcf-fifth]

| 事象 | 10月14日時点の状態 | 誤認を避ける単位 |
| --- | --- | --- |
| 影響4ゾーンの顧客VMファイル流出 | 調査で痕跡未確認、会社は流出なしと判断 | 仮想サーバー内データ |
| クラウドポータルの不正閲覧 | **確認** | 顧客48**社** |
| 個人名を含む可能性のあるメール | **可能性** | 2社、各1アドレス |
| ポータル登録情報の外部持ち出し | 痕跡未確認 | 閲覧と持ち出しを混同しない |
| ランサムウェアによる停止 | **確定** | 影響495**組織** |

## バックアップの存在と復元可能性は別

影響495社・自治体のうち**194組織**がIDCFのスナップショット機能を使っており、専門家の安全確認により**保存バックアップの取り出しが可能**と判明。しかしその時点では**取り出したデータを復元できるか・具体的な提供方法は検証中**である。**194社を復旧完了と数えず、495−194をデータ永久消失確定と数えない**。顧客自身の別環境バックアップも独立して評価する。[^idcf-fifth]

## 10月18日第6報：非影響ゾーンのバックアップサービス再開

IDCFが再開した**「IDCFクラウド バックアップ」**はradian／newtonゾーン、東日本リージョン2・3、西日本リージョン1など**VMが動作している非影響ゾーンの顧客向け**。このバックアップで別クラウドやオンプレミスへ復元できる。一方、**スナップショット機能は安全確認のため停止継続**、影響4ゾーンのVM全面復旧ではない。[^idcf-sixth]

| 復旧の境界 | 確認した状態 | 残る検証 |
| --- | --- | --- |
| 非影響ゾーンVM | 動作継続 | 顧客個別の安全確認 |
| 非影響ゾーンのバックアップ機能 | 10月18日再開 | 顧客環境での復元テスト |
| 全ゾーンのスナップショット機能 | 10月18日時点停止継続 | 安全確認・再開時刻 |
| 影響194組織の保存バックアップ | 取り出し可能 | **復元可能性と業務データ整合** |
| 495組織の業務 | 利用者ごとに異なる | 物流、決済、顧客向けサービスの正常化 |

事故前ホワイトペーパーの二段階認証・IP制限・監視体制に関する**制度・機能の説明**だけから、今回の初期侵入経路が管理コンソールだったと断定できない。[^source-2]

## 未確定

正確な侵入口、データ流出、別リージョンへの侵害、全顧客の復旧、財務影響、身代金要求はいずれも未確定。

[^source-0]: 発表資料／本文 — https://www.idcf.jp/news/topics/20261007002 （2026-10-08確認）。
[^source-1]: 10月7日初報 — https://www.idcf.jp/news/topics/20261007001 （2026-10-08確認）。
[^fibergate]: ファイバーゲート「クラウドサーバー停止に伴うサービス影響について」2026-10-07. https://www.fibergate.co.jp/news/14742/
[^nissui]: ニッスイ「日水物流株式会社におけるシステム障害について（第1報）」2026-10-07. https://www.nissui.co.jp/news/2026100702.html
[^source-2]: 2026年4月1日発行IDCFクラウドセキュリティホワイトペーパー第13版 — https://www.idcf.jp/pdf/cloud/pdf/IDCFCloud_security_WP.pdf （2026-10-08確認）。

[^idcf-fifth]: IDCフロンティア「〖第5報〗不正アクセスによる障害に関する調査の進捗について」2026-10-14. https://www.idcf.jp/news/topics/20261014001/
[^idcf-sixth]: IDCフロンティア「〖第6報〗バックアップサービスの提供再開について」2026-10-18. https://www.idcf.jp/news/topics/20261018001/
