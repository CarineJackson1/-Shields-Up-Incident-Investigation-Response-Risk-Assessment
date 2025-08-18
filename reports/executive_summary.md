📑 Executive Summary

Executive Summary – Cybersecurity Project (AIG Ransomware & APT34 Risk Assessment)

Overview:
This project simulated a real-world ransomware incident against AIG using CISA alerts, alongside a nation-state threat investigation (APT34). The goal was to demonstrate incident response under crisis and consulting-style risk assessment.

Key Findings:
	•	Ransomware Simulation revealed exposure to brute-force password attacks and unpatched RDP services.
	•	APT34 Threat Assessment showed risk of lateral movement and data exfiltration through phishing and supply-chain compromise.
	•	IAM Review indicated lack of consistent MFA enforcement.
	•	Cloud Security required stricter S3 encryption and logging.

Risks Identified:
	•	Critical: Active ransomware IOCs linked to CISA alerts (immediate patching required).
	•	High: APT34 phishing & lateral movement targeting unsegmented networks.
	•	Medium: Insider threats and outdated components.

Overall Security Posture:
🟠 Moderate-to-High Risk – The environment is vulnerable to both opportunistic ransomware and targeted nation-state activity.

Recommendations:
	1.	Enforce MFA across all privileged accounts (IAM hardening).
	2.	Patch all vulnerable services within 72 hours of CISA alert.
	3.	Deploy SIEM & EDR solutions for continuous monitoring.
	4.	Implement Zero Trust segmentation to reduce lateral movement.
	5.	Conduct quarterly penetration tests + annual risk assessments.

⸻

📝 Sample Incident Report (Excerpt)

Incident Timeline – AIG Ransomware Simulation

Time (UTC)	Event	Action Taken
08:15	CISA JSON alert received	Parsed IOCs using ransomware_alert_analysis.py
08:20	Suspicious encrypted ZIP detected	Launched brute-force recovery with password_bruteforce.py
08:45	Password cracked successfully	Decryption tool used to recover sample files
09:00	Critical advisory email sent	Stakeholders notified with mitigation steps
09:30	Incident report drafted	Documented findings & uploaded to reports/


⸻

