from collections import Counter
from datetime import datetime
from pathlib import Path


class ReportLogGenerator:

    def generate(
        self,
        findings,
        critical_findings,
        source_log,
        root_causes,
        serial_number
    ):

        report_name = Path(source_log).stem

        report_file = (
            f"reports/{report_name}_Report.log"
        )

        timestamp = datetime.now()

        primary = None

        if root_causes:

            primary = root_causes.get(
                "primary"
            )

        with open(
            report_file,
            "w",
            encoding="utf-8"
        ) as log:

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "FOXCONN FAILURE ANALYZER\n"
            )

            log.write(
                "Technical Diagnostic Report\n"
            )

            log.write(
                "Version 2.2.6\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            log.write(
                f"Serial Number : {serial_number}\n"
            )

            log.write(
                f"Source Log    : {source_log}\n"
            )

            log.write(
                f"Generated     : "
                f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            log.write("\n")

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "ROOT CAUSE ANALYSIS\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            if primary:

                log.write(
                    f"Rule ID      : {primary['id']}\n"
                )

                log.write(
                    f"Cause        : {primary['name']}\n"
                )

                log.write(
                    f"Confidence   : {primary['confidence']}\n"
                )

                log.write(
                    f"Priority     : {primary.get('priority','N/A')}\n"
                )

                log.write(
                    f"RCA Score    : {primary.get('score','N/A')}\n"
                )

                log.write(
                    f"Latest Event : "
                    f"{primary.get('latest_event_id','N/A')}\n"
                )

                log.write("\n")

                log.write(
                    "=" * 70 + "\n"
                )

                log.write(
                    "RECOMMENDED ACTIONS\n"
                )

                log.write(
                    "=" * 70 + "\n\n"
                )

                log.write(
                    primary.get(
                        "recommendation",
                        "N/A"
                    )
                )

                log.write("\n\n")

                log.write("\n")

                if primary.get(
                    "potential_causes"
                ):

                    log.write(
                        "Potential Causal Events\n"
                    )

                    log.write(
                        "-" * 30 + "\n"
                    )

                    for event_id in primary[
                        "potential_causes"
                    ]:

                        log.write(
                            f"Event ID {event_id}\n"
                        )

                    log.write("\n")

            component_counter = Counter(

                item.get(
                    "component",
                    "Unknown"
                )

                for item in findings

            )

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "COMPONENT SUMMARY\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            log.write(
                f"{'Component':<25}"
                f"{'Count':>10}\n"
            )

            log.write(
                "-" * 35 + "\n"
            )

            for component, qty in sorted(
                component_counter.items()
            ):

                log.write(
                    f"{component:<25}"
                    f"{qty:>10}\n"
                )

            log.write("\n")

            critical_counter = Counter(

                event.get(
                    "failure",
                    "Unknown"
                )

                for event in (
                    critical_findings
                    or []
                )

            )

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "TOP CRITICAL EVENTS\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            log.write(
                f"{'Critical Event':<55}"
                f"{'Count':>8}\n"
            )

            log.write(
                "-" * 65 + "\n"
            )

            for failure, qty in (

                critical_counter
                .most_common(10)

            ):

                log.write(
                    f"{failure:<55}"
                    f"{qty:>8}\n"
                )

            log.write("\n")

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "CRITICAL EVENT DETAILS\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            log.write(
                f"{'ID':<8}"
                f"{'Severity':<12}"
                f"{'GPU':<10}"
                f"{'Bianca':<12}"
                f"Failure\n"
            )

            log.write(
                "-" * 78 + "\n"
            )

            sorted_events = sorted(

                critical_findings or [],

                key=lambda x: (

                    int(
                        x.get(
                            "event_id",
                            0
                        )
                    )

                    if str(
                        x.get(
                            "event_id",
                            0
                        )
                    ).isdigit()

                    else 0

                )

            )

            for event in sorted_events:

                log.write(

                    f"{event.get('event_id',''):<8}"
                    f"{event.get('severity',''):<12}"
                    f"{event.get('gpu',''):<10}"
                    f"{event.get('bianca',''):<12}"
                    f"{event.get('failure','')}\n"

                )

            log.write("\n")

            log.write(
                "\n"
            )

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "CRITICAL EVENT DESCRIPTIONS\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            for event in sorted_events:

                description = str(

                    event.get(
                        "description",
                        "N/A"
                    )

                )

                log.write(
                    f"Event ID : {event.get('event_id','N/A')}\n"
                )

                log.write(
                    f"Failure  : {event.get('failure','N/A')}\n"
                )

                log.write(
                    f"Description : {description}\n"
                )

                log.write(
                    "-" * 70 + "\n"
                )

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "HMC EVENT DETAILS\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            log.write(
                f"{'Event ID':<10}"
                f"{'Component':<15}"
                f"{'Failure'}\n"
            )

            log.write(
                "-" * 70 + "\n"
            )

            for item in findings:

                log.write(

                    f"{item.get('event_id',''):<10}"
                    f"{item.get('component','Unknown'):<15}"
                    f"{item.get('failure','Unknown')}\n"

                )

            log.write(
                "\n"
            )

            log.write(
                "=" * 70 + "\n"
            )

            log.write(
                "HMC EVENT DESCRIPTIONS\n"
            )

            log.write(
                "=" * 70 + "\n\n"
            )

            for item in findings:

                log.write(
                    f"Event ID : {item.get('event_id','N/A')}\n"
                )

                log.write(
                    f"Failure  : {item.get('failure','N/A')}\n"
                )

                log.write(
                    f"Line     : {item.get('line','N/A')}\n"
                )

                log.write(
                    "-" * 70 + "\n"
                )