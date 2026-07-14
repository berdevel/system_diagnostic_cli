from collections import Counter
from datetime import datetime
from pathlib import Path


class MarkdownGenerator:

    def generate(
        self,
        findings,
        critical_findings=None,
        source_log="report"
    ):

        report_name = Path(source_log).stem

        with open(
            f"reports/{report_name}_Report.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "# FOXCONN FAILURE ANALYSIS REPORT\n\n"
            )

            file.write(
                f"Generated: {datetime.now()}\n\n"
            )

            file.write(
                f"Source Log: {source_log}\n\n"
            )

            file.write(
                f"Total Bianca Failures: {len(findings)}\n\n"
            )

            # ==========================================
            # BIANCA FAILURES
            # ==========================================

            file.write(
                "# BIANCA FAILURE ANALYSIS\n\n"
            )

            if findings:

                bianca_counter = Counter(
                    item.get("bianca", "Unknown")
                    for item in findings
                )

                file.write(
                    "## Bianca Failure Summary\n\n"
                )

                for bianca, total in bianca_counter.items():

                    file.write(
                        f"- {bianca}: {total}\n"
                    )

                file.write("\n")

                file.write(
                    "## Bianca Failure Details\n\n"
                )

                for item in findings:

                    file.write(
                        "### FAILURE DETECTED\n\n"
                    )

                    file.write(
                        f"- Failure       : "
                        f"{item.get('failure', 'Unknown')}\n"
                    )

                    file.write(
                        f"- Bianca        : "
                        f"{item.get('bianca', 'Unknown')}\n"
                    )

                    file.write(
                        f"- Module        : "
                        f"{item.get('module', 'Unknown')}\n"
                    )

                    file.write(
                        f"- Line Number   : "
                        f"{item.get('line', 'N/A')}\n"
                    )

                    file.write(
                        f"- Log Content   : "
                        f"{item.get('message', 'N/A')}\n"
                    )

                    file.write(
                        f"- Recommendation: "
                        f"{item.get('action', 'N/A')}\n\n"
                    )

            else:

                file.write(
                    "No Bianca failures detected.\n\n"
                )

            # ==========================================
            # NVIDIA CRITICAL EVENTS
            # ==========================================

            file.write(
                "\n---\n\n"
            )

            file.write(
                "# NVIDIA CRITICAL EVENTS ANALYSIS\n\n"
            )

            if critical_findings:

                file.write(
                    f"Total Critical Events: "
                    f"{len(critical_findings)}\n\n"
                )

                for event in critical_findings:

                    file.write(
                        "## CRITICAL EVENT\n\n"
                    )

                    file.write(
                        f"- Event ID       : "
                        f"{event.get('event_id', 'Unknown')}\n"
                    )

                    file.write(
                        f"- Date           : "
                        f"{event.get('created', 'Unknown')}\n"
                    )

                    file.write(
                        f"- Severity       : "
                        f"{event.get('severity', 'Unknown')}\n"
                    )

                    file.write(
                        f"- GPU            : "
                        f"{event.get('gpu', 'Unknown')}\n"
                    )

                    file.write(
                        f"- XID            : "
                        f"{event.get('xid', 'N/A')}\n"
                    )

                    file.write(
                        f"- Failure        : "
                        f"{event.get('failure', 'Unknown')}\n"
                    )

                    file.write(
                        f"- Description    : "
                        f"{event.get('description', 'N/A')}\n"
                    )

                    file.write(
                        f"- Recommendation : "
                        f"{event.get('recommendation', 'N/A')}\n"
                    )

                    file.write(
                        f"- Resolution     : "
                        f"{event.get('resolution', 'N/A')}\n\n"
                    )

            else:

                file.write(
                    "No Critical Events detected.\n\n"
                )

            # ==========================================
            # ROOT CAUSE ANALYSIS
            # ==========================================

            file.write(
                "\n---\n\n"
            )

            file.write(
                "# ROOT CAUSE ANALYSIS\n\n"
            )

            if critical_findings:

                xid_163_count = sum(
                    1
                    for event in critical_findings
                    if event.get("xid") == "163"
                )

                if xid_163_count:

                    file.write(
                        "## High Confidence Thermal Event\n\n"
                    )

                    file.write(
                        f"Detected XID 163 "
                        f"{xid_163_count} times.\n\n"
                    )

                    file.write(
                        "Affected GPUs:\n"
                    )

                    affected_gpus = sorted({
                        event.get("gpu", "Unknown")
                        for event in critical_findings
                        if event.get("gpu") != "Unknown"
                    })

                    for gpu in affected_gpus:

                        file.write(
                            f"- {gpu}\n"
                        )

                    file.write("\n")

                    file.write(
                        "Recommended Investigation:\n"
                    )

                    file.write(
                        "- Verify TIM condition.\n"
                    )

                    file.write(
                        "- Verify cold plate pressure.\n"
                    )

                    file.write(
                        "- Check airflow restrictions.\n"
                    )

                    file.write(
                        "- Verify fan speeds.\n"
                    )

                    file.write(
                        "- Review PCB temperature history.\n\n"
                    )

            file.write(
                "\n---\n"
            )