---
type: Cybersecurity Incident
title: PR TIMES — 2025年管理者画面侵害、共有アカウント・IP許可例外と発表前情報リスク
resource: https://prtimes.jp/main/html/rd/p/000001531.000000112.html
tags: [japan, saas, media, unauthorized-access, identity, shared-account, allowlist, pre-release-data, 2025]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T09:34:00+09:00 }
incident:
  organization: 株式会社PR TIMES
  sector: media-saas
  jurisdiction: JP
  incident_status: remediation_completed_publicly
  attack_type: unauthorized access, backdoor installation, possible data exfiltration
  earliest_known_activity: "2025-04-08"
  detected_at: "2025-04-25"
  first_disclosed_at: "2025-05-07"
  latest_public_update: "2026-03-16"
  public_record_checked_at: "2026-10-05T09:34:00+09:00"
  intrusion_vector: "管理者画面のIP許可リストに追加経緯不明のIPが残存し、通常利用されない社内共有アカウントが認証に利用された"
  affected_services: "PR TIMES運営側管理者画面。配信サービス自体は継続稼働"
  data_exposure: possible
  availability_impact: "公開サービス停止なし"
  restoration_state: "侵入経路・バックドアを遮断し、旧管理画面を廃止。新管理画面、削除データ保持期限、2段階認証、IP制限、ログイン通知・履歴等を段階実装"
  market_disclosure: "2025年Q1 IR資料で顧客解約・利用停止等を株主向けに説明"
  ai_relation: era_context_only
  response_latency:
    detection_latency: "後日確認された偵察2025-04-08〜09から4月25日検知まで約16〜17日。本格侵入4月24日からは約1日以内"
    containment_latency: "4月25日に初動遮断したが残存プロセスが4月27〜28日に活動。4月30日までに停止"
    public_disclosure_latency: "4月25日検知から5月7日公表まで12日。5月2日に警察・PPC・JIPDECへ速報"
  pre_incident_control_disclosure:
    state: partial
    declared_controls: ["IPアドレス認証", "BASIC認証", "ログインパスワード認証", "WAF", "個人情報の技術的安全管理措置"]
    applicability_to_failure_surface: direct
sources:
  - id: prtimes-initial
    resource: https://prtimes.jp/main/html/rd/p/000001531.000000112.html
    title: PR TIMES、不正アクセスによる情報漏えいの可能性に関するお詫びとご報告
  - id: prtimes-june-pdf
    resource: https://prtimes.jp/common/file/20250626_PRTIMES_UnauthorizedAccess_detail.pdf
    title: PR TIMES 不正アクセスの再発防止策の追加と実施予定について
  - id: prtimes-dec-pdf
    resource: https://prtimes.jp/common/file/20251216_PRTIMES_UnauthorizedAccess_detail.pdf
    title: 新管理者画面への移行完了および削除済みデータの保持期間に関するシステム実装のお知らせ
  - id: prtimes-mar-pdf
    resource: https://prtimes.jp/common/file/20260316_PRTIMES_loginalert.pdf
    title: セキュリティ強化のためのログイン関連機能追加のお知らせ
  - id: prtimes-privacy
    resource: https://prtimes.co.jp/policy/
    title: プライバシーポリシー
---

# 概要

PR TIMESは2025年4月25日、サーバー上の不審ファイルを検知し、前日から管理者画面へ第三者が不正アクセスしていたことを確認した。後日の調査では4月8〜9日に偵察と推察されるアクセスがあり、4月24〜25日に本格侵入、バックドア設置等が行われた。[^prtimes-initial]

個人情報は最大901,603件、発表前プレスリリース情報は1,182社1,682件がリスク範囲とされた。ログ不足等から実際の全取得範囲は確定できず、「アクセス可能だった情報」と「外部流出を確認した情報」を同一視しない。銀行口座番号・カード情報等の決済情報は対象に含まれないと公表された。[^prtimes-initial]

# 事故前の管理構成と侵入経路

運営側管理者画面はIPアドレス認証、BASIC認証、ログインパスワード認証の三段階を必要としていた。ところがコロナ禍のリモートワーク移行時にアクセス許可IPを増やした際、**追加経緯が不明なIPアドレスが残存**し、そのIPが侵入経路に使われた。さらに、認証には普段利用されていない社内管理の共有アカウントが使われた。[^prtimes-initial]

これは、認証機構の種類が複数あることより、許可リストの由来・期限・所有者と共有資格情報の棚卸しが重要である例である。

# 検知から封じ込め

4月25日に不審ファイルを停止し、特定IPを遮断、パスワード変更等を開始した。しかし4月27日深夜〜28日早朝に攻撃者が残したプロセス経由の攻撃が再度確認され、4月30日に当該プロセスを停止した。[^prtimes-initial]

したがって4月25日の初動は速いが、**初回遮断と侵害根絶は別マイルストーン**である。5月2日に警察へ相談し、個人情報保護委員会・JIPDECへ速報、5月7日に被害申告と利用者公表を行った。

# サービスと情報影響

プレスリリース配信機能自体は停止せず正常稼働を継続した一方、管理者画面に置かれた企業・メディア・個人ユーザー情報、インポートリスト、スタッフ情報、発表前プレスリリースがリスク対象となった。[^prtimes-initial]

可用性が維持されたことは、機密性影響が小さいことを意味しない。とりわけ発表前情報は、一般の個人情報とは異なる市場・企業広報上のタイミングリスクを持つ。

# 再発防止の実装追跡

2025年6月26日の追加対策では、管理者画面のIPを社内・VPN接続のみに限定、不正ファイル実行防止、管理者パスワード変更、不要共有アカウント削除に加え、全ユーザー向け2段階認証、企業ユーザー向けIP制限、WAF見直し、新管理者画面への移行等を工程付きで示した。[^prtimes-june-pdf]

12月16日には、侵入経路となった旧社内管理システムを完全停止し、IP制限・Google認証等を備えた新管理者画面へ移行した。削除済みデータについても、従来は復旧可能な形で残していたものを、削除後30日経過でデータベースから完全削除する仕様へ変更した。[^prtimes-dec-pdf]

2026年3月16日には企業管理画面のログイン通知、ログイン中端末表示・強制ログアウト、ログイン履歴強化を実装し、同社は2025年6月に公表した再発防止策がすべて完了したと説明している。[^prtimes-mar-pdf]

# 株主・事業上の予後

会社は2025年5月時点で連結業績への影響は軽微とした。その後の四半期IRでは、本件を株主向けにも説明し、少数ながら契約解約・利用停止が発生したことを開示した。技術的な無停止運用と、顧客信頼上の影響を分けて記録する。

# 防御上の教訓

- IP許可リストは追加理由、所有者、期限、最終利用日を記録し、リモートワーク等の緊急例外を恒久化しない。
- 共有管理アカウントを廃止し、個人識別可能な認証とMFAへ移行する。
- 「遮断した」後も残存プロセス・Webシェル・バックドアのハンティングを独立工程として持つ。
- 削除済みデータの論理削除・復旧保持期間も、侵害時のデータ露出面として設計する。
- SaaSでは公開サービスの稼働率と管理面・機密性侵害を分離する。
- 個別攻撃へのAI/LLM利用を示す公開証拠は確認していない。

[^prtimes-initial]: PR TIMES「不正アクセスによる情報漏えいの可能性に関するお詫びとご報告」2025-05-07.
[^prtimes-june-pdf]: PR TIMES「不正アクセス（5月7日発表）の再発防止策の追加と実施予定について」2025-06-26.
[^prtimes-dec-pdf]: PR TIMES「新管理者画面への移行完了および削除済みデータの保持期間に関するシステム実装のお知らせ」2025-12-16.
[^prtimes-mar-pdf]: PR TIMES「セキュリティ強化のためのログイン関連機能追加のお知らせ」2026-03-16.