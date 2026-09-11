FOXCONN FAILURE ANALYZER 
NVIDIA HGX / BIANCA DIAGNOSTIC PLATFORM 

VERSION 2.2.6 

================================================== 

WHAT'S NEW IN V2.2.6 

- Added Standalone Technical LOG Report Generator. 
- Added Standalone HTML Dashboard Report Generator. 
- Removed Markdown Report Dependency. 
- Added HMC Failure Events Reporting. 
- Added HMC Event Details Reporting. 
- Added HMC Event Descriptions Reporting. 
- Added Critical Event Details Reporting. 
- Added Critical Event Descriptions Reporting. 
- Added Affected Components Dashboard Section. 
- Added Recommended Actions Dashboard Section. 
- Added Primary RCA Hero Panel. 
- Added HTML Dashboard KPI Cards. 
- Added Automatic HTML Report Launch After Analysis. 
- Improved Report Architecture and Maintainability. 

================================================== 

DESCRIPTION FOXCONN 

Failure Analyzer automates NVIDIA HGX system diagnostics and Root Cause Analysis. The platform analyzes HMC logs and NVIDIA Redfish Critical Events, stores historical analysis results, detects recurring failures, correlates evidence, identifies Root Causes, and generates Technical LOG and HTML Dashboard reports. 

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
- Technical LOG Reports 
- HTML Dashboard Reports 
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
│ ├── SERIAL_Report.log 
│ └── SERIAL_Report.html 
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

FoxconnFailureAnalyzer.exe ^ --summary ^ --from 2026-07-01 ^ --to 2026-07-31 

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

Generated Files 
- Technical LOG Report (.log) 
- HTML Dashboard Report (.html) 

Technical LOG Report Includes 

- Root Cause Analysis 
- Recommended Actions 
- Potential Causal Events 
- Component Summary 
- Top Critical Events 
- Critical Event Details 
- Critical Event Descriptions 
- HMC Failure Events 
- HMC Event Descriptions 

HTML Dashboard Report 

Includes 

- KPI Dashboard Cards 
- Primary Root Cause Hero Panel 
- Recommended Actions Section 
- Affected Components 
- Top Findings 
- Top Critical Events 
- HMC Failure Events 
- HMC Event Details 
- Critical Event Details 
- Critical Event Descriptions 

Location 

reports\ 

================================================== 

HTML DASHBOARD 

The HTML Dashboard automatically opens after successful analysis. 

Dashboard Sections 

- KPI Summary Cards 
- Primary Root Cause 
- Recommended Actions 
- Affected Components 
- Top Findings 
- Top Critical Events 
- HMC Failure Events 
- HMC Event Details 
- Critical Event Details 
- Critical Event Descriptions 

================================================== 

REPAIR WORKFLOWS THERMAL FAILURES 

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

REPORT ARCHITECTURE 

The platform generates two independent reports from the same diagnostic dataset. 

Technical LOG Report 

Designed for: 

- Failure Analysis Engineers 
- Repair Validation 
- Ticket Attachments 
- Historical Review 

HTML Dashboard Report 

Designed for: 

- Fast Troubleshooting 
- RCA Review 
- Manufacturing Support 
- Executive Summaries 

================================================== 

RCA PRIORITIZATION 

Primary Root Cause Selection 

Considers 

- Rule Priority 
- Matched Conditions 
- Evidence Correlation 
- RCA Score 
- Event Recency 
- Latest Supporting Event ID 
- Potential Causal Events Recent events are weighted higher than historical events when determining the Primary Root Cause. 

================================================== 

IMPORTANT 

Always perform HMC Log Clear before every retest and before collecting final validation results. 

================================================== 

VERSION INFORMATION 

Application Version 

- FoxconnFailureAnalyzer v2.2.6 Catalog Version 
- RCA Catalog v2.2.6 Status 
- Stable Internal Release 

================================================== 

AUTHOR 

Juan Bernardo Perez Martinez 

FOXCONN 

Diagnostic Automation Project 

==================================================