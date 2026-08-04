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

        all_event_ids = []

        for event in critical_events:

            try:

                all_event_ids.append(

                    int(
                        event.get(
                            "event_id",
                            0
                        )
                    )

                )

            except:

                pass

        latest_global_event = max(
            all_event_ids,
            default=0
        )

        # ==========================
        # Rule Evaluation
        # ==========================

        for rule in ROOT_CAUSE_CATALOG:

            matched = True

            matched_conditions = 0

            latest_rule_event = 0

            for condition in rule["conditions"]:

                condition_found = False

                for token in evidence:

                    if condition.upper() in token:

                        condition_found = True

                        matched_conditions += 1

                        break

                if not condition_found:

                    matched = False

                    break

            if matched:

                for event in critical_events:

                    try:

                        event_id = int(
                            event.get(
                                "event_id",
                                0
                            )
                        )

                    except:

                        event_id = 0

                    event_text = (

                        (
                            event.get(
                                "failure",
                                ""
                            )

                            + " "

                            +

                            event.get(
                                "description",
                                ""
                            )

                        ).upper()

                    )

                    if any(

                        condition.upper() in event_text

                        for condition in rule["conditions"]

                    ):

                        latest_rule_event = max(

                            latest_rule_event,

                            event_id

                        )

                score = (

                    rule["priority"] * 100

                    +

                    matched_conditions * 25

                    +

                    latest_rule_event

                )

                rule_copy = rule.copy()

                rule_copy["score"] = score

                rule_copy["latest_event_id"] = latest_rule_event

                rule_copy["matched_conditions"] = matched_conditions

                matches.append(
                    rule_copy
                )

        matches.sort(

            key=lambda rule: rule["score"],

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