XID_CATALOG = {

    "8": {
        "name": "GPU Stopped Processing",
        "severity": "Error",
        "recommendation":
        "Restart application. If issue persists, collect diagnostic data and escalate."
    },

    "11": {
        "name": "Invalid or corrupted push buffer stream",
        "severity": "Critical",
        "recommendation":
        "Check CUDA application and driver."
    },

    "13": {
        "name": "Graphics Engine Exception",
        "severity": "Critical",
        "recommendation":
        "Use cuda-gdb or Compute Sanitizer."
    },

    "31": {
        "name": "GPU Memory Page Fault",
        "severity": "Critical",
        "recommendation":
        "Investigate CUDA application memory accesses. Run Compute Sanitizer or cuda-gdb."
    },

    "32": {
        "name": "PCIe / DMA Communication Fault",
        "severity": "Critical",
        "recommendation":
        "Inspect PCIe communication path and review GPU connectivity."
    },

    "43": {
        "name": "GPU stopped processing",
        "severity": "Critical",
        "recommendation":
        "Restart workload and inspect driver."
    },

    "45": {
        "name": "OS preemptive channel removal",
        "severity": "Warning",
        "recommendation":
        "Usually software-related."
    },

    "48": {
        "name": "Double Bit ECC Error",
        "severity": "Critical",
        "recommendation":
        "Perform GPU reset. Review ECC counters. Execute field diagnostics."
    },

    "54": {
        "name": "Auxiliary power not connected",
        "severity": "Critical",
        "recommendation":
        "Verify PSU and GPU power cables."
    },

    "56": {
        "name": "Display Engine Error",
        "severity": "Error",
        "recommendation":
        "Restart GPU and validate driver."
    },

    "62": {
        "name": "Thermal Event",
        "severity": "Critical",
        "recommendation":
        "Inspect cooling and airflow."
    },

    "63": {
        "name": "ECC Page Retirement",
        "severity": "Error",
        "recommendation":
        "Monitor memory degradation."
    },

    "64": {
        "name": "ECC Page Retirement Failure",
        "severity": "Critical",
        "recommendation":
        "Investigate possible hardware issue."
    },

    "69": {
        "name": "Graphics Engine Class Error",
        "severity": "Error",
        "recommendation":
        "Validate application and drivers."
    },

    "74": {
        "name": "NVLink Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink connectivity and review GPU-to-GPU communication errors."
    },

    "79": {
        "name": "GPU Fell Off Bus",
        "severity": "Critical",
        "recommendation":
        "Inspect PCIe connectivity and GPU hardware integrity."
    },

    "94": {
        "name": "Contained Memory Error",
        "severity": "Critical",
        "recommendation":
        "Restart affected application and review GPU memory health."
    },

    "95": {
        "name": "Uncontained Memory Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and execute memory diagnostics."
    },

    "110": {
        "name": "Security Fault",
        "severity": "Critical",
        "recommendation":
        "Inspect firmware and security logs."
    },

    "119": {
        "name": "GSP RPC Timeout",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and investigate GSP firmware behavior."
    },

    "120": {
        "name": "GSP Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and collect firmware diagnostics."
    },

    "149": {
        "name": "NVLink NETIR Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and reset GPU if required."
    },

    "154": {
        "name": "GPU Reset Required",
        "severity": "Critical",
        "recommendation":
        "Perform GPU reset and validate workload."
    },

    "163": {
        "name": "Power Smoothing Disabled Due To Thermal Event",
        "severity": "Critical",
        "recommendation":
        "Inspect thermal subsystem and resolve thermal condition before retest."
    }
}