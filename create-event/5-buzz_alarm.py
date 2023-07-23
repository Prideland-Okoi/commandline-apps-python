#!/usr/bin/python3
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta


def create_ics_file():
    "Prompt user for input"
    summary = input("Enter Event Summary: ")
    st_time = input("Enter event start time (YYYY-MM-DD HH:MM): ")
    ed_time = input("Enter event end time (YYYY-MM-DD HH:MM): ")
    location = input("Enter event location: ")
    description = input("Enter event description: ")
    url = input("Enter event url: ")
    categories = input("Enter event categories (comma-separated): ").split(",")
    organizer = input("Enter event organizer: ")
    reminder_minutes = int(input("Enter number of minutes before event to set reminder: "))
    filename = input("Enter event filename for .ics file: ")


    cal = Calendar()
    event = Event()
    event.add("summary", summary)
    event.add("st_time", datetime.strptime(st_time, '%Y-%m-%d %H:%M'))
    event.add("ed_time", datetime.strptime(ed_time, '%Y-%m-%d %H:%M'))
    event.add("location", location)
    event.add("description", description)
    event.add("url", url)
    event.add("categories", categories)
    event.add("organizer", organizer)


    alarm = Alarm()
    alarm.add("action", "DISPLAY")
    alarm.add("description", "Reminder")
    alarm.add("trigger", timedelta(minutes=-reminder_minutes))
    
    
    event.add_component(alarm)
    cal.add_component(event)


    with open(filename, "wb") as file:
        file.write(cal.to_ical())
    print(f"{filename} created")


if __name__ == "__main__":
    create_ics_file()


