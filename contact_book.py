"""
Features:

Add a new contact
Delete a contact
List all contacts
Search contact by name
Update a contact's details
Add an additional phone number to an existing contact
Add an additional email to an existing contact
Save/load all data to/from a single JSON file
"""

from validators import *
import json

class Contact:
    # Class-level counter to auto-assign unique IDs across all instances
    counter = 0

    def __init__(self, name, phone_numbers, emails, address):
        # Increment shared counter before assigning so IDs start at 1
        Contact.counter += 1
        self.__contact_id = Contact.counter  # Unique, immutable ID for this contact
        self.__name = name
        self.__phone_numbers = phone_numbers  # List of phone number strings
        self.__emails = emails                # List of email address strings
        self.__address = address

    # --- Getters ---

    def get_contact_id(self):
        return self.__contact_id

    def get_name(self):
        return self.__name

    def get_phone_numbers(self):
        return self.__phone_numbers

    def get_emails(self):
        return self.__emails

    def get_address(self):
        return self.__address

    # --- Setters (used when updating an existing contact) ---

    def set_name(self, name):
        self.__name = name

    def set_phone_numbers(self, phone_numbers):
        self.__phone_numbers = phone_numbers

    def set_emails(self, emails):
        self.__emails = emails

    def set_address(self, address):
        self.__address = address

    # --- Append helpers (used when adding extra entries without replacing) ---

    def add_email(self, email):
        self.__emails.append(email)

    def add_phone_number(self, phone_number):
        self.__phone_numbers.append(phone_number)

    def __str__(self):
        return f"Contact ID: {self.__contact_id}, Name: {self.__name}, Phone Numbers: {self.__phone_numbers}, Emails: {self.__emails}, Address: {self.__address}"


# In-memory list of Contact objects; populated from JSON on startup
contacts = []

def add_contact():
    """Collect details for a new contact from the user and append it to the list."""
    name = get_non_empty_string("Enter contact name: ")
    address = get_non_empty_string("Enter contact address: ")

    # Collect one or more email addresses
    emails = []
    while True:
        email = get_non_empty_string("Enter email address: ")
        emails.append(email)

        print("\nEnter 1 if you want to add another email.")
        print("Enter 0 if you do not want to add any more emails.\n")

        # Keep asking until the user enters a valid choice (0 or 1)
        while True:
            choice = get_positive_int("Type your choice and press enter: ")
            if 0 <= choice <= 1:
                break
            print("\nChoice needs to be between 0 to 1.")

        if choice == 0:
            break

    # Collect one or more phone numbers
    phone_numbers = []
    while True:
        phone_number = get_non_empty_string("Enter phone number: ")
        phone_numbers.append(phone_number)

        print("\nEnter 1 if you want to add another phone number.")
        print("Enter 0 if you do not want to add any more phone numbers.\n")

        # Keep asking until the user enters a valid choice (0 or 1)
        while True:
            choice = get_positive_int("Type your choice and press enter: ")
            if 0 <= choice <= 1:
                break
            print("\nChoice needs to be between 0 to 1.")

        if choice == 0:
            break

    contact = Contact(name, phone_numbers, emails, address)
    contacts.append(contact)
    save_to_json()  # Persist immediately after every change

def delete_contact():
    """Remove a contact by ID. Prints a message if not found or list is empty."""
    if len(contacts) == 0:
        print("No contacts found in the book.")
        return

    contact_id = get_positive_int("Enter contact ID: ")

    for contact in contacts:
        if contact.get_contact_id() == contact_id:
            contacts.remove(contact)
            save_to_json()
            return
    print("Contact not found.")

def list_all_contacts():
    """Print every contact in the book using Contact.__str__."""
    if len(contacts) == 0:
        print("No contacts found in the book.")
        return

    for contact in contacts:
        print(contact)

def search_by_name():
    """Find and print all contacts whose name exactly matches the user's input."""
    if len(contacts) == 0:
        print("No contacts found in the book.")
        return

    name = get_non_empty_string("Enter contact name: ")
    results = []

    for contact in contacts:
        if contact.get_name() == name:
            results.append(contact)

    if len(results) == 0:
        print("Contact not found.")
        return
    else:
        for result in results:
            print(result)

def update_contact_details():
    """
    Replace all fields of an existing contact identified by ID.
    The number of emails/phone numbers stays the same; only the values change.
    """
    if len(contacts) == 0:
        print("No contacts found in the book.")
        return

    contact_id = get_positive_int("Enter contact ID: ")

    name = get_non_empty_string("Enter updated contact name: ")
    address = get_non_empty_string("Enter updated contact address: ")

    updated_emails = []
    updated_phone_numbers = []

    for contact in contacts:
        if contact.get_contact_id() == contact_id:
            contact.set_name(name)
            contact.set_address(address)

            # Prompt for a replacement value for each existing email slot
            for i in range(len(contact.get_emails())):
                updated_emails.append(get_non_empty_string(f"Enter updated email address {i+1}: "))

            # Prompt for a replacement value for each existing phone number slot
            for i in range(len(contact.get_phone_numbers())):
                updated_phone_numbers.append(get_non_empty_string(f"Enter updated phone number {i+1}: "))

            contact.set_emails(updated_emails)
            contact.set_phone_numbers(updated_phone_numbers)
            save_to_json()
            return
    print("Contact not found.")

def add_new_phone_number():
    """Append an extra phone number to a contact without touching existing numbers."""
    if len(contacts) == 0:
        print("No contacts found in the book.")
        return

    contact_id = get_positive_int("Enter contact ID: ")

    for contact in contacts:
        if contact.get_contact_id() == contact_id:
            new_phone_number = get_non_empty_string("Enter new phone number to add: ")
            contact.add_phone_number(new_phone_number)
            save_to_json()
            return
    print("Contact not found.")

def add_new_email():
    """Append an extra email address to a contact without touching existing emails."""
    if len(contacts) == 0:
        print("No contacts found in the book.")
        return

    contact_id = get_positive_int("Enter contact ID: ")

    for contact in contacts:
        if contact.get_contact_id() == contact_id:
            new_email = get_non_empty_string("Enter new email to add: ")
            contact.add_email(new_email)
            save_to_json()
            return
    print("Contact not found.")

def save_to_json():
    """
    Serialize the in-memory contacts list to contacts.json.
    Called after every mutation so the file always reflects current state.
    """
    data = []
    for contact in contacts:
        data.append({
            "contact_id": contact.get_contact_id(),
            "name": contact.get_name(),
            "phone_numbers": contact.get_phone_numbers(),
            "emails": contact.get_emails(),
            "address": contact.get_address()
        })
    with open("contacts.json", "w") as file:
        json.dump(data, file, indent=4)

def load_from_json():
    """
    Populate the in-memory contacts list from contacts.json on startup.
    Sets Contact.counter to (id - 1) before constructing each object so the
    counter ends up at the highest saved ID, preventing ID collisions on the
    next add.
    Silently skips loading if the file doesn't exist yet (first run).
    """
    try:
        with open("contacts.json", "r") as file:
            data = json.load(file)
            for item in data:
                # Rewind counter so the Contact constructor lands on the saved ID
                Contact.counter = item["contact_id"] - 1
                contact = Contact(
                    item["name"],
                    item["phone_numbers"],
                    item["emails"],
                    item["address"]
                )
                contacts.append(contact)
    except FileNotFoundError:
        pass  # No existing save file — start fresh

def user_menu():
    """Display the main menu in a loop and dispatch to the chosen operation."""
    while True:
        print("\nEnter 1 to add contact")
        print("Enter 2 to delete contact")
        print("Enter 3 to list all contacts")
        print("Enter 4 to search by name")
        print("Enter 5 to update contact details")
        print("Enter 6 to add new phone number")
        print("Enter 7 to add new email")
        print("Enter 0 to Exit\n")

        # Re-prompt until the user enters a value in the valid menu range
        while True:
            choice = get_positive_int("Type your choice and press enter: ")
            if 0 <= choice <= 7:
                break
            print("\nChoice needs to be between 0 to 7.")

        if choice == 1:
            add_contact()
        elif choice == 2:
            delete_contact()
        elif choice == 3:
            list_all_contacts()
        elif choice == 4:
            search_by_name()
        elif choice == 5:
            update_contact_details()
        elif choice == 6:
            add_new_phone_number()
        elif choice == 7:
            add_new_email()
        elif choice == 0:
            print("\nGoodbye!")
            break


def main():
    # Load any previously saved contacts, then hand control to the menu
    load_from_json()
    user_menu()

if __name__ == "__main__":
    main()
