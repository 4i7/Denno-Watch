---
type: Cybersecurity Incident
title: DMM Bitcoin — TraderTraitorによる約482億円相当の暗号資産窃取
description: 北朝鮮を背景とするTraderTraitorがウォレット管理関係者を標的とし、GitHub上の悪性コードやセッション悪用を経て約4,502.9 BTCを窃取した事案。事業終了と顧客資産移管まで追跡する。
resource: https://www.npa.go.jp/news/release/20241224.html
tags: [japan, cryptocurrency, supply-chain, tradertraitor, dprk, theft, github, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: 株式会社DMM Bitcoin
  sector: cryptocurrency
  jurisdiction: JP
  incident_status: public_report_closed
  attack_type: targeted social engineering and supply-chain compromise leading to cryptocurrency theft
  earliest_known_activity: "2024-03"
  detected_at: "2024-05-31"
  first_disclosed_at: "2024-05-31"
  latest_public_update: "2025-03-08"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: "TraderTraitor social engineering against a Ginco employee; malicious pre-employment test code and subsequent session/communication abuse"
  affected_services: "cryptocurrency wallet transaction workflow"
  data_exposure: "integrity/asset-theft incident; personal-data exposure is not the principal confirmed harm"
  availability_impact: "withdrawal and service restrictions followed; DMM Bitcoin later ended service"
  restoration_state: "DMM Bitcoin service ended 2025-03-08; customer accounts and assets transferred to SBI VC Trade"
  downstream_impact: "4,502.9 BTC, approximately JPY 48.2 billion at the time, stolen"
  ai_relation: era_context_only
sources:
  - id: npa
    resource: https://www.npa.go.jp/news/release/20241224.html
    title: 北朝鮮を背景とするサイバー攻撃グループTraderTraitorによる暗号資産関連事業者を標的としたサイバー攻撃について
  - id: dmm-end
    resource: https://bitcoin.dmm.com/useful_information/market_report/20230105
    title: サービス終了のお知らせ
  - id: sbivc-transfer
    resource: https://www.sbivc.co.jp/dmm_vct
    title: DMM Bitcoinからの移管 特設サイト
---

# 概要

警察庁、関東管区警察局サイバー特別捜査部、警視庁はFBI・米国防総省DC3と共同で、2024年5月にDMM Bitcoinから約482億円相当の暗号資産が窃取された事件を、北朝鮮を背景とする「TraderTraitor」によるものと特定した。[^npa]

窃取された暗号資産は4,502.9 BTC。本件は暗号化による可用性事故ではなく、**正規の取引・署名ワークフローの完全性が侵害され、資産そのものが移転された事故**として扱う。

# 攻撃経路

警察庁等の共同分析では、2024年3月頃、攻撃者が採用担当者を装い、暗号資産ウォレット管理ソフトを提供するGincoの従業員へLinkedIn経由で接触した。採用試験を装ったGitHub上の悪性Pythonコードを実行させて侵害し、その後セッション情報等を悪用して同社の通信・取引ワークフローへ入り込んだ。5月にはDMM Bitcoinからの正規取引要求を改変し、資産を攻撃者管理先へ送らせたと整理されている。[^npa]

この連鎖では、ソフトウェア脆弱性だけでなく、採用を装った社会工学、開発者がコードを実行する信頼、認証済みセッション、企業間ワークフローが攻撃面になった。

# AIとの関係

悪性Pythonコードや高度な社会工学が用いられたが、公開された捜査資料は本件で生成AI/LLMが使用されたとはしていない。ローカルLLM時代の事例であることだけを根拠にAI攻撃へ分類しない。

# 影響と規制・事業上の予後

盗難後、DMM Bitcoinはサービス制限・顧客対応を続けたが、最終的に事業継続を断念した。2025年3月8日にサービスを終了し、顧客口座および預かり資産はSBI VCトレードへ移管された。[^dmm-end][^sbivc-transfer]

つまり技術的インシデントの予後は「システム復旧」ではなく、**被害事業者のサービス消滅と他社への顧客資産移管**まで到達した。

# 防御上の教訓

- 開発者・運用者向けの採用試験、GitHubリポジトリ、PoC実行は高権限環境から隔離する。
- セッションCookieや既認証状態はパスワード/MFAを迂回する価値ある認証資産として保護する。
- 企業間の取引要求は通信チャネルの認証だけでなく、内容の完全性・二者承認・独立照合を持つ。
- 金融・暗号資産では「データ漏えい件数」より、操作権限と取引完全性を主要被害軸にする。
- 攻撃者帰属は一般報道ではなく、捜査機関の共同評価を根拠にする。

[^npa]: 警察庁「北朝鮮を背景とするサイバー攻撃グループTraderTraitorによる暗号資産関連事業者を標的としたサイバー攻撃について（注意喚起）」2024-12-24.
[^dmm-end]: DMM Bitcoin「サービス終了のお知らせ」2025-03-08時点.
[^sbivc-transfer]: SBI VCトレード「DMM Bitcoinからの移管 特設サイト」.