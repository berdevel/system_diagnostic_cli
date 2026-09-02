# FoxconnFailureAnalyzer v2.2.5

Release Date: 2026-09-02

## New Features

- Interactive Menu Mode.
- Rich Terminal User Interface.
- RCA Scoring Engine.
- Event Recency Based RCA Prioritization.
- Latest Supporting Event Tracking.
- Potential Causal Event Analysis.
- Dashboard Summary Cards in HTML Reports.
- RCA Evidence Timeline.
- Top Critical Events Tables.
- Expanded NVIDIA XID Catalog.
- Expanded Power Fault Catalog Coverage.

## Improvements

- Improved thermal event correlation.
- Improved Root Cause Analysis accuracy.
- Improved RCA evidence correlation.
- Enhanced Critical Event reporting.
- Added CX8 visibility in Critical Events.
- Added Location visibility in Critical Events.
- Added Timestamp Validation Warnings.
- Added Bus-Bar reseat workflow before Bianca replacement.
- Added CX8 reseat workflow before replacement.
- Added coldplate verification workflow before replacement.
- Added HMC Log Clear guidance throughout all repair workflows.
- Improved RCA prioritization using rule priority, matched evidence and event recency.
- Added confidence, score and supporting event visibility throughout reports and console output.

## Reporting Enhancements

- Added Executive Summary section.
- Added RCA Evidence section.
- Added RCA Evidence Timeline.
- Added Secondary RCA Findings section.
- Added Matched Conditions visibility.
- Added RCA Score visibility.
- Added Latest Supporting Event visibility.
- Added Potential Causal Events section.
- Added Dashboard Summary Cards.
- Added Top Critical Events table.
- Added Critical Event Details table.
- Added Event Description table.
- Improved component correlation reporting.
- Improved report readability and troubleshooting flow.

## Root Cause Analysis Enhancements

Primary Root Cause selection now considers:

- Rule Priority
- Matched Conditions
- Evidence Correlation
- RCA Score
- Event Recency
- Latest Supporting Event ID
- Potential Causal Events

More recent events are weighted higher than historical events when determining the Primary Root Cause.

## Power Fault Coverage

Added detailed classification and troubleshooting guidance for:

- CPUVDD
- CPU_DVDD
- SOCVDD
- C2C
- PEX Switch 0.95V Rail
- NVVDD GPU Core
- HBMVDD
- HBMVDDQ
- HBMVPP
- HBI
- PEXDVDD
- FBVDDP
- FBVDDQ
- LPCAMM
- 1V2 Rail
- 1V8 Rail
- 12V Rail
- 3V3 Always-On Rail
- IO Mezzanine / CX8
- Thermal Protection Events

## NVIDIA XID Coverage

Added coverage and recommendations for:

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

## Repair Workflow Enhancements

### Thermal Failures

- Verify coldplate assembly.
- Verify coldplate screw torque.
- Verify TIM condition and contact pressure.
- Perform HMC Log Clear.
- Execute validation and retest.
- Replace affected coldplate only after failed retest.
- Escalate to Bianca replacement if the issue persists after coldplate replacement.
- Perform final validation after repair.

### CX8 Failures

- Perform complete CX8 reseat.
- Verify connector engagement and retention.
- Perform HMC Log Clear.
- Execute validation and retest.
- Replace affected CX8 only after failed retest.
- Escalate to Bianca replacement if the issue persists after CX8 replacement.
- Perform final validation after repair.

### Bianca Power Distribution Failures

- Perform complete Bus-Bar reseat.
- Verify connector engagement and torque.
- Perform HMC Log Clear.
- Execute validation and retest.
- Replace affected Bianca only after failed retest.
- Perform final validation after repair.

## Terminal User Interface

- Added Rich powered menu system.
- Added Rich analysis summary tables.
- Added Rich RCA panels.
- Added Top Findings table.
- Added Generated Outputs table.
- Improved readability and navigation.
- Added interactive execution mode without command line arguments.

## Fixes

- Thermal events incorrectly classified as Power Sequencing Failure.
- Incorrect RCA selection caused by exact string matching.
- Missing CX8 information in reports.
- Missing Location information in Critical Events.
- Incomplete RCA evidence generation.
- Legacy timestamp handling improvements.
- RCA rules not matching Redfish event descriptions correctly.
- Improved handling of recent events during RCA selection.
- Improved component visibility in reports.
- Improved RCA support evidence correlation.

## Validation Notice

IMPORTANT:

Always perform HMC Log Clear before every retest and before collecting final validation results.

## Version Information

Application Version:

- FoxconnFailureAnalyzer v2.2.5

Catalog Version:

- RCA Catalog v2.2.4

Status:

- Stable Internal Release