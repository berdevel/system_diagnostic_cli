# FoxconnFailureAnalyzer v2.2.4

Release Date: 2026-08-04

## New Features

- GPU Thermal Interrupt RCA.
- GPU Thermal Protection RCA.
- CX8 Root Cause Analysis workflow.
- RCA scoring engine.
- Event recency based RCA prioritization.
- Latest supporting event tracking.
- HMC Log Clear guidance across all repair workflows.
- Bianca escalation workflow after unsuccessful coldplate replacement.
- Bianca escalation workflow after unsuccessful CX8 replacement.

## Improvements

- Improved thermal event correlation.
- Improved Root Cause Analysis accuracy.
- Improved RCA evidence correlation.
- Expanded Power Fault Catalog coverage.
- Enhanced Critical Event reporting.
- Added CX8 visibility in Critical Events.
- Added Location visibility in Critical Events.
- Added timestamp validation warnings.
- Added Bus-Bar reseat workflow before Bianca replacement.
- Added CX8 reseat workflow before replacement.
- Added coldplate verification workflow before replacement.
- Improved RCA prioritization using rule priority, matched evidence and event recency.

## Reporting Enhancements

- Added RCA Evidence section.
- Added Secondary RCA Findings section.
- Added Matched Conditions visibility.
- Added RCA Score visibility.
- Added Latest Supporting Event visibility.
- Improved Critical Event summaries.
- Improved component correlation reporting.

## Power Fault Coverage

- Added detailed power rail classifications.
- Added CPUVDD fault coverage.
- Added CPU_DVDD fault coverage.
- Added SOCVDD fault coverage.
- Added C2C fault coverage.
- Added HBM power rail fault coverage.
- Added GPU Core Voltage fault coverage.
- Added PEX Switch rail fault coverage.
- Added HBI power rail fault coverage.
- Added CX8 fault coverage.
- Added 3V3 Always-On rail fault coverage.

## Repair Workflow Enhancements

### Thermal Failures

- Verify assembly before replacement.
- Verify screw torque and TIM condition.
- Retest before replacement.
- Replace coldplate only after failed retest.
- Escalate to Bianca replacement if failure persists after coldplate replacement.
- HMC Log Clear integrated into validation workflow.

### CX8 Failures

- CX8 reseat before replacement.
- Retest before replacement.
- Escalation path to Bianca replacement.
- HMC Log Clear integrated into validation workflow.

### Bianca Power Failures

- Bus-Bar reseat before replacement.
- Connector and torque verification.
- Retest before replacement.
- HMC Log Clear integrated into validation workflow.

## Fixes

- Thermal events incorrectly classified as Power Sequencing Failure.
- Incorrect RCA selection caused by exact string matching.
- Missing CX8 information in reports.
- Bianca naming inconsistencies.
- Incomplete RCA evidence generation.
- Legacy timestamp handling improvements.
- RCA rules not matching Redfish event descriptions correctly.
- Improved handling of recent events during RCA selection.

## Notes

Primary Root Cause selection now considers:

- Rule Priority
- Matched Conditions
- Evidence Correlation
- Event Recency
- Latest Supporting Event ID

More recent events are weighted higher than historical events when determining the Primary Root Cause.

IMPORTANT:

Always perform HMC Log Clear before every retest and before collecting final validation results.