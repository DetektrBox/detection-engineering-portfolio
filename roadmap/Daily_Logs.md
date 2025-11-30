### Day 1 - Configurations & Setup
## Goal: Setup the tooling and systems

- Gather/Fine-tune resources
- Config tools (LimaCharlie, OBS, VS Code & GitHub Repo, Sysmon, Etc.)
- Plan 14-Day Detection Engineering Sprint (Sigma, Live EDR Results, DaC ideas, Video Creation, etc.)

### Day 2 – Visibility: LimaCharlie vs Event Viewer
## Goal: Prove EDR telemetry > default Windows logs

# Event Viewer (stone age)
- Event ID 4688 only
- Command line often truncated
- No hashes, no parent lineage, no JSON

# LimaCharlie (2025 reality)
- Full untruncated command lines
- Hashes, parent/child tree, base addresses
- Real-time JSON streaming from the cloud
- Remote command execution from browser

# Live proof (2025-11-28):
- Every PowerShell spawn with -NoProfile -NoLogo -ExecutionPolicy Unrestricted
- All precursor behavior visible before any payload even runs

→ This is why detection engineers don’t use Event Viewer in 2025.

Next: Day 3 – Detection-as-Code (first live Sigma rule)

### Day 3 – Detection-as-Code (Live in Production)

## Goal: Deploy working detection for PowerShell download cradle (T1059.001)

# Result:
- Enabled LimaCharlie's official Sigma extension (4,000+ community rules)
- Real alerts fired immediately on PowerShell abuse
- Full MITRE ATT&CK tagging
- No custom YAML hell needed – production rules work out of the box

# Proof:
- Detections tab shows live alerts with T1059.001
- Timeline shows full untruncated command lines
- This is what real detection engineering looks like on Day 3

Next: Day 4 – Atomic Red Team + signed binary abuse that flies under AV

# Day 4 – From Red to Blue: Atomic Red Team → Custom Sigma

1. Executed real 2025 TTP (T1218.011 – signed-binary proxy via rundll32 url.dll)
2. Community Sigma rule fired (good)
3. Authored tighter, branded rule that reduces noise
4. Result: My rule fires faster, clearer, and with my name on it

This is detection engineering: understand the attack → improve the detection → own the outcome.