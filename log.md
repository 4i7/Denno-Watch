# Update log

## 2026-10-04

- Completed a second public-source sweep and expanded the 2026 corpus from 37 to **42 incident reports**.
- Added コープやまぐち: destructive unauthorized access deleted the LINE mini-app database; same-day backup restoration recovered service while confidentiality impact remained unresolved; the refined scope includes 69,586 and 143,126 main member-record populations plus smaller affected subsets.
- Added メディア4u: SMS-platform control-plane compromise with 95,412 confirmed leaked customer-management records, 22,928 records potentially containing personal information, and 280 unauthorized SMS messages sent through one customer account; OEM/reseller downstream handling is recorded separately.
- Added 扶桑電通: cloud-storage authentication-credential misuse with 26,489 potentially exposed customer/contact records; the final public investigation could not establish how credentials were obtained and remediation includes MFA for external users, password-policy strengthening, shared-folder governance and periodic account review.
- Added ドットマネー / ドットギフト: unauthorized access caused a prolonged whole-service stop; DotMoney later resumed in stages with mandatory phone verification for exchanges while DotGift was permanently terminated, establishing `service retirement` as a distinct incident outcome.
- Added マルタケ: pharmaceutical-wholesale ransomware with confirmed data exfiltration and attacker-site publication; preserved the progression from initial no-leak observation to later confirmation and documented alternate procedures / temporary servers used to maintain medicine supply.
- Screened スマレジEC as a watch candidate: a management-login vulnerability affected four customer environments, but the currently disclosed scope was not promoted into this material-core corpus pending broader impact or later expansion.
- Pinned the upstream OKF v0.2 specification used by the bundle to commit `ad30107c31c06aec8a7d5636e0d1058118604e6f`, recording both `okf_version` and producer-defined `okf_spec_revision` / `okf_spec_resource` at bundle root.
- Extended recovery semantics with `service retirement` and expanded the corpus audit with destructive-integrity recovery, communications control-plane abuse, credential-misuse-vs-acquisition distinction and divergent service-outcome findings.
- Completed a primary-source consistency audit of all 25 pre-existing incident concepts; no material contradiction was found. Preserved existing uncertainty, count units and evidence-state progressions rather than rewriting them into stronger claims.
- Added a durable [2026 corpus audit](methodology/corpus-audit-2026-10-04.md) documenting audit method, per-record results, OKF conformance notes, metadata debt and cross-incident findings.
- Confirmed the canonical OKF v0.2 specification lives in `GoogleCloudPlatform/open-knowledge-format`; timestamp-valued metadata emitted in this expansion uses explicit UTC offsets.
- Added 12 material incidents in the first audit expansion: 第一生命グループ、佐川急便、ヤマト運輸/クロネコ代金後払い、池上通信機、ロート製薬、日本トレクス、ApplyNow、VOISING、両毛システムズ、EPARKリラク＆エステ/PeakManager、日本交通、日本テレネット.
- Added PeakManager with the full count/evidence progression: initial ~33 million records at risk to confirmed external transfer of ~22.18 million records after refinement, explicitly retaining `records != people`; also captured sensitive health information in free-text notes and five note entries that may contain expired card data.
- Added VOISING as a detailed BI/analytics compromise case: known BI-tool vulnerability, ~170,000 confirmed leaked records, external publication, compromised-environment disposal, credential invalidation and data-minimization/monitoring changes.
- Added ApplyNow and Ryomo Systems as multi-organization downstream cases, preserving provider-side facts separately from affected-customer notifications and avoiding unsupported aggregation into unique-person totals.
- Added Dai-ichi Life as a long-retention HR case, with a ~120,000 current/former employee population and historical former-employee coverage extending back to 1967 for office staff.
- Added Sagawa and Yamato as current logistics cases while separating digital-service disruption from physical parcel operations and recording still-unknown counts/causes as unknown rather than estimates.
- Added Nihon Kotsu and Ikegami Tsushinki with explicit evidence progression from availability/integrity symptoms to later external-leak observations.
- Added Nippon Telenet with large entrusted BPO/CSS data populations, network-equipment entry at published granularity, and a clean-network rebuild / full endpoint reimaging as a security-state restoration milestone.
- Added producer-defined metadata fields for new concepts where public evidence requires them: `downstream_impact`, `regulatory_response`, `notification_state`, `business_continuity`, and `data_sensitivity`.
- Added `public_record_checked_at` and explicit recovery-phase semantics to the reporting standard so a source-check date is distinct from the date of the latest public incident update.
- Rechecked active primary-source records for Keio, Fines and Times Car; no newer incident disclosure was located, so their canonical `latest_public_update` values remain unchanged while the fresh check is recorded separately.
- Extended the Gyazo record through the September 29 staged recovery change, preserving the distinction between service restart, safe-default visibility and investigation closure.
- Added two distinct Yellow Hat group incidents rather than merging them: the 2rinkan member-server breach and the later Yellow Hat Web work-reservation breach.
- Recorded the confirmed 3,179,454-member exposure in the 2rinkan final report separately from the later maximum 1,801,499-member potential exposure.
- Captured the defensive effect of payment-data and system separation, and flagged the later incident for follow-up because a final public forensic result has not yet been located.
- Added the JCOM September 23 availability incident: external high-volume traffic caused DNS overload and a large-scale outage affecting up to about 4.08 million subscribed households; the report deliberately does not label the traffic as DDoS because malicious intent was not established in the public source.
- Added the Five Foxes / Comme Ca incident with a strict evidence-state distinction between a first-report ransomware suspicion and the later confirmed unauthorized-access / potential personal-data exposure findings, and repaired its missing index entry.
- Added the Seicomart app incident, preserving the progression from the initial roughly 570,000-account estimate to 572,022 confirmed viewed members and the partial-service recovery state.
- Added the Nichirei incident, separating the July cold-chain/frozen-food availability disruption and July 24 operational recovery from the later September confirmation of personal-data leakage.
- Added the Nihon Shisan Souken incident, preserving the evidence progression from ransomware and encryption through credential-theft attribution, possible exfiltration and confirmed customer-data publication on an attacker leak site.
- Added the Meitetsu Kyosho incident, tracking the broad June multi-service outage, later confirmation of attacks against multiple servers, staged service recovery and widening customer notification while preserving the fact that actual external data leakage remained unconfirmed as of the latest primary update.
- Explicitly excluded the August Cariteco Bike outage/restart from the Meitetsu Kyosho incident timeline because the company attributed that interruption to a separate Docomo Bike Share system failure.
- Added the OZmall incident and preserved the correction from the first-report maximum of 447,610 people to the second-report maximum of 442,779, including the newly clarified inclusion of some former members.
- Added the Tokyo Metro / Metpo incident, documenting that the directly affected server held only delivery-suspended email addresses and using it as an example of functional data separation limiting the observed blast radius.
- Added the LEAN BODY incident, documenting confirmed customer-data acquisition through a vulnerable internal Metabase analytics environment while deliberately leaving the CVE unidentified because the company did not publish one.
- Re-synchronized the year and top-level indexes; the 2026 corpus now contains 42 incident reports.

## 2026-10-03

- Initialized the Denno Watch knowledge bundle as OKF v0.2.
- Defined the incident reporting and evidence standard.
- Added the first 2026 incident corpus covering major publicly observable incidents from May through September.
- Expanded coverage with KDDI, Times Car, Helpfeel / Gyazo, Murauchi.com, and Fines incident records.
- Synchronized the year and top-level incident indexes with the current corpus.
