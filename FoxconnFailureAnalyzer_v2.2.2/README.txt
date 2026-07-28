FOXCONN FAILURE ANALYZER
NVIDIA HGX / BIANCA DIAGNOSTIC PLATFORM

VERSION 2.2.3

==================================================

WHAT'S NEW IN V2.2.3

- Improved thermal event correlation
- Added GPU Thermal Interrupt RCA
- Added GPU Thermal Protection RCA
- Added CX8 correlation and RCA workflow
- Added Location visibility in Critical Events
- Added CX8 visibility in Critical Events
- Added RCA Evidence section
- Added Timestamp Validation Warnings
- Added Bus-Bar reseat workflow before Bianca replacement
- Added CX8 reseat workflow before replacement
- Added Coldplate verification workflow before replacement

==================================================

DESCRIPTION

FOXCONN Failure Analyzer automates NVIDIA HGX
system diagnostics and Root Cause Analysis.

The tool analyzes logs and Redfish critical events,
stores historical analysis results, detects recurring
failures, and generates professional reports.

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
- Historical Database
- Serial Reports
- Historical Statistics
- Date Filtering
- Markdown Reports
- HTML Reports

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

Provides:

- Analysis History
- Root Cause History
- Component History
- Critical Event Summary
- Recurring Failure Detection

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

REPORTS

Generated:

- Markdown Report (.md)
- HTML Report (.html)
- RCA Evidence
- Component Correlation
- Coldplate Correlation
- CX8 Correlation
- Location Correlation
- Timestamp Validation Warnings

Location:

reports\

==================================================

REPAIR WORKFLOWS

THERMAL FAILURES

1. Verify coldplate installation.
2. Verify coldplate screw torque.
3. Verify TIM condition and contact pressure.
4. Correct assembly issues if found.
5. Execute validation and retest.
6. Replace the affected coldplate only if the issue reoccurs.

--------------------------------------------------

CX8 FAILURES

1. Perform complete CX8 reseat.
2. Verify connector engagement.
3. Execute validation and retest.
4. Replace the affected CX8 only if the issue reoccurs.

--------------------------------------------------

BIANCA POWER FAULTS

1. Perform complete Bus-Bar reseat.
2. Verify connector engagement and torque.
3. Execute validation and retest.
4. Replace the affected Bianca only if the issue reoccurs.

==================================================

DATABASE

diagnostics.db

Stores:

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

AUTHOR

Juan Bernardo Perez Martinez

FOXCONN Diagnostic Automation Project

==================================================