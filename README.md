# Detection Engineering Portfolio – Chris Bradford

![Detection Engineering Banner](https://media.licdn.com/dms/image/v2/D4E16AQEwvcSys-1BHw/profile-displaybackgroundimage-shrink_350_1400/B4EZf8ubK1HwAY-/0/1752291718131?e=1765411200&v=beta&t=kMZQivAtkJkCOxwi380tsy5PHjSM04YKKvJQoLMb5Ic)

**USAF Veteran** • **Clearance-Eligible** • **SC-200 + CJDE → Dec 2025**  
Former SOC Analyst (DefendEdge) → now executing a focused Detection Engineering sprint that turns raw telemetry into production-grade content.

**This is not a notes repo.**  
Everything here follows the same cycle I will use on your team:

> **Telemetry → Detection → Validation → Tuning → Automation → Documentation**

No copy-paste Sigma. No theory. Only content that has **fired real alerts in my lab**.

---

## What Is Inside Right Now

| Category                  | What It Proves                                                                                               | Folder |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|--------|
| **Telemetry Foundation**  | Sysmon • LimaCharlie • OSQuery • Windows Event Logs – cross-mapped field-by-field from the same TTPs                 | [`telemetry`](telemetry) |
| **Sigma Rules**           | Custom rules authored from my own telemetry – high-fidelity + noisy baselines + explicit tuning notes               | [`detections/sigma`](detections/sigma) |
| **Elastic / KQL / EQL**   | Sigma → Kibana translation with live screenshots of hits                                                            | [`detections/elastic`](detections/elastic) |
| **YARA Rules**            | Pattern-based detections for 2024–2025 families (LummaC2, AsyncRAT, Pikabot, Latentit, etc.)                        | [`yara`](yara) |
| **Adversary Simulation**  | Atomic Red Team • MITRE Caldera • Sliver C2 – full execution chains + telemetry exports                             | [`adversary-simulation`](adversary-simulation) |
| **Detection Stories**     | Red Canary-style narratives: TTP → raw telemetry → custom rule → alert → tuning → final version                     | [`detection-stories`](detection-stories) |
| **Detection-as-Code**     | GitHub Actions that **fail the build** on broken Sigma and auto-convert to Elastic on merge                          | [`.github/workflows`](.github/workflows) |
| **Malware Analysis**      | CAPA + HybridAnalysis on real samples → direct mapping to new detections                                            | [`malware`](malware) |
| **Flagship Case Study**   | End-to-end 2025 attack chain with multi-sensor telemetry, Sigma + Elastic, FP/FN analysis, SOC playbook, and diagram | [`case_studies/flagship`](case_studies/flagship) |

---

## 9-Day Detection Engineering Sprint (v2) – Live Right Now

I am **currently executing** this exact sprint. Watch the folders update daily.

| Day | Theme                                      | Core Deliverable |
|-----|--------------------------------------------|------------------|
| 1   | Telemetry Foundation                       | `telemetry/day1/` + field_mapping.md |
| 2   | Sigma From Scratch                         | 4 custom rules in `detections/sigma/day2/` |
| 3   | Atomic Red Team + Correlation              | `detection-stories/day3/` + multi-event chain |
| 4   | Elastic Stack                              | `detections/elastic/day4/` + live Kibana queries |
| 5   | Detection-as-Code Pipeline                 | CI that blocks broken rules |
| 6   | Caldera Emulation                          | Full ATT&CK chain + detection story |
| 7   | Sliver C2                                  | Beacon → injection → lateral + Sliver-specific Sigma |
| 8   | Malware & Static Analysis                  | CAPA + HybridAnalysis → new detections |
| 9   | Flagship Case Study                        | The portfolio centerpiece |

Progress is public – just watch the repo.

---

## Why You Should Hire Me as Your Next Detection Engineer

- 11 years of mission-driven discipline (USAF) + real SOC triage experience
- I **author** detections from raw telemetry instead of consuming community content
- I **validate** every rule in CI so nothing broken ever ships
- I **tune** based on lived alert-fatigue reality
- I **document** for 02:00 handoffs, not slide decks
- Clearance-eligible today • Targeting **SC-200** + **CJDE** by Dec 2025

**Open to:** Detection Engineer • Threat Detection Engineer • Security Content Engineer • MDR Engineer  
(Remote preferred • Cleared roles & CONUS welcome)

---

## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Christopher_Bradford-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chrisbradford-/)  
**Email:** Chris.H.Bradford@proton.me

**Last updated:** November 2025 – updated daily until hired

---

⭐ Star this repo if you’ve ever had to explain why a rule fires 400 times a day  
💬 Rule requests, feedback, job leads — always welcome

> **The best detection engineers don’t just read Sigma rules. They ship the ones everyone else ends up copying.**

— Chris Bradford, right now.