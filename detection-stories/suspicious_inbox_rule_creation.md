# Malicious Inbox Rule – Email Exfil (T1114.003)

**ATT&CK**: Collection – Email Collection  
**Observation**  
Compromised accounts create hidden forwarding/deletion rules.

**Rule** → [../sigma/cloud/m365/m365_susp_inbox_rule_malicious.yml](../sigma/cloud/m365/m365_susp_inbox_rule_malicious.yml)

**Lab Validation**  
Created rule via Graph API → alert in Sentinel within 60 seconds.

**Screenshot** → [/assets/inbox_rule.png](assets/inbox_rule.png)