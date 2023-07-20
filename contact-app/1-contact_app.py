#!/usr/bin/python3
import json


def create_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    return contact


def save_contact(contact):
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    contacts.append(contact)
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)


def edit_contact():
    name = input("Enter name of contact to edit: ")
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for contact in contacts:
        if contact["name"] == name:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            new_name = input("Enter new name (or press enter to skip): ")
            new_phone = input("Enter new phone number (or press enter to skip): ")
            new_email = input("Enter new email address (or press enter to skip): ")
            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            break
    else:
        print(f"No contact found with name {name}")
        return
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)


def delete_contact():
    name = input("Enter name of contact to delete: ")
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            del contacts[i]
            break
    else:
        print(f"No contact found with name {name}")
        return
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)


def list_contacts():
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def main():
    while True:
        print("\n\n")
        print("=" * 20)
        print("Contact App")
        print("=" * 20)
        print("1. Create Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Quit")
        choice = input("> ")
        if choice == "1":
            contact = create_contact()
            save_contact(contact)
            print(f"Contact saved:\n{contact}")
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
