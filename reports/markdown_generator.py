from collections import Counter


class MarkdownGenerator:

    def generate(self, findings):

        counts = Counter(
            item["severity"]
            for item in findings
        )

        with open(
            "DiagnosticReport.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("# System Diagnostic Report\n\n")

            file.write("## Summary\n\n")

            for level, qty in counts.items():

                file.write(
                    f"- {level}: {qty}\n"
                )

            file.write("\n## Findings\n\n")

            for item in findings:

                file.write(
                    f"- [{item['severity']}] "
                    f"Line {item['line']} : "
                    f"{item['message']}\n"
                )