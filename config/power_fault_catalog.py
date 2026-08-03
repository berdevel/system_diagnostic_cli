POWER_FAULT_CATALOG = {

    "PWR_FAIL_PEX_SW_0V95_MOD_0": {

        "failure":
        "Bianca#1 Power Failure (PEX_SW_0V95)",

        "recommendation":
        "Verify PEX rail stability, perform Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x2}": {

        "failure":
        "GPU_1 Thermal Over Temperature",

        "recommendation":
        "GPU_1 overheating detected on Bianca#1. Inspect left coldplate, verify screw torque and TIM condition. Perform retest. "
        "Replace left coldplate only if the issue reoccurs."
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x4}": {

        "failure":
        "GPU_2 Thermal Over Temperature",

        "recommendation":
        "GPU_2 overheating detected on Bianca#2. Inspect right coldplate, verify screw torque and TIM condition. Perform retest. "
        "Replace right coldplate only if the issue reoccurs."
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x8}": {

        "failure":
        "GPU_3 Thermal Over Temperature",

        "recommendation":
        "GPU_3 overheating detected on Bianca#2. Inspect right coldplate, verify screw torque and TIM condition. Perform retest. "
        "Replace right coldplate only if the issue reoccurs."
    },

    "PWR_FAIL_3V3_ALWAYS_ON{0x0}": {

        "failure":
        "Bianca Board Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Inspect and replace the affected Bianca board."
    },

    "PWR_FAIL_3V3_ALWAYS_ON{0x1}": {

        "failure":
        "3V3 Always-On Rail Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_FBVDDP_0": {

        "failure":
        "Bianca#1 Power Failure (FBVDDP)",

        "recommendation":
        "Verify memory power rail integrity, perform Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PS_RUN_PWR_FAULT": {

        "failure":
        "Power Sequencing Failure",

        "recommendation":
        "Review associated PWR_FAIL events and validate the identified component before retest."
    },

    "PWR_FAIL_1V2_MOD_0": {

        "failure":
        "1V2 Rail Failure",

        "recommendation":
        "Verify 1V2 rail stability, perform Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_1V2_MOD_1": {

        "failure":
        "1V2 Rail Failure",

        "recommendation":
        "Verify 1V2 rail stability, perform Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_FBVDDP_1": {

        "failure":
        "Bianca#2 Power Failure (FBVDDP)",

        "recommendation":
        "Verify memory power rail integrity, perform Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_NVVDD_GPU_0": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_NVVDD_GPU_1": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_NVVDD_GPU_2": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_NVVDD_GPU_3": {

        "failure":
        "GPU Core Power Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_CPUVDD_0{0x1}": {

        "failure":
        "CPUVDD Power Failure",

        "recommendation":
        "Verify CPUVDD power delivery, perform Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_CPUVDD_1{0x1}": {

        "failure":
        "CPUVDD Power Failure",

        "recommendation":
        "Verify CPUVDD power delivery, perform Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_PEX_SW_0V95_MOD_1": {

        "failure":
        "Bianca#2 Power Failure (PEX_SW_0V95)",

        "recommendation":
        "Verify PEX rail stability, perform Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_LPCAMM_0{0x1}": {

        "failure":
        "LPCAMM Power Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#1 only if the issue reoccurs."
    },

    "PWR_FAIL_LPCAMM_1{0x1}": {

        "failure":
        "LPCAMM Power Failure",

        "recommendation":
        "Perform Bus-Bar reseat, verify connector engagement and torque, then retest."
        "Replace Bianca#2 only if the issue reoccurs."
    },

    "PWR_FAIL_IO_MEZZ{0x1}": {

        "failure":
        "IO Mezzanine Failure",

        "recommendation":
        "Reseat affected CX8, verify connector engagement and perform retest. "
        "Replace Left CX8 only if the issue reoccurs."
    },

    "PWR_FAIL_IO_MEZZ{0x2}": {

        "failure":
        "IO Mezzanine Failure",

        "recommendation":
        "Reseat affected CX8, verify connector engagement and perform retest. "
        "Replace Right CX8 only if the issue reoccurs."
    },

    "PWR_FAIL_IO_MEZZ{0x3}": {

        "failure":
        "IO Mezzanine Failure",

        "recommendation":
        "Replace Both CX8 Cards."
    }
}