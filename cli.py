import argparse
import time
from pathlib import Path

from colorama import init, Fore

from parsers.log_parser import LogParser
from parsers.redfish_parser import RedfishParser
from database.sqlite_manager import SQLiteManager
from reports.markdown_generator import MarkdownGenerator

from parsers.root_cause_analyzer import (
    RootCauseAnalyzer
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
                "\n================================="
            )

            print(
                f"Analyzing: {logfile.name}"
            )

            print(
                "=================================\n"
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

        start_time = time.time()

        print(
            Fore.CYAN +
            "\n========== FOXCONN FAILURE ANALYZER v2.2 =========="
        )

        print()

        print(
            Fore.WHITE +
            f"Processing Log : "
            f"{Path(logfile).name}"
        )

        try:

            parser = LogParser()
            findings = parser.parse_log(logfile)

            # NUEVO PARSER PARA EVENTOS CRÍTICOS REDFISH
            redfish_parser = RedfishParser()

            critical_events = (
                redfish_parser.parse_critical_events(

                    logfile,

                    args.date_from,

                    args.date_to

                )
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

                    print(
                        f"Failure    : "
                        f"{event.get('failure','Unknown')}"
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

            report = MarkdownGenerator()

            report.generate(
                findings,
                critical_events,
                logfile,
                root_causes,
                serial_number
            )

            elapsed_time = round(
                time.time() - start_time,
                2
            )

            bianca1_count = sum(
                1
                for item in findings
                if item["bianca"] == "Bianca 1"
            )

            bianca2_count = sum(
                1
                for item in findings
                if item["bianca"] == "Bianca 2"
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

            print(
                Fore.CYAN +
                "\n================================="
            )

            print(
                Fore.CYAN +
                "SUMMARY"
            )

            print(
                Fore.CYAN +
                "=================================\n"
            )

            print(
                Fore.WHITE +
                f"Serial Number      : "
                f"{serial_number}"
            )

            print()

            print(
                Fore.GREEN +
                f"Total Findings     : "
                f"{len(findings)}"
            )

            print()

            print(
                Fore.YELLOW +
                f"Bianca Issues      : "
                f"{bianca1_count + bianca2_count}"
            )

            print(
                Fore.BLUE +
                f"Coldplate Issues   : "
                f"{coldplate_count}"
            )

            print(
                Fore.MAGENTA +
                f"CX8 Issues         : "
                f"{cx8_count}"
            )


            print(
                Fore.RED +
                f"Critical Events    : "
                f"{critical_count}"
            )

            print()

            if primary:

                print()

                print(
                    Fore.CYAN +
                    "Primary Root Cause :"
                )

                print(
                    Fore.RED +
                    primary["name"]
                )

                print()

                print(
                    Fore.YELLOW +
                    f"Confidence         : "
                    f"{primary['confidence']}"
                )

                print()

                print(
                    Fore.GREEN +
                    "Recommended Action :"
                )

                print(
                    Fore.GREEN +
                    primary["recommendation"]
                )

            if thermal_findings:

                print()

                print(
                    Fore.MAGENTA +
                    "Secondary Findings :"
                )

                for coldplate in thermal_findings:

                    print(
                        Fore.MAGENTA +
                        f"- {coldplate} Coldplate Thermal Event"
                    )

            report_name = Path(logfile).stem

            print(
                Fore.CYAN +
                "\n================================="
            )

            print(
                Fore.CYAN +
                "OUTPUTS"
            )

            print(
                Fore.CYAN +
                "=================================\n"
            )

            print(
                Fore.BLUE +
                "Database            : diagnostics.db"
            )

            print(
                Fore.BLUE +
                f"Markdown Report     : "
                f"reports/{report_name}_Report.md"
            )

            print(
                Fore.BLUE +
                f"HTML Report         : "
                f"reports/{report_name}_Report.html"
            )

            print()

            print(
                Fore.GREEN +
                f"Process Time        : "
                f"{elapsed_time} sec"
            )

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

        parser.print_help()