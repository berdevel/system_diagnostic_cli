FOXCONN FAILURE ANALYZER
NVIDIA HGX / BIANCA DIAGNOSTIC PLATFORM

VERSION 2.1

==================================================

DESCRIPTION

FOXCONN Failure Analyzer automates NVIDIA HGX
system diagnostics and Root Cause Analysis.

The tool analyzes logs and critical Redfish events,
identifies hardware failures, stores historical data,
and generates professional reports.

==================================================

FEATURES

- Bianca Failure Detection
- Coldplate Failure Detection
- CX8 Failure Detection
- NVIDIA XID Detection
- CPU Firmware Event Analysis
- Redfish Critical Event Analysis
- Root Cause Analysis (RCA)
- Markdown Reports
- HTML Reports
- SQLite Historical Database
- Historical Statistics
- Date Range Filtering

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

Generated Reports

- Markdown Report (.md)
- HTML Report (.html)

Location

reports\

==================================================

DATABASE

diagnostics.db

Stored Information

- Analysis History
- Root Causes
- Component Failures
- Critical Events
- Serial History
- Statistics

==================================================

SUPPORTED COMPONENTS

- Bianca 1
- Bianca 2
- Left Coldplate
- Right Coldplate
- CX8
- GPUs
- CPUs

==================================================

AUTHOR

Juan Bernardo Perez Martinez

FOXCONN Diagnostic Automation Project

==================================================