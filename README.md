# FOXCONN FAILURE ANALYZER

## Overview

FOXCONN Failure Analyzer is a Python-based diagnostic platform designed to automate NVIDIA HGX system troubleshooting, failure analysis, and root cause identification.

The tool parses diagnostic logs and Redfish event data, identifies hardware failures using Regex and rule-based detection, correlates findings with NVIDIA critical events, performs automated Root Cause Analysis (RCA), stores historical results in SQLite, and generates professional Markdown and HTML reports.

---

## Version

**FoxconnFailureAnalyzer v2.2.5**

---

### What's New in v2.2.5

- Added interactive menu mode.
- Added Rich terminal user interface.
- Added RCA scoring engine.
- Added event recency weighting for RCA selection.
- Added latest supporting event tracking.
- Added potential causal event analysis.
- Added HTML dashboard cards.
- Added RCA evidence timeline.
- Added top critical events tables.
- Added HMC Log Clear guidance throughout repair workflows.
- Expanded Power Fault Catalog coverage.
- Expanded NVIDIA XID Catalog coverage.
- Improved thermal, CX8 and Bianca troubleshooting workflows.

---

## Key Features

### Diagnostic Analysis

- Automated Log Parsing
- Redfish Critical Event Analysis
- Component Failure Detection
- Bianca Failure Identification
- Coldplate Failure Identification
- CX8 Failure Identification
- GPU Thermal Event Detection
- NVIDIA XID Analysis
- CPU Firmware Failure Detection
- Power Sequencing Failure Detection

### Root Cause Analysis

- Rule-Based RCA Engine
- Confidence Scoring
- RCA Scoring Engine
- Evidence Correlation
- Event Recency Based RCA Prioritization
- Latest Supporting Event Correlation
- Potential Causal Event Detection
- Matched Condition Tracking
- Primary Root Cause Identification
- Secondary Findings Detection
- Corrective Action Recommendations
- Recurring Failure Detection
- Thermal Interrupt Detection
- Thermal Protection Correlation
- Power Distribution Fault Analysis
- CX8 Root Cause Analysis

### Reporting

- Executive Summary
- Failure Highlights
- Component Statistics
- Component Failure Analysis
- Critical Event Analysis
- Root Cause Analysis
- RCA Evidence
- RCA Evidence Timeline
- Secondary Findings
- Markdown Report Generation
- HTML Report Generation
- RCA Score
- Latest Supporting Event
- Matched Conditions
- Dashboard Summary Cards

### Historical Analytics

- SQLite Database Integration
- Analysis History
- Serial Number History
- Root Cause Statistics
- Component Statistics
- Critical Event Tracking
- Historical Trend Analysis
- Serial Intelligence Reports

### CLI Features

- Single Log Analysis
- Multi-Log Analysis
- Verbose Mode
- Date Range Filtering
- Historical Queries
- Serial Reports
- Top RCA Reports
- Top Component Reports
- Top Serial Reports
- Historical Summary Reports
- Interactive Menu Mode
- Rich Terminal Interface

---

## Project Structure

```text
FoxconnFailureAnalyzer/

├── cli.py
├── diagnostics.db
│
├── config/
│
├── parsers/
│
├── database/
│
├── reports/
│
├── logs/
│
├── generators/
│
└── tests/
```

---

## Supported Components

- Bianca#1 (Left)
- Bianca#2 (Right)
- Left Coldplate
- Right Coldplate
- Left CX8
- Right CX8
- GPUs
- CPUs

---

## Interactive Menu Mode

Launch without arguments:

```bash
python cli.py
```

Available options:

- Analyze Single Log
- Analyze All Logs
- Serial History
- Serial Report
- Top RCA
- Top Components
- Top Serials
- Historical Summary

---

## Analyze a Log

```bash
python cli.py logs\example_log.txt
```

---

## Analyze a Log (Verbose)

```bash
python cli.py logs\example_log.txt --verbose
```

---

## Analyze All Logs

```bash
python cli.py --all
```

---

## Analyze All Logs (Verbose)

```bash
python cli.py --all --verbose
```

---

## Generate Sample Logs

```bash
python cli.py --generate 50000
```

---

## Historical Database Queries

### Serial History

```bash
python cli.py --history P233262530256042
```

### Serial History with Date Filter

```bash
python cli.py \
--history P233262530256042 \
--from 2026-07-01 \
--to 2026-07-31
```

---

### Serial Intelligence Report

```bash
python cli.py --serial-report P233262530256042
```

Displays:

- Analysis History
- Root Cause History
- Component History
- Critical Event Summary
- Recurring Failure Detection
- Historical Repair Recommendation

---

### Top Root Causes

```bash
python cli.py --top-rca
```

### Top Root Causes by Date

```bash
python cli.py \
--top-rca \
--from 2026-07-01 \
--to 2026-07-31
```

---

### Top Components

```bash
python cli.py --top-components
```

---

### Top Serials

```bash
python cli.py --top-serials
```

---

### Historical Summary

```bash
python cli.py --summary
```

### Historical Summary by Date Range

```bash
python cli.py \
--summary \
--from 2026-07-01 \
--to 2026-07-31
```

---

## Reports

Each successful analysis generates:

```text
reports/

SERIAL_Report.md

SERIAL_Report.html
```

Generated Reports Include:

- Executive Summary
- Failure Highlights
- Component Statistics
- Critical Event Analysis
- Root Cause Analysis
- RCA Evidence
- RCA Evidence Timeline
- Corrective Actions
- Secondary Findings
- Location Correlation
- Coldplate Correlation
- CX8 Correlation
- Timestamp Validation Warnings
- RCA Score
- Latest Supporting Event
- Matched Conditions
- Potential Causal Events
- Dashboard Summary Cards

---

## SQLite Database

The application stores historical data in:

```text
diagnostics.db
```

### Analysis History

- Serial Number
- Analysis Date
- Source Log
- Root Cause ID
- Root Cause Name
- Confidence
- Total Findings
- Total Critical Events

### Component Failures

- Event ID
- Component
- Assembly
- Bianca
- Coldplate
- CX8
- Failure
- Recommendation
- Line Number

### Critical Events

- Event ID
- Timestamp
- Severity
- GPU
- CPU
- Bianca
- Assembly
- Coldplate
- XID
- Failure
- Recommendation

---

## Supported Detections

### Power Rail Failures

- CPUVDD
- CPU_DVDD
- SOCVDD
- C2C
- PEX Switch 0.95V
- NVVDD GPU Core
- HBMVDD
- HBMVDDQ
- HBMVPP
- HBI
- PEXDVDD
- FBVDDP
- FBVDDQ
- 1V2 Rail
- 1V8 Rail
- 12V Rail
- 3V3 Always-On Rail

### Bianca Failures

- PWR_FAIL_CPU
- PWR_FAIL_SOC
- PWR_FAIL_PEX_SW
- PWR_FAIL_IO_MEZZ
- PWR_FAIL_NVVDD
- PWR_FAIL_HBMVDD

### Thermal Events

- GPU Thermal Over Temperature
- GPU Thermal Warning Events
- GPU Thermal Interrupt Events (THERM_OVERT_INT)
- GPU Thermal Protection Events (XID 163)
- Thermal Shutdown Events

### CPU Firmware Events

- AP0_PRIMARY_AuthenticateError
- AP0_SECONDARY_AuthenticateError
- ErrorAuthApFw
- Firmware Authentication Failures
- Firmware Verification Failures

### NVIDIA Events

- XID 8
- XID 11
- XID 13
- XID 25
- XID 31
- XID 32
- XID 37
- XID 38
- XID 43
- XID 45
- XID 46
- XID 48
- XID 54
- XID 60
- XID 62
- XID 63
- XID 64
- XID 74
- XID 79
- XID 92
- XID 94
- XID 95
- XID 109
- XID 110
- XID 119
- XID 120
- XID 121
- XID 136
- XID 137
- XID 140
- XID 143
- XID 144
- XID 145
- XID 146
- XID 147
- XID 148
- XID 149
- XID 150
- XID 154
- XID 156
- XID 158
- XID 163
- XID 164
- XID 165
- XID 171
- XID 172

---

## Technology Stack

- Python
- SQLite
- Regex
- OOP
- Markdown
- HTML
- Rich
- Redfish
- NVIDIA Diagnostics
- Root Cause Analysis
- Automation

---

## Troubleshooting Workflows

### Thermal Failures

1. Verify coldplate installation.
2. Verify coldplate screw torque.
3. Verify TIM condition and coldplate contact.
4. Correct installation issues if identified.
5. Perform HMC Log Clear.
6. Execute validation and retest.
7. Replace the affected coldplate only if the failure reoccurs after retest.
8. Perform HMC Log Clear.
9. Execute validation and retest.
10. If the issue persists, replace the Bianca assembly associated with the affected GPU.
11. Perform HMC Log Clear.
12. Execute final validation.

### CX8 / IO Mezzanine Failures

1. Perform complete CX8 reseat.
2. Verify connector engagement and retention mechanism.
3. Perform HMC Log Clear.
4. Execute validation and retest.
5. Replace the affected CX8 only if the failure reoccurs after retest.
6. Perform HMC Log Clear.
7. Execute validation and retest.
8. If the issue persists, replace the Bianca assembly associated with the affected CX8.
9. Perform HMC Log Clear.
10. Execute final validation.

### Bianca Power Distribution Faults

1. Perform complete Bus-Bar reseat.
2. Verify connector engagement and torque.
3. Perform HMC Log Clear.
4. Execute validation and retest.
5. Replace the affected Bianca only if the failure reoccurs after retest.
6. Perform HMC Log Clear.
7. Execute final validation.

---

## RCA Prioritization

Primary Root Cause selection considers:

- RCA Priority
- Matched Evidence
- Matched Conditions
- RCA Score
- Event Recency
- Latest Supporting Event ID
- Potential Causal Events

More recent events are weighted higher than historical events when selecting the Primary Root Cause.

---

## Validation Notice

Always perform HMC Log Clear before every retest and before collecting final validation results.

---

## Roadmap

### v2.3

- Dashboard HTML
- Graphs and Visualizations

### v2.4

- Excel Export
- PDF Reports

### v2.5

- Fleet Summary
- Fleet Analytics

### v3.0

- Web Dashboard
- REST API

---

## Author

Juan Bernardo Perez Martinez

FOXCONN Diagnostic Automation Project