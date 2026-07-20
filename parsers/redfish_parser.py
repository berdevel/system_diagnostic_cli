import json
import re

from config.xid_catalog import XID_CATALOG
from config.power_fault_catalog import POWER_FAULT_CATALOG


class RedfishParser:

    def parse_critical_events(self, logfile):

        findings = []

        with open(
            logfile,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            data = json.load(file)

        events = data.get("Members", [])

        for event in events:

            if event.get("Severity") != "Critical":
                continue

            message = event.get(
                "Message",
                ""
            )

            gpu = "Unknown"

            origin = (
                event.get("Links", {})
                .get("OriginOfCondition", {})
                .get("@odata.id", "")
            )

            gpu_match = re.search(
                r'HGX_GPU_(\d+)',
                origin,
                re.IGNORECASE
            )

            if gpu_match:
                gpu = f"GPU_{gpu_match.group(1)}"

            xid = "N/A"

            xid_match = re.search(
                r'XID\s+(\d+)',
                message,
                re.IGNORECASE
            )

            if xid_match:
                xid = xid_match.group(1)

            failure = "Unknown Critical Event"

            recommendation = (
                "Review NVIDIA documentation."
            )

            if xid != "N/A":

                xid_info = XID_CATALOG.get(

                    xid,

                    {
                        "name": "Unknown XID",
                        "recommendation":
                        "Review NVIDIA documentation."
                    }

                )

                failure = xid_info["name"]

                recommendation = (
                    xid_info["recommendation"]
                )

            for keyword, info in POWER_FAULT_CATALOG.items():

                if keyword in message:

                    failure = info["failure"]

                    recommendation = (
                        info["recommendation"]
                    )

                    break
            
            # ==========================================
            # Infer GPU from Failure Description
            # ==========================================

            if gpu == "Unknown":

                if "GPU_0" in failure:
                    gpu = "GPU_0"

                elif "GPU_1" in failure:
                    gpu = "GPU_1"

                elif "GPU_2" in failure:
                    gpu = "GPU_2"

                elif "GPU_3" in failure:
                    gpu = "GPU_3"

            bianca = "Unknown"

            if gpu in [

                "GPU_0",
                "GPU_1"

            ]:

                bianca = "Bianca#1"

            elif gpu in [

                "GPU_2",
                "GPU_3"

            ]:

                bianca = "Bianca#2"

            coldplate = "N/A"

            thermal_event = (

                "THERM" in message.upper()

                or

                "THERMAL" in message.upper()

                or

                "OVERT" in message.upper()

                or

                xid == "163"

            )

            if thermal_event:

                if gpu in [

                    "GPU_0",
                    "GPU_1"

                ]:

                    coldplate = "Left"

                elif gpu in [

                    "GPU_2",
                    "GPU_3"

                ]:

                    coldplate = "Right"

            cpu_match = re.search(

                r'CPU_(\d+)',

                message,

                re.IGNORECASE

            )

            if cpu_match:

                cpu = (
                    f"CPU_{cpu_match.group(1)}"
                )

            else:

                cpu = "Unknown"

            if cpu == "CPU_0":

                bianca = "Bianca#1"

            elif cpu == "CPU_1":

                bianca = "Bianca#2"

            findings.append({

                "event_id": event.get(
                    "Id",
                    "Unknown"
                ),

                "created": event.get(
                    "Created",
                    "Unknown"
                ),

                "severity": event.get(
                    "Severity",
                    "Unknown"
                ),

                "gpu": gpu,

                "cpu": cpu,

                "bianca": bianca,

                "coldplate": coldplate,

                "xid": xid,

                "failure": failure,

                "recommendation": recommendation,

                "description": message,

                "resolution": event.get(
                    "Resolution",
                    "N/A"
                )

            })

        return findings