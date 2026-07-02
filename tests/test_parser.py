from parsers.log_parser import LogParser


def test_parser():

    parser = LogParser()

    findings = parser.parse_log(
        "logs/sample.log"
    )

    assert isinstance(findings, list)