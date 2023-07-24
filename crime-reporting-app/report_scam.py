#!/usr/bin/python3
import json


def report_scam(number, date, crime_type, description):
    report = {
        "number": number,
        "date": date,
        "crime_type": crime_type,
        "description": description
    }
    try:
        with open("scam_reports.json", "a") as f:
            json.dump(report, f)
            f.write("\n")
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")
