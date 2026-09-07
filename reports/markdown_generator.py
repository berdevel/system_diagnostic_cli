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
            f"reports/{report_name}_Report.log",
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
            # ROOT CAUSE ANALYSIS
            # ==========================================

            file.write(
                "\n---\n\n"
            )

            file.write(
                "# ROOT CAUSE ANALYSIS\n\n"
            )

            if root_causes and root_causes.get("primary"):

                primary = root_causes["primary"]

                primary_conditions = primary.get(
                    "conditions",
                    []
                )

                file.write(
                    "## EXECUTIVE SUMMARY\n\n"
                )

                file.write(
                    "| Item | Value |\n"
                )

                file.write(
                    "|------|-------|\n"
                )

                file.write(
                    f"| Rule ID | {primary['id']} |\n"
                )

                file.write(
                    f"| Cause | {primary['name']} |\n"
                )

                file.write(
                    f"| Confidence | {primary['confidence']} |\n"
                )

                file.write(
                    f"| Priority | {primary['priority']} |\n"
                )

                file.write(
                    f"| Matched Conditions | {primary.get('matched_conditions','N/A')} |\n"
                )

                file.write(
                    f"| RCA Score | {primary.get('score','N/A')} |\n"
                )

                if primary.get("latest_event_id"):

                    file.write(
                        f"Latest Supporting Event | {primary.get('latest_event_id','N/A')} |\n\n"
                    )

                file.write("\n")

                if primary.get("potential_causes"):

                    file.write(
                        "Potential Causal Events\n\n"
                    )

                    for event_id in primary[
                        "potential_causes"
                    ]:

                        file.write(
                            f"- Event ID {event_id}\n"
                        )

                    file.write("\n")

                rca_biancas = set()

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

                        bianca = (
                            item.get(
                                "bianca",
                                ""
                            )
                            .replace(
                                "Bianca 1",
                                "Bianca#1"
                            )
                            .replace(
                                "Bianca 2",
                                "Bianca#2"
                            )
                        )

                        if bianca not in [

                            None,
                            "",
                            "Unknown",
                            "N/A"

                        ]:

                            rca_biancas.add(
                                bianca
                            )

                affected_coldplates = sorted({

                    event.get("coldplate")

                    for event in findings

                    if event.get("coldplate") not in [
                        None,
                        "",
                        "Unknown",
                        "N/A"
                    ]

                })

                file.write(
                    "## Affected Components\n\n"
                )

                for bianca in sorted(
                    rca_biancas
                ):

                    file.write(
                        f"- {bianca}\n"
                    )

                for coldplate in affected_coldplates:

                    file.write(
                        f"- {coldplate} Coldplate\n"
                    )

                file.write("\n")

                file.write(
                    "## Recommended Actions\n\n"
                )

                file.write(
                    primary["recommendation"] + "\n\n"
                )

                supporting_events = set()

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

                        supporting_events.add(
                            item.get("event_id")
                        )

                for event in (critical_findings or []):

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

                        for condition in primary_conditions

                    ):

                        supporting_events.add(
                            event.get("event_id")
                        )

                if supporting_events:

                    file.write(
                        "## RCA Evidence Timeline\n\n"
                    )

                    file.write(
                        "| Sequence | Event ID |\n"
                    )

                    file.write(
                        "|----------|----------|\n"
                    )

                    for idx, event_id in enumerate(

                        sorted(supporting_events),

                        start=1

                    ):

                        file.write(
                            f"| {idx} | {event_id} |\n"
                        )

                    file.write("\n")

                secondary = root_causes.get(
                    "secondary",
                    []
                )

                if secondary:

                    file.write(
                        "## Secondary Findings\n\n"
                    )

                    for rule in secondary:

                        file.write(
                            f"- {rule['name']} "
                            f"(Priority {rule['priority']})\n"
                        )

            else:

                file.write(
                    "No matching root cause rule found.\n"
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

                            bianca = (
                                item["bianca"]
                                .replace(
                                    "Bianca 1",
                                    "Bianca#1"
                                )
                                .replace(
                                    "Bianca 2",
                                    "Bianca#2"
                                )
                            )

                            locations.add(
                                bianca
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
    "## Top Critical Events\n\n"
                )

                file.write(
                    "| Critical Event | Count |\n"
                )

                file.write(
                    "|---------------|-------|\n"
                )

                for failure, qty in critical_counter.most_common(10):

                    file.write(
                        f"| {failure} | {qty} |\n"
                    )

                file.write("\n")

                file.write(
                    "## Critical Event Details\n\n"
                )

                file.write(
                    "| Event ID | Severity | Failure | GPU | CPU | Bianca | Location |\n"
                )

                file.write(
                    "|----------|----------|---------|-----|-----|--------|----------|\n"
                )

                sorted_events = sorted(

                    critical_findings,

                    key=lambda event: (

                        int(
                            event.get(
                                "event_id",
                                0
                            )
                        )

                        if str(
                            event.get(
                                "event_id",
                                0
                            )
                        ).isdigit()

                        else 0

                    )

                )

                for event in sorted_events:

                    gpu = event.get(
                        "gpu",
                        ""
                    )

                    cpu = event.get(
                        "cpu",
                        ""
                    )

                    bianca = event.get(
                        "bianca",
                        ""
                    )

                    location = event.get(
                        "location",
                        ""
                    )

                    file.write(

                        f"| {event.get('event_id','')} "
                        f"| {event.get('severity','')} "
                        f"| {event.get('failure','')} "
                        f"| {gpu} "
                        f"| {cpu} "
                        f"| {bianca} "
                        f"| {location} |\n"

                    )

                file.write("\n")

                file.write(
                    "## Event Descriptions\n\n"
                )

                file.write(
                    "| Event ID | Description |\n"
                )

                file.write(
                    "|----------|-------------|\n"
                )

                for event in sorted_events:

                    description = (

                        event.get(
                            "description",
                            "N/A"
                        )
                        .replace("\n", " ")
                        .replace("|", "/")

                    )

                    file.write(

                        f"| {event.get('event_id','')} "
                        f"| {description} |\n"

                    )

                file.write("\n")

            else:

                file.write(
                    "No Critical Events detected.\n\n"
                )

        # ==========================================
        # HTML REPORT GENERATION
        # ==========================================

        log_file = (
            f"reports/{report_name}_Report.log"
        )

        html_file = (
            f"reports/{report_name}_Report.html"
        )

        with open(
            log_file,
            "r",
            encoding="utf-8"
        ) as md:

            md_content = md.read()

        html_body = markdown.markdown(
            md_content,
            extensions=["tables"]
        )

        dashboard = f"""
        <div class="card-container">

        <div class="card">
        <div class="card-title">Serial Number</div>
        <div class="card-value">{serial_number}</div>
        </div>

        <div class="card">
        <div class="card-title">Findings</div>
        <div class="card-value">{len(findings)}</div>
        </div>

        <div class="card">
        <div class="card-title">Critical Events</div>
        <div class="card-value">{len(critical_findings or [])}</div>
        </div>

        <div class="card">
        <div class="card-title">Primary RCA</div>
        <div class="card-value">
        {
        root_causes["primary"]["id"]
        if root_causes and root_causes.get("primary")
        else "N/A"
        }
        </div>
        </div>

        <div class="card rca-score">
        <div class="card-title">RCA Score</div>
        <div class="card-value">
        {
        root_causes["primary"].get("score","N/A")
        if root_causes and root_causes.get("primary")
        else "N/A"
        }
        </div>
        </div>
        <p>
        <div class="card latest-event">
        <div class="card-title">Latest Event</div>
        <div class="card-value">
        {
        root_causes["primary"].get("latest_event_id","N/A")
        if root_causes and root_causes.get("primary")
        else "N/A"
        }
        </div>
        </div>

        </div>
        """

        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">

        <head>

        <meta charset="UTF-8">

        <title>
        FoxconnFailureAnalyzer Report
        </title>

        <style>

        .card-container {{

            display: flex;

            flex-wrap: wrap;

            gap: 20px;

            margin-bottom: 40px;

            padding-bottom: 25px;

            border-bottom: 2px solid #d9d9d9;
        }}

        .card {{

            background: white;

            border-left: 6px solid #003366;

            border-radius: 10px;

            padding: 15px;

            min-width: 220px;

            box-shadow: 0 2px 8px rgba(0,0,0,.15);
        }}

        .card-title {{

            color: #666;

            font-size: 12px;
        }}

        .card-value {{

            color: #003366;

            font-size: 24px;

            font-weight: bold;
        }}

        .rca-score {{

            color: #008000;

            font-size: 28px;

            font-weight: bold;
        }}

        .latest-event {{

            color: #cc5500;

            font-size: 28px;

            font-weight: bold;
        }}

        table {{

            width: 100%;

            border-collapse: collapse;

            margin-top: 15px;

            margin-bottom: 20px;
        }}

        th {{

            background-color: #003366;

            color: white;

            padding: 12px;
        }}

        td {{

            border: 1px solid #ddd;

            padding: 10px;
        }}

        tr:hover {{

            background-color: #eef5ff;
        }}

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

        {dashboard}
        <p>
        <p>
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