CATALOG_VERSION = "2.2.2"

ROOT_CAUSE_CATALOG = [

    {
        "id": "RCA-001",

        "version": "2.0",

        "priority": 120,

        "name": "GPU Thermal Event",

        "confidence": "HIGH",

        "conditions": [

            "XID_163",
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

        Execute final validation after replacement.

        IMPORTANT:
        Always perform HMC Log Clear before every retest and before collecting final validation results.
        """
    },

    {
        "id": "RCA-003",

        "version": "1.0",

        "priority": 100,

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

        Run full validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#1 (Left).

        Re-run validation after Bianca replacement.
        """
    },

    {
        "id": "RCA-004",

        "version": "1.0",

        "priority": 100,

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

        Run full validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after Bus-Bar reseat and retest, replace Bianca#2 (Right).

        Re-run validation after Bianca replacement.
        """
    },

    {
        "id": "RCA-005",

        "version": "2.0",

        "priority": 115,

        "name": "CPUVDD Rail Failure - Bianca#1",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPUVDD_0"

        ],

        "recommendation":

        """
        Perform complete Bus-Bar reseat.

        Verify power rail stability.

        Execute validation and retest.

        If the failure reoccurs after retest, replace Bianca#1 (Left).

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-006",

        "version": "2.0",

        "priority": 115,

        "name": "CPUVDD Rail Failure - Bianca#2",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPUVDD_1"

        ],

        "recommendation":

        """
        Perform complete Bus-Bar reseat.

        Verify power rail stability.

        Execute validation and retest.

        If the failure reoccurs after retest, replace Bianca#2 (Right).

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-007",

        "version": "2.0",

        "priority": 115,

        "name": "GPU Core Power Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_NVVDD_GPU"

        ],

        "recommendation":

        """
        Perform complete Bus-Bar reseat.

        Verify GPU power rail integrity.

        Execute validation and retest.

        If the same fault reoccurs, replace the affected Bianca assembly.

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-008",

        "version": "2.0",

        "priority": 110,

        "name": "FBVDDP Power Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_FBVDDP"

        ],

        "recommendation":

        """
        Perform complete Bus-Bar reseat.

        Verify rail stability and connectors.

        Execute validation and retest.

        If the same fault reoccurs, replace the affected Bianca assembly.

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-009",

        "version": "1.0",

        "priority": 20,

        "name": "Power Sequencing Failure",

        "confidence": "MEDIUM",

        "conditions": [

            "PS_RUN_PWR_FAULT"

        ],

        "recommendation":

        """
        Review related PWR_FAIL events.
        Verify power sequence integrity.
        """
    },

    {
        "id": "RCA-010",

        "version": "2.0",

        "priority": 100,

        "name": "I/O Mezzanine Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_IO_MEZZ"

        ],

        "recommendation":

        """
        Perform complete CX8 reseat procedure.

        Verify CX8 card installation, connector engagement and retention mechanism.

        Execute full validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same failure reoccurs after CX8 reseat and retest, replace the affected CX8 card.

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-011",

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

        If any installation issue is found, correct the assembly and perform a complete validation and retest.

        If the issue is not reproducible after retest, return the unit to service.

        If the thermal interrupt reoccurs after installation correction and retest, replace the affected coldplate assembly.

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-012",

        "version": "2.0",

        "name": "GPU Thermal Protection Triggered",

        "priority": 125,

        "confidence": "HIGH",

        "conditions": [

            "XID_163"

        ],

        "recommendation":

        """
        Inspect coldplate installation before replacement.

        Verify coldplate seating, screw torque and overall mechanical assembly.

        Verify TIM condition and proper contact pressure.

        If any assembly issue is identified, correct the installation and execute full validation and retest.

        If the fault is not reproducible after retest, return the unit to service.

        If the same thermal protection event reoccurs after installation correction and retest, replace the affected coldplate assembly.

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-013",

        "version": "1.0",

        "priority": 115,

        "name": "Bianca#1 - PEX Switch 0.95V Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_PEX_SW_0V95_MOD_0"

        ],

        "recommendation":

        """
        Perform complete Bus-Bar reseat.

        Verify PEX rail stability.

        Execute validation and retest.

        If the same failure reoccurs after retest, replace Bianca#1 (Left) assembly.

        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-014",

        "version": "1.0",

        "priority": 115,

        "name": "Bianca#2 - PEX Switch 0.95V Rail Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_PEX_SW_0V95_MOD_1"

        ],

        "recommendation":

        """
        Perform complete Bus-Bar reseat.

        Verify PEX rail stability.

        Execute validation and retest.

        If the same failure reoccurs after retest, replace Bianca#2 (Right) assembly.

        Re-run validation after replacement.
        """
    }

]