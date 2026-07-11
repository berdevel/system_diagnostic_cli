XID_CATALOG = {

    "8": {
        "name": "GPU stopped processing",
        "severity": "Error",
        "recommendation":
        "Restart application and verify GPU health."
    },

    "11": {
        "name": "Invalid or corrupted push buffer stream",
        "severity": "Error",
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
        "Check memory accesses and CUDA code."
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
        "Reset GPU. Consider replacement if recurring."
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
        "Check NVLink connectivity and topology."
    },

    "79": {
        "name": "GPU Fallen Off The Bus",
        "severity": "Critical",
        "recommendation":
        "Power cycle system and evaluate for RMA."
    },

    "94": {
        "name": "Contained ECC Error",
        "severity": "Warning",
        "recommendation":
        "Restart affected workload."
    },

    "95": {
        "name": "Uncontained ECC Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and investigate hardware."
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
        "Update firmware and GPU driver."
    },

    "120": {
        "name": "GSP Error",
        "severity": "Critical",
        "recommendation":
        "Collect logs and evaluate firmware."
    },

    "154": {
        "name": "GPU Reset Required",
        "severity": "Critical",
        "recommendation":
        "Perform GPU reset and validate workload."
    },

    "163": {
        "name": "PSHC disengaged due to thermal event",
        "severity": "Critical",
        "recommendation":
        "Check heatsink contact, TIM, airflow, fan speed, PCB temperature and thermal throttling history."
    }
}