# インシデントレポート

重大な業務影響、機微・大規模なデータ影響、顧客・委託先・サプライチェーンへの波及、または他組織でも再利用価値の高い防御上の知見が確認できる事例を収録する。収録は深刻度ランキングではなく、日本国内の全セキュリティ公表を網羅した一覧とも主張しない。

## 2023〜2025年 — ローカルLLM時代の補助比較コーパス

2026年中心の事例集を、一般利用者が実用的なオープンウェイトLLMをローカル運用できる時代へ入った2023年7月前後まで遡って補完する。個別攻撃へのAI/LLM利用は公開証拠がある場合だけ認定し、時代背景と因果関係を分離する。

補助コーパスは2023年7件、2024年7件、2025年12件の計26件。全収録68件の再調査は[2026-10-05全収録事例再調査](../methodology/full-corpus-reaudit-2026-10-05.md)、事故前の統制と実侵害の比較は[統制ギャップ比較](../analysis/pre-incident-control-gap-comparison-2023-2025-2026-10-05.md)、一次PDF・IR・規制資料は[既存台帳](../analysis/pre-incident-security-and-ir-pdf-ledger-2023-2025.md)と[追加台帳](../analysis/pre-incident-security-and-ir-evidence-ledger-extension-2026-10-05.md)を参照。

### 2025年

| 組織 | 類型 | 比較上の主題 |
| --- | --- | --- |
| [快活CLUB / FiT24](2025/kaikatsu-club-unauthorized-access.md) | 会員システム不正アクセス | 729万件の漏えい可能性、即時隔離、約1か月のアプリ制限、実流出未確認 |
| [NTTコミュニケーションズ](2025/ntt-communications-unauthorized-access.md) | 不正アクセス | EDR/NDR/UEBA等の事故前公表、初動と全侵害範囲確定の時間差 |
| [保険見直し本舗グループ](2025/hoken-minaoshi-honpo-ransomware.md) | ランサムウェア | ネットワーク機器、即時隔離、保険会社への下流影響、24時間監視・CISO体制 |
| [損保ジャパン](2025/sompo-japan-web-system-breach.md) | Webサブシステム不正アクセス | Zero Trust/SASE/SOC等の事故前公表、大規模保険データ、金融庁報告徴求 |
| [PR TIMES](2025/pr-times-unauthorized-access.md) | 管理者画面侵害 | IP許可例外、共有アカウント、残存プロセス、発表前情報、2026年まで段階是正 |
| [IIJ / IIJセキュアMX](2025/iij-secure-mx-zero-day.md) | 未公知脆弱性悪用 | 8か月超の潜伏、メール・認証情報、通信の秘密、行政指導 |
| [審調社](2025/shinchosa-ransomware.md) | ランサムウェア | ネットワーク機器脆弱性、保護ソフト無効化、医療情報、委託先波及 |
| [ハウステンボス](2025/huis-ten-bosch-breach.md) | 不正アクセス・暗号化 | リモートアクセス機器、約150万人規模の顧客情報、機微な従業員情報、BCP |
| [ローレルバンクマシン / Jijilla](2025/laurel-bank-machine-jijilla-breach.md) | 身代金要求を伴う不正アクセス | AI-OCR、反復認証攻撃、DB削除・窃取可能性、CSIRT/ISO等の平時公表 |
| [アサヒグループHD](2025/asahi-group-ransomware.md) | ランサムウェア | 約10日前の侵入、ゼロトラスト移行前端末、権限管理、物流・会計・内部統制 |
| [ASKUL](2025/askul-ransomware.md) | ランサムウェア | 約4か月半の潜伏、MFA例外、EDR/監視カバレッジ、バックアップ、物流・IR |
| [サンリオエンターテイメント](2025/sanrio-entertainment-ransomware.md) | ランサムウェア | リモートアクセス機器、初期最大約200万件→最終漏えい未確認、約6か月復旧 |

### 2024年

| 組織 | 類型 | 比較上の主題 |
| --- | --- | --- |
| [富士通](2024/fujitsu-stealth-malware.md) | 検知回避型マルウェア | CISO等の事故前ガバナンス、49台、未知・回避型挙動への検知適応 |
| [HOYA](2024/hoya-cyberattack.md) | サイバー攻撃・データ流出 | 複数業務停止、復旧後約1年を経た個人データ流出確定 |
| [DMM Bitcoin](2024/dmm-bitcoin-tradertraitor.md) | 社会工学・取引完全性侵害 | TraderTraitor、約4,502.9 BTC、事業終了と顧客資産移管 |
| [イセトー](2024/iseto-ransomware.md) | ランサムウェア | VPN、便宜保存・削除不徹底、ISO 27001/27017・PrivacyMark停止→再開、経営体制再構築 |
| [ニデックインスツルメンツ](2024/nidec-instruments-ransomware.md) | ランサムウェア | 管理者資格情報、EDR即応、翌日バックアップ復旧、国内外グループ波及 |
| [KADOKAWA / ドワンゴ](2024/kadokawa-ransomware.md) | ランサムウェア | private cloud、遠隔再起動、出版/Web/教育、翌年度財務影響 |
| [カシオ計算機](2024/casio-ransomware.md) | ランサムウェア | 事故前の訓練・監視・ゼロトラスト・ISO 27001と、海外を含む実装不足の比較 |

### 2023年

| 組織 | 類型 | 比較上の主題 |
| --- | --- | --- |
| [エムケイシステム / 社労夢](2023/mk-system-sharomu-ransomware.md) | SaaSランサムウェア | 最大約2,242万人管理、弱い認証・パッチ・ログ監視不備、数千の委託元報告・IR影響 |
| [名古屋港NUTS](2023/nagoya-port-nuts-ransomware.md) | ランサムウェア | 2023-07-18直前比較、保守VPN、港湾物流、約60時間の復旧 |
| [セイコーグループ](2023/seiko-group-ransomware.md) | ランサムウェア | 約6万人、EDR/MFA等の事故後強化 |
| [LINEヤフー](2023/line-yahoo-shared-auth-breach.md) | 委託先・共有認証侵害 | 共通認証・ネットワーク、第三者集中、2026年規制当局向け最終報告 |
| [JAXA](2023/jaxa-vpn-m365-breach.md) | VPN装置侵害→Microsoft 365 | 外部通報、未知マルウェア、資格情報窃取、情報分離、2025年度まで恒久対策 |
| [カシオ ClassPad.net](2023/casio-classpad-development-environment.md) | 開発環境DB侵害 | 開発環境の設定・運用、翌年の別系統ランサムウェアとの長期比較 |
| [NTT西日本グループ](2023/ntt-west-insider-data-exfiltration.md) | 内部不正 | 約10年、特権アクセス、初期調査失敗、2026年までの長期是正 |

## 2026年

| 組織 | 最初の公表 | インシデント | 公開上の状態 |
| --- | --- | --- | --- |
| [第一生命グループ](2026/daiichi-life-hr-system-breach.md) | 2026-10-02 | 共有人事システム侵害／現職・退職者約12万人 | 調査中 |
| [佐川急便](2026/sagawa-package-tracking-breach.md) | 2026-09-30 | 荷物追跡システム侵害／約100日分の配送関連情報に影響可能性 | Webサービス停止／調査中 |
| [ヤマト運輸](2026/yamato-kuroneko-postpay-breach.md) | 2026-09-29 | クロネコ代金後払い侵害／顧客の請求・購買関連情報 | サービス停止／調査中 |
| [セイコーマート](2026/seicomart-app-breach.md) | 2026-09-29 | アプリサーバー侵害／572,022人の閲覧を確認 | 復旧中／調査中 |
| [OZmall / スターツ出版](2026/ozmall-unauthorized-access.md) | 2026-09-27 | 不正アクセス／最大442,779人が閲覧された可能性 | サービス復旧／監視中 |
| [東京メトロ / メトポ](2026/tokyo-metro-metpo-mail-breach.md) | 2026-09-27 | メールサービス侵害／約5.9万件のアドレスが閲覧・取得された可能性 | 調査中 |
| [京王電鉄](2026/keio-electric-ransomware.md) | 2026-09-26 | ランサムウェア／グループシステム障害 | 調査中 |
| [株式会社ファインズ](2026/fines-reservation-system-breach.md) | 2026-09-25 | 予約システムへの不正アクセス／153万レコード | 調査中 |
| [タイムズモビリティ / パーク２４](2026/times-car-web-breach.md) | 2026-09-25 | Webシステム侵害／660万アカウント／本人確認書類 | 調査中 |
| [池上通信機](2026/ikegami-tsushinki-cyberattack-leak.md) | 2026-09-24 | サーバー不正アクセス／ファイル暗号化／攻撃者サイト掲載 | ネットワーク隔離／調査中 |
| [JCOM](2026/jcom-dns-external-traffic-outage.md) | 2026-09-23 | 外部からの大量通信／DNS過負荷／最大約408万加入世帯に影響 | 復旧済み／原因公表済み |
| [Helpfeel / Gyazo](2026/helpfeel-gyazo-breach.md) | 2026-09-16 | 不正アクセス／2,362万ユーザー／大規模な画像メタデータ影響 | サービス復旧／調査中 |
| [LEAN BODY](2026/lean-body-metabase-breach.md) | 2026-09-15 | Metabase脆弱性悪用／約44万アカウント／顧客データ取得を確認 | 封じ込め済み／調査継続 |
| [ロート製薬](2026/rohto-direct-sales-system-breach.md) | 2026-09-11 | 通販システム／顧客情報・通話音声が取得された可能性 | 調査中 |
| [日本トレクス](2026/japan-trex-unauthorized-access-outage.md) | 2026-09-11 | 不正アクセス／調達・部品発注・メール障害 | 復旧済み／公表上の調査完了 |
| [ApplyNow](2026/applynow-recruitment-platform-breach.md) | 2026-09-09 | 採用SaaS侵害／応募者・雇用関連データへ下流影響 | 下流通知／調査中 |
| [コープやまぐち](2026/coop-yamaguchi-line-miniapp-breach.md) | 2026-08-28 | LINEミニアプリDB／全データ削除／主要組合員レコード212,712件と追加対象 | サービス復旧／機密性調査継続 |
| [イエローハット](2026/yellowhat-web-reservation-breach.md) | 2026-08-28 | Web作業予約システム侵害／最大1,801,499人 | 調査中 |
| [VOISING](2026/voising-bi-tool-breach.md) | 2026-08-18 | BIツール既知脆弱性悪用／約17万レコードの流出確認 | 調査完了／監視中 |
| [さくらインターネット](2026/sakura-internet-unauthorized-access.md) | 2026-08-17 | 不正アクセス／マルウェア／顧客管理情報への影響可能性 | 監視中 |
| [両毛システムズ](2026/ryomo-systems-ransomware-supply-chain.md) | 2026-08-15 | VPNアカウント悪用／ランサムウェア／受託データを介した下流影響 | 調査中／下流通知 |
| [REXT Holdings / REXT](2026/rext-ransomware.md) | 2026-08-10 | ランサムウェア／小売業務影響／漏えい可能性のある情報のオンライン掲載確認 | 調査中 |
| [シーイーシー](2026/cec-datacenter-ransomware.md) | 2026-08-06 | ランサムウェア／データセンターサービス停止 | 公表上の調査完了 |
| [株式会社イノベーション](2026/innovation-github-breach.md) | 2026-08-04 | GitHub不正アクセス／リポジトリ情報流出 | 公表上の調査完了 |
| [Ｅストアー / ショップサーブ](2026/estore-shopserve-breach.md) | 2026-08-01 | 不正アクセス／購買データ持ち出し | 調査中 |
| [EPARKリラク＆エステ / PeakManager](2026/epark-peakmanager-breach.md) | 2026-07-31 | 顧客DBの持ち出し・削除／精査後約2,218万レコード | フォレンジック結果公表／監視中 |
| [株式会社ムラウチドットコム](2026/murauchi-dotcom-breach.md) | 2026-07-24 | Webシステム侵害／顧客レコード7,716,811件 | 公表上の調査完了 |
| [扶桑電通](2026/fuso-dentsu-cloud-storage-breach.md) | 2026-07-22 | クラウドストレージ認証情報悪用／26,489件に影響可能性 | 調査完了／監視中 |
| [メディア4u](2026/media4u-sms-platform-breach.md) | 2026-07-14 | SMS基盤侵害／管理レコード95,412件流出／不正SMS280件 | サービス継続／影響範囲精査 |
| [ファイブフォックス / コムサ](2026/five-foxes-ransomware-suspected-breach.md) | 2026-07-14 | 不正アクセス／ランサムウェア疑い／顧客・従業員情報 | 調査中 |
| [ニチレイ](2026/nichirei-cyberattack-logistics-breach.md) | 2026-07-13 | サイバー攻撃／低温物流・冷凍食品出荷障害／個人情報流出確認 | 業務復旧／調査継続 |
| [日本交通](2026/nihon-kotsu-malware-breach.md) | 2026-07-13 | マルウェア／予約・配車障害／ファイル外部流出確認 | 復旧中／データ範囲調査 |
| [アフラック生命保険](2026/aflac-life-unauthorized-access.md) | 2026-06-30 | 不正アクセス／大規模個人情報漏えい | 監視中／サービス復旧 |
| [KDDI](2026/kddi-isp-mail-breach.md) | 2026-06-23 | 共有ISPメール基盤／当時未認知のソフトウェア脆弱性／認証情報 | 公表上の調査完了／規制対応継続 |
| [名鉄協商](2026/meitetsu-kyosho-multi-server-breach.md) | 2026-06-23 | 複数サーバーへの不正アクセス／複数サービスの長期障害／顧客情報影響可能性 | 部分復旧／調査中 |
| [ハンズホールディングス](2026/hands-holdings-ransomware.md) | 2026-06-22 | ランサムウェア／従業員・マイナンバー情報への影響可能性 | 調査中 |
| [フェースグループ](2026/faith-ransomware.md) | 2026-06-22 | VPN経由ランサムウェア／暗号化・削除 | 復旧中 |
| [ドットマネー / ドットギフト](2026/dotmoney-dotgift-breach.md) | 2026-06-11 | 不正アクセス／長期全面停止／段階復旧／ドットギフト終了 | ドットマネー復旧／ドットギフト終了 |
| [日本資産総研](2026/nihon-shisan-souken-ransomware-leak.md) | 2026-05-14 | 認証情報窃取に関連するランサムウェア／暗号化／顧客データの攻撃者サイト掲載確認 | 業務復旧／再発防止継続 |
| [マルタケ](2026/marutake-ransomware-leak.md) | 2026-04-28 | ランサムウェア／長期業務障害／情報持ち出し・攻撃者サイト掲載確認 | 仮環境運用／監視中 |
| [２りんかんイエローハット](2026/yellowhat-2rinkan-breach.md) | 2026-04-23 | API関連不正アクセス／会員3,179,454人 | 公表上の調査完了／サービス再構築待ち |
| [日本テレネット](2026/nippon-telenet-ransomware-bpo-breach.md) | 2026-03-17 | ネットワーク機器からの侵入／ランサムウェア／大規模受託データ | 調査完了／監視中 |

証拠状態と各フィールドの意味は[インシデント記録基準](/methodology/reporting-standard.md)、2026年42件の基準監査は[2026年事例集監査](/methodology/corpus-audit-2026-10-04.md)、全68件の最新再調査は[2026-10-05全収録事例再調査](/methodology/full-corpus-reaudit-2026-10-05.md)を参照。

## 海外比較ケース

海外事例は国内68件の集計には含めず、長期予後、第三者・認証・集中リスク、訴訟・保険・規制等を補う比較資料として分離する。詳細は[海外比較インシデント](international/index.md)を参照。
