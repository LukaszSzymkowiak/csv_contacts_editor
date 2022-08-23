from contacts import *


def main():
    contact = Contacts()
    while True:
        contacts_list = Contacts.get_contacts()
        user_choice = input("1 - show all contacts\n"
                            "2 - show contact phone\n"
                            "3 - add contact\n"
                            "4 - change contact name\n"
                            "5 - change contact phone\n"
                            "6 - delete contact\n"
                            "0 - quit\n"
                            "Input: ")
        print()

        if user_choice == "0":
            break
        elif user_choice == "1":
            contact.show_contacts(contacts_list)

        elif user_choice == "2":
            contact_name = input("Contact name: ").capitalize()
            contact_phone = contact.get_number(contacts_list, contact_name)
            if contact_phone:
                print(f"Phone: {contact_phone}\n")

        elif user_choice == "3":
            contact.add_contact(contacts_list)

        elif user_choice == "4":
            contact_name = input(
                "Select contact to change name: ").capitalize()
            contact.change_name(contacts_list, contact_name)

        elif user_choice == "5":
            contact_name = input(
                "Select contact to change phone number: ").capitalize()
            contact_phone = contact.get_number(contacts_list, contact_name)
            if contact_phone:
                contact.change_phone(int(contact_phone))
            else:
                continue
        elif user_choice == "6":
            contact.delete_contact(contacts_list)

        else:
            print("Invalid command\n")


if __name__ == "__main__":
    main()
