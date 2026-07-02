from collections import Counter


class MarkdownGenerator:

    def generate(self, findings):

        counts = Counter(
            item["severity"]
            for item in findings
        )

        with open(
            "reports/DiagnosticReport.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "# Linux Diagnostic Report\n\n"
            )

            file.write(
                "## Incident Summary\n\n"
            )

            for severity, total in counts.items():

                file.write(
                    f"- {severity}: {total}\n"
                )

            file.write(
                "\n## Detailed Findings\n\n"
            )

            for item in findings:

                file.write(
                    f"- [{item['severity']}] "
                    f"Line {item['line']} "
                    f"=> {item['message']}\n"
                )

            file.write(
                "\n## Recommended Actions\n\n"
            )

            file.write(
                "1. Investigate CRITICAL events immediately.\n"
            )

            file.write(
                "2. Review ERROR events.\n"
            )

            file.write(
                "3. Monitor WARNING events.\n"
            )