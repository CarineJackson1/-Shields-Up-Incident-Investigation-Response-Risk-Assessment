
# 📝 Cybersecurity Incident Report – Ransomware Simulation

**Prepared by:** Carine Jackson – Cybersecurity Lead  
**Date:** 08/17/2025  
**Incident ID:** AIG-RW-2025-0817  

---

## 1. Executive Summary

On **August 17, 2025**, the cybersecurity team conducted a **simulated ransomware attack** scenario against AIG’s infrastructure using **CISA threat intelligence alerts**.  
The exercise tested the organization’s **incident detection, containment, response, and recovery capabilities**.  

**Key Outcomes:**
- Demonstrated ability to parse CISA JSON alerts for IOCs.  
- Successfully simulated file decryption through brute-force recovery.  
- Validated stakeholder communication templates under crisis conditions.  
- Identified weaknesses in **IAM enforcement, RDP exposure, and patch management**.  

---

## 2. Incident Timeline

| Time (UTC) | Event | Action Taken |
|------------|-------|--------------|
| 08:15 | CISA JSON alert received | Parsed IOCs using `ransomware_alert_analysis.py` |
| 08:20 | Suspicious encrypted ZIP detected | Launched brute-force recovery with `password_bruteforce.py` |
| 08:45 | Password cracked successfully | Decryption tool used to recover compromised test files |
| 09:00 | Critical advisory email sent | Stakeholders notified with mitigation & containment steps |
| 09:30 | Documentation completed | Drafted report and uploaded to security repo |

---

## 3. Findings

- **Vulnerabilities Observed**  
  - Weak password protections on compressed archives.  
  - RDP service exposed without MFA controls.  
  - Delays in patching known vulnerabilities.  

- **Strengths Observed**  
  - Quick alert triage and IOC identification.  
  - Effective recovery using brute-force decryption tool.  
  - Timely communication with stakeholders.  

---

## 4. Impact Assessment

- **Confidentiality:** At risk due to weak password protections and potential data exposure.  
- **Integrity:** No direct corruption simulated, but attacker persistence possible.  
- **Availability:** Files successfully decrypted and restored — availability impact mitigated.  

---

## 5. Recommendations

1. **IAM Hardening** – Enforce MFA for all privileged accounts.  
2. **RDP Security** – Restrict RDP access to VPN users only, consider disabling where not required.  
3. **Patch Management** – Apply vendor patches within **72 hours** of CISA alert release.  
4. **Monitoring & Detection** – Integrate EDR/ SIEM to monitor persistence attempts.  
5. **Regular Testing** – Conduct quarterly ransomware tabletop exercises.  

---

## 6. Attachments / Evidence

- ✅ `ransomware_alert_analysis.py` (IOC parser)  
- ✅ `password_bruteforce.py` (ethical brute-force recovery script)  
- ✅ `incident_report_screenshots/` (simulation evidence)  
- ✅ `stakeholder_emails/critical_alert_advisory.txt`  

---

🔒 **Status:** Incident simulation closed – findings documented and sent to stakeholders.
