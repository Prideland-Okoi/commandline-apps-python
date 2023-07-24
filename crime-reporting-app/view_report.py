#!/usr/bin/python3
import json


def view_reports():
    try:
        with open("scam_reports.json", "r") as f:
            for line in f:
                report = json.loads(line)
                print(f"Number: {report['number']}")
                print(f"Date: {report['date']}")
                print(f"Crime Type: {report['crime_type']}")
                print(f"Description: {report['description']}")
                print()
    except Exception as e:
        print(f"An error occurred while reading the reports: {e}")
