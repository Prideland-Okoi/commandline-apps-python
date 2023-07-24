#!/usr/bin/python3
from view_report import view_reports
from report_scam import report_scam
from search_report import search_reports
import json


def main():
    while True:
        print("Welcome to the Scammer Journal App!")
        print("1. Report a scam")
        print("2. View scam reports")
        print("3. Search reports")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            number = input("Enter the phone number: ")
            date = input("Enter the date of the scam (YYYY-MM-DD): ")
            crime_type = input("Enter the type of crime: ")
            description = input("Enter a description of the scam: ")
            report_scam(number, date, crime_type, description)
            print("Scam reported successfully!")
        elif choice == "2":
            view_reports()
        elif choice == "3":
            number = input("Enter the phone number to search for: ")
            search_reports(number)
        elif choice == "4":
            print("Bye!!!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
