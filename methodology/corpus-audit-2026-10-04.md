---
type: Corpus Audit
title: 2026 major-incident corpus audit — 2026-10-04
description: Primary-source consistency review of the pre-existing Denno Watch corpus plus expansion with additional material Japanese incidents and cross-incident defensive findings.
resource: https://github.com/4i7/Denno-Watch
status: draft
tags: [audit, japan, cybersecurity, incidents, okf, 2026]
generated: { by: openai/gpt-5.6-sol, at: 2026-10-04T05:25:00+09:00 }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format (OKF) v0.2 specification
    author: organization:GoogleCloudPlatform
---

# Scope

This audit re-checked the 25 incident records already present in `incidents/2026/` before this change and expanded the corpus with 12 additional incidents selected for at least one of the following: material operational disruption, sensitive or large-scale data exposure, downstream/supply-chain blast radius, unusually long-lived data exposure, or unusually reusable defensive findings.

The audit is limited to publicly observable information. It does not claim that unpublished facts do not exist.

# Method

Each incident was reviewed using the reporting standard with the following checks:

1. Locate the latest affected-organization or responsible-provider disclosure and compare it with the current record.
2. Check regulator/law-enforcement or directly affected customer disclosures where they materially refine scope.
3. Separate `earliest_known_activity`, detection, first disclosure, latest public incident update, and the date this public record was checked.
4. Preserve evidence progression rather than silently rewriting history: possible → confirmed; estimate → corrected count; no evidence initially → later external-leak confirmation.
5. Preserve source units. A record/account/item count is not converted into people without source support, and potentially overlapping populations are not summed into a unique-person total.
6. Separate containment, service restoration, security-state restoration, data-impact determination, investigation closure, and long-term remediation.
7. Do not infer a CVE, attacker, ransomware family, exploit path, DDoS intent, or credential-theft mechanism unless a public source establishes it.
8. Treat affected-customer/partner notices as downstream evidence, not as proof that the downstream organization itself was directly breached.

# OKF conformance note

Denno Watch continues to target OKF v0.2. The canonical specification is currently the `GoogleCloudPlatform/open-knowledge-format` repository. The current specification describes OKF as Markdown concepts with YAML frontmatter and allows producer-defined fields in addition to the standardized provenance/trust/lifecycle families.[^okf-spec]

The current v0.2 text also requires timestamp-valued keys to use ISO 8601 datetimes with an explicit UTC offset. New records in this audit therefore use explicit offsets for generated/check/staleness timestamps. Because the v0.2 specification has evolved while retaining the same version label, consumers that require byte-for-byte conformance should pin an upstream revision in addition to recording `okf_version: "0.2"` at bundle root.

# Existing 25-record consistency audit

No material contradiction was located between the existing record and the reviewed public record for the following 25 concepts. Where later disclosures changed certainty or counts, the existing record already preserved the progression rather than erasing the earlier state.

| Existing record | Audit result | Material point preserved |
| --- | --- | --- |
| セイコーマート | consistent | initial ~570k possibility → 572,022 confirmed viewed members; payment/card data separation maintained |
| OZmall / スターツ出版 | consistent | initial max 447,610 → corrected max 442,779; former members included |
| 東京メトロ / メトポ | consistent | about 59k delivery-suspended email addresses; affected server data separation preserved |
| 京王電鉄 | consistent | ransomware affects group/business systems; railway operation excluded from impact; no newer disclosure located in the fresh check |
| ファインズ | consistent with count-semantics caution | 1,536,322 records retained as source unit; extraction-vs-affected-population semantics not overstated |
| タイムズモビリティ / パーク２４ | consistent | ~6.6M account data acquisition and later ~1.6M identity-document impact kept separate |
| JCOM | consistent | external high-volume traffic and DNS overload recorded without inferring malicious DDoS intent |
| Helpfeel / Gyazo | consistent | 23.62M-user data impact and staged visibility/service recovery through 2026-09-29 maintained |
| LEAN BODY | consistent | vulnerable Metabase environment and confirmed acquisition recorded without inventing a CVE |
| イエローハット Web作業予約 | consistent | up to 1,801,499 potential scope remains distinct from the separate 2りんかん incident |
| さくらインターネット | consistent | unauthorized access/malware and potential customer-management exposure; external exfiltration not promoted to confirmed |
| REXT | consistent | initial low-leak-risk assessment → later online publication observation preserved |
| シーイーシー | consistent | data-center ransomware and service outage retained as publicly closed report |
| イノベーション | consistent | 62,691 → 62,689 correction preserved; repository leak distinguished from production-DB compromise |
| Ｅストアー / ショップサーブ | consistent | purchase-data exfiltration remains under investigation where final public closure is absent |
| ムラウチドットコム | consistent | 7,716,811-customer-record scope and completed public investigation retained |
| ファイブフォックス / コムサ | consistent | first-report ransomware suspicion not upgraded beyond later public evidence |
| ニチレイ | consistent | July logistics availability recovery separated from September personal-data leak confirmation |
| アフラック生命 | consistent | large-scale personal-data incident and later service-recovery state retained |
| KDDI | consistent | 12,231,954 email-address population and 7,616,173 password subset; shared-ISP downstream scope; regulatory follow-up retained |
| 名鉄協商 | consistent | multiple-server attack, long recovery and widening notification retained while actual external leak remains unconfirmed |
| ハンズホールディングス | consistent | ransomware and employee/My Number exposure risk retained without unsupported attacker attribution |
| フェースグループ | consistent | VPN-associated ransomware/encryption/deletion evidence retained at published granularity |
| 日本資産総研 | consistent | credential-related intrusion → ransomware → possible exfiltration → confirmed attacker-site publication progression retained |
| 2りんかんイエローハット | consistent | API-related incident and 3,179,454-member confirmed exposure kept separate from later Yellow Hat reservation incident |

## Existing-record maintenance debt

Some earlier concepts were created before `public_record_checked_at` became a canonical Denno Watch field. This audit provides a corpus-level dated consistency check, but it does not falsely stamp every old concept as freshly re-generated. Future material edits to those concepts should add/update `public_record_checked_at` while leaving `latest_public_update` unchanged when no new incident disclosure exists.

# Newly added material incidents

| New concept | Why it is material |
| --- | --- |
| 第一生命グループ | ~120,000 current/former employee population; former office employees back to 1967; shared HR system |
| 佐川急便 | package sender/recipient data including roughly 100 days of logistics records; Web-service shutdown while physical delivery continued |
| ヤマト運輸 / クロネコ代金後払い | purchase/credit/billing context with strong social-engineering value; service remains suspended |
| 池上通信機 | unauthorized server access + file encryption + attacker-site publication observation; internal network isolation |
| ロート製薬 | direct-sales customer data and customer-support call audio potentially acquired |
| 日本トレクス | business-facing systems stopped, alternative channels used, later no external leak observed and full restart |
| ApplyNow | recruitment SaaS downstream impact across organizations; high-sensitivity employment/identity data possible depending on service |
| VOISING | ~170,000 confirmed records; BI known vulnerability; compromised environment discarded instead of restored |
| 両毛システムズ | VPN-account abuse → ransomware; multiple entrusted organizations affected by retained data copies |
| EPARKリラク＆エステ / PeakManager | initial ~33M records → confirmed external transfer of ~22.18M records; sensitive health data and free-text schema escape |
| 日本交通 | malware-driven dispatch/reservation disruption followed by confirmed external leakage of company-held files |
| 日本テレネット | ransomware with entrusted BPO/CSS data populations; clean-network rebuild, full endpoint reimaging and SOC/MFA/EDR hardening |

# Cross-incident findings

## 1. Availability recovery and confidentiality closure run on different clocks

Nichirei, REXT, Nihon Kotsu, Meitetsu Kyosho and other cases show the same pattern: services can be restored while the confidentiality investigation remains open, and later external evidence can materially change the incident state. Denno Watch therefore treats “service restored” as one recovery phase, never as automatic incident closure.

## 2. Analytics and BI systems are production-data boundaries

LEAN BODY (Metabase), ApplyNow (data analytics tool) and VOISING (BI tool) independently show that internal analytics environments can hold enough production-derived personal data to create a major breach. Patch urgency, internet exposure, least privilege, data minimization, audit logging and credential isolation must apply to analytics tooling at the same rigor as customer-facing production services.

## 3. Historical and dormant data amplify blast radius

The corpus now contains multiple forms of stale-but-sensitive data:

- Tokyo Metro: email addresses already suspended from delivery.
- ApplyNow downstream customers: historical applicant data after the original recruitment period and, in some cases, after service use had ended.
- Dai-ichi Life: former office employees dating back to 1967.
- Nippon Telenet / Ryomo Systems: entrusted copies retained in service-provider environments.
- PeakManager: duplicate/historical customer ledgers maintained independently by stores.

Retention and deletion verification should therefore be modeled as security controls, not merely privacy administration.

## 4. Free-text fields defeat schema-based sensitivity assumptions

PeakManager is a strong example: the product had no designed card-data field, yet five note entries contained values that could be card information, and the same notes could include health-status information. A data inventory that classifies only formal columns will miss sensitive values embedded in free text, attachments, recordings and logs.

## 5. Provider compromises create a second data topology

ApplyNow, KDDI, Ryomo Systems and Nippon Telenet show that the organization holding the data at incident time may not be the organization the data subjects interacted with. Incident modeling needs both:

- the compromised provider/system boundary; and
- the downstream customer/entrusted-data ownership boundary.

This is why downstream counts must not be automatically summed into a provider-level unique-person total.

## 6. Data separation and non-retention produce observable damage reduction

Several incidents show real scope reduction because some data simply was not in the affected system:

- Tokyo Metro's affected server held delivery-suspended email addresses rather than the full membership dataset.
- ApplyNow downstream notices indicate videos/images/PDFs were held separately from the attacked analytics scope.
- VOISING did not retain card credentials or login passwords in the affected data.
- Yamato's current postpay scope excludes card data and passwords.

“Do not collect / do not co-locate” is often stronger than attempting to protect every field after aggregation.

## 7. Corrected counts must remain historical facts

The corpus includes several corrections or refinements that should never be silently overwritten:

- OZmall: 447,610 maximum → 442,779 maximum.
- Innovation: 62,691 → 62,689.
- Seicomart: initial roughly 570,000 possible → 572,022 confirmed viewed.
- PeakManager: initial roughly 33 million records at risk → about 22.18 million records after deduplication/analysis, with external transfer confirmed.

The earlier number describes the state of knowledge at that point; the later number describes a different evidence state.

## 8. “No leak observed” is not “no sensitive data was exposed to risk”

Nippon Telenet's forensics found no external-transfer trace, yet the compromised environment contained very large entrusted-data populations. Japan Trex also demonstrates that an availability incident can conclude with no external leakage observed. Denno Watch records both the data-at-risk population and the final evidence state rather than collapsing them into a binary breach/no-breach label.

## 9. Clean rebuild can be a security-state restoration milestone

Nippon Telenet created an independent clean network and reimaged all business PCs. VOISING discarded the compromised environment and invalidated/rotated credentials rather than returning the environment to service. These are stronger, observable security-state restoration milestones than “system restarted”.

## 10. Business continuity should be recorded independently from cyber root cause

Japan Trex used FAX/alternative procedures, and Nihon Kotsu retained GO app/taxi-stand/street-hail options while specific reservation/dispatch channels were impaired. The ability to deliver core business through an alternate channel is a separate defensive property from whether the intrusion itself has been eradicated.

# Recommended incident metadata extensions

The following producer-defined fields are now used in newly added concepts because they repeatedly proved necessary to describe public outcomes without overloading existing fields:

- `downstream_impact`
- `regulatory_response`
- `notification_state`
- `business_continuity`
- `data_sensitivity`

These are additive OKF producer fields. They do not change the meaning of the existing canonical Denno Watch fields.

# Follow-up rule

For active incidents, a future recheck must distinguish:

- a new incident disclosure: update `latest_public_update` and `public_record_checked_at`;
- no new disclosure found: update only `public_record_checked_at` (and `stale_after` if needed);
- a corrected count or certainty change: preserve the prior state in the timeline and update the canonical current state.

[^okf-spec]: GoogleCloudPlatform, Open Knowledge Format v0.2 specification, canonical repository checked 2026-10-04.
