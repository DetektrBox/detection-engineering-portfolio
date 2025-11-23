# Living off the Land – Rundll32 Network Activity (T1218.011)

**ATT&CK**: Defense Evasion – Signed Binary Proxy Execution  
**Observation**  
Adversaries abuse rundll32.exe to download and execute payloads directly.

**Rule** → [../sigma/windows/process_creation/proc_creation_win_susp_rundll32_network.yml](../sigma/windows/process_creation/proc_creation_win_susp_rundll32_network.yml)

**Lab Validation**  
Atomic Red Team T1218.011 → fires instantly in Splunk and Elastic.

**Screenshot** → [/assets/rundll32_network.png](assets/rundll32_network.png)