POWER_FAULT_CATALOG = {

    "PWR_FAIL_FBVDDP_1": {

        "failure":
        "Bianca#1 Power Failure (FBVDDP)",

        "recommendation":
        "Replace Bianca#1 (Left Bianca)."
    },

    "PWR_FAIL_PEX_SW_0V95_MOD_0": {

        "failure":
        "Bianca#1 Power Failure (PEX_SW_0V95)",

        "recommendation":
        "Replace Bianca#1 (Left Bianca)."
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x2}": {

        "failure":
        "GPU_1 Thermal Over Temperature",

        "recommendation":
        "GPU_1 overheating detected on Bianca#1. Replace cold plate and thermal interface material (TIM)."
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x4}": {

        "failure":
        "GPU_2 Thermal Over Temperature",

        "recommendation":
        "GPU_2 overheating detected on Bianca#2. Replace cold plate and thermal interface material (TIM)."
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x8}": {

        "failure":
        "GPU_3 Thermal Over Temperature",

        "recommendation":
        "GPU_3 overheating detected on Bianca#2. Replace cold plate and thermal interface material (TIM)."
    },

    "PWR_FAIL_3V3_ALWAYS_ON{0x0}": {

        "failure":
        "Bianca Board Failure",

        "recommendation":
        "Inspect and replace the affected Bianca board."
    },

    "PWR_FAIL_3V3_ALWAYS_ON{0x1}": {

        "failure":
        "3V3 Always-On Rail Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_FBVDDP_0{0x1}": {

        "failure":
        "FBVDDP Failure",

        "recommendation":
        "Reseat and reroute cables first. If the issue persists, replace the primary Bianca card."
    },

    "PS_RUN_PWR_FAULT": {

        "failure":
        "Power Sequencing Failure",

        "recommendation":
        "Review associated PWR_FAIL codes to determine the root cause."
    },

    "PWR_FAIL_1V2_MOD_0": {

        "failure":
        "1V2 Rail Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_1V2_MOD_1": {

        "failure":
        "1V2 Rail Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_FBVDDP_1{0x1}": {

        "failure":
        "FBVDDP Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_NVVDD_GPU_0": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_NVVDD_GPU_1": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_NVVDD_GPU_2": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_NVVDD_GPU_3": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_CPUVDD_0{0x1}": {

        "failure":
        "CPUVDD Power Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_CPUVDD_1{0x1}": {

        "failure":
        "CPUVDD Power Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_PEX_SW_0V95_MOD_0{0x1}": {

        "failure":
        "PEX Switch 0.95V Rail Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_PEX_SW_0V95_MOD_1{0x1}": {

        "failure":
        "PEX Switch 0.95V Rail Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_LPCAMM_0{0x1}": {

        "failure":
        "LPCAMM Power Failure",

        "recommendation":
        "Replace Left Bianca."
    },

    "PWR_FAIL_LPCAMM_1{0x1}": {

        "failure":
        "LPCAMM Power Failure",

        "recommendation":
        "Replace Right Bianca."
    },

    "PWR_FAIL_IO_MEZZ{0x1}": {

        "failure":
        "IO Mezzanine Failure",

        "recommendation":
        "Replace Left CX8."
    },

    "PWR_FAIL_IO_MEZZ{0x2}": {

        "failure":
        "IO Mezzanine Failure",

        "recommendation":
        "Replace Right CX8."
    },

    "PWR_FAIL_IO_MEZZ{0x3}": {

        "failure":
        "IO Mezzanine Failure",

        "recommendation":
        "Replace Both CX8 Cards."
    }
}