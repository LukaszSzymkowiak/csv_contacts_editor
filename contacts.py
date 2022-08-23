import csv
import pandas as pd
import re


class Contacts:
    def __init__(self):
        self.name = "Contacts"

    @classmethod
    def get_contacts(cls):
        contacts = []
        with open("contacts.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(
                    {"Name": row["Name"].capitalize(), "Phone": row["Phone"]})
        return contacts

    def show_contacts(self, contacts_list):
        if len(contacts_list) == 0:
            print("No contacts")
        else:
            print("Contacts")
            for contact in sorted(contacts_list, key=lambda contact: contact["Name"]):
                print(f"{contact['Name']}: {contact['Phone']}")
        print()

    def get_number(self, contacts_list, contact_name):
        try:
            if next(contact for contact in contacts_list if contact["Name"] == f"{contact_name}"):
                with open("contacts.csv") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if contact_name in row["Name"]:
                            return row["Phone"]
        except StopIteration:
            print("Contact doesn't exist\n")

    def add_contact(self, contacts_list):
        contact_name = input("Contact name: ").capitalize()
        try:
            if next(contact for contact in contacts_list if contact["Name"] == f"{contact_name}"):
                print("Contact name exists\n")
        except StopIteration:
            while True:
                contact_number = input(
                    "Number in format XXX-XXX-XXX or XXXXXXXXX: ")
                print()
                if matches := re.search(r"^([0-9]{9}|[0-9]{3}-[0-9]{3}-[0-9]{3})$", contact_number):
                    with open("contacts.csv", "a") as file:
                        writer = csv.DictWriter(
                            file, fieldnames=["Name", "Phone"])
                        writer.writerow(
                            {"Name": contact_name, "Phone": contact_number.replace("-", "")})
                        print(
                            f"{contact_name}: {contact_number.replace('-', '')} added to contacts\n")
                        break
                else:
                    print("Invalid phone number format\n")
                    continue

    # using pandas
    def change_name(self, contacts_list, contact_name):
        try:
            if next(contact for contact in contacts_list if contact["Name"] == f"{contact_name}"):
                new_name = input("New contact name: ")
                df = pd.read_csv("contacts.csv")
                df["Name"] = df["Name"].replace(
                    {f"{contact_name}": f"{new_name}"})
                df.to_csv("contacts.csv", index=False)
                print(f"Name changed to {new_name}\n")
        except StopIteration:
            print("Contact doesn't exist\n")

    # using pandas
    def change_phone(self, contact_phone):
        new_phone = input("Number in format XXX-XXX-XXX or XXXXXXXXX: ")
        if matches := re.search(r"^([0-9]{9}|[0-9]{3}-[0-9]{3}-[0-9]{3})$", new_phone):
            df = pd.read_csv("contacts.csv")
            df["Phone"] = df["Phone"].replace(
                {contact_phone: f"{new_phone.replace('-', '')}"})
            df.to_csv("contacts.csv", index=False)
            print(f"Phone changed to {new_phone}\n")
        else:
            print("Invalid phone number format\n")

    # using pandas
    def delete_contact(self, contacts_list):
        contact_name = input("Select contact to delete: ").capitalize()
        try:
            if next(contact for contact in contacts_list if contact["Name"] == f"{contact_name}"):
                df = pd.read_csv("contacts.csv")
                df.drop(df.index[(df["Name"] == contact_name)],
                        axis=0, inplace=True)
                df.to_csv("contacts.csv", index=False)
                print(f"{contact_name} deleted\n")
        except StopIteration:
            print("Contact doesn't exist\n")
