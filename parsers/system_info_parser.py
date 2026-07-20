from pathlib import Path
import re


class SystemInfoParser:

    def get_serial_number(
        self,
        logfile
    ):

        filename = (
            Path(logfile).stem
        )

        match = re.search(

            r'(P\d{15})',

            filename,

            re.IGNORECASE

        )

        if match:

            return match.group(1)

        return "UNKNOWN"