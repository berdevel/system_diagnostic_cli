from datetime import datetime
import sqlite3


class SQLiteManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "diagnostics.db"
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS analysis_history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                serial_number TEXT,

                analysis_date TEXT,

                source_log TEXT,

                root_cause_id TEXT,

                root_cause_name TEXT,

                confidence TEXT,

                total_findings INTEGER,

                critical_events INTEGER

            )

        """)

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS component_failures (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                serial_number TEXT,

                event_id TEXT,

                component TEXT,

                assembly TEXT,

                bianca TEXT,

                coldplate TEXT,

                cx8 TEXT,

                failure TEXT,

                recommendation TEXT,

                line_number INTEGER

            )

        """)

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS critical_events (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                serial_number TEXT,

                event_id TEXT,

                created TEXT,

                severity TEXT,

                gpu TEXT,

                cpu TEXT,

                bianca TEXT,

                assembly TEXT,

                coldplate TEXT,

                xid TEXT,

                failure TEXT,

                recommendation TEXT

            )

        """)

        self.connection.commit()

    def save_analysis(

        self,
        serial_number,
        logfile,
        root_causes,
        findings_count,
        critical_count

    ):

        primary = root_causes.get(
            "primary"
        )

        if not primary:

            return

        self.cursor.execute("""

            INSERT INTO analysis_history (

                serial_number,

                analysis_date,

                source_log,

                root_cause_id,

                root_cause_name,

                confidence,

                total_findings,

                critical_events

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            serial_number,

            datetime.now().isoformat(),

            logfile,

            primary["id"],

            primary["name"],

            primary["confidence"],

            findings_count,

            critical_count

        )

        )

        self.connection.commit()

    def save_findings(

        self,
        serial_number,
        findings

    ):

        for item in findings:

            self.cursor.execute("""

                INSERT INTO component_failures (

                    serial_number,

                    event_id,

                    component,

                    assembly,

                    bianca,

                    coldplate,

                    cx8,

                    failure,

                    recommendation,

                    line_number

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                serial_number,

                item.get("event_id"),

                item.get("component"),

                item.get("assembly"),

                item.get("bianca"),

                item.get("coldplate"),

                item.get("cx8"),

                item.get("failure"),

                item.get("action"),

                item.get("line")

            )

            )

        self.connection.commit()

    def save_critical_events(

        self,
        serial_number,
        events

    ):

        for event in events:

            self.cursor.execute("""

                INSERT INTO critical_events (

                    serial_number,

                    event_id,

                    created,

                    severity,

                    gpu,

                    cpu,

                    bianca,

                    assembly,

                    coldplate,

                    xid,

                    failure,

                    recommendation

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                serial_number,

                event.get("event_id"),

                event.get("created"),

                event.get("severity"),

                event.get("gpu"),

                event.get("cpu"),

                event.get("bianca"),

                event.get("assembly"),

                event.get("coldplate"),

                event.get("xid"),

                event.get("failure"),

                event.get("recommendation")

            )

            )

        self.connection.commit()

    def close(self):

        self.connection.close()

    def get_serial_history(
        self,
        serial_number
    ):

        self.cursor.execute(

            """

            SELECT

                analysis_date,

                root_cause_name,

                confidence

            FROM analysis_history

            WHERE serial_number = ?

            ORDER BY analysis_date DESC

            """,

            (serial_number,)

        )

        return self.cursor.fetchall()
    
    def get_top_root_causes(self):

        self.cursor.execute(

            """

            SELECT

                root_cause_name,

                COUNT(*)

            FROM analysis_history

            GROUP BY root_cause_name

            ORDER BY COUNT(*) DESC

            LIMIT 10

            """

        )

        return self.cursor.fetchall()
    
    def get_top_components(self):

        self.cursor.execute(

            """

            SELECT

                component,

                COUNT(*)

            FROM component_failures

            GROUP BY component

            ORDER BY COUNT(*) DESC

            """

        )

        return self.cursor.fetchall()
    
    def get_top_serials(self):

        self.cursor.execute(

            """

            SELECT

                serial_number,

                COUNT(*)

            FROM analysis_history

            GROUP BY serial_number

            ORDER BY COUNT(*) DESC

            LIMIT 20

            """

        )

        return self.cursor.fetchall()