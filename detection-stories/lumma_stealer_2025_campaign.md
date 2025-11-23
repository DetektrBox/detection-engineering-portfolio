# LummaC2 Stealer – 2025 Resurgence (T1555.003)

**ATT&CK**: Credential Access – Credentials from Password Stores  
**Threat**: LummaC2 (2025 variants)

**Observation**  
In late 2025, Lumma evolved to use reflective DLL loading via regsvr32/rundll32 with embedded .dat payloads downloaded to AppData.

**Detection Logic**  
Sigma rule monitors rundll32/regsvr32 spawning with HTTP URLs + AppData paths.

**Rule** → [../sigma/windows/process_creation/proc_creation_win_lumma_stealer.yml](../sigma/windows/process_creation/proc_creation_win_lumma_stealer.yml)

**Lab Validation**  
Tested with actual Lumma sample (SHA256: available on request) + Atomic Red Team → fires reliably in <3 seconds.

**Alert Screenshot** → [/assets/lumma_alert.png](assets/lumma_alert.png) *(add later)*

**False Positive Rate**: Low – tuned out legitimate MSI installers