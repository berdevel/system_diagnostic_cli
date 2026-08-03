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
        root_causes=None,
        serial_number="Unknown"
    ):

        report_name = Path(source_log).stem

        with open(
            f"reports/{report_name}_Report.md",
            "w",
            encoding="utf-8"
        ) as file:

            report_timestamp = datetime.now()

            file.write(
    "# FOXCONN FAILURE ANALYSIS REPORT\n\n"
            )

            file.write(
                "## System Information\n\n"
            )

            file.write(
                f"- Serial Number: "
                f"{serial_number}\n"
            )

            file.write(
                f"- Source Log: "
                f"{source_log}\n"
            )

            file.write(
                f"- Report Date: "
                f"{report_timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            file.write(
                f"- Total Component Failures: "
                f"{len(findings)}\n\n"
            )

            if findings:

                most_common_failure = Counter(

                    item["failure"]

                    for item in findings

                ).most_common(1)

                if most_common_failure:

                    failure_name = (
                        most_common_failure[0][0]
                    )

                    failure_count = (
                        most_common_failure[0][1]
                    )

                    file.write(
                        "## FAILURE HIGHLIGHTS\n\n"
                    )

                    if (

                        root_causes

                        and

                        root_causes.get(
                            "primary"
                        )

                    ):

                        file.write(

                            f"Primary Root Cause: "

                            f"{root_causes['primary']['name']}\n\n"

                        )

                    file.write(

                        f"Most Frequent Failure: "

                        f"{failure_name}\n\n"

                    )

                    file.write(

                        f"Occurrences: "

                        f"{failure_count}\n\n"

                    )

            # ==========================================
            # COMPONENT FAILURES
            # ==========================================

            file.write(
                "# COMPONENT FAILURE ANALYSIS\n\n"
            )

            if findings:

                component_counter = Counter(
                    item.get(
                        "component",
                        "Unknown"
                    )
                    for item in findings
                )

                file.write(
                    "## Component Failure Summary\n\n"
                )

                for component, total in component_counter.items():

                    file.write(
                        f"- {component}: {total}\n"
                    )

                file.write("\n")

                file.write(
                    "## Component Statistics\n\n"
                )

                component_groups = {}

                for item in findings:

                    component = item.get(
                        "component",
                        "Unknown"
                    )

                    if component not in component_groups:

                        component_groups[
                            component
                        ] = []

                    component_groups[
                        component
                    ].append(item)

                for component, items in component_groups.items():

                    file.write(
                        f"### {component}\n\n"
                    )

                    file.write(
                        f"- Total Failures : "
                        f"{len(items)}\n"
                    )

                    failure_counter = Counter(

                        item.get("failure")

                        for item in items

                    )

                    if failure_counter:

                        file.write(
                            "- Common Failures:\n"
                        )

                        for failure, qty in (

                            failure_counter.most_common()

                        ):

                            file.write(
                                f"  - {failure}: {qty}\n"
                            )

                    locations = set()

                    recommendations = set()

                    for item in items:

                        if item.get(
                            "bianca"
                        ) not in [

                            "Unknown",
                            "N/A"

                        ]:

                            locations.add(
                                item["bianca"]
                            )

                        if item.get(
                            "coldplate"
                        ) not in [

                            "Unknown",
                            "N/A"

                        ]:

                            locations.add(
                                f"{item['coldplate']} Coldplate"
                            )

                        if item.get(
                            "cx8"
                        ) not in [

                            "Unknown",
                            "N/A"

                        ]:

                            locations.add(
                                f"{item['cx8']} CX8"
                            )

                        if item.get(
                            "action"
                        ) not in [

                            None,
                            "",
                            "N/A"

                        ]:

                            recommendations.add(
                                item["action"]
                            )

                    if locations:

                        file.write(
                            "- Affected Components:\n"
                        )

                        for location in sorted(
                            locations
                        ):

                            file.write(
                                f"  - {location}\n"
                            )

                    if recommendations:

                        file.write(
                            "- Recommendations:\n"
                        )

                        for recommendation in sorted(
                            recommendations
                        ):

                            file.write(
                                f"  - {recommendation}\n"
                            )

                    file.write("\n")

                file.write(
                    "## Component Failure Details\n\n"
                )

                grouped_failures = {}

                for item in findings:

                    failure = item["failure"]

                    if failure not in grouped_failures:

                        grouped_failures[
                            failure
                        ] = []

                    grouped_failures[
                        failure
                    ].append(item)

                for failure, items in grouped_failures.items():

                    file.write(
                        f"### {failure}\n\n"
                    )

                    file.write(
                        f"Occurrences: "
                        f"{len(items)}\n\n"
                    )

                    file.write(
                        "Event IDs:\n\n"
                    )

                    sorted_items = sorted(

                        items,

                        key=lambda x: (

                            int(
                                x["event_id"]
                            )

                            if str(
                                x["event_id"]
                            ).isdigit()

                            else 999999

                        )

                    )

                    for item in sorted_items:

                        file.write(
                            f"- {item['event_id']}\n"
                        )

                    file.write("\n")

                    first_item = items[0]

                    file.write(
                        f"Component: "
                        f"{first_item.get('component')}\n\n"
                    )

                    if first_item.get(
                        "assembly"
                    ) not in [

                        "Unknown",
                        "N/A",
                        None,
                        ""

                    ]:

                        file.write(
                            f"Assembly: "
                            f"{first_item['assembly']}\n\n"
                        )

                    if first_item.get(
                        "bianca"
                    ) not in [

                        "Unknown",
                        "N/A"

                    ]:

                        file.write(
                            f"Bianca: "
                            f"{first_item['bianca']}\n\n"
                        )

                    if first_item.get(
                        "coldplate"
                    ) not in [

                        "Unknown",
                        "N/A"

                    ]:

                        file.write(
                            f"Coldplate: "
                            f"{first_item['coldplate']}\n\n"
                        )

                    if first_item.get(
                        "cx8"
                    ) not in [

                        "Unknown",
                        "N/A",
                        None,
                        ""

                    ]:

                        file.write(

                            f"CX8: "
                            f"{first_item['cx8']}\n\n"

                        )

                    file.write(
                        f"Recommendation: "
                        f"{first_item.get('action','N/A')}\n\n"
                    )

            else:

                file.write(

                    "No repairable component "
                    "was identified.\n\n"

                )

                file.write(

                    "Critical events may exist "
                    "but could not be mapped "
                    "to a replaceable assembly.\n\n"

                )


            # ==========================================
            # NVIDIA CRITICAL EVENTS
            # ==========================================

            file.write(
                "\n---\n\n"
            )

            legacy_timestamps = any(

                event.get(
                    "invalid_timestamp",
                    False
                )

                for event in (

                    critical_findings

                    or

                    []

                )

            )

            file.write(
                "# NVIDIA CRITICAL EVENTS ANALYSIS\n\n"
            )

            if legacy_timestamps:

                file.write(

                    "WARNING: Legacy or invalid "
                    "BMC timestamps detected.\n\n"

                )


            if critical_findings:

                file.write(
                    f"Total Critical Events: "
                    f"{len(critical_findings)}\n\n"
                )

                critical_counter = Counter(

                    event.get(
                        "failure",
                        "Unknown"
                    )

                    for event in critical_findings

                )

                file.write(
                    "## Critical Event Summary\n\n"
                )

                for failure, qty in (

                    critical_counter.most_common()

                ):

                    file.write(
                        f"- {failure}: {qty}\n"
                    )

                file.write("\n")

                for event in critical_findings:

                    file.write(
                        "## CRITICAL EVENT\n\n"
                    )

                    file.write(
                        f"- Event ID       : "
                        f"{event.get('event_id', 'Unknown')}\n"
                    )

                    event_date = event.get(
                        "created",
                        "Unknown"
                    )

                    if event.get(
                        "invalid_timestamp",
                        False
                    ):

                        event_date = (
                            "Legacy / Invalid "
                            "BMC Timestamp"
                        )

                    file.write(
                        f"- Date           : "
                        f"{event_date}\n"
                    )


                    file.write(
                        f"- Severity       : "
                        f"{event.get('severity', 'Unknown')}\n"
                    )

                    if event.get("gpu") != "Unknown":
                    
                        file.write(
                            f"- GPU            : "
                            f"{event.get('gpu')}\n"
                        )

                    if event.get("cpu") != "Unknown":

                        file.write(

                            f"- CPU            : "
                            f"{event.get('cpu')}\n"

                        )

                    file.write(
                        f"- Bianca         : "
                        f"{event.get('bianca', 'Unknown')}\n"
                    )

                    if (

                        event.get("location") not in [

                            None,
                            "",
                            "Unknown",
                            "N/A"

                        ]

                        and

                        event.get("coldplate") == "N/A"

                        and

                        event.get("cx8") == "N/A"

                    ):

                        file.write(

                            f"- Location       : "
                            f"{event.get('location')}\n"

                        )

                    if event.get("coldplate") != "N/A":

                        file.write(
                            f"- Coldplate      : "
                            f"{event.get('coldplate')}\n"
                        )

                    if event.get("cx8") not in [

                        None,
                        "",
                        "Unknown",
                        "N/A"

                    ]:

                        file.write(

                            f"- CX8            : "
                            f"{event.get('cx8')}\n"

                        )

                    if event.get("xid") != "N/A":

                        file.write(
                            f"- XID            : "
                            f"{event.get('xid')}\n"
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

            if (

                root_causes

                and

                root_causes.get(
                    "primary"
                )

            ):

                primary = (
                    root_causes[
                        "primary"
                    ]
                )

                file.write(
                    "## PRIMARY ROOT CAUSE\n\n"
                )

                file.write(
                    f"Serial Number: "
                    f"{serial_number}\n\n"
                )

                file.write(
                    f"Catalog Version: "
                    f"{root_causes['catalog_version']}\n\n"
                )

                file.write(
                    f"Rule ID: "
                    f"{primary['id']}\n\n"
                )

                file.write(
                    f"Rule Version: "
                    f"{primary['version']}\n\n"
                )

                file.write(
                    f"Priority: "
                    f"{primary['priority']}\n\n"
                )

                file.write(
                    f"Cause: "
                    f"{primary['name']}\n\n"
                )

                file.write(
                    f"Confidence: "
                    f"{primary['confidence']}\n\n"
                )

                affected_biancas = sorted({

                    event.get(
                        "bianca"
                    )
                    .replace(
                        "Bianca 1",
                        "Bianca#1"
                    )
                    .replace(
                        "Bianca 2",
                        "Bianca#2"
                    )

                    for event in findings

                    if event.get(
                        "bianca"
                    ) not in [

                        "Unknown",
                        "N/A",
                        None,
                        ""

                    ]

                })

                affected_cx8 = sorted({

                    event.get(
                        "cx8"
                    )

                    for event in findings

                    if event.get(
                        "cx8"
                    ) not in [

                        "Unknown",
                        "N/A",
                        None,
                        ""

                    ]

                })

                affected_coldplates = sorted({

                    event.get(
                        "coldplate",
                        "N/A"
                    )

                    for event in findings

                    if event.get(
                        "coldplate"
                    ) not in [

                        "Unknown",
                        "N/A",
                        None,
                        ""

                    ]

                })

                primary_conditions = []

                if root_causes and root_causes.get(
                    "primary"
                ):

                    primary_conditions = (

                        root_causes["primary"]
                        .get(
                            "conditions",
                            []
                        )

                    )

                supporting_events = []

                for item in findings:

                    failure = (

                        item.get(
                            "failure",
                            ""
                        ).upper()

                    )

                    if any(

                        condition.upper() in failure

                        for condition in primary_conditions

                    ):

                        supporting_events.append(

                            item.get(
                                "event_id"
                            )

                        )


                if supporting_events:

                    file.write(
                        "Evidence Supporting RCA:\n\n"
                    )

                    for event_id in supporting_events:

                        file.write(
                            f"- Event ID {event_id}\n"
                        )

                    file.write("\n")

                if affected_biancas:

                    file.write(
                        "Affected Bianca Modules:\n\n"
                    )

                    for bianca in affected_biancas:

                        file.write(
                            f"- {bianca}\n"
                        )

                    file.write("\n")

                file.write(
                    "Recommended Actions:\n\n"
                )

                file.write(
                    primary[
                        "recommendation"
                    ] + "\n\n"
                )

                if affected_biancas:

                    file.write(
                        "Implementation Notes:\n\n"
                    )

                    file.write(
                        "- Bianca replacement includes the corresponding coldplate assembly.\n\n"
                    )

                if affected_coldplates:

                    file.write(
                        "Additional Thermal Findings:\n\n"
                    )

                    for coldplate in affected_coldplates:

                        file.write(
                            f"- Thermal event detected on "
                            f"{coldplate} Coldplate\n"
                        )

                    file.write("\n")

                    file.write(
                        "Recommended Thermal Actions:\n\n"
                    )

                    file.write(
                        "- Inspect TIM condition\n"
                    )

                    file.write(
                        "- Verify coldplate contact pressure\n"
                    )

                    file.write(
                        "- Review temperature history\n\n"
                    )

                if affected_cx8:

                    file.write(
                        "Affected CX8 Modules:\n\n"
                    )

                    for cx8 in affected_cx8:

                        file.write(
                            f"- {cx8} CX8\n"
                        )

                    file.write("\n")

                secondary = (
                    root_causes.get(
                        "secondary",
                        []
                    )
                )

                if secondary:

                    file.write(
                        "## SECONDARY FINDINGS\n\n"
                    )

                    for rule in secondary:

                        file.write(
                            f"- {rule['name']} "
                            f"(Priority "
                            f"{rule['priority']})\n"
                        )

            else:

                file.write(
                    "No matching root cause rule found.\n"
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