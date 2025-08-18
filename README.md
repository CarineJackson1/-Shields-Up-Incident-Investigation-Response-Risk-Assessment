# 🛡️ Cybersecurity Incident Investigation/Response & Risk Assessment

#Cybersecurity #IncidentResponse #ThreatIntel #RiskAssessment #ThreatDetection #DigitalForensics #CyberDefense #SOC #InfoSec #BreachResponse  
---

cybersecurity-incident-response-risk-assessment/
│── README.md
│
├── risk_assessment/
│   ├── APT34_threat_intel_report.pdf   # ✅ Use your uploaded PDF here
│   ├── risk_assessment_report.md       # (optional, summary in Markdown)
│   └── cybersecurity_risk_matrix.xlsx
│
├── reports/
│   ├── risk_matrix.md
│   ├── executive_summary.md
│   ├── incident_report.md
│   └── final_combined_report.pdf
│
└── ransomware_response/
    ├── password_bruteforce.py
    ├── ransomware_alert_analysis.py
    ├── file_decryptor_sim.py
    └── stakeholder_emails/

---

## 📚 Project Overview

This repository unifies **two cybersecurity projects**:

1. **Incident Response Simulation (AIG Ransomware Attack)**  
   - Uses **CISA threat intelligence** to detect, analyze, and respond.  
   - Simulates recovery with decryption tools and ethical brute-force methods.  
   - Includes **stakeholder communication templates** and **incident reports**.  

2. **Threat Investigation & Risk Assessment (APT34 Attack)**  
   - Investigates APT34 with **OSINT + MITRE ATT&CK mapping**.  
   - Performs a **risk assessment** with impact on Confidentiality, Integrity, and Availability.  
   - Delivers **professional-grade reports** for clients & stakeholders.  

Together, this project demonstrates **both SOC Analyst skills (hands-on detection & response)** and **Cybersecurity Consulting skills (risk assessment & reporting)**.

---

## 🧰 Tools & Technologies

- 🐍 Python (alert parsing, brute-force recovery tools)
- 🗂 JSON/CSV parsing (CISA alerts)
- 🔍 OSINT Tools: Shodan, VirusTotal, OTX, SecurityTrails
- 🧩 MITRE ATT&CK framework
- 📄 Markdown/PDF for reports
- 📊 Risk Matrix (Excel/Markdown)

---

## 🔍 Key Components

### 🔹 Ransomware Response
- `ransomware_alert_analysis.py` → Parses CISA JSON alerts into CSV  
- `file_decryptor_sim.py` → Simulates decryption of encrypted files  
- `password_bruteforce.py` → Ethical brute-force of encrypted ZIPs  
- `incident_report.md` → Incident timeline, mitigation & recovery steps  
- `stakeholder_emails/` → Pre-written templates for internal/external comms  

### 🔹 Threat Investigation & Risk Assessment
- **APT34 Threat Intel Report** (OSINT, MITRE ATT&CK mapping)  
- **Risk Matrix** (Likelihood × Impact scoring)  
- **Risk Assessment Report** → Client-ready mitigation strategies  

---

## 📊 Outcomes

✅ Applied **real-world threat intelligence** (CISA, MITRE ATT&CK)  
✅ Strengthened **SOC workflows**: detection, response, recovery  
✅ Delivered **professional reports** (incident timeline, risk matrix)  
✅ Practiced **stakeholder communication under crisis**  
✅ Demonstrated **dual-role skills**: hands-on SOC + strategic consulting  

---

## 📧 Sample Stakeholder Advisory  

> 🚨 This advisory email notifies infrastructure owners of an **active ransomware threat**, referencing **CISA/FBI/NSA alerts** and recommending immediate mitigations (MFA enforcement, patching, RDP lockdown).  

---

## 🏁 Deliverables

- 🐍 Python scripts (`ransomware_response/`)
- 📄 Threat Intelligence Report (APT34)  
- 📄 Cybersecurity Risk Assessment Report (with matrix)  
- 📨 Stakeholder Communication Templates  
- 📑 Final Combined Report (executive summary + evidence)  

---

## 📸 Demo Screenshot
![Ransomware Response Simulation](assets/ransomware_sim_screenshot.png)

---

## 📂 Next Steps
- Expand to include **cloud IAM security review** (AWS, Azure)  
- Add **SIEM correlation rules** for automated detection  
- Run a **red-team vs. blue-team simulation** for realism  

---

## 📄 Reports & Deliverables

- [🧾 Cybersecurity Threat Intelligence Report (APT34, PDF)](risk_assessment/APT34_threat_intel_report.pdf)
- [📊 Risk Matrix (Markdown)](reports/risk_matrix.md)
- [📑 Executive Summary](reports/executive_summary.md)
- [📝 Incident Report Timeline](reports/incident_report.md)
- [📄 Final Combined Report (PDF)](reports/final_combined_report.pdf)
