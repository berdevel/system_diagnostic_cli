# FOXCONN FAILURE ANALYZER

## Overview

FOXCONN Failure Analyzer is a Python-based diagnostic platform designed to automate NVIDIA HGX system troubleshooting, failure analysis, and root cause identification.

The tool parses diagnostic logs and Redfish event data, identifies hardware failures using Regex and rule-based detection, correlates findings with NVIDIA critical events, performs automated Root Cause Analysis (RCA), stores historical results in SQLite, and generates professional Markdown and HTML reports.

---

## Version

**FoxconnFailureAnalyzer v2.2.3**

---

### What's New in v2.2.3

- Improved thermal event correlation.
- Added GPU Thermal Interrupt RCA.
- Added GPU Thermal Protection RCA.
- Added CX8 visibility in Critical Events.
- Added Location visibility in Critical Events.
- Improved RCA evidence generation.
- Added timestamp validation warnings.
- Added Bus-Bar reseat workflow before Bianca replacement.
- Added CX8 reseat workflow before replacement.
- Added coldplate verification workflow before replacement.

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
- Evidence Correlation
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
- Secondary Findings
- Markdown Report Generation
- HTML Report Generation

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

- Bianca 1
- Bianca 2
- Left Coldplate
- Right Coldplate
- CX8
- GPUs
- CPUs

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
- Corrective Actions
- Secondary Findings
- Location Correlation
- Coldplate Correlation
- CX8 Correlation
- Timestamp Validation Warnings

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

### NVIDIA Events

- XID 163
- XID 154
- XID 149
- XID 79
- XID 48
- XID 31

---

## Technology Stack

- Python
- SQLite
- Regex
- OOP
- Markdown
- HTML
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
5. Execute validation and retest.
6. Replace the affected coldplate only if the failure reoccurs after retest.

### CX8 / IO Mezzanine Failures

1. Perform complete CX8 reseat.
2. Verify connector engagement and retention mechanism.
3. Execute validation and retest.
4. Replace the affected CX8 only if the failure reoccurs after retest.

### Bianca Power Distribution Faults

1. Perform complete Bus-Bar reseat.
2. Verify connector engagement and torque.
3. Execute validation and retest.
4. Replace the affected Bianca only if the failure reoccurs after retest.

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