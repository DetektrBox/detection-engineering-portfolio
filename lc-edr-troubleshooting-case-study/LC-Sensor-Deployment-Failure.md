# LimaCharlie EDR Sensor Deployment Failure  
**Root-Cause Analysis of a Global Vendor Outage – 28 Nov 2025**

> **TL;DR**  
> LimaCharlie’s public EDR sensor download endpoints (all OSes) served the wrong binary for ≈12 hours. I proved it was vendor-side in <90 minutes, filed the ticket that got it fixed, and kept my 14-day detection sprint on schedule by pivoting to Sysmon + Sigma.

## Symptoms
- Every EDR download link returned `https://downloads.limacharlie.io/sensor/...` returned `hcp_*_release_4.33.20.exe` (HCP placeholder) instead of the expected `lc_sensor.exe` / `rphcp.exe`.
- Affected **Windows 32/64, macOS, Linux** equally.
- Adapter downloads succeeded → isolated the problem to EDR-specific CDN paths.
- Direct URLs returned 404 or wrong artifact.
- BITS jobs stalled with `0x80070004 – The server may be misconfigured`.

## Proof It Was Vendor-Side (all local checks passed)

```powershell
Resolve-DnsName downloads.limacharlie.io                # Success
Test-NetConnection sensor.limacharlie.io -Port 443      # TcpTestSucceeded: True
New-NetFirewallRule -DisplayName "LimaCharlie" -Direction Outbound -Protocol TCP -RemotePort 443 -Action Allow

| Platform       | Expected File       | Actual File Served                    | Result |
|----------------|---------------------|---------------------------------------|--------|
| Windows 64-bit | lc_sensor.exe       | hcp_win_x64_release_4.33.20.exe       | Wrong  |
| macOS          | limacharlie.pkg     | hcp_macos_release_...                 | Wrong  |
| Linux 64-bit   | limacharlie.deb     | hcp_linux_x86_64_release_...          | Wrong  |

Impact & Immediate Mitigation

Blocked new sensor enrollment for the entire LimaCharlie user base during the window.
My response: Instant pivot to Sysmon (SwiftOnSecurity config) + Atomic Red Team + Sigma pipeline.
Result: Delivered 15+ validated detections and MITRE coverage the same day — zero days lost.

Resolution

Submitted detailed ticket to answers@limacharlie.io with repro steps, hashes, and cross-platform evidence.
LimaCharlie engineering confirmed CDN misconfiguration within 4 hours and rolled back the broken release.

Key Takeaways (what separates juniors from hires)

Never assume “the vendor is fine” — validate file hashes, not filenames.
Isolate variables in minutes — proving adapters worked eliminated 95 % of local causes.
Document like the fix depends on it — because sometimes it does.
Build detection pipelines that survive cloud outages — EDR down ≠ detection engineering down.

This is ownership on day zero.
Related Artifacts in this Repo
→ /sigma/ – 15+ Sigma rules written same day
→ /mitre/0xChrisB-coverage-v18.json – 15 techniques painted green despite the outage
→ /SNAPSHOTS/ – Sysmon event screenshots used for rule creation

[![Case Study](https://img.shields.io/badge/Case%20Study-LC%20Sensor%20Incident-blue?style=for-the-badge)](https://github.com/DetektrBox/detection-engineering-portfolio/blob/main/lc-edr-troubleshooting-case-study/LC-Sensor-Deployment-Failure.md)
