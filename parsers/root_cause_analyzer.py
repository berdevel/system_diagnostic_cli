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

        # ==========================
        # Findings
        # ==========================

        for finding in findings:

            evidence.add(

                finding.get(
                    "failure",
                    ""
                ).upper()

            )

        # ==========================
        # Critical Events
        # ==========================

        for event in critical_events:

            xid = event.get(
                "xid",
                ""
            )

            if xid and xid != "N/A":

                evidence.add(
                    f"XID_{xid}"
                )

            failure = (

                event.get(
                    "failure",
                    ""
                ).upper()

            )

            evidence.add(
                failure
            )

            description = (

                event.get(
                    "description",
                    ""
                ).upper()

            )

            evidence.add(
                description
            )

        matches = []

        # ==========================
        # Rule Evaluation
        # ==========================

        for rule in ROOT_CAUSE_CATALOG:

            matched = True

            for condition in rule["conditions"]:

                condition_found = any(

                    condition.upper() in token

                    for token in evidence

                )

                if not condition_found:

                    matched = False

                    break

            if matched:

                matches.append(
                    rule
                )

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