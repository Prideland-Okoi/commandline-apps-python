#!/usr/bin/python3
from icalendar import Calendar, Event
from datetime import datetime


def create_ics_file():
    "Prompt user for input"
    summary = input("Enter Event Summary: ")
    st_time = input("Enter event start time (YYYY-MM-DD HH:MM): ")
    ed_time = input("Enter event end time (YYYY-MM-DD HH:MM): ")
    location = input("Enter event location: ")
    filename = input("Enter event filename for .ics file: ")


    cal = Calendar()
    event = Event()
    event.add("summary", summary)
    event.add("st_time", datetime.strptime(st_time, '%Y-%m-%d %H:%M'))
    event.add("ed_time", datetime.strptime(ed_time, '%Y-%m-%d %H:%M'))
    event.add("location", location)
    cal.add_component(event)


    with open(filename, "wb") as file:
        file.write(cal.to_ical())
    print(f"{filename} created")


if __name__ == "__main__":
    create_ics_file()
