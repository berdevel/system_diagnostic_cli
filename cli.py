import argparse
import time
from pathlib import Path

from parsers.log_parser import LogParser
from database.sqlite_manager import SQLiteManager
from reports.markdown_generator import MarkdownGenerator
from colorama import init, Fore, Style

init(autoreset=True)


class DiagnosticTool:

    def run(self, logfile):

        if not Path(logfile).exists():

            print(
                Fore.RED +
                Style.BRIGHT +
                f"ERROR: Log file not found -> {logfile}"
            )

            return

        start_time = time.time()

        
        print(
            Fore.CYAN +
            "\n========== SYSTEM DIAGNOSTIC =========="
        )

        print(
            Fore.WHITE +
            f"Processing log: {logfile}"
        )


        try:

            parser = LogParser()
            findings = parser.parse_log(logfile)

            database = SQLiteManager()
            database.save_findings(findings)

            report = MarkdownGenerator()
            report.generate(findings)

            elapsed_time = round(
                time.time() - start_time,
                2
            )

            critical_count = sum(
                1
                for item in findings
                if item["severity"] == "CRITICAL"
            )

            error_count = sum(
                1
                for item in findings
                if item["severity"] == "ERROR"
            )

            warning_count = sum(
                1
                for item in findings
                if item["severity"] == "WARNING"
            )

            print(
                Fore.CYAN +
                "\n========== RESULTS =========="
            )

            print(
                Fore.GREEN +
                f"Total Findings : {len(findings)}"
            )

            print(
                Fore.RED +
                f"Critical Events: {critical_count}"
            )

            print(
                Fore.YELLOW +
                f"Errors         : {error_count}"
            )

            print(
                Fore.MAGENTA +
                f"Warnings       : {warning_count}"
            )

            print(
                Fore.BLUE +
                "Database       : diagnostics.db"
            )

            print(
                Fore.BLUE +
                "Report         : reports/DiagnosticReport.md"
            )

            print(
                Fore.GREEN +
                f"Process Time   : {elapsed_time} sec"
            )

        except Exception as error:

            print(
                Fore.RED +
                Style.BRIGHT +
                "\nExecution Failed"
            )

            print(
                Fore.RED +
                f"Reason: {error}"
            )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Linux System Diagnostic CLI"
    )

    parser.add_argument(
        "logfile",
        nargs="?",
        help="Path to log file"
    )

    parser.add_argument(
        "--generate",
        type=int,
        help="Generate fake log file with N lines"
    )

    parser.add_argument(
    "--generate-and-analyze",
    type=int,
    help="Generate fake logs and analyze them"
    )

    args = parser.parse_args()

    if args.generate:

        from generators.fake_log_generator import FakeLogGenerator

        generator = FakeLogGenerator()

        generator.generate(
            "logs/generated.log",
            args.generate
        )

        print(
            f"Generated logs/generated.log with {args.generate} entries"
        )

    elif args.logfile:

        DiagnosticTool().run(args.logfile)

    elif args.generate_and_analyze:

        from generators.fake_log_generator import FakeLogGenerator

        logfile = "logs/generated.log"

        generator = FakeLogGenerator()
        generator.generate(
            logfile,
            args.generate_and_analyze
        )

        DiagnosticTool().run(logfile)

    else:

        parser.print_help()