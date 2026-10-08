---
type: Cybersecurity Incident
title: "ABAHOUSE INTERNATIONAL — 受注DB侵害と注文に一致する不審な返金メール"
resource: https://abahouse.co.jp/news/2005/
tags: [japan, 2026, retail, ecommerce, identity, phishing]
status: draft
stale_after: 2026-10-12T00:00:00+09:00
generated: { by: openai/gpt-6, at: 2026-10-08T06:48:28.488+00:00 }
incident:
  organization: "株式会社アバハウスインターナショナル"
  sector: "retail-ecommerce"
  jurisdiction: "JP"
  incident_status: "investigating"
  attack_type: "unauthorized-login-and-malicious-program"
  first_disclosed_at: "2026-10-03"
  latest_public_update: "2026-10-03"
  public_record_checked_at: "2026-10-08T06:48:28.488+00:00"
  data_exposure: "possible"
  earliest_known_activity: "2026-09-27 night to 09-28 (estimated)"
  detected_at: "2026-09-28 customer reports"
  intrusion_vector: "不正ログイン・不備悪用・不正プログラム、初期認証の取得原因不明"
  affected_services: "EC会員・受注DB"
  secondary_abuse: "実際の注文と一致する不審な返金案内メールの受信報告。侵入との因果関係未確定"
  restoration_state: "把握した侵入経路遮断済、調査中"
  notification_state: "2026-10-02に対象可能性顧客へメール、退会者も含む"
  regulatory_response: "PPC報告済"
  data_sensitivity: "氏名・住所・電話・メール・生年月日・性別・会員ID・購買履歴。カード番号等は決済代行で保持"
sources:
  - id: abahouse
    resource: https://abahouse.co.jp/news/2005/
    title: "不正アクセスによる個人情報漏えいに関するお詫びとご報告"
    author: "organization:アバハウスインターナショナル"
---

# ABAHOUSE INTERNATIONAL — 受注DB侵害と注文に一致する不審な返金メール

## 経緯と確認された事項

9月27日夜〜28日ごろ海外の第三者による侵入があったと推定。28日に実注文に一致する不審な返金案内メールが複数の顧客に届いたため調査を開始し、不正ログイン、不正プログラムの設置・実行と会員・受注DBへのアクセス痕跡を確認した。[^abahouse]

## 外部取得と二次被害の境界

氏名、住所、メール、電話、生年月日、性別、会員ID、商品名・金額・配送先等の注文情報に**漏えい可能性**。被害人数と実取得量は未確定。カード情報は決済代行会社管理で会社DBには保存していない。実注文情報と一致する返金を装った不審メールは観測済みだが、メールの送信主体と侵害行為の同一性は未確定。[^abahouse]

## 対応と予後

侵入経路を遮断し、10月2日対象可能性顧客へメール通知。退会1か月後に会員情報を削除するが、法令・会計対応の受注履歴は退会後も一定期間保管するため退会者へも通知した。PPCへ報告。再発防止策、実漏えい人数、返金メールによる金銭的被害の有無は追跡中。[^abahouse]

[^abahouse]: アバハウスインターナショナル「不正アクセスによる個人情報漏えいに関するお詫びとご報告」. https://abahouse.co.jp/news/2005/
