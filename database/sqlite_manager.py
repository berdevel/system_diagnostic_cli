import sqlite3


class SQLiteManager:

    def __init__(self):

        self.connection = sqlite3.connect("diagnostics.db")

        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS incidents(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            severity TEXT,
            line INTEGER,
            message TEXT
        )
        """)

    def save_findings(self, findings):

        cursor = self.connection.cursor()

        for item in findings:

            cursor.execute(
                """
                INSERT INTO incidents
                (severity, line, message)
                VALUES (?, ?, ?)
                """,
                (
                    item["severity"],
                    item["line"],
                    item["message"]
                )
            )

        self.connection.commit()