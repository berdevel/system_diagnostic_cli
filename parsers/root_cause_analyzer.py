from config.root_cause_catalog import (
    ROOT_CAUSE_CATALOG,
    CATALOG_VERSION
)


class RootCauseAnalyzer:

    def analyze(
        self,
        findings,
        critical_events
    ):

        evidence = set()

        for finding in findings:

            evidence.add(
                finding["failure"].upper()
            )

        for event in critical_events:

            xid = event.get(
                "xid",
                ""
            )

            if xid and xid != "N/A":

                evidence.add(
                    f"XID_{xid}"
                )

            description = (
                event.get(
                    "description",
                    ""
                ).upper()
            )

            if "PWR_FAIL_GPU_THERM_OVERT" in description:

                evidence.add(
                    "PWR_FAIL_GPU_THERM_OVERT"
                )

            if "PS_RUN_PWR_FAULT" in description:

                evidence.add(
                    "PS_RUN_PWR_FAULT"
                )

        matches = []

        for rule in ROOT_CAUSE_CATALOG:

            if all(

                condition in evidence

                for condition in rule[
                    "conditions"
                ]

            ):

                matches.append(rule)

        matches.sort(

            key=lambda rule: (

                rule["priority"],

                len(
                    rule["conditions"]
                )

            ),

            reverse=True

        )

        return {

            "catalog_version":
            CATALOG_VERSION,

            "primary":
            matches[0]
            if matches
            else None,

            "secondary":
            matches[1:]
            if len(matches) > 1
            else []

        }