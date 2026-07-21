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
            "\n========== FOXCONN FAILURE ANALYZER =========="
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
                    logfile
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

            database = SQLiteManager()
            database.save_findings(findings)

            serial_number = (
                Path(logfile)
                .stem
                .split("_")[0]
            )

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
                "\n================================="
            )

            print(
                "SUMMARY"
            )

            print(
                "=================================\n"
            )

            print(
                f"Serial Number      : "
                f"{serial_number}"
            )

            print()

            print(
                f"Total Findings     : "
                f"{len(findings)}"
            )

            print()

            print(
                f"Bianca Issues      : "
                f"{bianca1_count + bianca2_count}"
            )

            print(
                f"Coldplate Issues   : "
                f"{coldplate_count}"
            )

            print(
                f"CX8 Issues         : "
                f"{cx8_count}"
            )

            print()

            print(
                f"Critical Events    : "
                f"{critical_count}"
            )

            print()

            if primary:

                print(
                    "Primary Root Cause :"
                )

                print(
                    primary["name"]
                )

                print()

                print(
                    f"Confidence         : "
                    f"{primary['confidence']}"
                )

                print()

                print(
                    "Recommended Action :"
                )

                print(
                    primary["recommendation"]
                )

            if thermal_findings:

                print()

                print(
                    "Secondary Findings :"
                )

                for coldplate in thermal_findings:

                    print(
                        f"- {coldplate} Coldplate Thermal Event"
                    )

            report_name = Path(logfile).stem

            print(
                "\n================================="
            )

            print(
                "OUTPUTS"
            )

            print(
                "=================================\n"
            )

            print(
                "Database            : diagnostics.db"
            )

            print(
                f"Markdown Report     : "
                f"reports/{report_name}_Report.md"
            )

            print(
                f"HTML Report         : "
                f"reports/{report_name}_Report.html"
            )

            print()

            print(
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

    elif args.logfile:

        tool.run(
            args.logfile,
            verbose=args.verbose
        )

    else:

        parser.print_help()