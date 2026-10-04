---
type: Cybersecurity Incident
title: HOYA — 2024年サイバー攻撃・システム障害と個人データ流出
description: 2024年3月30日に発生したサイバー攻撃で複数事業のシステムが停止し、後日医療・採用・取引先・従業員等の個人データ外部流出を確認した事案。
resource: https://www.hoya.com/news/%E3%82%B5%E3%82%A4%E3%83%90%E3%83%BC%E6%94%BB%E6%92%83%E3%81%AB%E3%82%88%E3%82%8B%E5%80%8B%E4%BA%BA%E6%83%85%E5%A0%B1%E3%81%AE%E5%A4%96%E9%83%A8%E6%B5%81%E5%87%BA%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/
tags: [japan, manufacturing, healthcare, cyberattack, outage, personal-data, 2024]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-05T07:08:00+09:00 }
incident:
  organization: HOYA株式会社
  sector: manufacturing-healthcare
  jurisdiction: JP
  incident_status: monitoring
  attack_type: malicious cyberattack causing system outage and data exfiltration
  earliest_known_activity: "2024-03-30"
  detected_at: "2024-03-30"
  first_disclosed_at: "2024-04-01"
  latest_public_update: "2025-04-14"
  public_record_checked_at: "2026-10-05T07:08:00+09:00"
  intrusion_vector: not_publicly_disclosed
  affected_services: "multiple group systems; confirmed leaked data from PENTAX Life Care and Medical business systems"
  data_exposure: confirmed
  availability_impact: "manufacturing/order and other group systems were temporarily disrupted"
  restoration_state: "systems restored and ordinary operations resumed; 2025 notice confirmed external personal-data leakage"
  regulatory_response: "reported to the Personal Information Protection Commission"
  ai_relation: era_context_only
sources:
  - id: hoya-leak
    resource: https://www.hoya.com/news/%E3%82%B5%E3%82%A4%E3%83%90%E3%83%BC%E6%94%BB%E6%92%83%E3%81%AB%E3%82%88%E3%82%8B%E5%80%8B%E4%BA%BA%E6%83%85%E5%A0%B1%E3%81%AE%E5%A4%96%E9%83%A8%E6%B5%81%E5%87%BA%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/
    title: サイバー攻撃による個人情報の外部流出について
---

# 概要

2024年3月30日、HOYAのシステムが第三者からサイバー攻撃を受け、グループの複数業務にシステム障害が生じた。3月31日以降ネットワーク遮断・安全確認・復旧を進め、4月2日には漏えいしたとみられるファイルへ個人情報が含まれる可能性を把握した。2025年4月14日の調査結果で、PENTAXライフケア・メディカル事業の一部システムから個人データの外部流出を確認した。[^hoya-leak]

# 確認された個人データ

2025年確報で明示された主な対象は、内視鏡検査受診者約1,000人、採用関連情報約500人、取引先関係者約2,000人、従業員・退職者・家族約3,000人で、銀行口座・身分証明書・給与等を含む場合がある。カード情報の流出は確認されていない。[^hoya-leak]

この確報は、事故当初の「システム障害」から、1年以上後に外部流出が確認されたことを示す。初報時点の被害認識を固定せず、長期フォレンジックの結果を追う必要がある。

# 即応性

攻撃翌日の3月31日以後にシステムをネットワークから遮断し、分析、安全確保、復旧を実施した。4月2日には個人情報を含むファイル漏えいの可能性を認識しており、可用性復旧と機密性調査が並行した。[^hoya-leak]

# 事故前公表との比較

HOYAは事故以前の統合報告等でも個人情報保護や従業員向けサイバーセキュリティ教育を説明していた。一方、本件の公開原因は具体的な初期侵入経路まで明らかにされていないため、事故前に公表していた教育・プライバシー管理が今回の侵入面へ直接適用される統制だったとは断定しない。

事故後はセキュリティ対策ソフト、パスワード、監視、個人情報管理を強化した。ここでは「対策公表済みだったのに侵害された」という単純評価ではなく、**事故前に公表された統制の範囲より、実際のシステム可用性・侵入耐性・復旧設計の方が広い問題だった可能性**を残す。

# 予後

同社の後年の経営資料では、複数事業の製造・受注システム等が一時停止したものの復旧し、通常操業へ戻ったこと、サイバーセキュリティの包括的見直しを進めたことが説明されている。技術的なサービス復旧と、個人データ影響の確定に約1年の時間差があった点を保持する。

# 防御上の教訓

- サービス復旧を「事故終了」とみなさず、漏えい調査の長期尾部を追う。
- 医療・採用・給与・口座等は人数以上に長期悪用可能性を評価する。
- 事故前統制は実際の失敗面へどの程度適用されるかを分離して比較する。
- AI/LLM利用の公開証拠はない。

[^hoya-leak]: HOYA「サイバー攻撃による個人情報の外部流出について」2025-04-14.