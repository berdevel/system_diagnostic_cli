import argparse
import time
from pathlib import Path
import webbrowser
from collections import Counter

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from rich.progress import Progress
from rich.columns import Columns
from rich.console import Group

console = Console()

from colorama import init, Fore

from parsers.log_parser import LogParser
from parsers.redfish_parser import RedfishParser
from database.sqlite_manager import SQLiteManager

from reports.report_log_generator import (
    ReportLogGenerator
)

from reports.report_html_generator import (
    ReportHtmlGenerator
)

from parsers.root_cause_analyzer import (
    RootCauseAnalyzer
)

from config.root_cause_catalog import (
    CATALOG_VERSION
)

init(autoreset=True)


class DiagnosticTool:

    def analyze_all_logs(
        self,
        verbose=False
    ):

        logs_directory = Path("logs")

        if not logs_directory.exists():

            print("Logs directory not found.")

            return

        log_files = list(
            logs_directory.glob("*.txt")
        )

        if not log_files:

            print("No log files found.")

            return

        print(
            f"\nFound {len(log_files)} log files.\n"
        )

        for logfile in log_files:

            print(
                "\n================================================================="
            )

            print(
                f"Analyzing: {logfile.name}"
            )

            print(
                "=================================================================\n"
            )

            self.run(
                str(logfile),
                verbose=verbose
            )

    def run(
        self,
        logfile,
        verbose=False
    ):
        
        if not Path(logfile).exists():
            print(
                Fore.RED +
                f"ERROR: Log file not found -> {logfile}"
            )
            return

        console.clear()

        start_time = time.time()

        print(
            Fore.CYAN +
            "\n================ FOXCONN FAILURE ANALYZER v2.2.6 ================"
        )

        print()

        print(
            Fore.WHITE +
            f"Processing Log : "
            f"{Path(logfile).name}"
        )

        try:

            with Progress() as progress:

                task = progress.add_task(
                    "[cyan]Analyzing Log...",
                    total=4
                )

                parser = LogParser()

                findings = parser.parse_log(
                    logfile
                )

                progress.update(
                    task,
                    advance=1,
                    description="[cyan]Parsing Findings..."
                )

                redfish_parser = RedfishParser()

                critical_events = (
                    redfish_parser.parse_critical_events(
                        logfile,
                        args.date_from,
                        args.date_to
                    )
                )

                progress.update(
                    task,
                    advance=1,
                    description="[cyan]Parsing Critical Events..."
                )

                root_cause_analyzer = (
                    RootCauseAnalyzer()
                )

                root_causes = (
                    root_cause_analyzer.analyze(
                        findings,
                        critical_events
                    )
                )

                progress.update(
                    task,
                    advance=1,
                    description="[cyan]Running RCA..."
                )

                progress.update(
                    task,
                    advance=1,
                    description="[green]Completed"
                )

            primary = root_causes.get(
                "primary"
            )

            if verbose:
            
                for event in critical_events:

                    print(
                        f"\n[ID {event['event_id']}]"
                    )

                    if event.get("line"):

                        print(
                            f"Line       : "
                            f"{event['line']}"
                        )

                    if event.get("gpu") not in [
                        None,
                        "",
                        "Unknown"
                    ]:

                        print(
                            f"GPU        : "
                            f"{event['gpu']}"
                        )

                    if event.get("cpu") not in [
                        None,
                        "",
                        "Unknown"
                    ]:

                        print(
                            f"CPU        : "
                            f"{event['cpu']}"
                        )

                    if event.get("bianca") not in [
                        None,
                        "",
                        "Unknown",
                        "N/A"
                    ]:

                        print(
                            f"Bianca     : "
                            f"{event['bianca']}"
                        )

                    if event.get("coldplate") not in [
                        None,
                        "",
                        "Unknown",
                        "N/A"
                    ]:

                        print(
                            f"Coldplate  : "
                            f"{event['coldplate']}"
                        )

                    if event.get("xid") not in [
                        None,
                        "",
                        "Unknown",
                        "N/A"
                    ]:

                        print(
                            f"XID        : "
                            f"{event['xid']}"
                        )

                    severity = event.get(
                        "xid_severity",
                        "Info"
                    )

                    if severity == "Critical":

                        color = Fore.RED

                    elif severity == "Error":

                        color = Fore.MAGENTA

                    elif severity == "Warning":

                        color = Fore.YELLOW

                    else:

                        color = Fore.CYAN

                    print(
                        color +
                        f"Failure    : "
                        f"{event.get('failure','Unknown')}"
                    )

                    print(
                        color +
                        f"Severity   : "
                        f"{severity}"
                    )

            serial_number = (
                Path(logfile)
                .stem
                .split("_")[0]
            )

            database = SQLiteManager()
            database.save_analysis(

                serial_number,

                logfile,

                root_causes,

                len(findings),

                len(critical_events)

            )

            database.save_findings(

                serial_number,

                findings

            )

            database.save_critical_events(

                serial_number,

                critical_events

            )

            database.close()

            ReportLogGenerator().generate(
                findings,
                critical_events,
                logfile,
                root_causes,
                serial_number
            )

            ReportHtmlGenerator().generate(
                findings,
                critical_events,
                logfile,
                root_causes,
                serial_number
            )

            report_name = Path(logfile).stem

            html_report = (
                Path("reports") /
                f"{report_name}_Report.html"
            )

            try:

                webbrowser.open(
                    html_report.resolve().as_uri()
                )

            except:

                pass

            elapsed_time = round(
                time.time() - start_time,
                2
            )

            bianca1_count = sum(

                1

                for item in findings

                if item.get(
                    "bianca"
                ) in [

                    "Bianca#1",
                    "Bianca 1"

                ]

            )

            bianca2_count = sum(

                1

                for item in findings

                if item.get(
                    "bianca"
                ) in [

                    "Bianca#2",
                    "Bianca 2"

                ]

)

            coldplate_count = sum(

                1

                for item in findings

                if item.get("component")
                == "Coldplate"

            )

            cx8_count = sum(

                1

                for item in findings

                if item.get("component")
                == "CX8"

            )

            thermal_findings = sorted({

                item.get(
                    "coldplate"
                )

                for item in findings

                if item.get(
                    "coldplate"
                ) not in [

                    "Unknown",
                    "N/A",
                    None,
                    ""

                ]

            })

            critical_count = len(
                critical_events
            )

            summary = Table(

                title="Analysis Summary",
                box=box.ROUNDED,
                border_style="cyan",
                header_style="bold cyan"

            )

            summary.add_column(
                "Metric"
            )

            summary.add_column(
                "Value"
            )

            summary.add_row(
                "Serial Number",
                serial_number
            )

            summary.add_row(
                "Findings",
                str(len(findings))
            )

            summary.add_row(
                "Critical Events",
                str(critical_count)
            )

            summary.add_row(
                "Bianca #1 Issues",
                str(bianca1_count)
            )

            summary.add_row(
                "Bianca #2 Issues",
                str(bianca2_count)
            )

            summary.add_row(
                "Coldplate Issues",
                str(coldplate_count)
            )

            summary.add_row(
                "CX8 Issues",
                str(cx8_count)
            )

            top_findings = Counter(

                item.get(
                    "failure",
                    "Unknown"
                )

                for item in findings

            )

            top_table = Table(

                title="Top Findings",
                box=box.ROUNDED,
                border_style="yellow",
                header_style="bold yellow"

            )

            top_table.add_column(
                "Failure"
            )

            top_table.add_column(
                "Count",
                justify="right"
            )

            for failure, qty in (

                top_findings.most_common(5)

            ):

                top_table.add_row(
                    failure,
                    str(qty)
                )

            critical_counter = Counter(

                event.get(
                    "failure",
                    "Unknown"
                )

                for event in critical_events

            )

            top_events = Table(

                title="Top Critical Events",
                box=box.ROUNDED,
                border_style="magenta",
                header_style="bold magenta"

            )

            top_events.add_column(
                "Critical Event"
            )

            top_events.add_column(
                "Count",
                justify="right"
            )

            for failure, qty in (

                critical_counter.most_common(5)

            ):

                top_events.add_row(
                    failure,
                    str(qty)
                )

            print()

            if primary:

                severity_color = {

                    "HIGH": "red",

                    "MEDIUM": "yellow",

                    "LOW": "cyan"

                }.get(
                    primary["confidence"],
                    "white"
                )

                rca = Table(
                
                    title="Primary Root Cause",
                    box=box.ROUNDED,
                    border_style="red",
                    header_style="bold red"
    
                )
    
                rca.add_column(
                    "Metric"
                )
    
                rca.add_column(
                    "Value"
                )
    
                rca.add_row(
                    "Rule ID",
                    f"{primary['id']}"
                )
    
                rca.add_row(
                    "Confidence",
                    f"[{severity_color}]{primary['confidence']}[/{severity_color}]"
                )
    
                rca.add_row(
                    "RCA Score",
                    f"{primary.get('score','N/A')}"
                )
    
                rca.add_row(
                    "Latest Event",
                    f"{primary.get('latest_event_id','N/A')}"
                )

                recommendation = (

                    primary.get(
                        "recommendation",
                        ""
                    )
                    .strip()

                )

                if verbose:

                    print()

                    print(
                        Fore.GREEN +
                        "Recommended Actions:"
                    )

                    for line in recommendation.splitlines():

                        if line.strip():

                            print(
                                Fore.GREEN +
                                line.strip()
                            )

            console.print()
                        
            console.print(

                Columns(

                    [

                        summary,

                        rca

                    ],

                    width=40,

                    equal=True,

                    expand=True

                )

            )

            console.print()
            
            console.print(

                Columns(

                    [

                        top_table,

                        top_events

                    ],

                   width=40,

                    equal=True,

                    expand=True

                )

            )

            secondary = root_causes.get(
                "secondary",
                []
            )

            if secondary:

                secondary_table = Table(
                    title="Secondary RCA Matches",
                    box=box.ROUNDED,
                    border_style="green",
                    header_style="bold green"
                )

                secondary_table.add_column("Rule")
                secondary_table.add_column("Name")

                for rule in secondary[:3]:

                    secondary_table.add_row(
                        rule["id"],
                        rule["name"]
                    )

            if thermal_findings:

                thermal_table = Table(
                    title="Secondary Findings",
                    box=box.ROUNDED,
                    border_style="purple",
                    header_style="bold purple"
                )

                thermal_table.add_column(
                    "Finding"
                )

                for coldplate in thermal_findings:

                    thermal_table.add_row(
                        f"{coldplate} Coldplate Thermal Event"
                    )

            outputs = Table(
                title="Generated Outputs",
                box=box.ROUNDED,
                border_style="blue",
                header_style="bold blue"
            )

            outputs.add_column("Artifact")
            outputs.add_column("Location")

            outputs.add_row(
                "Catalog Version",
                CATALOG_VERSION
            )

            outputs.add_row(
                "Database",
                "diagnostics.db"
            )

            outputs.add_row(
                "LOG Report",
                f"reports/{report_name}_Report.log"
            )

            outputs.add_row(
                "HTML Report",
                f"reports/{report_name}_Report.html"
            )

            outputs.add_row(
                "Process Time",
                f"{elapsed_time} sec"
            )

            console.print()

            console.print(

                Columns(

                    [

                        secondary_table,

                        thermal_table

                    ],

                    width=40,

                    equal=True,

                    expand=True

                )

            )

            console.print()
            console.print(outputs)

            if verbose:
            
                print("\nDetected Failures:")

                for item in findings:

                    print()

                    print(
                        f"Event ID  : "
                        f"{item.get('event_id', 'N/A')}"
                    )

                    print(
                        f"Component : "
                        f"{item.get('component', 'Unknown')}"
                    )

                    if item.get("bianca") != "N/A":

                        print(
                            f"Bianca    : "
                            f"{item['bianca']}"
                        )

                    if item.get("coldplate") != "N/A":

                        print(
                            f"Coldplate : "
                            f"{item['coldplate']}"
                        )

                    if item.get("cx8") != "N/A":

                        print(
                            f"CX8       : "
                            f"{item['cx8']}"
                        )

                    print(
                        f"Failure   : "
                        f"{item['failure']}"
                    )

                    print(
                        f"Line      : "
                        f"{item['line']}"
                    )

                    print(
                        "-" * 40
                    )

        except Exception as error:

            import traceback

            print(
                Fore.RED +
                "\nExecution Failed"
            )

            print(
                Fore.RED +
                f"Reason: {error}"
            )

            print(
                Fore.RED +
                "\nFull Traceback:\n"
            )

            traceback.print_exc()

        print("\n" * 1)

    def show_history(

        self,
        serial_number,
        date_from=None,
        date_to=None

    ):

        database = SQLiteManager()

        history = database.get_serial_history(

            serial_number,

            date_from,

            date_to

        )

        print(
            "\n================================="
        )

        print(
            f"SERIAL HISTORY"
        )

        print(
            "=================================\n"
        )

        print(
            f"Serial Number : {serial_number}\n"
        )

        if not history:

            print(
                "No records found."
            )

            return

        for row in history:

            print(
                f"Date       : {row[0]}"
            )

            print(
                f"Root Cause : {row[1]}"
            )

            print(
                f"Confidence : {row[2]}"
            )

            print("-" * 40)

    def show_top_rca(

        self,
        date_from=None,
        date_to=None

    ):

        database = SQLiteManager()

        results = (
            database.get_top_root_causes(

                date_from,

                date_to

            )
        )

        print(
            "\n================================="
        )

        print(
            "TOP ROOT CAUSES"
        )

        print(
            "=================================\n"
        )

        for name, total in results:

            print(
                f"{total:>5}  {name}"
            )

    def show_top_components(self):

        database = SQLiteManager()

        results = (
            database.get_top_components()
        )

        print(
            "\n================================="
        )

        print(
            "TOP COMPONENT FAILURES"
        )

        print(
            "=================================\n"
        )

        for component, total in results:

            print(
                f"{total:>5}  {component}"
            )

    def show_top_serials(self):

        database = SQLiteManager()

        results = (
            database.get_top_serials()
        )

        print(
            "\n================================="
        )

        print(
            "MOST PROBLEMATIC SERIALS"
        )

        print(
            "=================================\n"
        )

        for serial, total in results:

            print(
                f"{total:>5}  {serial}"
            )

    def show_summary(

        self,
        date_from=None,
        date_to=None

    ):

        database = SQLiteManager()

        summary = database.get_summary(

            date_from,
            date_to

        )

        top_rca = database.get_top_root_causes(

            date_from,
            date_to

        )

        top_components = (
            database.get_top_components()
        )

        print(
            "\n================================="
        )

        print(
            "DIAGNOSTIC SUMMARY"
        )

        print(
            "=================================\n"
        )

        if date_from or date_to:

            print(
                f"From : {date_from}"
            )

            print(
                f"To   : {date_to}\n"
            )

        print(
            f"Total Analyses   : "
            f"{summary[0] or 0}"
        )

        print(
            f"Total Findings   : "
            f"{summary[1] or 0}"
        )

        print(
            f"Critical Events  : "
            f"{summary[2] or 0}"
        )

        print()

        print(
            "Top RCA"
        )

        print(
            "-" * 25
        )

        for name, qty in top_rca[:5]:

            print(
                f"{qty:>5}  {name}"
            )

        print()

        print(
            "Top Components"
        )

        print(
            "-" * 25
        )

        for component, qty in top_components[:5]:

            print(
                f"{qty:>5}  {component}"
            )

    def show_serial_report(

        self,
        serial_number

    ):

        database = SQLiteManager()

        report = (

            database.get_serial_report(
                serial_number
            )

        )

        database.close()

        print(
            "\n================================="
        )

        print(
            "SERIAL REPORT"
        )

        print(
            "=================================\n"
        )

        print(
            f"Serial Number : "
            f"{serial_number}\n"
        )

        general = report["general"]

        total_analyses = general[0] or 0

        first_seen = general[1] or "N/A"

        last_seen = general[2] or "N/A"

        print(
            f"Total Analyses : "
            f"{total_analyses}"
        )

        print(
            f"First Analysis : "
            f"{first_seen}"
        )

        print(
            f"Latest Analysis: "
            f"{last_seen}"
        )

        print()

        print(
            "-" * 40
        )

        print(
            "RCA HISTORY"
        )

        print(
            "-" * 40
        )

        print()

        for rca, qty in report["rca"]:

            print(
                f"{qty:>5}  {rca}"
            )

        print()

        print(
            "-" * 40
        )

        print(
            "COMPONENT HISTORY"
        )

        print(
            "-" * 40
        )

        print()

        for component, qty in report["components"]:

            print(
                f"{qty:>5}  {component}"
            )

        print()

        critical = report["critical"]

        if critical:

            print(
                "-" * 40
            )

            print(
                "CRITICAL EVENTS"
            )

            print(
                "-" * 40
            )

            print()

            total_criticals = sum(

                qty

                for _, qty in critical

            )

            print(
                f"Total Critical Events : "
                f"{total_criticals}"
            )

            print()

            print(
                "Most Frequent:"
            )

            print(
                critical[0][0]
            )

            print()

        if report["rca"]:

            top_rca = report["rca"][0]

            print(
                "-" * 40
            )

            print(
                "REPAIR RECOMMENDATION"
            )

            print(
                "-" * 40
            )

            print()

            print(
                "Most Frequent RCA"
            )

            print(
                top_rca[0]
            )

            print()

            if top_rca[1] >= 3:

                print(
                    "Status"
                )

                print(
                    "RECURRING FAILURE DETECTED"
                )

def show_menu():

    console.clear()

    console.print()

    logs_count = len(
                list(
                    Path("logs").glob("*.txt")
                )
            )

    menu_grid = Table.grid(
        padding=(0, 2)
    )

    menu_grid.add_column(width=50)
    menu_grid.add_column(width=35)

    logo = """
    [bold cyan]
               ███████╗███████╗ █████╗
               ██╔════╝██╔════╝██╔══██╗
               █████╗  █████╗  ███████║
               ██╔══╝  ██╔══╝  ██╔══██║
               ██║     ██║     ██║  ██║
               ╚═╝     ╚═╝     ╚═╝  ╚═╝
    [/bold cyan]
          [bold bright_white]FOXCONN FAILURE ANALYZER[/bold bright_white] [bold yellow]v2.2.6[/bold yellow]
      [bright_black]NVIDIA HGX / GB200 Diagnostic Platform[/bright_black]
    """

    menu_text = f"""
    [cyan]Catalog Version:[/cyan] {CATALOG_VERSION}
    [cyan]Logs Available :[/cyan] {logs_count}

    [bold]1[/bold]  Analyze Log
    [bold]2[/bold]  Analyze All Logs
    [bold]3[/bold]  Serial History
    [bold]4[/bold]  Serial Report
    [bold]5[/bold]  Top RCA
    [bold]6[/bold]  Top Components
    [bold]7[/bold]  Top Serials
    [bold]8[/bold]  Summary
    [bold red]9[/bold red]  Exit
    """

    menu_grid.add_row(
        logo,
        menu_text
    )

    console.print(

        Panel.fit(

            menu_grid,

            border_style="cyan",

            title="",

            padding=(0, 1)

        )

    )

    console.print()

    return input(
        Fore.CYAN +
        f"Select Option > " + Fore.WHITE
    ).strip()


def interactive_mode(tool):

    while True:

        option = show_menu()

        # ======================================
        # Analyze Single Log
        # ======================================

        if option == "1":

            logs = sorted(
                list(
                    Path("logs").glob(
                        "*.txt"
                    )
                )
            )

            if not logs:

                console.print(
                    "[red]No log files found[/red]"
                )

                continue

            table = Table(
                title="Available Logs",
                box=box.ROUNDED,
                header_style="bold cyan"
            )

            table.add_column(
                "#",
                justify="center"
            )

            table.add_column(
                "Log File"
            )

            table.add_column(
                "Size",
                justify="right"
            )

            for idx, log in enumerate(
                logs,
                start=1
            ):

                table.add_row(
                    str(idx),
                    log.name,
                    f"{round(log.stat().st_size / 1024, 1)} KB"
                )

            console.print(table)

            try:

                selection = int(
                    input(
                        Fore.CYAN +
                        f"\nSelect Log: " + Fore.WHITE
                    )
                )

                logfile = logs[
                    selection - 1
                ]

                tool.run(
                    str(logfile)
                )

                input(
                    Fore.YELLOW +
                    f"\nPress ENTER to return to menu..."
                )

            except Exception:

                console.print(
                    "[red]Invalid Selection[/red]"
                )

        # ======================================
        # Analyze All Logs
        # ======================================

        elif option == "2":

            tool.analyze_all_logs()

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Serial History
        # ======================================

        elif option == "3":

            serial = input(
                Fore.CYAN +
                f"\nSerial Number: " + Fore.WHITE
            )

            tool.show_history(
                serial
            )

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Serial Report
        # ======================================

        elif option == "4":

            serial = input(
                Fore.CYAN +
                f"\nSerial Number: " + Fore.WHITE
            )

            tool.show_serial_report(
                serial
            )

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Top RCA
        # ======================================

        elif option == "5":

            tool.show_top_rca()

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Top Components
        # ======================================

        elif option == "6":

            tool.show_top_components()

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Top Serials
        # ======================================

        elif option == "7":

            tool.show_top_serials()

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Summary
        # ======================================

        elif option == "8":

            tool.show_summary()

            input(
                Fore.YELLOW +
                f"\nPress ENTER to return to menu..."
            )

        # ======================================
        # Exit
        # ======================================

        elif option == "9":

            print(
                Fore.YELLOW +
                f"\nGoodbye.\n"
            )

            break

        else:

            print(
                "\nInvalid Option.\n"
            )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="FOXCONN HGX Failure Analyzer"
    )

    parser.add_argument(
        "logfile",
        nargs="?",
        help="Path to log file"
    )

    parser.add_argument(
        "--generate",
        type=int,
        help="Generate N fake log lines"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Analyze all logs in logs folder"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed findings and critical events"
    )

    parser.add_argument(
        "--history",
        help="Show history for a serial number"
    )

    parser.add_argument(
        "--top-rca",
        action="store_true",
        help="Show top root causes"
    )

    parser.add_argument(
        "--top-components",
        action="store_true",
        help="Show top component failures"
    )

    parser.add_argument(
        "--top-serials",
        action="store_true",
        help="Show most problematic serials"
    )

    parser.add_argument(
        "--from",
        dest="date_from",
        help="Start date (YYYY-MM-DD)"
    )

    parser.add_argument(
        "--to",
        dest="date_to",
        help="End date (YYYY-MM-DD)"
    )

    parser.add_argument(

        "--summary",

        action="store_true",

        help="Show historical summary"

    )

    parser.add_argument(

        "--serial-report",

        help="Generate historical report for a serial number"

    )

    args = parser.parse_args()

    tool = DiagnosticTool()

    advanced_mode = any(

        [

            args.logfile,

            args.generate,

            args.all,

            args.history,

            args.top_rca,

            args.top_components,

            args.top_serials,

            args.summary,

            args.serial_report

        ]

    )


    if args.generate:

        from generators.fake_log_generator import (
            FakeLogGenerator
        )

        generator = FakeLogGenerator()

        generator.generate(
            "logs/generated.log",
            args.generate
        )

        print(
            f"Generated {args.generate} lines."
        )

    elif args.all:

        tool.analyze_all_logs(
            verbose=args.verbose
        )

    elif args.history:

        tool.show_history(

            args.history,

            args.date_from,

            args.date_to

        )

    elif args.top_rca:

        tool.show_top_rca(

            args.date_from,

            args.date_to

        )

    elif args.top_components:

        tool.show_top_components()

    elif args.top_serials:

        tool.show_top_serials()

    elif args.logfile:

        tool.run(
            args.logfile,
            verbose=args.verbose
        )

    elif args.summary:

        tool.show_summary(

            args.date_from,

            args.date_to

        )

    elif args.serial_report:

        tool.show_serial_report(
            args.serial_report
        )

    else:

        if not advanced_mode:

            interactive_mode(
                tool
            )

        else:

            parser.print_help()