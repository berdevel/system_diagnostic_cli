import argparse
import time
from pathlib import Path

from colorama import init, Fore

from parsers.log_parser import LogParser
from parsers.redfish_parser import RedfishParser
from database.sqlite_manager import SQLiteManager
from reports.markdown_generator import MarkdownGenerator

init(autoreset=True)


class DiagnosticTool:

    def analyze_all_logs(self):

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

            self.run(str(logfile))

    def run(self, logfile):

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

        print(
            Fore.WHITE +
            f"Processing log: {logfile}"
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

            for event in critical_events:

                print(
                    f"ID {event['event_id']} | "
                    f"{event['gpu']} | "
                    f"XID {event['xid']} | "
                    f"{event['failure']}"
                )

            database = SQLiteManager()
            database.save_findings(findings)

            report = MarkdownGenerator()

            report.generate(
                findings,
                critical_events,
                logfile
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

            critical_count = len(
                critical_events
            )

            print(
                Fore.GREEN +
                "\n========== RESULTS =========="
            )

            print(
                Fore.CYAN +
                f"Total Findings : {len(findings)}"
            )

            print(
                Fore.YELLOW +
                f"Bianca 1 Issues : {bianca1_count}"
            )

            print(
                Fore.MAGENTA +
                f"Bianca 2 Issues : {bianca2_count}"
            )

            print(
                Fore.RED +
                f"Critical Events: {critical_count}"
            )

            print(
                Fore.BLUE +
                "Database       : diagnostics.db"
            )

            report_name = (
                Path(logfile).stem
            )

            print(
                Fore.BLUE +
                f"Report         : reports/{report_name}_Report.md"
            )

            print(
                Fore.GREEN +
                f"Process Time   : {elapsed_time} sec"
            )

            print("\nDetected Failures:")

            for item in findings:

                print(
                    f"[{item['bianca']}] "
                    f"{item['failure']} "
                    f"(Line {item['line']})"
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

        tool.analyze_all_logs()

    elif args.logfile:

        tool.run(args.logfile)

    else:

        parser.print_help()