---
type: Analysis Log
title: バックアップ・復元可能性・クリーン復旧 — 「バックアップあり」を復旧能力へ分解する
description: バックアップの存在ではなく、分離、変更不能性、復元試験、構成・秘密情報、復旧先の信頼性、業務整合性まで含めて実効的な復旧能力を評価する。
tags: [analysis, backup, recovery, ransomware, resilience, restoration, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T20:57:00+09:00 }
sources:
  - id: cisa-stopransomware
    resource: https://www.cisa.gov/stopransomware/ransomware-guide
    title: StopRansomware Guide
    author: organization:CISA
  - id: nist-ir
    resource: https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations
    title: NIST Revises SP 800-61
    author: organization:NIST
  - id: nist-ot-backup
    resource: https://csrc.nist.gov/pubs/sp/1339/final
    title: OT Backup Quick Start Guide
    author: organization:NIST
  - id: coop-yamaguchi
    resource: https://www.yamaguti-coop.or.jp/line-miniapp-incident-report2/
    title: コープやまぐちLINEミニアプリへの不正アクセスによる個人情報漏えいのおそれについて（第二報）
    author: organization:生活協同組合コープやまぐち
---

# 目的

「バックアップを取っている」は、復旧能力を意味しない。

事故時に必要なのは、**正しい時点のデータ・構成・ソフトウェア・秘密情報を、攻撃者から分離された信頼できる環境へ、目標時間内に復元し、業務側が正しい状態だと確認できること**である。

CISAはランサムウェア対策として、重要データのオフライン・暗号化バックアップ、定期的な可用性・完全性試験、ゴールデンイメージ、IaCテンプレート等を推奨している。アクセス可能なバックアップは攻撃者に削除・暗号化され得るため、分離が重要になる。[^cisa-stopransomware]

NIST SP 800-61r3でも、バックアップを作成・保護・維持・試験することを復旧に重要な統制として扱う。[^nist-ir]

# 復旧能力を七つへ分解する

| 要素 | 確認すること |
| --- | --- |
| 1. 対象網羅性 | データだけでなく構成・コード・証明書・手順等があるか |
| 2. 時点 | 必要なRPOを満たす復旧点があるか |
| 3. 分離 | 本番の侵害資格情報から削除・改変できないか |
| 4. 完全性 | バックアップ自体が改ざん・暗号化されていないか |
| 5. 復元可能性 | 実際に復元試験したか |
| 6. 復旧先の信頼 | 侵害済み環境へそのまま戻していないか |
| 7. 業務整合性 | 復元後のデータ・取引・外部連携が正しいか |

この七要素のどれか一つが欠けると、「バックアップ成功率100%」でも実際の復旧に失敗し得る。

# 何をバックアップするか

## データ

- DB。
- ファイル。
- オブジェクトストレージ。
- SaaS上の重要データ。
- ログ・監査証跡。

## 構成

- OS・アプリ設定。
- ネットワーク設定。
- IAMポリシー。
- クラウド設定。
- IaCテンプレート。
- CI/CD設定。

## 復旧に必要なソフトウェア

- ゴールデンイメージ。
- インストーラー。
- パッケージ。
- ソースコード。
- ライセンス情報。

## 信頼材料

- 証明書。
- 鍵の復旧手順。
- 秘密情報の再発行手順。
- ルート／特権アカウントの緊急復旧経路。

秘密情報そのものを不用意にバックアップへ複製するのではなく、安全な復旧・再発行経路を確保する。

## OT・現場系

NIST SP 1339はOTバックアップについて、制御ロジック、I/O一覧、安全要求、制御記述、原因結果表、ネットワーク・配線図、ヒストリアン設定等の工学資料も復旧に必要になり得ると整理している。[^nist-ot-backup]

# 分離を三種類に分ける

## 論理分離

- 別アカウント。
- 別テナント。
- 別資格情報。
- 削除保護。
- 変更不能ストレージ。

## ネットワーク分離

- 常時マウントしない。
- 本番セグメントから直接管理できない。
- 復旧時だけ限定接続する。

## 管理分離

最も見落とされやすい。

本番管理者とバックアップ管理者が同じIdP・同じ特権アカウント・同じ回復メールに依存していれば、データが別ストレージでも同時侵害される可能性がある。

# 「変更不能」の限界

変更不能ストレージでも、次は別問題である。

- 保存前に既に暗号化・破壊されていた。
- 保持期間が短すぎる。
- 管理者が保存ポリシー自体を変更できる。
- 復旧に必要な構成や鍵がない。
- 復元先が依然侵害されている。

したがって `immutable: true` を復旧保証として扱わない。

# 復元試験は「ファイルが戻った」で終わらない

復元試験を段階化する。

1. バックアップを読み出せる。
2. データ形式・ハッシュ・整合性が正しい。
3. 新しい環境へ復元できる。
4. アプリが起動する。
5. 認証・外部連携が動く。
6. 業務トランザクションを通せる。
7. 業務部門がデータ整合性を確認できる。
8. 想定RTO/RPO内に完了する。

本番への復元を毎回行う必要はないが、机上演習だけでは実測RTOにならない。

# 復旧点の選択

攻撃者が侵入してから検知まで数週間ある場合、「最新バックアップ」が最も汚染されている可能性がある。

復旧点選択には次が必要になる。

- 侵害開始の推定期間。
- 永続化・マルウェアの有無。
- 資格情報変更履歴。
- 構成変更履歴。
- バックアップ生成時刻。
- 重要取引の欠損量。

一つの復旧点だけでなく、複数世代を保持する価値がここにある。

# クリーン復旧

CISAはランサムウェア後、重要システムをクリーンなネットワークへ優先復旧し、復旧時にクリーン環境を再感染させないよう注意することを推奨している。[^cisa-stopransomware]

Denno Watchでは、次を区別する。

```text
restore_in_place
  既存環境へデータを戻す

rebuild_and_restore
  既知良好なOS/構成から再構築しデータを戻す

parallel_clean_environment
  分離した新環境を作り、検証後に切り替える
```

大規模侵害で信頼境界が不明な場合、単純な `restore_in_place` では侵害条件を温存する可能性がある。

# 国内の実例: コープやまぐち

2026年8月27日のコープやまぐち事例では、LINEミニアプリが利用するデータベースへ第三者が不正アクセスし、**DB内の全データが削除**された。外部アクセス遮断後、同日中にバックアップから復元し、対策後にサービスを再開している。[^coop-yamaguchi]

これは「破壊的な完全性被害でも、バックアップが実効的なら可用性を短時間で回復できる」具体例である。

ただし、サービス復旧は機密性調査の完了を意味しない。外部への取得有無は別問題として残った。

この事例から、復旧成功の記録には少なくとも次を分ける必要がある。

- データを戻せたか。
- どの時点へ戻ったか。
- 欠損があったか。
- サービスが再開したか。
- 漏えい調査が終わったか。

# ランサムウェアでは復旧元そのものが標的になる

CISAは、ランサムウェアがアクセス可能なバックアップを探索し、削除・暗号化して復元を困難にすることを前提に、オフラインバックアップと定期試験を勧めている。[^cisa-stopransomware]

そのため防御側は、バックアップサーバーを「保存装置」ではなく**最重要の復旧基盤**として扱う。

優先統制:

- 本番AD/IdPからの独立度を上げる。
- 管理アクセスを最小化する。
- MFAと特権分離。
- 削除・保持設定変更を強く制限。
- バックアップ管理操作を別ログへ保存。
- 復旧用資格情報を平時の端末へ常置しない。
- 定期的に破壊シナリオで復元する。

# SaaS・クラウドのバックアップ

「クラウドだからバックアップ不要」とは限らない。

区別する。

- 提供事業者の耐障害性。
- 誤削除からの復元。
- ランサムウェア・悪意ある管理者からの復元。
- テナント侵害からの復元。
- サービス提供者そのものの停止への代替。

同一クラウドアカウント内のスナップショットだけでは、アカウント乗っ取り時の削除耐性が不足する場合がある。

# RTO/RPOだけでは足りない

| 指標 | 意味 |
| --- | --- |
| RPO | どこまでのデータ損失を許容するか |
| RTO | サービスをいつまでに戻すか |
| 復元成功率 | テストで正常復元できた割合 |
| クリーン復旧時間 | 信頼できる新環境へ戻す実測時間 |
| 業務検証時間 | IT復旧後、業務側が受入可能になるまで |
| 最古利用可能世代 | 潜伏期間を遡れるバックアップ世代 |
| 管理分離度 | 本番侵害資格情報でバックアップを破壊できる範囲 |

RTOを「VM起動まで」と定義すると、実際の業務復旧を過小評価する。

# 復旧後の照合

復元後は、失われた期間に発生した正規取引を再投入する場合がある。

必要になり得る作業:

- 受注・決済の再入力。
- 外部システムとの再照合。
- 重複送信・二重請求の確認。
- 在庫・会計残高の照合。
- 通知・予約の再送。
- 監査ログの連結。

「サービスが動いた時刻」と「業務データが正しいと確認できた時刻」を分ける。

# メタデータ候補

```yaml
recoverability:
  backup_available: unknown
  backup_isolation: unknown
  immutable_or_delete_protected: unknown
  restore_tested_before_incident: unknown
  recovery_point: null
  estimated_data_loss_window: unknown
  clean_environment_used: unknown
  configuration_rebuilt: unknown
  credentials_rotated: unknown
  business_reconciliation_completed_at: null
  measured_rto: null
  measured_rpo: null
```

公開資料で確認できない項目は推測しない。

# 経営側が聞くべき質問

- 最後に**本番とは別環境へ**復元したのはいつか。
- AD/IdPが完全に侵害された場合でもバックアップを守れるか。
- バックアップ管理者の資格情報はどこに依存するか。
- 30日潜伏した攻撃でも汚染前へ戻れるか。
- データ以外に、構成・コード・証明書・ネットワーク図を戻せるか。
- 何時間で顧客サービスではなく「重要業務」を再開できるか。
- 外部SaaS停止時のデータ持ち出し・代替経路があるか。

# 関連資料

- [サイバーインシデントのライフサイクルと復旧判定](incident-lifecycle-and-recovery-knowledge-base-2026-10-04.md)
- [失敗モードと防御統制の対応表](control-failure-mode-crosswalk-2026-10-04.md)
- [OT・重要インフラの安全・復旧リスク](ot-critical-infrastructure-safety-and-recovery-2026-10-04.md)
- [インシデント対応指標と経営判断トリガー](incident-response-metrics-and-decision-triggers-2026-10-04.md)
- [知識基盤拡張監査](knowledge-base-expansion-audit-2026-10-04.md)

[^cisa-stopransomware]: CISA, “#StopRansomware Guide” https://www.cisa.gov/stopransomware/ransomware-guide
[^nist-ir]: NIST, “NIST Revises SP 800-61: Incident Response Recommendations and Considerations for Cybersecurity Risk Management” https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations
[^nist-ot-backup]: NIST SP 1339, “OT Backup Quick Start Guide” https://csrc.nist.gov/pubs/sp/1339/final
[^coop-yamaguchi]: 生活協同組合コープやまぐち「コープやまぐちLINEミニアプリへの不正アクセスによる個人情報漏えいのおそれについて（第二報）」https://www.yamaguti-coop.or.jp/line-miniapp-incident-report2/
