import re
from parsers.regex_patterns import PATTERNS


class LogParser:

    def parse_log(self, logfile):

        findings = []

        with open(logfile, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                for severity, patterns in PATTERNS.items():

                    for pattern in patterns:

                        if re.search(pattern, line, re.IGNORECASE):

                            findings.append({
                                "line": line_number,
                                "severity": severity,
                                "message": line.strip()
                            })

                            break

        return findings