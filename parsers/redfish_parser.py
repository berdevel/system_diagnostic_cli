import json
import re

from datetime import datetime
from config.xid_catalog import XID_CATALOG
from config.power_fault_catalog import POWER_FAULT_CATALOG
from config.cpu_firmware_catalog import (
    CPU_FIRMWARE_CATALOG
)
from config.failure_catalog import (
    FAILURE_CATALOG
)
from config.location_mapper import (

    LOCATION_TO_BIANCA,

    LOCATION_TO_COLDPLATE,

    LOCATION_TO_CX8

)


class RedfishParser:

    def parse_critical_events(

        self,
        logfile,
        date_from=None,
        date_to=None

    ):

        if isinstance(date_from, str):

            date_from = datetime.strptime(
                date_from,
                "%Y-%m-%d"
            ).date()

        if isinstance(date_to, str):

            date_to = datetime.strptime(
                date_to,
                "%Y-%m-%d"
            ).date()

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

            created = event.get(
                "Created"
            )

            event_date = None

            if created:

                try:

                    event_date = datetime.fromisoformat(
                        created.replace(
                            "Z",
                            "+00:00"
                        )
                    )

                except ValueError:

                    event_date = None

            invalid_timestamp = True

            if event_date:

                invalid_timestamp = (

                    event_date.year < 2020

                )

            # Apply date filters only if timestamp looks valid

            if not invalid_timestamp:

                if date_from and event_date.date() < date_from:

                    continue

                if date_to and event_date.date() > date_to:

                    continue

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

            message_upper = message.upper()

            location = None

            for keyword, info in CPU_FIRMWARE_CATALOG.items():

                if keyword in message_upper:

                    failure = info["failure"]

                    recommendation = (
                        info["recommendation"]
                    )

                    break

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

            for fault, mapped_location in (
                FAILURE_CATALOG.items()
            ):

                if fault.upper() in message_upper:

                    location = mapped_location

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
            
            # ==========================================
            # Infer Bianca from PWR_FAIL module
            # ==========================================

            message_upper = message.upper()

            if bianca == "Unknown":

                bianca = (

                    LOCATION_TO_BIANCA.get(

                        location,

                        "Unknown"

                    )

                )

            coldplate = "N/A"

            catalog_coldplate = (

                LOCATION_TO_COLDPLATE.get(
                    location
                )

            )

            if catalog_coldplate:

                coldplate = catalog_coldplate

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

            if bianca == "Unknown":

                if cpu == "CPU_0":

                    bianca = "Bianca#1"

                elif cpu == "CPU_1":

                    bianca = "Bianca#2"

            assembly = "Unknown"

            if bianca == "Bianca#1":

                assembly = "Bianca#1 Assembly"

            elif bianca == "Bianca#2":

                assembly = "Bianca#2 Assembly"

            cx8 = (

                LOCATION_TO_CX8.get(

                    location,

                    "N/A"

                )

            )

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

                "location": location,

                "cx8": cx8,

                "assembly": assembly,

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