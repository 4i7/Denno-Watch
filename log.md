# Update log

## 2026-10-04

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
- Re-synchronized the year and top-level indexes; the initial corpus now contains 22 incident reports.

## 2026-10-03

- Initialized the Denno Watch knowledge bundle as OKF v0.2.
- Defined the incident reporting and evidence standard.
- Added the first 2026 incident corpus covering major publicly observable incidents from May through September.
- Expanded coverage with KDDI, Times Car, Helpfeel / Gyazo, Murauchi.com, and Fines incident records.
- Synchronized the year and top-level incident indexes with the current corpus.
