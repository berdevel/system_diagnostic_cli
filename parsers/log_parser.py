import re

from config.failure_catalog import FAILURE_CATALOG

BIANCA_MAPPING = {
    "Module 0": "Bianca 1",
    "Module 1": "Bianca 2"
}


class LogParser:

    def parse_log(self, logfile):

        findings = []

        with open(
            logfile,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line_number, line in enumerate(file, start=1):

                line_lower = line.lower()

                for failure, module in FAILURE_CATALOG.items():

                    if failure.lower() in line_lower:

                        findings.append({

                            "line": line_number,

                            "failure": failure,

                            "module": module,

                            "bianca": BIANCA_MAPPING[module],

                            "action": "Replace affected Bianca",

                            "message": line.strip()

                        })

        return findings