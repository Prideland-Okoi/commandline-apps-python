#!/usr/bin/python3
from scammer_app import ScammerApp
import json


def main():
    app = ScammerApp()
    while True:
        print("Welcome to the Scam Reporting App!")
        print("1. Report a scam")
        print("2. View scam reports")
        print("3. Search for a report")
        print("4. Delete a report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            number = input("Enter the phone number: ")
            date = input("Enter the date of the scam (YYYY-MM-DD): ")
            description = input("Enter a description of the scam: ")
            app.report_scam(number, date, description)
        elif choice == "2":
            app.view_reports()
        elif choice == "3":
            number = input("Enter the phone number to search for: ")
            app.search_reports(number)
        elif choice == "4":
            case_number = input("Enter case number of the report to delete: ")
            app.delete_report(case_number)
        elif choice == "5":
            print("Bye!!!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
