#!/usr/bin/python3
from icalendar import Calendar, Event
from datetime import datetime
import sys


def create_ics_file(summary, st_time, ed_time, location, filename):
    "Read input from terminal"
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
    summary = sys.argv[1]
    st_time = sys.argv[2]
    ed_time = sys.argv[3]
    location = sys.argv[4]
    filename = sys.argv[5]

    create_ics_file(summary, st_time, ed_time, location, filename)
