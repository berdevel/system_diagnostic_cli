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

            current_event_id = "Unknown"
            seen = set()

            for line_number, line in enumerate(file, start=1):

                line_lower = line.lower()

                event_match = re.search(

                    r'"Id"\s*:\s*"(\d+)"',

                    line

                )

                if event_match:

                    current_event_id = (
                        event_match.group(1)
                    )

                for failure, module in FAILURE_CATALOG.items():

                    if failure in line_lower:

                        # ==========================================
                        # COMPONENT
                        # ==========================================

                        component = "Unknown"

                        if module in [
                            "Module 0",
                            "Module 1"
                        ]:

                            component = "Bianca"

                        elif "Coldplate" in module:

                            component = "Coldplate"

                        elif "CX8" in module:

                            component = "CX8"

                        # ==========================================
                        # BIANCA
                        # ==========================================

                        bianca = "N/A"

                        if module == "Module 0":

                            bianca = "Bianca 1"

                        elif module == "Module 1":

                            bianca = "Bianca 2"

                        # ==========================================
                        # COLDPLATE
                        # ==========================================

                        coldplate = "N/A"

                        if module == "Left Coldplate":

                            coldplate = "Left"

                        elif module == "Right Coldplate":

                            coldplate = "Right"

                        # ==========================================
                        # CX8
                        # ==========================================

                        cx8 = "N/A"

                        if module == "Left CX8":

                            cx8 = "Left"

                        elif module == "Right CX8":

                            cx8 = "Right"

                        elif module == "Both CX8":

                            cx8 = "Both"

                        finding_key = (

                            current_event_id,

                            failure

                        )

                        action = "Investigate"

                        if component == "Bianca":

                            action = (
                                f"Replace {bianca}"
                            )

                        elif component == "Coldplate":

                            action = (
                                f"Replace {coldplate} Coldplate"
                            )

                        elif component == "CX8":

                            action = (
                                f"Replace {cx8} CX8"
                            )

                        if finding_key in seen:

                            continue

                        seen.add(finding_key)

                        assembly = "Unknown"

                        if bianca == "Bianca 1":

                            assembly = "Bianca#1 Assembly"

                        elif bianca == "Bianca 2":

                            assembly = "Bianca#2 Assembly"

                        findings.append({

                            "event_id": current_event_id,

                            "failure": failure,

                            "component": component,

                            "bianca": bianca,

                            "assembly": assembly,

                            "coldplate": coldplate,

                            "cx8": cx8,

                            "module": module,

                            "action": action,

                            "line": line_number,

                            "message": line

                        })

        return findings