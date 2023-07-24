#!/usr/bin/python3
import json


def delete_report(case_number):
    try:
        with open("Scam_Report.json", "r") as f:
            reports = [json.loads(line) for line in f]
        reports = [report for report in reports if report["case_number"] != case_number]
        with open("Scam_Report.json", "w") as f:
            for report in reports:
                json.dump(report, f)
                f.write("\n")
        print(f"Report with case number {case_number} deleted successfully!")
    except Exception as e:
        print(f"An error occurred while deleting the report: {e}")
