CATALOG_VERSION = "2.2.4"

ROOT_CAUSE_CATALOG = [

    {
        "id": "RCA-001",

        "version": "2.0",

        "priority": 120,

        "name": "GPU Thermal Event",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_GPU_THERM_OVERT"

        ],

        "recommendation":

        """
        Verify coldplate installation and mechanical assembly.

        Confirm all coldplate screws are properly installed and torqued.

        Verify proper coldplate contact and TIM coverage.

        Correct any installation issue identified.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the issue is not reproducible after retest, return the unit to service.

        If the thermal fault reoccurs after installation correction and retest, replace the affected coldplate assembly.

        Perform HMC Log Clear again.

        Execute validation and retest.

        If the thermal issue persists after coldplate replacement, replace the Bianca assembly associated with the affected GPU.

        Perform HMC Log Clear again.

        Execute final validation after Bianca replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-002",

        "version": "1.0",

        "priority": 100,

        "match": "ANY",

        "name": "Bianca#1 Power Distribution Fault",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPU_DVDD_0",
            "PWR_FAIL_SOCVDD_0",
            "PWR_FAIL_1V8_MOD_0",
            "PWR_FAIL_1V2_MOD_0",
            "PWR_FAIL_12V_0",
            "PWR_FAIL_C2C_0"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#1 (Left).

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-003",

        "version": "1.0",

        "priority": 100,

        "match": "ANY",

        "name": "Bianca#2 Power Distribution Fault",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_12V_INPUT_VALID_1",
            "PWR_FAIL_12V_INPUT_VALID_0",
            "PWR_FAIL_CPU_DVDD_1",
            "PWR_FAIL_SOCVDD_1",
            "PWR_FAIL_1V8_MOD_1",
            "PWR_FAIL_1V2_MOD_1"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#2 (Right).

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-004",

        "version": "2.0",

        "priority": 115,

        "name": "CPUVDD Rail Failure - Bianca#1",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPUVDD_0"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#1 (Left).

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-005",

        "version": "2.0",

        "priority": 115,

        "name": "CPUVDD Rail Failure - Bianca#2",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPUVDD_1"

        ],

        "recommendation":

       """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#2 (Right).

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-006",

        "version": "2.0",

        "priority": 115,

        "name": "GPU Core Power Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_NVVDD_GPU"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace the Bianca assembly associated with the affected GPU.

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-007",

        "version": "2.0",

        "priority": 110,

        "name": "FBVDDP Power Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_FBVDDP"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace the associated Bianca assembly.

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-008",

        "version": "1.0",

        "priority": 20,

        "name": "Power Sequencing Failure",

        "confidence": "MEDIUM",

        "conditions": [

            "PS_RUN_PWR_FAULT"

        ],

        "recommendation":

        """
        Review all associated PWR_FAIL events and identify the originating component or power rail.

        Verify power sequence integrity and confirm the primary source of the fault.

        Perform the corrective action associated with the identified failing component.

        Perform HMC Log Clear.

        Execute validation and retest.

        If no specific failing component can be identified, perform complete Bus-Bar reseat and retest.

        If the issue persists, continue troubleshooting based on the newly generated events after retest.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-009",

        "version": "2.0",

        "priority": 100,

        "match": "ANY",

        "name": "I/O Mezzanine Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_IO_MEZZ"

        ],

        "recommendation":

        """
        Perform complete CX8 reseat procedure.

        Verify CX8 card installation, connector engagement and retention mechanism.

        Perform HMC Log Clear.

        Execute full validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after CX8 reseat and retest, replace the affected CX8 card.

        Perform HMC Log Clear again.

        Execute validation and retest.

        If the issue persists after CX8 replacement, replace the Bianca assembly associated with the affected CX8.

        Perform HMC Log Clear again.

        Execute final validation after Bianca replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-010",

        "version": "2.0",

        "name": "GPU Thermal Interrupt",

        "priority": 130,

        "confidence": "HIGH",

        "conditions": [

            "THERM_OVERT_INT"

        ],

        "recommendation":

        """
        Verify coldplate installation and mechanical assembly.

        Confirm all coldplate screws are properly installed and torqued.

        Verify proper coldplate contact and TIM coverage.

        Correct any installation issue identified.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the issue is not reproducible after retest, return the unit to service.

        If the thermal fault reoccurs after installation correction and retest, replace the affected coldplate assembly.

        Perform HMC Log Clear again.

        Execute validation and retest.

        If the thermal issue persists after coldplate replacement, replace the Bianca assembly associated with the affected GPU.

        Perform HMC Log Clear again.

        Execute final validation after Bianca replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-011",

        "version": "2.0",

        "name": "GPU Thermal Protection Triggered",

        "priority": 125,

        "confidence": "HIGH",

        "conditions": [

            "XID_163"

        ],

        "recommendation":

       """
        Verify coldplate installation and mechanical assembly.

        Confirm all coldplate screws are properly installed and torqued.

        Verify proper coldplate contact and TIM coverage.

        Correct any installation issue identified.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the issue is not reproducible after retest, return the unit to service.

        If the thermal fault reoccurs after installation correction and retest, replace the affected coldplate assembly.

        Perform HMC Log Clear again.

        Execute validation and retest.

        If the thermal issue persists after coldplate replacement, replace the Bianca assembly associated with the affected GPU.

        Perform HMC Log Clear again.

        Execute final validation after Bianca replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-012",

        "version": "1.0",

        "priority": 115,

        "name": "Bianca#1 - PEX Switch 0.95V Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_PEX_SW_0V95_MOD_0"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#1 (Left).

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-013",

        "version": "1.0",

        "priority": 115,

        "name": "Bianca#2 - PEX Switch 0.95V Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_PEX_SW_0V95_MOD_1"

        ],

        "recommendation":

        """
        Perform a complete Bus-Bar reseat procedure.

        Verify Bus-Bar installation, torque and connector engagement.

        Perform HMC Log Clear.

        Execute validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#2 (Right).

        Perform HMC Log Clear again.

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    }

]