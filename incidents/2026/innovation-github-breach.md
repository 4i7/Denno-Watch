---
type: Cybersecurity Incident
title: 株式会社イノベーション — GitHub認証情報悪用とリポジトリ内個人情報流出
description: GitHubアクセストークン管理不備とリポジトリへの個人情報保存が組み合わさり、62,689名分の情報漏えいにつながった事案。
resource: https://www.innovation.co.jp/2026/08/github%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E8%A9%B3%E7%B4%B0%E8%AA%BF%E6%9F%BB%E3%81%AE%E5%AE%8C%E4%BA%86%E3%81%8A%E3%82%88/
tags: [japan, github, source-code, credentials, personal-data, secret-management, 2026]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
incident:
  organization: 株式会社イノベーション
  sector: information-services
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: "unauthorized GitHub access using stolen credential"
  earliest_known_activity: unknown
  detected_at: not_publicly_disclosed
  first_disclosed_at: "2026-08-04"
  latest_public_update: "2026-08-10"
  intrusion_vector: "GitHub credential stored directly in an internal development-system configuration file was stolen and abused; how it was stolen is not publicly detailed"
  affected_services: "GitHub repositories used for software development/system management"
  data_exposure: confirmed
  availability_impact: not_observed
  restoration_state: "compromised credential revoked; repository and governance remediation completed/under further automation"
  secondary_abuse: not_observed
sources:
  - id: innovation-final
    resource: https://www.innovation.co.jp/2026/08/github%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E8%A9%B3%E7%B4%B0%E8%AA%BF%E6%9F%BB%E3%81%AE%E5%AE%8C%E4%BA%86%E3%81%8A%E3%82%88/
    title: GitHubへの不正アクセスに関する詳細調査の完了およびセキュリティ対策強化のお知らせ（確定報）
  - id: innovation-correction
    resource: https://www.innovation.co.jp/2026/08/github%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B%EF%BC%88%E7%A2%BA%E5%AE%9A%E5%A0%B1%EF%BC%89/
    title: GitHubへの不正アクセスに関するお知らせ（確定報）の一部訂正について
  - id: innovation-archive
    resource: https://www.innovation.co.jp/2026/08/
    title: 株式会社イノベーション 2026年8月ニュース
---

# Executive summary

株式会社イノベーションは2026年8月4日、ソフトウェア開発・システム管理に利用するGitHubへの不正アクセスを公表した。8月7日の確定報で、社内開発システムのプログラム設定ファイルにGitHubへアクセスする認証情報が直接記載されており、第三者がその認証情報を取得・悪用したことを直接原因として公表した。さらに、分析・開発作業の過程で個人情報がGitHubリポジトリ内に保存されていたことが、情報流出へつながった第二の要因とされた。[^innovation-final]

流出対象は8月7日時点で62,691名分とされたが、8月10日に集計上の誤りとして **62,689名分** に訂正された。内訳は氏名62,631件、メールアドレス62,689件、電話番号506件。調査対象範囲自体の誤りではなく、社内集計・共有過程で件数記載を誤ったと説明している。[^innovation-correction]

本番データベースへの不正アクセス、本番環境からの情報漏えい、不正利用等の二次被害は確認されず、漏えいはGitHubリポジトリ内の情報に限定されたと最終報で確認された。[^innovation-final]

# Observable timeline

| Date | Observable event |
| --- | --- |
| 2026-08-04 | GitHubへの不正アクセスを第一報として公表。[^innovation-archive] |
| 2026-08-07 | 詳細調査完了。認証情報の管理不備と、個人情報のリポジトリ保存という二つの原因、対象件数、再発防止策を確定報として公表。[^innovation-final] |
| 2026-08-10 | 対象人数・メールアドレス件数を62,691から62,689へ訂正。対象範囲の調査ではなく集計・記載過程の誤りと説明。[^innovation-correction] |

# Impact

## Confidentiality

訂正後の確定値は62,689名分。公開内訳は次のとおり。[^innovation-correction]

| Data | Corrected count |
| --- | ---: |
| 氏名 | 62,631件 |
| メールアドレス | 62,689件 |
| 電話番号 | 506件 |

これは本番DBから抜き取られたデータではなく、分析・開発作業の過程でGitHubリポジトリに保存されていた個人情報が不正アクセスの対象となったもの。[^innovation-final]

## Production systems

本番データベースへの不正アクセス、本番環境からの情報漏えいは確認されていない。したがってソースコード管理面の侵害を、根拠なく本番環境侵害へ拡張しない。[^innovation-final]

## Availability and secondary abuse

サービス停止などの可用性影響は公表されていない。流出した可能性のある個人情報の不正利用等による二次被害も確定報時点では確認されていない。[^innovation-final]

# Technical findings

公表された原因は二つに分離されている。[^innovation-final]

1. **認証情報管理の不備** — 社内開発システムの一部で、GitHubへアクセスする認証情報がプログラム設定ファイルへ直接記載されていた。第三者がこれを不正取得し、GitHubへの不正アクセスに悪用した。
2. **データ配置の不備** — 本来は厳重管理すべき個人情報の一部が、分析・開発作業の過程でGitHubリポジトリ内にも保存されていた。

認証情報が設定ファイルから「どのように」第三者へ渡ったのか、設定ファイルを保持していた内部開発システムの侵害経路は公開されていない。したがって、GitHub自体の脆弱性や認証突破が原因だったとは扱わない。

# Response and recovery

## Credential / GitHub controls

- 影響したアクセストークンを無効化・停止。[^innovation-final]
- トークン権限と発行ワークフローを見直し、組織全体で統制された仕組みへ切り替え。[^innovation-final]
- レビュールールを見直し・強化。[^innovation-final]
- GitHubリポジトリへのアクセス監視を強化。[^innovation-final]

## Personal-data controls

- 個人情報を含むデータをリポジトリへ保存しない運用ルールへ変更。[^innovation-final]
- 既存リポジトリの点検・是正を完了。[^innovation-final]
- 個人情報がリポジトリへアップロードされた場合に検知する仕組みを導入。[^innovation-final]
- 混入を未然に遮断する自動チェックの導入を進行。[^innovation-final]

# Prognosis / current state

8月7日に詳細調査完了を公表し、8月10日に件数訂正を行っている。主要原因・影響範囲・対策が公開されているため `public_report_closed` とする。ただし自動遮断など一部の強化策は確定報時点で導入途中だった。[^innovation-final]

# Defensive lessons

- **Secret scanningだけでは十分でない。** 本事案は「秘密情報がコード/設定へ入る問題」と「個人情報がリポジトリへ入る問題」が独立して存在し、両方が重なって被害になった。制御も資格情報とデータ分類の二系統が必要。[^innovation-final]
- **設定ファイル内の長寿命資格情報を前提にしない。** 権限・発行・失効を組織統制し、漏えい時に即座に無効化できる設計が必要。[^innovation-final]
- **開発データの由来と持込規則を監査する。** 分析用データがリポジトリへ残ると、ソースコード管理の侵害が個人情報漏えいへ変わる。[^innovation-final]
- **訂正履歴を消さない。** 62,691から62,689への変更は調査範囲の変更ではなく集計ミスだったため、Denno Watchでは最新値を採用しつつ訂正経緯も保持する。[^innovation-correction]

# Unknowns / withheld details

- GitHub認証情報が第三者に取得された具体的経路
- 悪用された認証情報の権限範囲・有効期間
- 不正アクセス開始時刻と継続期間
- 影響リポジトリ数・ソースコードへのアクセス範囲
- 攻撃主体

[^innovation-final]: 株式会社イノベーション「GitHubへの不正アクセスに関する詳細調査の完了およびセキュリティ対策強化のお知らせ（確定報）」2026-08-07.
[^innovation-correction]: 株式会社イノベーション「GitHubへの不正アクセスに関するお知らせ（確定報）の一部訂正について」2026-08-10.
[^innovation-archive]: 株式会社イノベーション「2026年8月 News」.
