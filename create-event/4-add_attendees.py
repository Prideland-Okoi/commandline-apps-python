#!/usr/bin/python3
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime


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
    attendee_count = int(input("Enter number of attendees: "))
    attendees = []
    for i in range(attendee_count):
        attendee_email = input(f"Enter email address for attendee {i + 1}: ")
        attendee_name = input(f"Enter name for attendee {i + 1}: ")
        attendee = vCalAddress(f"MAILTO: {attendee_email}")
        attendee.params["cn"] = vText(attendee_name)
        attendee.params["ROLE"] = vText("REQ-PARTICIPANT")
        attendees.append(attendee)
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
    for attendee in attendees:
        event.add("attendee", attendee, encode = 0)
    cal.add_component(event)


    with open(filename, "wb") as file:
        file.write(cal.to_ical())
    print(f"{filename} created")


if __name__ == "__main__":
    create_ics_file()


