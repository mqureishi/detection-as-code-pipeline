# Detection-as-Code (DaC) Validation Pipeline

A production-grade **Detection-as-Code (DaC)** validation and CI/CD automation pipeline designed to treat security detection rules with the same rigorous quality control as application source code.

---

## 🚀 Project Overview
In modern Security Operations (SecOps), detection engineering requires automated testing to ensure rules are syntactically correct, structurally compliant, and mapped to adversary behavior frameworks before deployment. This repository automates the validation of Sigma-based detection rules using Python and GitHub Actions.

---

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.12 (with isolated virtual environments via `venv`)
* **Libraries:** `PyYAML` for automated syntax parsing and schema validation
* **CI/CD Automation:** GitHub Actions (`.github/workflows/validate_rules.yml`)
* **Threat Intelligence Frameworks:** MITRE ATT&CK (e.g., Technique T1033 for System Owner/User Discovery)

---

## 📁 Repository Structure
```text
detection-as-code-pipeline/
├── .github/
│   └── workflows/
│       └── validate_rules.yml   # CI/CD automation pipeline workflow
├── rules/
│   └── suspicious_whoami_recon.yml # Sigma detection rule with MITRE mapping
├── tests/
│   └── test_rules_syntax.py     # Custom Python schema & syntax validator
├── venv/                        # Local isolated Python virtual environment
├── README.md                    # Project documentation
└── LICENSE                      # Open-source license
