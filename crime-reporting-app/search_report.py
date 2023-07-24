#!/usr/bin/python3
import json


def search_reports(number):
    try:
        with open("scam_reports.json", "r") as f:
            found = False
            for line in f:
                report = json.loads(line)
                if report["number"] == number:
                    print(f"Number: {report['number']}")
                    print(f"Date: {report['date']}")
                    print(f"Crime Type: {report['crime_type']}")
                    print(f"Description: {report['description']}")
                    print()
                    found = True
            if not found:
                print(f"No reports found for number {number}")
    except Exception as e:
        print(f"An error occurred while searching for reports: {e}")
