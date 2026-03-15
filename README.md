# contact-book-python

A Python command-line application to manage a contact book,
built using Object-Oriented Programming (OOP) principles.

## About
This program allows users to add, delete, search, and update contacts
via a console menu. Each contact supports multiple phone numbers and
email addresses stored as lists. Data is persisted across sessions
using a single JSON file. Built as a personal OOP and JSON practice
project.

## Features
- Contact class with private attributes (ID, name, phone numbers,
  emails, address)
- Auto-incrementing unique contact IDs
- Getter and setter methods for all attributes
- Dedicated append methods for adding extra phones and emails
- Add a new contact with multiple phone numbers and emails
- Delete a contact by ID
- List all contacts
- Search contacts by name
- Update all fields of an existing contact
- Add an additional phone number to an existing contact
- Add an additional email to an existing contact
- Save/load all data to/from a single JSON file for persistence
- Thoroughly commented and docstringed throughout for readability
- Input validation separated into a dedicated validators.py module

## Project Structure
```
contact-book-python/
│
├── contact_book.py     ← main program
├── validators.py       ← input validation functions
└── contacts.json       ← contact records (auto-generated)
```

## How to Run
```bash
python contact_book.py
```

## Built With
- Python 3
- OOP — classes, private attributes, getter/setter methods,
  append helper methods
- JSON module for nested data persistence
- Separated input validation module for clean, reusable code

## Data Persistence
All contacts including nested phone numbers and emails are saved
to contacts.json after every operation and fully restored on next
launch. JSON is used over CSV here to naturally handle each
contact's variable number of phones and email addresses.

## JSON Structure
```json
[
    {
        "contact_id": 1,
        "name": "Al Amin Alif",
        "phone_numbers": ["+46722099130"],
        "emails": ["alamin.alif.7@gmail.com"],
        "address": "Borlänge, Sweden"
    }
]
```
