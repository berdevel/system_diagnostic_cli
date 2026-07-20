from collections import Counter
from datetime import datetime
from pathlib import Path

import markdown


class MarkdownGenerator:

    def generate(
        self,
        findings,
        critical_findings=None,
        source_log="report",
        root_causes=None
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

            if root_causes:

                for cause in root_causes:

                    file.write(
                        f"## {cause['name']}\n\n"
                    )

                    file.write(
                        f"Confidence: "
                        f"{cause['confidence']}\n\n"
                    )

                    file.write(
                        "Recommended Actions:\n\n"
                    )

                    file.write(
                        f"{cause['recommendation']}\n\n"
                    )

            else:

                file.write(
                    "No matching root "
                    "cause rule found.\n"
                )

        # ==========================================
        # HTML REPORT GENERATION
        # ==========================================

        md_file = (
            f"reports/{report_name}_Report.md"
        )

        html_file = (
            f"reports/{report_name}_Report.html"
        )

        with open(
            md_file,
            "r",
            encoding="utf-8"
        ) as md:

            md_content = md.read()

        html_body = markdown.markdown(
            md_content,
            extensions=["tables"]
        )

        html_template = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>
FoxconnFailureAnalyzer Report
</title>

<style>

body {{
    font-family: Arial, sans-serif;
    max-width: 1200px;
    margin: auto;
    padding: 30px;
    background-color: #f4f6f9;
}}

.header {{
    background-color: #003366;
    color: white;
    padding: 20px;
    border-radius: 10px;
}}

.section {{
    background-color: white;
    padding: 20px;
    margin-top: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}}

h1 {{
    margin: 0;
}}

h2 {{
    color: #003366;
}}

h3 {{
    color: #0055aa;
}}

table {{
    width: 100%;
    border-collapse: collapse;
}}

th {{
    background-color: #003366;
    color: white;
    padding: 10px;
}}

td {{
    border: 1px solid #ddd;
    padding: 10px;
}}

tr:nth-child(even) {{
    background-color: #f2f2f2;
}}

code {{
    background-color: #efefef;
    padding: 2px 4px;
}}

</style>

</head>

<body>

<div class="header">

<h1>FoxconnFailureAnalyzer</h1>

<p>
Automated HGX / Bianca Diagnostic Report
</p>

</div>

<div class="section">

{html_body}

</div>

</body>

</html>
"""

        with open(
            html_file,
            "w",
            encoding="utf-8"
        ) as html:

            html.write(
                html_template
            )