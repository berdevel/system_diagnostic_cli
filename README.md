# FoxconnFailureAnalyzer

Automated diagnostic and root cause analysis tool for NVIDIA HGX/Bianca platforms.

FoxconnFailureAnalyzer parses Redfish Event Logs, detects NVIDIA XID events, identifies Bianca power failures, analyzes critical system events, and generates technical reports with actionable recommendations.

---

# Features

## Bianca Failure Detection

Detects known power-related failures including:

- PWR_FAIL_CPU_DVDD
- PWR_FAIL_CPUVDD
- PWR_FAIL_SOCVDD
- PWR_FAIL_1V2_MOD
- PWR_FAIL_PEX_SW_0V95_MOD
- PWR_FAIL_NVVDD_GPU
- PWR_FAIL_HBMVDD_GPU
- PWR_FAIL_GPU_THERM_OVERT
- PWR_FAIL_IO_MEZZ
- PWR_FAIL_LPCAMM

Maps failures to:

- Bianca 1 (Module 0)
- Bianca 2 (Module 1)

Provides automatic corrective actions.

---

## NVIDIA Critical Event Analysis

Parses Redfish JSON event logs and identifies:

- Critical Events
- NVIDIA Driver Events
- Thermal Events
- Power Events
- GPU Faults
- NVIDIA XID Events

Examples:

- XID 163
- PS_RUN_PWR_FAULT
- PWR_FAIL_GPU_THERM_OVERT
- GPU_THERM_WARN_INT

---

## Root Cause Analysis

Correlates:

- XID Events
- Thermal Events
- PWR_FAIL Events
- GPU Failures

Generates probable root-cause information.

---

## Report Generation

Creates one report per analyzed log.

Generated reports contain:

- Failure Summary
- Bianca Analysis
- Critical Event Analysis
- Root Cause Analysis
- Recommendations

Example:

```text
reports/

├── HGX_Log_001_Report.md
├── HGX_Log_002_Report.md
├── HGX_Log_003_Report.md
```

---

## Database Storage

Stores findings in:

```text
diagnostics.db
```

for historical tracking and future analysis.

---

# Project Structure

```text
FoxconnFailureAnalyzer/

├── cli.py

├── config/
│   ├── failure_catalog.py
│   ├── power_fault_catalog.py
│   └── xid_catalog.py

├── parsers/
│   ├── log_parser.py
│   └── redfish_parser.py

├── database/
│   └── sqlite_manager.py

├── reports/
│   └── markdown_generator.py

├── generators/
│   └── fake_log_generator.py

├── logs/

├── reports/

├── diagnostics.db

├── requirements.txt

└── README.md
```

---

# Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

Windows CMD:

```cmd
venv\Scripts\activate
```

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

## Analyze a Single Log

```bash
python cli.py logs\example_log.txt
```

---

## Analyze All Logs

Place the log files in:

```text
logs/
```

Run:

```bash
python cli.py --all
```

---

## Generate Test Logs

```bash
python cli.py --generate 50000
```

---

# Supported Failure Types

## Bianca Failures

Examples:

```text
PWR_FAIL_PEX_SW_0V95_MOD_0
PWR_FAIL_PEX_SW_0V95_MOD_1
PWR_FAIL_CPUVDD_0
PWR_FAIL_CPUVDD_1
PWR_FAIL_NVVDD_GPU_0
PWR_FAIL_NVVDD_GPU_1
PWR_FAIL_NVVDD_GPU_2
PWR_FAIL_NVVDD_GPU_3
```

---

## NVIDIA XID Events

Examples:

```text
XID 163
XID 154
XID 79
XID 48
XID 43
XID 31
```

---

## Thermal Events

Examples:

```text
GPU Thermal Over Temperature

PSHC disengaged due to thermal event

GPU_THERM_WARN_INT
```

---

# Example Output

```text
=============================================
         FOXCONN FAILURE ANALYZER
 NVIDIA HGX / BIANCA Diagnostics Tool
=============================================

ID 76 | GPU_2 | XID 163 | PSHC disengaged due to thermal event

ID 79 | GPU_3 | XID 163 | PSHC disengaged due to thermal event

ID 99 | GPU_1 | XID 163 | PSHC disengaged due to thermal event
```

---

# Example Root Cause Analysis

```text
Root Cause:

GPU Thermal Event

Evidence:

- XID 163 detected
- GPU Thermal Over Temperature detected
- PS_RUN_PWR_FAULT detected

Recommended Actions:

- Verify TIM condition
- Verify cold plate pressure
- Check airflow restrictions
- Review fan speed logs
- Review GPU temperature history
```

---

# Technologies

- Python
- SQLite
- JSON
- Markdown Reporting
- Colorama
- Regular Expressions
- NVIDIA HGX Diagnostics
- Redfish Event Logs

---

# Future Enhancements

- PDF Reports
- CSV Export
- Web Dashboard
- Streamlit Interface
- Historical Trend Analysis
- Automated RCA Engine
- Email Notifications
- Failure Statistics Dashboard

---

# Disclaimer

This tool is intended to assist engineers during validation, diagnostics and troubleshooting activities.

Engineers must always follow official NVIDIA, Foxconn and customer troubleshooting procedures before making repair or replacement decisions.