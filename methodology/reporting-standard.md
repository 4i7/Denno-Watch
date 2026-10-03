---
type: Reference
title: Denno Watch incident reporting standard
description: Evidence, provenance, lifecycle and field semantics for public incident records.
tags: [methodology, incident-response, provenance, okf]
status: draft
generated: { by: openai/gpt-5.6-sol, at: 2026-10-03T13:11:00Z }
sources:
  - id: okf-v02
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format v0.2 specification
    author: team:GoogleCloudPlatform
---

# Purpose

Denno Watch records what can be established from public evidence about major cyber incidents affecting organizations in Japan. The corpus is optimized for later defensive use: understanding what happened, what was affected, how response and recovery progressed, what remained unknown, and which controls can be learned from the disclosed facts.

The bundle follows OKF v0.2: concept documents are Markdown with YAML frontmatter; provenance is stored in `sources`; claim-level citations use matching footnote IDs; machine generation and independent verification are separate signals.[^okf-v02]

# Inclusion

An incident is in scope when public evidence shows at least one of the following:

- material interruption of business or customer-facing services;
- confirmed or plausible exposure of large-scale, sensitive or authentication data;
- compromise with meaningful downstream, supplier, infrastructure or multi-organization blast radius;
- a technically reusable defensive lesson that is unusually well documented by the affected organization.

Inclusion is not a severity ranking. Denno Watch does not assign companies a score or infer business damage that has not been disclosed.

# Evidence hierarchy

Use sources in this order where available:

1. affected organization, parent/subsidiary or directly responsible service provider;
2. regulator, law-enforcement or other competent public authority;
3. directly affected partner or customer organization;
4. high-quality secondary reporting that adds independently observable facts.

Secondary reporting must not override a later primary correction. Anonymous attacker claims, leak-site claims and social-media posts are recorded only when independently corroborated or when the fact being recorded is merely that the claim/publication itself exists.

# Fact states

Do not collapse absence of evidence into a negative finding.

| State | Meaning |
| --- | --- |
| `confirmed` | Explicitly established by a cited source. |
| `possible` | The source says exposure/impact cannot be excluded or may have occurred. |
| `not_observed` | Investigation states that evidence of the event was not found. This is not proof that it never happened. |
| `not_publicly_disclosed` | The organization has not published the detail, or explicitly withheld it. |
| `unknown` | Public evidence is insufficient to determine the fact. |
| `not_applicable` | The field does not apply to the incident. |

# Canonical incident metadata

Incident concepts use `type: Cybersecurity Incident` plus a producer-defined `incident` mapping. Fields may be extended when the public record requires it.

| Field | Meaning |
| --- | --- |
| `organization` | Primary affected organization. |
| `sector` | Broad business sector. |
| `jurisdiction` | Primary jurisdiction; currently `JP` for this corpus. |
| `incident_status` | Public lifecycle such as `investigating`, `recovering`, `monitoring`, or `public_report_closed`. |
| `attack_type` | Publicly established incident class; never inferred solely from symptoms. |
| `earliest_known_activity` | Earliest activity the public investigation ties to the incident. |
| `detected_at` | Detection time/date if disclosed. |
| `first_disclosed_at` | First public disclosure date. |
| `latest_public_update` | Latest primary update incorporated into the record. |
| `intrusion_vector` | Confirmed route, or an explicit unknown/withheld state. |
| `affected_services` | Material systems/services publicly described as affected. |
| `data_exposure` | `confirmed`, `possible`, `not_observed`, or `unknown`. |
| `availability_impact` | Whether operations/services were disrupted. |
| `restoration_state` | Latest publicly observable recovery condition. |
| `secondary_abuse` | Publicly reported misuse after the incident. |

Dates in the incident mapping use the precision actually published. Never invent a time. OKF-native timestamps such as `generated.at`, `verified[].at` and `stale_after` use ISO 8601 with an explicit offset as required by OKF.[^okf-v02]

# Required report sections

Each report should contain:

1. **Executive summary** - the smallest accurate account of the incident.
2. **Observable timeline** - activity, detection, disclosure, response, restoration and later findings in chronological order.
3. **Impact** - availability, confidentiality, integrity, customer/employee/partner and downstream effects.
4. **Technical findings** - only what public evidence establishes about access, malware, credentials, infrastructure and attack path.
5. **Response and recovery** - containment, investigation, notification, rebuilding and preventive measures.
6. **Prognosis / current state** - the latest operational and investigative state, not a speculative forecast.
7. **Defensive lessons** - bounded lessons directly supported by the disclosed facts.
8. **Unknowns / withheld details** - important unanswered questions so readers do not mistake silence for certainty.

# Counts and corrections

Preserve the unit used by the source: people, accounts, records, stores, systems, etc. A record count must not be restated as a number of unique people unless the source says so. If an organization corrects a number, the corrected value becomes canonical and the prior value remains in the timeline with the correction noted.

# Freshness and review

Machine-authored reports include `generated` and remain `status: draft` until independently checked. Do not add `verified` merely because the same agent reread the source: OKF reserves `verified` for an actual confirmation event distinct from generation.[^okf-v02]

Ongoing incidents should use `stale_after` so consumers can detect when a new source check is due. Closed or mature reports may omit it, but should still record `latest_public_update`.

# Safety and publication boundary

The corpus is defensive and public-source-only. It may document disclosed intrusion paths and control failures, but should not add unpublished exploit steps, secrets, credentials, personal data samples, or operational details whose only value would be to facilitate abuse.

[^okf-v02]: Open Knowledge Format v0.2 specification.
