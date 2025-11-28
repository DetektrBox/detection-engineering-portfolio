# Detection Engineering Portfolio -- Chris Bradford

![Detection Engineering Banner](https://media.licdn.com/dms/image/v2/D4E16AQEwvcSys-1BHw/profile-displaybackgroundimage-shrink_350_1400/B4EZf8ubK1HwAY-/0/1752291718131?e=1765411200&v=beta&t=kMZQivAtkJkCOxwi380tsy5PHjSM04YKKvJQoLMb5Ic)  


**USAF Veteran** • **Active Clearance-Eligible** • **SC-200 + CJDE Dec 2025**  
Former SOC Analyst (DefendEdge) → now shipping **production-ready, lab-validated detection content daily**

**Every single rule in this repo fires real alerts in my lab** (Splunk | Elastic | Microsoft Sentinel | Atomic Red Team). No theory, only content that works.

## What’s Inside (Live & Growing)

| Category                       | Count | Details                                                                                   | Folder Link                                 |
|--------------------------------|-------|-------------------------------------------------------------------------------------------|---------------------------------------------|
| **Sigma Rules**                | 30+   | Windows • Linux • macOS • Cloud • Identity • Fully MITRE-mapped & tuned                   | [`/sigma`](sigma)                           |
| **YARA Rules**                 | 12+   | 2024–2025 families (LummaC2, AsyncRAT, Pikabot, Latentit, etc.)                           | [`/yara`](yara)                             |
| **Detection Stories**          | 10    | Red Canary/CrowdStrike-style narratives: TTP → Detection → Alert screenshots              | [`/detection-stories`](detection-stories)   |
| **Threat Campaign Write-up**   | 1     | Full 2025 campaign deep-dive with timeline, TTPs, custom rules, and hunting queries       | [`/threat-campaigns`](threat-campaigns)     |
| **Detection-as-Code Pipeline** | 3     | GitHub Actions: Sigma lint • YARA compile • rule validation on every push                 | [`.github/workflows`](.github/workflows)    |
| **Automation Scripts**         | 3+    | Sigma → Splunk/Elastic converters • bulk YARA tester • MITRE enrichment script            | [`/automation`](automation)                 |
| **Assets**                     | –     | Screenshots of alerts firing in my lab • banners • rule validation evidence • Atomic Red Team results | [`/assets`](assets)             |


## Why Hire Me as Your Next Detection Engineer?

- 11 years of mission-critical discipline (USAF) + real SOC triage (800+ incidents)
- Proven ability to author, tune, validate, and automate high-fidelity detections
- Clearance-eligible today: ready for DoD/contractor roles
- Actively pursuing **Microsoft SC-200** and **CJDE** (target completion Dec 2025)
- 100% public, production-grade portfolio — recruiters can see the quality instantly

**Open to**: Detection Engineer • Threat Detection Engineer • Security Content Developer • SOC Content Engineer  
(Remote or Cleared –- CONUS)

## Let’s Connect
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Christopher_Bradford-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chrisbradford-/)  
**Email**: Chris.H.Bradford@proton.me

**Last updated**: November 2025 — updated daily until I land the role

---
### MITRE ATT&CK Coverage (T1059.001 already green)

![T1059.001 – PowerShell EncodedCommand caught live](https://raw.githubusercontent.com/DetektrBox/detection-engineering-portfolio/main/mitre/t1059.001-green-screenshot.png)

**Caught live 2025-11-28** – Sysmon Event 4688 + custom Sigma rule  
Full layer JSON in repo: [`mitre/0xchrisb-detection-coverage-v18.json`](mitre/0xchrisb-detection-coverage-v18.json)

Updated daily until I land the role.
---

⭐ **Star this repo** if you find the content useful  
💬 Feedback, rule requests, or job leads — always welcome!

*“The best detection engineers don’t just read Sigma rules — they write the ones everyone else uses.”* – Me, right now.