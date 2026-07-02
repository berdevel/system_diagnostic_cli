import argparse
import time
from pathlib import Path

from parsers.log_parser import LogParser
from database.sqlite_manager import SQLiteManager
from reports.markdown_generator import MarkdownGenerator


class DiagnosticTool:

    def run(self, logfile):

        if not Path(logfile).exists():
            print(f"ERROR: Log file not found -> {logfile}")
            return

        start_time = time.time()

        print("\n========== SYSTEM DIAGNOSTIC ==========")
        print(f"Processing log: {logfile}")

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

            print("\n========== RESULTS ==========")
            print(f"Total Findings : {len(findings)}")
            print(f"Critical Events: {critical_count}")
            print(f"Errors         : {error_count}")
            print(f"Warnings       : {warning_count}")
            print(f"Database       : diagnostics.db")
            print("Report         : reports/DiagnosticReport.md")
            print(f"Process Time   : {elapsed_time} sec")

        except Exception as error:

            print("\nExecution Failed")
            print(f"Reason: {error}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Linux System Diagnostic CLI"
    )

    parser.add_argument(
        "logfile",
        help="Path to log file"
    )

    args = parser.parse_args()

    DiagnosticTool().run(args.logfile)