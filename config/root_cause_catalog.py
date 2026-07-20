CATALOG_VERSION = "1.0.0"

CATALOG_VERSION = "1.0.0"

ROOT_CAUSE_CATALOG = [

    {
        "id": "RCA-001",

        "version": "1.0",

        "priority": 80,

        "name": "GPU Thermal Event",

        "confidence": "HIGH",

        "conditions": [

            "XID_163",
            "PWR_FAIL_GPU_THERM_OVERT"

        ],

        "recommendation":

        """
        Verify thermal interface material (TIM).
        Verify cold plate installation.
        Check airflow restrictions.
        Verify fan operation.
        Review GPU temperature history.
        """
    },

    {
        "id": "RCA-002",

        "version": "1.0",

        "priority": 60,

        "name": "GPU Thermal Degradation",

        "confidence": "MEDIUM",

        "conditions": [

            "XID_163"

        ],

        "recommendation":

        """
        Review thermal performance.
        Check TIM condition.
        Verify heatsink pressure.
        """
    },

    {
        "id": "RCA-003",

        "version": "1.0",

        "priority": 100,

        "name": "PEX Switch 0.95V Rail Failure - Bianca 1",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_PEX_SW_0V95_MOD_0"

        ],

        "recommendation":

        """
        Replace Bianca#1 (Left).
        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-004",

        "version": "1.0",

        "priority": 100,

        "name": "PEX Switch 0.95V Rail Failure - Bianca 2",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_PEX_SW_0V95_MOD_1"

        ],

        "recommendation":

        """
        Replace Bianca#2 (Right).
        Re-run validation after replacement.
        """
    },

    {
        "id": "RCA-005",

        "version": "1.0",

        "priority": 100,

        "name": "CPUVDD Failure - Bianca 1",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPUVDD_0"

        ],

        "recommendation":

        """
        Replace Bianca#1 (Left).
        Verify power rail stability.
        """
    },

    {
        "id": "RCA-006",

        "version": "1.0",

        "priority": 100,

        "name": "CPUVDD Failure - Bianca 2",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_CPUVDD_1"

        ],

        "recommendation":

        """
        Replace Bianca#2 (Right).
        Verify power rail stability.
        """
    },

    {
        "id": "RCA-007",

        "version": "1.0",

        "priority": 100,

        "name": "GPU Core Power Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_NVVDD_GPU"

        ],

        "recommendation":

        """
        Verify GPU power rail.
        Replace affected Bianca if failure persists.
        """
    },

    {
        "id": "RCA-008",

        "version": "1.0",

        "priority": 100,

        "name": "FBVDDP Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_FBVDDP"

        ],

        "recommendation":

        """
        Reseat affected cables.
        Verify connectors.
        Replace Bianca if failure persists.
        """
    },

    {
        "id": "RCA-009",

        "version": "1.0",

        "priority": 40,

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

        "version": "1.0",

        "priority": 100,

        "name": "I/O Mezzanine Failure",

        "confidence": "HIGH",

        "conditions": [

            "PWR_FAIL_IO_MEZZ"

        ],

        "recommendation":

        """
        Replace affected CX8 card.
        Re-run validation.
        """
    }

]