import argparse

from parsers.log_parser import LogParser
from database.sqlite_manager import SQLiteManager
from reports.markdown_generator import MarkdownGenerator


class DiagnosticTool:

    def run(self, logfile):

        parser = LogParser()
        findings = parser.parse_log(logfile)

        database = SQLiteManager()
        database.save_findings(findings)

        report = MarkdownGenerator()
        report.generate(findings)

        print("Analysis completed")
        print(f"Findings: {len(findings)}")
        print("Database: diagnostics.db")
        print("Report: DiagnosticReport.md")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Linux Diagnostic Tool"
    )

    parser.add_argument(
        "logfile",
        help="Path to log file"
    )

    args = parser.parse_args()

    DiagnosticTool().run(args.logfile)