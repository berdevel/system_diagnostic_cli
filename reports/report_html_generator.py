from pathlib import Path
from collections import Counter


class ReportHtmlGenerator:

    def generate(
        self,
        findings,
        critical_findings,
        source_log,
        root_causes,
        serial_number
    ):

        report_name = Path(source_log).stem

        html_file = (
            f"reports/{report_name}_Report.html"
        )

        primary = None

        if root_causes:

            primary = root_causes.get(
                "primary"
            )

        findings_count = len(findings)

        critical_count = len(
            critical_findings or []
        )

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

        event_rows = ""

        for item in findings:

            event_rows += f"""
            <tr>
                <td>{item.get('event_id','')}</td>
                <td>{item.get('component','')}</td>
                <td>{item.get('failure','')}</td>
            </tr>
            """

        events_table = f"""
        <div class="section">

            <h2>HMC Failure Events</h2>

            <table>

                <tr>
                    <th>Event ID</th>
                    <th>Component</th>
                    <th>Failure</th>
                </tr>

                {event_rows}

            </table>

        </div>
        """

        event_detail_rows = ""

        for item in findings:

            line_text = str(
                item.get(
                    "line",
                    ""
                )
            ).replace(
                "<",
                "&lt;"
            ).replace(
                ">",
                "&gt;"
            )

            event_detail_rows += f"""
            <tr>
                <td>{item.get('event_id','')}</td>
                <td>{line_text}</td>
            </tr>
            """

        event_details = f"""
        <div class="section">

            <h2>HMC Event Details</h2>

            <table>

                <tr>
                    <th>Event ID</th>
                    <th>Raw Event Text</th>
                </tr>

                {event_detail_rows}

            </table>

        </div>
        """

        recommendation_html = ""

        if primary:

            recommendation_html = f"""
            <div class="section">

                <h2>Recommended Actions</h2>

                <div class="recommendation">

                    <pre>
        {primary.get("recommendation","N/A")}
                    </pre>

                </div>

            </div>
            """

        description_rows = ""

        for event in (critical_findings or []):

            description_rows += f"""
            <tr>
                <td>{event.get('event_id','')}</td>
                <td>{event.get('description','')}</td>
            </tr>
            """

        description_table = f"""
        <div class="section">

        <h2>Event Descriptions</h2>

        <table>

        <tr>
        <th>Event ID</th>
        <th>Description</th>
        </tr>

        {description_rows}

        </table>

        </div>
        """

        critical_detail_rows = ""

        for event in (critical_findings or []):

            critical_detail_rows += f"""
            <tr>
                <td>{event.get('event_id','')}</td>
                <td>{event.get('severity','')}</td>
                <td>{event.get('gpu','')}</td>
                <td>{event.get('bianca','')}</td>
                <td>{event.get('failure','')}</td>
            </tr>
            """

        critical_details_table = f"""
        <div class="section">

        <h2>Critical Event Details</h2>

        <table>

        <tr>
        <th>Event ID</th>
        <th>Severity</th>
        <th>GPU</th>
        <th>Bianca</th>
        <th>Failure</th>
        </tr>

        {critical_detail_rows}

        </table>

        </div>
        """

        affected_components = sorted({

            item.get("component")

            for item in findings

            if item.get("component")

        })

        component_html = ""

        for component in affected_components:

            component_html += f"""
            <div class="component-chip">
                {component}
            </div>
            """

        components_section = f"""
        <div class="section">

        <h2>Affected Components</h2>

        <div class="component-container">

        {component_html}

        </div>

        </div>
        """

        findings_counter = Counter(
            item.get(
                "failure",
                "Unknown"
            )
            for item in findings
        )

        top_findings_rows = ""

        for failure, qty in findings_counter.most_common(10):

            top_findings_rows += f"""
            <tr>
                <td>{failure}</td>
                <td>{qty}</td>
            </tr>
            """

        top_findings_table = f"""
        <div class="section">

        <h2>Top Findings</h2>

        <table>

        <tr>
        <th>Failure</th>
        <th>Count</th>
        </tr>

        {top_findings_rows}

        </table>

        </div>
        """

        top_events_rows = ""

        for failure, qty in (
            critical_counter.most_common(10)
        ):

            top_events_rows += f"""
            <tr>
                <td>{failure}</td>
                <td>{qty}</td>
            </tr>
            """

        html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<title>
Foxconn Failure Analyzer
</title>

<style>

body {{
    font-family: Arial,sans-serif;
    background:#f4f6f9;
    max-width:1400px;
    margin:auto;
    padding:30px;
}}

.header {{
    background:#003366;
    color:white;
    padding:25px;
    border-radius:12px;
}}

.cards {{
    display:flex;
    flex-wrap:wrap;
    gap:20px;
    margin-top:25px;
}}

.card {{
    flex:1;
    min-width:250px;
    background:white;
    border-left:8px solid #0066cc;
    padding:20px;
    border-radius:12px;
    box-shadow:0 4px 12px rgba(0,0,0,.15);
}}

.card-title {{
    color:#666;
    font-size:12px;
    text-transform:uppercase;
}}

.card-value {{
    font-size:28px;
    font-weight:bold;
    margin-top:10px;
}}

.hero {{
    background:linear-gradient(
        135deg,
        #003366,
        #0055aa
    );

    color:white;

    padding:30px;

    border-radius:15px;

    margin-top:30px;
}}

.hero-name {{
    font-size:42px;
    font-weight:bold;
}}

.section {{
    background:white;
    margin-top:25px;
    padding:20px;
    border-radius:12px;
    box-shadow:0 4px 10px rgba(0,0,0,.08);
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th {{
    background:#003366;
    color:white;
    padding:10px;
}}

td {{
    border:1px solid #ddd;
    padding:10px;
}}

.recommendation {{

    background: #f8fbff;

    border-left: 6px solid #0055aa;

    padding: 20px;

    border-radius: 10px;

    white-space: pre-wrap;
}}

.component-container {{

    display:flex;

    flex-wrap:wrap;

    gap:10px;
}}

.component-chip {{

    background:#eef5ff;

    padding:10px 15px;

    border-radius:20px;

    border-left:4px solid #0055aa;
}}

</style>

</head>

<body>

<div class="header">

<pre>
███████╗███████╗ █████╗
██╔════╝██╔════╝██╔══██╗
█████╗  █████╗  ███████║
██╔══╝  ██╔══╝  ██╔══██║
██║     ██║     ██║  ██║
╚═╝     ╚═╝     ╚═╝  ╚═╝
</pre>

<h1>FOXCONN FAILURE ANALYZER</h1>

<p>NVIDIA HGX / GB200 Diagnostic Platform</p>

</div>

<div class="cards">

<div class="card">
<div class="card-title">Serial Number</div>
<div class="card-value">{serial_number}</div>
</div>

<div class="card">
<div class="card-title">Findings</div>
<div class="card-value">{findings_count}</div>
</div>

<div class="card">
<div class="card-title">Critical Events</div>
<div class="card-value">{critical_count}</div>
</div>

<div class="card">
<div class="card-title">RCA Score</div>
<div class="card-value">
{primary.get('score','N/A') if primary else 'N/A'}
</div>
</div>

<div class="card">
<div class="card-title">Latest Event</div>
<div class="card-value">
{primary.get('latest_event_id','N/A') if primary else 'N/A'}
</div>
</div>

</div>

<div class="hero">

<div>PRIMARY ROOT CAUSE</div>

<div class="hero-name">
{primary['name'] if primary else 'N/A'}
</div>

<div>
Confidence:
{primary['confidence'] if primary else 'N/A'}
</div>

</div>

{recommendation_html}

{components_section}

{top_findings_table}

<div class="section">

<h2>Top Critical Events</h2>

<table>

<tr>
<th>Critical Event</th>
<th>Count</th>
</tr>

{top_events_rows}

</table>

</div>

{events_table}

{event_details}

{critical_details_table}

{description_table}

</body>
</html>
"""

        with open(
            html_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)