import random

EVENTS = [
    "INFO Service started",
    "WARNING Network timeout detected",
    "ERROR Failed to start application",
    "CRITICAL Kernel panic detected",
    "ERROR Exception during database access",
    "WARNING Memory usage exceeds threshold",
    "CRITICAL Segmentation fault"
]


class FakeLogGenerator:

    def generate(self, filename, lines=10000):

        with open(filename, "w", encoding="utf-8") as file:

            for _ in range(lines):

                file.write(
                    random.choice(EVENTS) + "\n"
                )

        print(
            f"Generated {lines} log entries in {filename}"
        )


if __name__ == "__main__":

    FakeLogGenerator().generate(
        "logs/sample.log",
        10000
    )