from config.root_cause_catalog import (
    ROOT_CAUSE_CATALOG
)


class RootCauseAnalyzer:

    def analyze(

        self,
        findings,
        critical_events

    ):

        evidence = set()

        # Bianca Failures

        for finding in findings:

            evidence.add(

                finding["failure"].upper()

            )

        # Critical Events

        for event in critical_events:

            xid = event.get(
                "xid",
                ""
            )

            if xid:

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

                for condition

                in rule["conditions"]

            ):

                matches.append(rule)

        return matches