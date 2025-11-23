# Impossible Travel – Azure AD Sign-in (T1078.004 / T1110)

**Observation**  
Adversaries with compromised credentials often connect from geographically impossible locations.

**Detection Logic**  
Sigma rule flags successful Azure AD sign-ins where previous success was >2000 km away and <1 hour apart.

**Rule** → [../sigma/cloud/azure/azure_susp_signin_impossible_travel.yml](../sigma/cloud/azure/azure_susp_signin_impossible_travel.yml)

**Lab Validation**  
Simulated with two VMs (US + Russia) → alert fires in <30 seconds.

**Alert Screenshot** → [/assets/impossible_travel.png](assets/impossible_travel.png) *(add later)*