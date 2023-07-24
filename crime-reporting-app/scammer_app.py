#!/usr/bin/python3
import json
import random


class ScammerApp:
    def __init__(self):
        self.crime_categories = ["Ponzi", "Identity Fraud", "Phishing", "Vishing", "Sextortion",  "Smishing", "Lottery Scam", "Extortion", "Tech Support Scam"]

    def report_scam(self, number, date, description):
        print("Select a crime category:")
        for i, category in enumerate(self.crime_categories):
            print(f"{i + 1}. {category}")
        crime_type = self.crime_categories[int(input("Enter your choice: ")) - 1]
        case_number = f"{crime_type[:3]}-{date.replace('-', '')}-{random.randint(1000, 9999)}"
        report = {
            "case_number": case_number,
            "number": number,
            "date": date,
            "crime_type": crime_type,
            "description": description
        }
        try:
            with open("scammer_reports.json", "a") as f:
                json.dump(report, f)
                f.write("\n")
            print(f"Scam reported successfully! Case number: {case_number}")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")

    def view_reports(self):
        try:
            with open("scammer_reports.json", "r") as f:
                for line in f:
                    report = json.loads(line)
                    print(f"Case Number: {report['case_number']}")
                    print(f"Number: {report['number']}")
                    print(f"Date: {report['date']}")
                    print(f"Crime Type: {report['crime_type']}")
                    print(f"Description: {report['description']}")
                    print()
        except Exception as e:
            print(f"An error occurred while reading the reports: {e}")

    def search_reports(self, number):
        try:
            with open("scammer_reports.json", "r") as f:
                found = False
                for line in f:
                    report = json.loads(line)
                    if report["number"] == number:
                        print(f"Case Number: {report['case_number']}")
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

    def delete_report(self, case_number):
        try:
            with open("scammer_reports.json", "r") as f:
                reports = [json.loads(line) for line in f]
            reports = [report for report in reports if report["case_number"] != case_number]
            with open("scammer_reports.json", "w") as f:
                for report in reports:
                    json.dump(report, f)
                    f.write("\n")
            print(f"Report with case number {case_number} deleted successfully!")
        except Exception as e:
            print(f"An error occurred while deleting the report: {e}")
