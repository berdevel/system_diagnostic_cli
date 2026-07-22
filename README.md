# FOXCONN FAILURE ANALYZER

## Overview

FOXCONN Failure Analyzer is a Python-based diagnostic platform designed to automate NVIDIA HGX system troubleshooting, failure analysis, and root cause identification.

The tool parses diagnostic logs and Redfish event data, identifies hardware failures using Regex and rule-based detection, correlates findings with NVIDIA critical events, performs automated Root Cause Analysis (RCA), stores historical results in SQLite, and generates professional Markdown and HTML reports.

---

## Version

**FoxconnFailureAnalyzer v2.1**

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
- CPU Firmware Event Analysis
- Power Sequencing Failure Detection

### Root Cause Analysis

- Rule-Based RCA Engine
- Confidence Scoring
- Hardware Correlation
- Evidence Tracking
- Primary Root Cause Identification
- Secondary Findings Detection
- Corrective Action Recommendations

### Reports

- Executive Summary
- Failure Highlights
- Component Statistics
- Component Failure Details
- Critical Event Analysis
- Root Cause Analysis
- RCA Evidence
- Secondary Findings
- Markdown Report Generation
- HTML Report Generation

### Historical Database

- SQLite Storage
- Analysis History
- Serial Number History
- Root Cause Statistics
- Component Statistics
- Critical Event Tracking

### CLI Features

- Single Log Analysis
- Multiple Log Analysis
- Verbose Mode
- Historical Queries
- Top RCA Reports
- Top Component Reports
- Top Serial Reports
- Date Range Filtering

---

## Project Structure

```
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

## Historical Queries

### View Serial History

```bash
python cli.py --history P233262530256042
```

### View Serial History with Date Filter

```bash
python cli.py \
--history P233262530256042 \
--from 2026-07-01 \
--to 2026-07-31
```

---

### Top Root Causes

```bash
python cli.py --top-rca
```

### Top Root Causes by Date Range

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

---

### Historical Summary by Date Range

```bash
python cli.py \
--summary \
--from 2026-07-01 \
--to 2026-07-31
```

---

## Report Outputs

Each successful analysis generates:

```
reports/

SERIAL_Report.md

SERIAL_Report.html
```

---

## SQLite Database

The tool stores historical data in:

```
diagnostics.db
```

### Stored Information

#### Analysis History

- Serial Number
- Analysis Date
- Source Log
- Root Cause ID
- Root Cause Name
- Confidence Level
- Total Findings
- Total Critical Events

#### Component Failures

- Event ID
- Component
- Assembly
- Bianca
- Coldplate
- CX8
- Failure
- Recommendation
- Line Number

#### Critical Events

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

## Current Roadmap

### v2.2

- Serial Report
- Historical Repair Recommendations

### v2.3

- Dashboard HTML
- Charts and Visualizations

### v2.4

- Excel Export

### v3.0

- Web Interface
- Fleet Dashboard

---

## Technology Stack

- Python
- Regex
- SQLite
- Markdown
- HTML
- Redfish
- Root Cause Analysis
- OOP
- Automation

---

## Author

Juan Bernardo Perez Martinez

FOXCONN Diagnostic Automation Project