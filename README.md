# System Diagnostic CLI

## Overview

CLI tool developed in Python to automate fault diagnosis in Linux environments.

The tool analyzes log files, detects critical events using Regular Expressions (Regex), classifies issues, stores incidents in SQLite and generates an automated Markdown report.

This project simulates real-world troubleshooting activities commonly performed by Validation Engineers, Test Engineers and Linux Support Engineers.

---

## Features

- Command Line Interface (CLI)
- Log Parsing
- Regex Pattern Detection
- Fault Classification
- SQLite Database Storage
- Automated Markdown Report
- Object Oriented Programming (OOP)

---

## Technologies

- Python 3
- SQLite
- Regex
- Markdown
- Linux Logs

---

## Execution

python cli.py logs/sample.log

---

## Output

- diagnostics.db
- DiagnosticReport.md

---

## Business Value

Reduces diagnosis time by:

- Automating log analysis
- Detecting critical failures
- Standardizing troubleshooting workflows
- Generating documentation automatically

This is especially useful in manufacturing and validation environments such as Foxconn where large volumes of logs must be analyzed quickly.