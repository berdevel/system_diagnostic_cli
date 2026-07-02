# System Diagnostic CLI

## Project Overview

System Diagnostic CLI is a Python-based tool designed to automate Linux log analysis and troubleshooting.

The solution parses log files, identifies failures using Regular Expressions (Regex), classifies incidents, stores findings in SQLite, and generates automated Markdown reports.

---

## Features

- Command Line Interface (CLI)
- Object-Oriented Design (OOP)
- Regular Expression Parsing
- SQLite Database Integration
- Automated Markdown Reports
- Massive Log Simulation
- Unit Testing with Pytest

---

## Architecture

parsers/
database/
reports/
generators/
config/
tests/

---

## Use Cases

- Linux troubleshooting
- Manufacturing validation environments
- Failure analysis
- Automated diagnostics
- QA engineering support

---

## Run Analysis

python cli.py logs/sample.log

---

## Generate Test Logs

python generators/fake_log_generator.py

---

## Run Tests

pytest

---

## Business Value

This solution reduces troubleshooting time by automatically identifying critical events in large log files and generating standardized diagnostic reports.

The project demonstrates:

- Python
- Linux
- Regex
- SQLite
- Automation
- OOP
- Root Cause Analysis
- Test Engineering