FOXCONN FAILURE ANALYZER
NVIDIA HGX / BIANCA DIAGNOSTIC TOOL

========================================

DESCRIPTION

This tool analyzes NVIDIA HGX/Bianca logs and Redfish event logs.

It can:

- Detect Bianca power failures
- Detect NVIDIA XID events
- Detect thermal events
- Detect critical Redfish events
- Generate Root Cause Analysis
- Generate Markdown reports

========================================

FOLDER STRUCTURE

FoxconnFailureAnalyzer/

│
├── FoxconnFailureAnalyzer.exe
├── logs/
├── reports/
└── README.txt

========================================

ANALYZE ALL LOGS

1. Copy log files into the logs folder.

2. Open Command Prompt.

3. Run:

FoxconnFailureAnalyzer.exe --all

4. Reports will be generated inside:

reports/

========================================

ANALYZE A SINGLE LOG

FoxconnFailureAnalyzer.exe logs\example_log.txt

========================================

GENERATE SAMPLE LOGS

FoxconnFailureAnalyzer.exe --generate 50000

========================================

REPORTS

Each analyzed log generates an individual report.

Example:

reports/

HGX_Log_001_Report.md

HGX_Log_002_Report.md

HGX_Log_003_Report.md

========================================

SUPPORTED DETECTIONS

Bianca Failures:

- CPUVDD
- CPU_DVDD
- SOCVDD
- 1V2 Rail
- PEX_SW_0V95
- NVVDD GPU
- HBMVDD GPU
- IO_MEZZ
- LPCAMM

NVIDIA Events:

- XID 163
- XID 154
- XID 79
- XID 48
- XID 31

Thermal Events:

- GPU Thermal Over Temperature
- PSHC disengaged due to thermal event
- GPU_THERM_WARN_INT

========================================

OUTPUT

The tool generates:

- Failure Summary
- Critical Event Analysis
- Root Cause Analysis
- Corrective Actions

========================================

VERSION

FoxconnFailureAnalyzer v1.0

========================================