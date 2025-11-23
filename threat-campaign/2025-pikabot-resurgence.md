# 2025 Pikabot Resurgence – Full Campaign Breakdown

**Threat Actor**: TA577 → Pikabot (new loader family)  
**Initial Access**: Malspam → ISO/LNK → Cobalt Strike → Pikabot  
**Active**: Jan 2025 – present

## TTP Summary (MITRE ATT&CK)
| Technique                     | ID           | Detection Rule |
|-------------------------------|--------------|----------------|
| Phishing: Attachment          | T1566.001    | — |
| Signed Binary Proxy Execution | T1218.011    | proc_creation_win_pikabot_dropper.yml |
| Obfuscated Files              | T1027        | file_event_susp_lnk_creation.yml |
| Process Injection             | T1055        | (in progress) |

## Custom Detections Shipped
- Sigma: [Pikabot Dropper via mshta](sigma/windows/process_creation/proc_creation_win_pikabot_dropper.yml)
- YARA: [Pikabot 2025 strings](yara/pikabot_2025.yar)
- KQL Hunting Query (Sentinel):
```kql
SigninLogs
| where TimeGenerated > ago(7d)
| where ResultType == "0"
| where IPAddress in ("185.117.73.132", "193.233.132.51")