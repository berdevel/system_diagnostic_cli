# FOXCONN FAILURE ANALYZER

## Overview

FOXCONN Failure Analyzer is a Python-based diagnostic platform designed to automate NVIDIA HGX system troubleshooting, failure analysis, and root cause identification.

The tool parses diagnostic logs and Redfish event data, identifies hardware failures using Regex and rule-based detection, correlates findings with NVIDIA critical events, performs automated Root Cause Analysis (RCA), stores historical results in SQLite, and generates professional Markdown and HTML reports.

---

## Key Features

### Diagnostic Analysis

- Automated log parsing
- Redfish Critical Event Analysis
- Component Failure Detection
- Bianca Failure Identification
- Coldplate Failure Identification
- CX8 Failure Identification
- GPU Thermal Event Detection
- NVIDIA XID Analysis
- CPU Firmware Failure Detection
- Power Sequencing Failure Detection
- Rule-Based Hardware Correlation

### Root Cause Analysis

- Rule-Based RCA Engine
- Confidence Scoring
- Evidence Correlation
- Primary Root Cause Identification
- Secondary Findings Detection
- Corrective Action Recommendations
- Failure-to-Component Mapping

### Reporting

- Executive Summary
- Failure Highlights
- Component Statistics
- Component Failure Analysis
- Critical Event Analysis
- Root Cause Analysis
- Evidence Supporting RCA
- Secondary Findings
- Markdown Report Generation
- HTML Report Generation

### Historical Analytics

- SQLite Database Integration
- Analysis History
- Serial Number History
- Root Cause Statistics
- Component Failure Statistics
- Critical Event Tracking
- Historical Trend Analysis

### CLI Features

- Standard Analysis Mode
- Verbose Analysis Mode
- Historical Queries
- Top Root Cause Reporting
- Top Component Reporting
- Top Serial Number Reporting
- Single Log Processing
- Multi-Log Processing

---

## Project Structure

```text
FoxconnFailureAnalyzer/

├── cli.py
├── diagnostics.db
│
├── config/
│   ├── power_fault_catalog.py
│   ├── xid_catalog.py
│   ├── cpu_firmware_catalog.py
│   └── ...
│
├── parsers/
│   ├── log_parser.py
│   ├── redfish_parser.py
│   └── root_cause_analyzer.py
│
├── database/
│   └── sqlite_manager.py
│
├── reports/
│   ├── markdown_generator.py
│   ├── *.md
│   └── *.html
│
├── generator*/
│   └── fake_log_generator.py
│
*── logs/
│
└── tests/
```

---

##*Supported Components

### HGX Comp*nents

- Bianca 1
- Bianca 2
- Lef* Coldplate
- Right Coldplate
- CX8*Adapters
- GPUs
- CPUs

### Assemb*ies

- Bianca#1 Assembly
- Bianca#* Assembly

---

## Supported Event*Sources

- Diagnostic Logs
- Redfi*h Events
- NVIDIA XID Events
- Pow*r Sequencing Events
- Thermal Even*s
- CPU Firmware Events

---

## R*n Analysis

Analyze a single log:
*```bash
python cli.py logs\example*log.txt
```

---

## Run Analysis *Verbose)

Displays all detected fa*lures and critical events.

```bas*
python cli.py logs\example_log.tx* --verbose
```

---

## Analyze Al* Logs

Process every log file foun* inside the logs directory.

```ba*h
python cli.py --all
```

---

##*Analyze All Logs (Verbose)

```bas*
python cli.py --all --verbose
```*
---

## Generate Sample Logs

Gen*rate synthetic logs for testing.

*``bash
python cli.py --generate 50*00
```

---

## Historical Databas* Queries

### View Serial History
*```bash
python cli.py --history P2*3262530256042
```

Example Output:*
```text
Date       : 2026-07-20
R*ot Cause : PEX Switch 0.95V Rail F*ilure - Bianca 2
Confidence : HIGH*```

---

### View Top Root Causes*
```bash
python cli.py --top-rca
`*`

Example Output:

```text
TOP RO*T CAUSES

68   PEX Switch 0.95V Ra*l Failure - Bianca 2
23   GPU Ther*al Event
12   CX8 Failure
```

---*
### View Top Components

```bash
*ython cli.py --top-components
```
*Example Output:

```text
TOP COMPO*ENT FAILURES

187   Bianca
44    C*ldplate
19    CX8
```

---

### Vi*w Most Problematic Serials

```bas*
python cli.py --top-serials
```

*xample Output:

```text
MOST PROBL*MATIC SERIALS

12   P2332625302560*2
9    P233262530111010
8    P2332*2530555123
```

---

## Report Out*uts

Each successful analysis gene*ates:

```text
reports/

├── SERIA*_Report.md
└── SERIAL_Report.html
*``

Generated Reports Include:

- *ystem Information
- Failure Highli*hts
- Component Failure Summary
- *omponent Statistics
- Critical Eve*t Analysis
- Root Cause Analysis
-*Evidence Supporting RCA
- Correcti*e Actions
- Secondary Findings

--*

## SQLite Database

Historical a*alysis data is automatically store* in:

```text
diagnostics.db
```

*## Stored Information

#### Analys*s History

- Serial Number
- Analy*is Date
- Source Log
- Root Cause *D
- Root Cause Name
- Confidence L*vel
- Total Findings
- Total Criti*al Events

#### Component Failures*
- Event ID
- Component
- Assembly*- Bianca
- Coldplate
- CX8
- Failu*e
- Recommendation
- Line Number

*### Critical Events

- Event ID
- *imestamp
- Severity
- GPU
- CPU
- *ianca
- Assembly
- Coldplate
- XID*- Failure
- Recommendation

---

#* Supported Detections

### Bianca *ailures

- PWR_FAIL_CPU
- PWR_FAIL*SOC
- PWR_FAIL_PEX_SW
- PWR_FAIL_I*_MEZZ
- PWR_FAIL_NVVDD
- PWR_FAIL_*BMVDD

### Coldplate Failures

- G*U Thermal Over Temperature
- GPU T*ermal Warning Events
- Thermal Shu*down Events

### CPU Firmware Even*s

- AP0_PRIMARY_AuthenticateError*- AP0_SECONDARY_AuthenticateError
* ErrorAuthApFw

### NVIDIA Events
*- XID 163
- XID 154
- XID 79
- XID*48
- XID 31

---

## Example Analy*is Workflow

```text
Log File
    *
Log Parser
    ↓
Redfish Parser
 *  ↓
Failure Detection
    ↓
Critic*l Event Correlation
    ↓
Root Cau*e Analysis
    ↓
SQLite Storage
  * ↓
Markdown Report
    ↓
HTML Repo*t
```

---

## Technology Stack

-*Python
- Regular Expressions (Rege*)
- SQLite
- Object-Oriented Progr*mming (OOP)
- Markdown
- HTML
- Ro*t Cause Analysis
- NVIDIA Diagnostics
- Redfish
- Automation

---

## Business Value

FOXCONN Failure Analyzer reduces troubleshooting time by automatically correlating failures, critical events, and hardware symptoms into a structured Root Cause Analysis workflow.

The solution provides:

- Faster Diagnostics
- Standardized Reporting
- Historical Trend Analysis
- Failure Correlation
- Automated Recommendations
- Manufacturing Validation Support
- QA Engineering Support
- Test Engineering Support
- Historical Failure Intelligence

---

## Version

**FoxconnFailureAnalyzer v2.0**

---

## Author

**Juan Bernardo Perez Martinez**

FOXCONN Diagnostic Automation Project