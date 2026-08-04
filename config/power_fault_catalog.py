HMC_REMINDER = (
    "IMPORTANT: Perform HMC Log Clear before retest "
    "and before collecting final validation results."
)

POWER_FAULT_CATALOG = {

    # Bianca#1 PWR Fail Errors

    "PWR_FAIL_PEX_SW_0V95_MOD_0": {

        "failure":
        "Bianca#1 PEX Switch 0.95V Rail Power Failure",

        "recommendation":
        "Verify PEX Switch 0.95V rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_1V2_MOD_0": {
        
        "failure":
        "Bianca#1 1V2 Rail Failure",

        "recommendation":
        "Verify 1.2V module power rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_1V8_MOD_0": {
        
        "failure":
        "Bianca#1 1V8 Rail Failure",

        "recommendation":
        "Verify 1.8V module power rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_12V_0": {
            
        "failure":
        "Bianca#1 12V Rail Failure",

        "recommendation":
        "Verify 12V module power rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_12V_INPUT_VALID_0": {
                        
        "failure":
        "Bianca#1 12V Rail Failure",

        "recommendation":
        "Verify 12V module power rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_3V3_ALWAYS_ON{0x1}": {
    
        "failure":
        "Bianca#1 3V3 Always-On Rail Failure",

        "recommendation":
        "Verify 3.3V rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_FBVDDP_0": {

        "failure":
        "Bianca#1 HBM Memory Power Rail Failure",

        "recommendation":
        "Verify HBM memory power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_FBVDDQ_0": {
    
        "failure":
        "Bianca#1 HBM Interface Memory Rail Failure",

        "recommendation":
        "Verify HBM memory interface power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_FBVDD1_0": {
        
        "failure":
        "Bianca#1 HBM Memory Voltage Rail Failure",

        "recommendation":
        "Verify HBM memory voltage rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_FBVDD2_0": {
        
        "failure":
        "Bianca#1 HBM Memory Voltage Rail Failure",

        "recommendation":
        "Verify HBM memory voltage rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_0_GA": {
    
        "failure":
        "Bianca#1 GPU Core Voltage Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_0_GB": {
        
        "failure":
        "Bianca#1 GPU Core Voltage Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_1_GA": {
        
        "failure":
        "Bianca#1 GPU Core Voltage Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_1_GB": {
        
        "failure":
        "Bianca#1 GPU Core Voltage Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_CPUVDD_0": {
    
        "failure":
        "Bianca#1 CPUVDD Power Failure",

        "recommendation":
        "Verify CPU core power delivery integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_LPCAMM_0": {
    
        "failure":
        "Bianca#1 LPCAMM Power Failure",

        "recommendation":
        "Verify LPCAMM power delivery integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_C2C_0": {

        "failure":
        "Bianca#1 Chip-to-Chip Interface Power Path Failure",

        "recommendation":
        "Verify chip-to-chip power path integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_SOCVDD_0": {

        "failure":
        "Bianca#1 Power Failure (SOCVDD)",

        "recommendation":
        "Verify SoC power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_CPU_DVDD_0": {

        "failure":
        "Bianca#1 Power Failure (CPU_DVDD)",

        "recommendation":
        "Verify CPU digital power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_0_CDAB": {

        "failure":
        "GPU0 (Bianca#1) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_0_ABCD": {
    
        "failure":
        "GPU0 (Bianca#1) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_1_CDAB": {
    
        "failure":
        "GPU1 (Bianca#1) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_1_ABCD": {
    
        "failure":
        "GPU1 (Bianca#1) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDDQL_GPU_0": {
    
        "failure":
        "GPU0 (Bianca#1) HBM VDDQ Low Rail Failure",

        "recommendation":
        "Verify HBM VDDQ power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVPP_GPU_0": {
        
        "failure":
        "GPU0 (Bianca#1) HBM Programming Voltage Rail Failure",

        "recommendation":
        "Verify HBM VPP power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVPP_GPU_1": {
            
        "failure":
        "GPU1 (Bianca#1) HBM Programming Voltage Rail Failure",

        "recommendation":
        "Verify HBM VPP power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_PEXDVDD_GPU_0": {
            
        "failure":
        "GPU0 (Bianca#1) GPU PCIe Power Rail Failure",

        "recommendation":
        "Verify GPU PCIe power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_PEXDVDD_GPU_1": {
                
        "failure":
        "GPU1 (Bianca#1) GPU PCIe Power Rail Failure",

        "recommendation":
        "Verify GPU PCIe power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBIVDD_GPU_0": {
                
        "failure":
        "GPU0 (Bianca#1) High Bandwidth Interface Rail Failure",

        "recommendation":
        "Verify HBI power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBIVDD_GPU_1": {
                    
        "failure":
        "GPU1 (Bianca#1) High Bandwidth Interface Rail Failure",

        "recommendation":
        "Verify HBI power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#1 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    # Bianca#2 PWR Fail Errors

    "PWR_FAIL_3V3_ALWAYS_ON{0x2}": {
        
        "failure":
        "Bianca#2 3V3 Always-On Rail Failure",

        "recommendation":
        "Verify 3.3V rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_1V8_MOD_1": {
            
        "failure":
        "Bianca#2 1V8 Rail Failure",

        "recommendation":
        "Verify 1.8V module power rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_12V_INPUT_VALID_1": {
                    
        "failure":
        "Bianca#2 12V Rail Failure",

        "recommendation":
        "Verify 12V module power rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_1V2_MOD_1": {

        "failure":
        "Bianca#2 1V2 Rail Failure",

        "recommendation":
        "Verify affected power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_FBVDDP_1": {

        "failure":
        "Bianca#2 Power Failure (FBVDDP)",

        "recommendation":
        "Verify HBM memory power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDDQL_GPU_2": {
        
        "failure":
        "GPU2 (Bianca#2) HBM VDDQ Low Rail Failure",

        "recommendation":
        "Verify HBM VDDQ power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVPP_GPU_2": {
                
        "failure":
        "GPU2 (Bianca#2) HBM Programming Voltage Rail Failure",

        "recommendation":
        "Verify HBM VPP power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVPP_GPU_3": {
            
        "failure":
        "GPU3 (Bianca#2) HBM Programming Voltage Rail Failure",

        "recommendation":
        "Verify HBM VPP power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_2_CDAB": {
    
        "failure":
        "GPU2 (Bianca#2) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_2_ABCD": {
    
        "failure":
        "GPU2 (Bianca#2) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_3_CDAB": {
        
        "failure":
        "GPU3 (Bianca#2) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBMVDD_GPU_3_ABCD": {
    
        "failure":
        "GPU3 (Bianca#2) HBM Core Voltage Failure",

        "recommendation":
        "Verify HBM power delivery, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBIVDD_GPU_2": {
                        
        "failure":
        "GPU2 (Bianca#2) High Bandwidth Interface Rail Failure",

        "recommendation":
        "Verify HBI power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_HBIVDD_GPU_3": {
                    
        "failure":
        "GPU3 (Bianca#2) High Bandwidth Interface Rail Failure",

        "recommendation":
        "Verify HBI power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_PEXDVDD_GPU_2": {
                    
        "failure":
        "GPU2 (Bianca#2) GPU PCIe Power Rail Failure",

        "recommendation":
        "Verify GPU PCIe power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_PEXDVDD_GPU_3": {
                
        "failure":
        "GPU3 (Bianca#2) GPU PCIe Power Rail Failure",

        "recommendation":
        "Verify GPU PCIe power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_2_GB": {

        "failure":
        "Bianca#2 GPU Core Power Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_2_GA": {
    
        "failure":
        "Bianca#2 GPU Core Power Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_3_GB": {

        "failure":
        "Bianca#2 GPU Core Power Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_NVVDD_GPU_3_GA": {
    
        "failure":
        "Bianca#2 GPU Core Power Failure",

        "recommendation":
        "Verify GPU core power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_CPUVDD_1": {

        "failure":
        "Bianca#2 CPUVDD Power Failure",

        "recommendation":
        "Verify CPU core power delivery integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_SOCVDD_1": {
    
        "failure":
        "Bianca#2 Power Failure (SOCVDD)",

        "recommendation":
        "Verify SoC power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_CPU_DVDD_1": {
    
        "failure":
        "Bianca#2 Power Failure (CPU_DVDD)",

        "recommendation":
        "Verify CPU digital power rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_PEX_SW_0V95_MOD_1": {

        "failure":
        "Bianca#2 Power Failure (PEX_SW_0V95)",

        "recommendation":
        "Verify PEX Switch 0.95V rail stability, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_LPCAMM_1": {

        "failure":
        "Bianca#2 LPCAMM Power Failure",

        "recommendation":
        "Verify LPCAMM power delivery integrity, perform complete Bus-Bar reseat and retest. "
        "Replace Bianca#2 only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    # Generic Power Fault Errors

    "PS_RUN_PWR_FAULT": {

        "failure":
        "Power Sequencing Failure",

        "recommendation":
        "Review associated PWR_FAIL events and identify the originating component or power rail. "
        "Perform required corrective action, execute validation and retest. "
        "If no specific failing component can be identified, perform complete Bus-Bar reseat and retest. "
        + HMC_REMINDER
    },

    "PWR_FAIL_3V3_ALWAYS_ON{0x0}": {

        "failure":
        "Bianca Board Power Failure",

        "recommendation":
        "Verify 3.3V always-on rail integrity, perform complete Bus-Bar reseat and retest. "
        "Replace affected Bianca only if the issue reoccurs after retest. "
        + HMC_REMINDER
    },

    # GPU Thermal Fail Errors

    "PWR_FAIL_CPU_THERM_OVERT_0": {
        
        "failure":
        "CPU_0 (Bianca#1) Thermal Over Temperature",

        "recommendation":
        "Inspect coldplate assembly, verify screw torque and TIM condition, then perform retest. "
        "Replace Left Coldplate only if the issue reoccurs after retest. "
        "If the thermal issue persists after coldplate replacement, replace Bianca#1. "
        + HMC_REMINDER
    },

    "PWR_FAIL_CPU_THERM_OVERT_1": {
            
        "failure":
        "CPU_1 (Bianca#2) Thermal Over Temperature",

        "recommendation":
        "Inspect coldplate assembly, verify screw torque and TIM condition, then perform retest. "
        "Replace Right Coldplate only if the issue reoccurs after retest. "
        "If the thermal issue persists after coldplate replacement, replace Bianca#2. "
        + HMC_REMINDER
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x1}": {
        
        "failure":
        "GPU_0 (Bianca#1) Thermal Over Temperature",

        "recommendation":
        "Inspect coldplate assembly, verify screw torque and TIM condition, then perform retest. "
        "Replace Left Coldplate only if the issue reoccurs after retest. "
        "If the thermal issue persists after coldplate replacement, replace Bianca#1. "
        + HMC_REMINDER
    },
    
    "PWR_FAIL_GPU_THERM_OVERT{0x2}": {
    
        "failure":
        "GPU_1 (Bianca#1) Thermal Over Temperature",

        "recommendation":
        "Inspect coldplate assembly, verify screw torque and TIM condition, then perform retest. "
        "Replace Left Coldplate only if the issue reoccurs after retest. "
        "If the thermal issue persists after coldplate replacement, replace Bianca#1. "
        + HMC_REMINDER
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x4}": {

        "failure":
        "GPU_2 (Bianca#2) Thermal Over Temperature",

        "recommendation":
        "Inspect coldplate assembly, verify screw torque and TIM condition, then perform retest. "
        "Replace Right Coldplate only if the issue reoccurs after retest. "
        "If the thermal issue persists after coldplate replacement, replace Bianca#2. "
        + HMC_REMINDER
    },

    "PWR_FAIL_GPU_THERM_OVERT{0x8}": {

        "failure":
        "GPU_3 (Bianca#2) Thermal Over Temperature",

        "recommendation":
        "Inspect coldplate assembly, verify screw torque and TIM condition, then perform retest. "
        "Replace Right Coldplate only if the issue reoccurs after retest. "
        "If the thermal issue persists after coldplate replacement, replace Bianca#2. "
        + HMC_REMINDER
    },

    # CX8 PWR Fail Errors

    "PWR_FAIL_IO_MEZZ{0x1}": {

        "failure":
        "Left IO Mezzanine Failure",

        "recommendation":
        "Reseat Left CX8, verify connector engagement and perform retest. "
        "Replace Left CX8 only if the issue reoccurs after retest. "
        "If the issue persists after CX8 replacement, replace Bianca#1. "
        + HMC_REMINDER

    },

    "PWR_FAIL_IO_MEZZ{0x2}": {

        "failure":
        "Right IO Mezzanine Failure",

        "recommendation":
        "Reseat Right CX8, verify connector engagement and perform retest. "
        "Replace Right CX8 only if the issue reoccurs after retest. "
        "If the issue persists after CX8 replacement, replace Bianca#2. "
        + HMC_REMINDER
    },

    "PWR_FAIL_IO_MEZZ{0x3}": {

        "failure":
        "Both IO Mezzanine Failure",

        "recommendation":
        "Reseat Both CX8, verify connector engagement and perform retest. "
        "Replace Both CX8 only if the issue reoccurs after retest. "
        "If the issue persists after CX8 replacement, replace Both Bianca Assemblys. "
        + HMC_REMINDER
    }
}