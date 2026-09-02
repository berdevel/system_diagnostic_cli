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

    "25": {

        "name": "Illegal Push Buffer",
        "severity": "Critical",
        "recommendation":
        "Verify application workload and CUDA execution path. Review software and driver interaction."

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

    "37": {

        "name": "Driver Firmware Error",
        "severity": "Error",
        "recommendation":
        "Review driver and firmware compatibility. Collect logs if issue persists."

    },

    "38": {

        "name": "Firmware Watchdog Timeout",
        "severity": "Critical",
        "recommendation":
        "Review GPU firmware state and collect diagnostics."

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

    "46": {

        "name": "GPU Timeout",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and investigate GPU workload stability."

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

    "60": {

        "name": "Video Processor Exception",
        "severity": "Error",
        "recommendation":
        "Restart workload and investigate software interaction."

    },

    "62": {

        "name": "PMU Halt Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and collect firmware diagnostics."

    },

    "63": {

        "name": "GPU Memory Remapping Event",
        "severity": "Warning",
        "recommendation":
        "Review ECC counters and memory remapping activity."

    },

    "64": {

        "name": "GPU Memory Remapping Failure",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and review ECC health. Execute diagnostics if issue persists."

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
        "Inspect NVLink connectivity and review GPU-to-GPU communication path."

    },

    "79": {
        "name": "GPU Fell Off Bus",
        "severity": "Critical",
        "recommendation":
        "Inspect PCIe connectivity and GPU hardware integrity."
    },

    "92": {

        "name": "High Correctable ECC Error Rate",
        "severity": "Warning",
        "recommendation":
        "Monitor ECC events and collect diagnostics if error rate increases."

    },

    "94": {

        "name": "Contained Memory Error",
        "severity": "Warning",
        "recommendation":
        "Restart affected application and review GPU memory health."

    },

    "95": {

        "name": "Uncontained Memory Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and execute memory diagnostics."

    },

    "109": {

        "name": "Context Switch Timeout",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and investigate workload behavior."

    },

   "110": {

        "name": "Security Fault",
        "severity": "Critical",
        "recommendation":
        "Revert recent hardware changes and investigate platform integrity."

    },

    "119": {

        "name": "GSP RPC Timeout",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and investigate firmware/GSP communication."

    },

    "120": {

        "name": "GSP Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and collect GSP diagnostics."

    },

    "121": {

        "name": "C2C Error",
        "severity": "Error",
        "recommendation":
        "Review Grace-GPU C2C communication and monitor for repeated occurrences."

    },

    "136": {

        "name": "Link Training Failure",
        "severity": "Critical",
        "recommendation":
        "Investigate link signal integrity and perform GPU reset."

    },

    "137": {

        "name": "NVLink Privilege Error",
        "severity": "Error",
        "recommendation":
        "Investigate NVLink peer-to-peer memory accesses and software behavior."

    },

    "140": {

        "name": "Unrecoverable ECC Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and execute memory diagnostics."

    },

    "143": {

        "name": "GPU Initialization Error",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and review platform initialization sequence."

    },

    "144": {

        "name": "NVLink SAW Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review link stability."

    },

    "145": {

        "name": "NVLink RLW Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review link stability."

    },

    "146": {

        "name": "NVLink TLW Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review link stability."

    },

    "147": {

        "name": "NVLink TREX Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review link stability."

    },

    "148": {

        "name": "NVLink NVLPW_CTRL Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review link stability."

    },

    "149": {

        "name": "NVLink NETIR Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review GPU fabric stability."

    },

    "150": {

        "name": "NVLink MSE Error",
        "severity": "Critical",
        "recommendation":
        "Inspect NVLink communication path and review GPU fabric stability."

    },

    "154": {

        "name": "GPU Recovery Action Changed",
        "severity": "Error",
        "recommendation":
        "Review associated XID events to determine the required recovery action."

    },

    "156": {

        "name": "Resource Retirement Event",
        "severity": "Warning",
        "recommendation":
        "Review GPU resource retirement status and monitor for repeat events."

    },

    "158": {

        "name": "GPU Fatal Timeout",
        "severity": "Critical",
        "recommendation":
        "Reset GPU and collect diagnostics."

    },

    "163": {

        "name": "Power Smoothing Disabled Due To Thermal Event",
        "severity": "Critical",
        "recommendation":
        "Inspect cooling subsystem, coldplate condition and thermal environment."

    },

    "164": {

        "name": "Power Smoothing Lifetime Warning",
        "severity": "Warning",
        "recommendation":
        "Monitor power swings and evaluate future GPU replacement requirements."

    },

    "165": {

        "name": "Power Smoothing Lifetime Exhausted",
        "severity": "Info",
        "recommendation":
        "Evaluate GPU replacement if power smoothing functionality is required."

    },

    "171": {

        "name": "Uncorrectable DRAM Error",
        "severity": "Critical",
        "recommendation":
        "Review ECC counters and execute memory diagnostics."

    },

    "172": {

        "name": "Uncorrectable SRAM Error",
        "severity": "Critical",
        "recommendation":
        "Review ECC counters and execute diagnostics."

    }
}