---
type: Corpus Audit
title: Denno-Watch 2026-10-08 即時更新・既存状態差分の監査
resource: https://github.com/4i7/Denno-Watch
tags: [japan, status-delta, audit, 2026]
status: draft
generated: { by: openai/gpt-6, at: 2026-10-08T14:54:00+09:00 }
---

# 実施結果

前回2026年10月7日時点の国内77件（2026年51件）から、今回**新規6件**を追加。国内**83件**（2026年57件、2023年7件、2024年7件、2025年12件）。全国で発生した事例を網羅する数値ではない。

- [IDCフロンティア — IDCFクラウドのランサムウェア／495企業・自治体に障害](../../incidents/2026/idc-frontier-cloud-ransomware.md): 個人情報への影響 unknown。
- [戸田建設 — 支払管理システム等から取引先・従業員情報流出](../../incidents/2026/toda-construction-business-system-breach.md): 個人情報への影響 confirmed。
- [関西国際大学 — eポートフォリオ外部取得／個人識別情報は調査中](../../incidents/2026/kansai-university-international-eportfolio-breach.md): 個人情報への影響 possible。
- [日本原子力研究開発機構 — JRR-3研究支援サイト／175人の身分証・健診情報流出](../../incidents/2026/jaea-jrr3-research-portal-exfiltration.md): 個人情報への影響 confirmed。
- [日本経済新聞社 M365 — Microsoft 365アカウント侵害／偽装メール約9000通と日経BPへの連鎖](../../incidents/2026/nikkei-m365-phishing-mail-breach.md): 個人情報への影響 possible。
- [日本経済新聞社 Workspace — Google Workspace不正ログイン／1646人に漏えい疑い](../../incidents/2026/nikkei-google-workspace-breach.md): 個人情報への影響 possible。

# 既存記録の確度・ステータスの変動

**スカラコミュニケーションズ / i-ask：2026年10月7日に新たな下流公表**。損保ジャパンのSMILING ROADへの影響として**約6万件（重複を含む問い合わせ単位）**の漏えい可能性が公式PDFに追加された。情報にはドライバーID・運転アラート等も含まれる。最大5社・713,126問い合わせという供給者側母数や、`data_exposure: possible`は維持する。新たな6万を**足さない**。通知・委託先管理の見直しは進行中であり、完了と扱わない。一次資料: https://www.sompo-japan.co.jp/-/media/SJNK/files/news/2026/20261007_1.pdf?la=ja-JP 、https://scala-com.jp/news/2026/10-1/。

## 10月8日に再確認した既存の直近レコード

| 事例 | 確認資料 | 結果 |
| --- | --- | --- |
| 焼肉きんぐ | https://www.monogatari.co.jp/news/261005_news/ | 10,788,963件 confirmed、その他の大きな訂正は確認元記事にはなし |
| GMO infoQ | https://gmo-research.ai/pressroom/notice/notice-20261005 | 948,498件・ポイント不正利用611件／2,869,500円の既報維持 |
| MrMax | https://www.mrmax.co.jp/info/incident_20261006/ | confirmed 最大1,735,154人の上限維持 |
| 大起水産 | https://www.daiki-suisan.co.jp/files/optionallink/00000164_file.pdf | possible 174,933人を維持 |
| 楽天ドライブ | https://support.rakuten-drive.com/hc/ja/articles/62934949147929 | 保存ファイル閲覧・取得の既報確認状態を維持 |
| デジタル庁 GSS | https://www.digital.go.jp/news/2026-0911-01 | 約246,000件は possible のまま |
| スカラi-ask | https://scala-com.jp/news/2026/10-1/ と https://www.sompo-japan.co.jp/-/media/SJNK/files/news/2026/20261007_1.pdf?la=ja-JP | 下流損保ジャパン追加、供給者漏えいpossibleのまま |
| 大阪公立大学 | https://e.omu.ac.jp/ と https://e.omu.ac.jp/announce/?p=6 | 10月8日まで全授業休講。10月9日以降の復旧は未確定 |

この確認は**最新の一次告知と直近の既存記録**を対象とした差分調査であり、従来の国内77件すべての継続調査を完了した意味ではない。未走査の資料には「不変」と判定せず**未検証**とする。最新公表日と確認日時は別フィールド。

# 公的な状況認識の新規変動

JPCERT/CCが10月8日、既知脆弱性、管理API不正操作、Metabase CVE-2026-72898という異なる技術類型の報告を注意喚起。個人情報保護委員会が10月7日、大規模漏えいに関する注意喚起を発表。事案を共通の攻撃者やキャンペーンに結び付ける資料ではない。一次資料: https://www.jpcert.or.jp/at/2026/at260030.html 、https://www.ppc.go.jp/news/careful_information/261007_alert/。

# 今回未収録、継続調査候補

HISタイ子会社（2025年12月攻撃、2026年10月公表、旅券最大627人）、日経BPの二次被害を別レコード化する必要性、ニッポンレンタカーの別手法55会員、らしんばん、ABAHOUSE、エネルギー経済研究所、日本化粧品工業会、スタディサプリ、i-ask他顧客、2023〜2025年の全レコードの新規続報、財務・行政・復旧の長期予後。

# 境界

`confirmed` / `possible` / `unknown` を区別する。人数・問い合わせ・ファイル・メール送信を合算しない。新たな警告の攻撃類型は、固有の証拠がない個別事例へは帰属しない。
