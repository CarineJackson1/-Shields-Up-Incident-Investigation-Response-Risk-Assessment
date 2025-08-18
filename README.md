# 🛡️ Cybersecurity Incident Investigation, Response & Risk Assessment

#Cybersecurity #IncidentResponse #ThreatIntel #RiskAssessment #ThreatDetection #DigitalForensics #CyberDefense #SOC #InfoSec #BreachResponse  

---

## 📂 Repository Structure
cybersecurity-incident-response-risk-assessment/
│── README.md
│
├── risk_assessment/
│   ├── APT34_threat_intel_report.pdf    # ✅ Threat Intel Report (uploaded PDF)
│   ├── risk_assessment_report.md        # (Optional summary in Markdown)
│   └── cybersecurity_risk_matrix.xlsx   # Risk matrix in Excel
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

This repository unifies **two major cybersecurity projects**:  

### 🔹 1. Incident Response Simulation – *AIG Ransomware Attack*  
- Leverages **CISA threat intelligence** for detection & analysis  
- Simulates recovery via **ethical brute-force decryption tools**  
- Provides **stakeholder communication templates** & full **incident timeline report**  

### 🔹 2. Threat Investigation & Risk Assessment – *APT34 Attack*  
- Uses **OSINT + MITRE ATT&CK mapping** to analyze adversary TTPs  
- Conducts **risk assessment** across Confidentiality, Integrity, Availability (CIA triad)  
- Produces **consulting-grade risk reports** with mitigation strategies  

👉 Together, this project showcases both:  
- 🕵️ **SOC Analyst skills** (hands-on detection, threat response, recovery)  
- 📊 **Consulting skills** (risk analysis, strategy, stakeholder communication)  

---

## 🧰 Tools & Technologies  

- 🐍 **Python** – alert parsing, brute-force recovery tools  
- 🗂 **JSON/CSV** – parsing structured threat intel (CISA feeds)  
- 🔍 **OSINT** – Shodan, VirusTotal, OTX, SecurityTrails  
- 🧩 **MITRE ATT&CK Framework** – TTP mapping for APT34  
- 📄 **Markdown & PDF Reports** – executive summaries, intel reports, risk assessments  
- 📊 **Risk Matrix** – likelihood × impact scoring  

---

## 🔍 Key Components  

### 🦠 Ransomware Response
- `ransomware_alert_analysis.py` → Parses CISA JSON alerts into CSV  
- `file_decryptor_sim.py` → Simulates decrypting compromised files  
- `password_bruteforce.py` → Ethical brute-force recovery tool for encrypted ZIPs  
- `incident_report.md` → Incident timeline, findings, recommendations  
- `stakeholder_emails/` → Crisis-ready communication templates  

### 🎯 Threat Investigation & Risk Assessment
- **APT34 Threat Intel Report (PDF)** – OSINT + MITRE ATT&CK mapping  
- **Risk Matrix** – Likelihood × Impact scoring for threats  
- **Risk Assessment Report** – Client-facing recommendations & mitigations  

---

## 📊 Outcomes  

✅ Applied **real-world threat intelligence** (CISA, MITRE ATT&CK)  
✅ Strengthened **SOC workflows**: detection → containment → recovery  
✅ Produced **professional reports** (incident timeline, risk matrix, executive summary)  
✅ Practiced **clear stakeholder communication under crisis**  
✅ Demonstrated **dual-role capability**: technical SOC + strategic consulting  

---

## 📧 Sample Stakeholder Advisory  

🚨 *Critical Ransomware Alert:*  
> This advisory email notifies infrastructure owners of an **active ransomware campaign**, referencing **CISA/FBI/NSA alerts**.  
> **Mitigation Steps:** Enforce MFA, apply patches, restrict RDP access.  

🔗 [View Critical Alert Advisory (PDF)](https://github.com/CarineJackson1/-cybersecurity-incident-investigation-threat-intelligence-reporting/blob/main/ransomeware_response/stakeholder_emails_critical_alert_advisory.txt.pdf)  

---

## 🏁 Deliverables  

- 🐍 Python scripts (`ransomware_response/`)  
- 📄 [APT34 Threat Intelligence Report (PDF)](risk_assessment/APT34_threat_intel_report.pdf)  
- 📊 [Cybersecurity Risk Matrix (Markdown)](reports/risk_matrix.md)  
- 📑 [Executive Summary](reports/executive_summary.md)  
- 📝 [Incident Report Timeline](reports/incident_report.md)  
- 📄 [Final Combined Report (PDF)](reports/final_combined_report.pdf)  
- 📨 [Stakeholder Communication Templates](ransomware_response/stakeholder_emails/)  

---

## 📸 Demo Screenshot  

![Ransomware Response Simulation](assets/ransomware_sim_screenshot.png)  

---

## 🚀 Next Steps  

- Expand with **cloud IAM security review** (AWS, Azure)  
- Add **SIEM correlation rules** for automated detection  
- Run a **Red-Team vs Blue-Team simulation** for realism  
- Integrate findings into a **SOC Playbook** for repeatable response  

---
