FOXCONN FAILURE ANALYZER
NVIDIA HGX / BIANCA DIAGNOSTIC PLATFORM

==================================================

DESCRIPTION

FOXCONN Failure Analyzer is an automated diagnostic
and Root Cause Analysis (RCA) platform for NVIDIA
HGX/Bianca systems.

The tool analyzes system logs and Redfish event logs,
detects hardware failures, correlates critical events,
performs Root Cause Analysis, stores historical results
in SQLite, and generates professional reports.

==================================================

KEY FEATURES

Diagnostic Analysis

- Bianca Failure Detection
- Coldplate Failure Detection
- CX8 Failure Detection
- NVIDIA XID Analysis
- GPU Thermal Event Detection
- CPU Firmware Failure Detection
- Power Sequencing Failure Detection
- Critical Redfish Event Analysis

Root Cause Analysis

- Rule-Based RCA Engine
- Confidence Scoring
- Evidence Correlation
- Corrective Action Recommendations
- Primary and Secondary Findings

Reporting

- Failure Highlights
- Component Statistics
- Critical Event Analysis
- Root Cause Analysis
- Markdown Reports
- HTML Reports

Historical Analytics

- SQLite Database
- Analysis History
- Serial History
- Root Cause Statistics
- Component Statistics

==================================================

FOLDER STRUCTURE

FoxconnFailureAnalyzer/

│
├── FoxconnFailureAnalyzer.exe
├── diagnostics.db
├── logs/
├── reports/
└── README.txt

==================================================

ANALYZE A SINGLE LOG

FoxconnFailureAnalyzer.exe logs\example_log.txt

==================================================

ANALYZE A SINGLE LOG (VERBOSE)

Shows all findings and critical events.

FoxconnFailureAnalyzer.exe logs\example_log.txt --verbose

==================================================

ANALYZE ALL LOGS

1. Copy logs into the logs folder

2. Run:

FoxconnFailureAnalyzer.exe --all

==================================================

ANALYZE ALL LOGS (VERBOSE)

FoxconnFailureAnalyzer.exe --all --verbose

==================================================

VIEW SERIAL HISTORY

FoxconnFailureAnalyzer.exe --history SERIAL_NUMBER

Example:

FoxconnFailureAnalyzer.exe --history P233262530256042

==================================================

TOP ROOT CAUSES

FoxconnFailureAnalyzer.exe --top-rca

==================================================

TOP COMPONENT FAILURES

FoxconnFailureAnalyzer.exe --top-components

==================================================

MOST PROBLEMATIC SERIALS

FoxconnFailureAnalyzer.exe --top-serials

==================================================

GENERATE SAMPLE LOGS

FoxconnFailureAnalyzer.exe --generate 50000

==================================================

REPORTS

Each analyzed log generates:

- Markdown Report (.md)
- HTML Report (.html)

Example:

reports/

P233262530256042_Report.md

P233262530256042_Report.html

==================================================

DATABASE

diagnostics.db

Stored Information

- Serial Numbers
- Analysis History
- Root Causes
- Findings
- Critical Events
- Components
- Corrective Actions
- Confidence Levels

==================================================

SUPPORTED COMPONENTS

- Bianca 1
- Bianca 2
- Left Coldplate
- Right Coldplate
- CX8 Adapters
- GPUs
- CPUs

==================================================

SUPPORTED DETECTIONS

Bianca Failures

- PWR_FAIL_CPU
- PWR_FAIL_SOC
- PWR_FAIL_PEX_SW
- PWR_FAIL_IO_MEZZ
- PWR_FAIL_NVVDD
- PWR_FAIL_HBMVDD

Coldplate Failures

- GPU Thermal Over Temperature
- GPU Thermal Warning Events
- Thermal Shutdown Events

CPU Firmware Events

- AuthenticateError
- AP0_PRIMARY_AuthenticateError
- AP0_SECONDARY_AuthenticateError
- ErrorAuthApFw

NVIDIA Events

- XID 163
- XID 154
- XID 79
- XID 48
- XID 31

==================================================

OUTPUT

Executive Summary

- Serial Number
- Failure Counts
- Critical Event Counts
- Root Cause
- Confidence
- Recommended Action

Detailed Analysis

- Failure Highlights
- Component Statistics
- Failure Details
- Critical Events
- RCA Evidence
- Secondary Findings

==================================================

VERSION

FoxconnFailureAnalyzer v2.0

==================================================

AUTHOR

Juan Bernardo Perez Martinez

FOXCONN Diagnostic Automation Project

==================================================