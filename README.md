Third-Party Vendor Risk Assessment Tracker (GRC)

 Overview

This project simulates a **Third-Party Vendor Risk Management (TPRM)** system used by enterprise security and GRC teams to assess, track, and govern risks introduced by external vendors.

The system evaluates vendors based on **access level, data sensitivity, business criticality, and security maturity**, registers risks formally, and manages **risk acceptance through time-bound exceptions**. A Streamlit-based dashboard provides visibility for both **CISO-level leadership** and **GRC analysts**.

This project is designed as a **governance-focused simulation**, emphasizing explainable risk decisions rather than UI complexity.

---

 Why Third-Party Risk Management Matters

Modern enterprises rely heavily on third-party vendors (SaaS, MSPs, contractors, support vendors). These vendors often have access to sensitive data or systems, making them a major source of security and compliance risk.

Key challenges addressed:

* Lack of visibility into vendor access and data exposure
* Inconsistent risk assessment across vendors
* Poor tracking of risk acceptance and exceptions
* Expired exceptions leading to hidden compliance gaps

This project demonstrates how these challenges are handled in **real-world GRC workflows**.

---

Key Features

 Vendor Inventory

* Centralized record of all third-party vendors
* Captures business function, vendor type, data sensitivity, access level, and criticality

 Risk Assessment Engine

* Calculates **inherent risk** using weighted factors:

  * Access level
  * Data sensitivity
  * Business criticality
  * Vendor security maturity
* Produces a normalized risk score (0–100)

Risk Register (GRC Core)

 Formal risk records with:

  * Inherent risk vs residual risk
  * Risk category and description
  * Risk owner and status
* Aligns with how auditors and compliance teams expect risks to be documented

Exception & Risk Acceptance Workflow

* Supports business-driven exceptions (e.g., admin access)
* Requires justification, approver, and expiry date
* Automatically:

  * Reduces residual risk for active exceptions
  * Reverts risk when exceptions expire

Scenario-Based Risk Modeling

* High-risk vendors with active exceptions
* Critical vendors with expired exceptions
* High-risk vendors without approved exceptions
* Medium and low-risk vendors requiring no action

Streamlit Dashboards

**CISO Dashboard**:

  * High/critical risk vendors
  * Risks accepted by exception
  * Expired exceptions
**GRC Analyst Dashboard**:

  * Full risk register
  * Exception tracking
  * Operational risk visibility


Architecture Overview

```
vendor-risk-tracker/
│
├── data/                # Vendor, risk, and exception data (JSON)
├── services/            # Risk scoring, vendor assessment, exception logic
├── dashboards/          # Dashboard logic (non-UI)
│
├── app.py               # Terminal-based simulation
├── streamlit_app.py     # Web-based dashboard (presentation layer)
```

Design Principles

* Separation of concerns: Logic is decoupled from UI
* Explainable risk decisions: No black-box scoring
* Governance-first approach: Risk acceptance is documented, time-bound, and reviewable

How IAM Connects to This Project

Identity and Access Management (IAM) controls **who gets access**.
Third-Party Risk Management determines **whether that access should exist at all**.

This project complements IAM by providing:

* Risk-based justification for vendor access
* Governance oversight for privileged access
* Audit-ready documentation of risk acceptance decisions

How to Run the Project

1. Install Dependencies
pip install streamlit

2. Run Terminal Simulation (Optional)
python app.py

3. Run Web Dashboard
streamlit run streamlit_app.py

The dashboard will open at:
http://localhost:8501

Intended Audience

* IAM Engineers
* GRC Analysts
* Security Engineers
* Students preparing for enterprise security roles

This project is a **functional simulation** intended for learning and demonstration purposes. It is not a production-ready GRC platform but reflects **real-world governance workflows and decision-making patterns** used in enterprises.


Author
Prajwal DM
Cybersecurity | IAM | GRC | Identity-First Security
