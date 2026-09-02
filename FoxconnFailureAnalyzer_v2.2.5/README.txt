FOXCONN FAILURE ANALYZER
NVIDIA HGX / BIANCA DIAGNOSTIC PLATFORM

VERSION 2.2.5

==================================================

WHAT'S NEW IN V2.2.5

- Interactive Menu Mode
- Rich Terminal User Interface
- RCA Scoring Engine
- Event Recency Based RCA Prioritization
- Latest Supporting Event Tracking
- Potential Causal Event Analysis
- HTML Dashboard Cards
- RCA Evidence Timeline
- Top Critical Events Tables
- HMC Log Clear Guidance Across All Repair Workflows
- Expanded Power Fault Catalog Coverage
- Expanded NVIDIA XID Catalog Coverage
- Improved Thermal, CX8 and Bianca Troubleshooting Workflows

==================================================

DESCRIPTION

FOXCONN Failure Analyzer automates NVIDIA HGX
system diagnostics and Root Cause Analysis.

The tool analyzes logs and Redfish critical events,
stores historical analysis results, detects recurring
failures, correlates evidence, and generates
professional Markdown and HTML reports.

==================================================

FEATURES

- Bianca Failure Detection
- Coldplate Failure Detection
- CX8 Failure Detection
- NVIDIA XID Detection
- GPU Thermal Event Detection
- GPU Thermal Interrupt Detection
- GPU Thermal Protection Detection
- CPU Firmware Event Analysis
- Redfish Critical Event Analysis
- Root Cause Analysis (RCA)
- RCA Evidence Correlation
- RCA Scoring Engine
- Event Recency Based RCA Prioritization
- Latest Supporting Event Correlation
- Potential Causal Event Detection
- Historical Database
- Serial Reports
- Historical Statistics
- Date Filtering
- Markdown Reports
- HTML Reports
- Rich Terminal Interface
- Interactive Menu Mode
- Power Rail Failure Classification
- HMC Log Clear Workflow Guidance

==================================================

INTERACTIVE MENU MODE

Run without parameters:

FoxconnFailureAnalyzer.exe

Available Functions

- Analyze Single Log
- Analyze All Logs
- Serial History
- Serial Report
- Top RCA
- Top Components
- Top Serials
- Historical Summary

==================================================

FOLDER STRUCTURE

FoxconnFailureAnalyzer/

├── FoxconnFailureAnalyzer.exe
├── diagnostics.db
├── logs/
├── reports/
└── README.txt

==================================================

ANALYZE A SINGLE LOG

FoxconnFailureAnalyzer.exe logs\logfile.txt

==================================================

ANALYZE A SINGLE LOG (VERBOSE)

FoxconnFailureAnalyzer.exe logs\logfile.txt --verbose

==================================================

ANALYZE ALL LOGS

FoxconnFailureAnalyzer.exe --all

==================================================

ANALYZE ALL LOGS (VERBOSE)

FoxconnFailureAnalyzer.exe --all --verbose

==================================================

GENERATE SAMPLE LOGS

FoxconnFailureAnalyzer.exe --generate 50000

==================================================

SERIAL HISTORY

FoxconnFailureAnalyzer.exe --history SERIAL_NUMBER

Example

FoxconnFailureAnalyzer.exe --history P233262530256042

==================================================

SERIAL REPORT

FoxconnFailureAnalyzer.exe --serial-report SERIAL_NUMBER

Provides

- Analysis History
- Root Cause History
- Component History
- Critical Event Summary
- Recurring Failure Detection
- Historical Repair Recommendation

==================================================

TOP ROOT CAUSES

FoxconnFailureAnalyzer.exe --top-rca

==================================================

TOP COMPONENT FAILURES

FoxconnFailureAnalyzer.exe --top-components

==================================================

TOP SERIAL NUMBERS

FoxconnFailureAnalyzer.exe --top-serials

==================================================

DATABASE SUMMARY

FoxconnFailureAnalyzer.exe --summary

==================================================

DATE FILTERS

Example

FoxconnFailureAnalyzer.exe ^
--summary ^
--from 2026-07-01 ^
--to 2026-07-31

==================================================

ADVANCED MODE

Analyze Log

FoxconnFailureAnalyzer.exe logfile.txt

Analyze All Logs

FoxconnFailureAnalyzer.exe --all

Top RCA

FoxconnFailureAnalyzer.exe --top-rca

Historical Summary

FoxconnFailureAnalyzer.exe --summary

==================================================

REPORTS

Generated

- Markdown Report (.md)
- HTML Report (.html)
- Executive Summary
- RCA Evidence
- RCA Evidence Timeline
- RCA Score
- Latest Supporting Event
- Potential Causal Events
- Secondary RCA Findings
- Component Correlation
- Coldplate Correlation
- CX8 Correlation
- Location Correlation
- Timestamp Validation Warnings
- Dashboard Summary Cards

Location

reports\

==================================================

REPAIR WORKFLOWS

THERMAL FAILURES

1. Verify coldplate installation.
2. Verify coldplate screw torque.
3. Verify TIM condition and contact pressure.
4. Correct assembly issues if found.
5. Perform HMC Log Clear.
6. Execute validation and retest.
7. Replace the affected coldplate only if the issue reoccurs.
8. Perform HMC Log Clear.
9. Execute validation and retest.
10. If the issue persists, replace the Bianca assembly associated with the affected GPU.
11. Perform HMC Log Clear.
12. Execute final validation.

--------------------------------------------------

CX8 FAILURES

1. Perform complete CX8 reseat.
2. Verify connector engagement and retention.
3. Perform HMC Log Clear.
4. Execute validation and retest.
5. Replace the affected CX8 only if the issue reoccurs.
6. Perform HMC Log Clear.
7. Execute validation and retest.
8. If the issue persists, replace the Bianca assembly associated with the affected CX8.
9. Perform HMC Log Clear.
10. Execute final validation.

--------------------------------------------------

BIANCA POWER FAULTS

1. Perform complete Bus-Bar reseat.
2. Verify connector engagement and torque.
3. Perform HMC Log Clear.
4. Execute validation and retest.
5. Replace the affected Bianca only if the issue reoccurs.
6. Perform HMC Log Clear.
7. Execute final validation.

==================================================

DATABASE

diagnostics.db

Stores

- Analysis History
- Serial History
- Root Causes
- Component Failures
- Critical Events
- Historical Statistics

==================================================

SUPPORTED COMPONENTS

- Bianca#1 (Left)
- Bianca#2 (Right)
- Left Coldplate
- Right Coldplate
- Left CX8
- Right CX8
- GPUs
- CPUs

==================================================

RCA PRIORITIZATION

Primary Root Cause selection considers

- Rule Priority
- Matched Conditions
- Evidence Correlation
- RCA Score
- Event Recency
- Latest Supporting Event ID
- Potential Causal Events

Recent events are weighted higher than
historical events when determining the
Primary Root Cause.

==================================================

IMPORTANT

Always perform HMC Log Clear before every
retest and before collecting final validation
results.

==================================================

AUTHOR

Juan Bernardo Perez Martinez

FOXCONN Diagnostic Automation Project

==================================================