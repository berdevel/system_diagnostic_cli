import sqlite3


class SQLiteManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "diagnostics.db"
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS findings (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                failure TEXT,

                bianca TEXT,

                module TEXT,

                line_number INTEGER,

                message TEXT

            )

        """)

        self.connection.commit()

    def save_findings(self, findings):

        for item in findings:

            self.cursor.execute("""

                INSERT INTO findings (

                    failure,

                    bianca,

                    module,

                    line_number,

                    message

                )

                VALUES (?, ?, ?, ?, ?)

            """,

            (

                item.get(
                    "failure",
                    "Unknown"
                ),

                item.get(
                    "bianca",
                    "Unknown"
                ),

                item.get(
                    "module",
                    "Unknown"
                ),

                item.get(
                    "line",
                    0
                ),

                item.get(
                    "message",
                    ""
                )

            )

            )

        self.connection.commit()

        self.connection.close()