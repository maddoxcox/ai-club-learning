# Day 7: Contact Book
# A CLI contact manager with JSON persistence.

import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from JSON file. Return empty list if file doesn't exist."""
    # TODO: Check if file exists
    # TODO: Read and parse JSON
    # TODO: Handle corrupted JSON
    return []


def save_contacts(contacts):
    """Save contacts to JSON file."""
    # TODO: Write contacts to JSON file with nice formatting (indent=2)
    pass


def add_contact(contacts):
    """Add a new contact."""
    # TODO: Prompt for name, phone, email, category
    # TODO: Generate unique ID
    # TODO: Append to contacts list
    # TODO: Save to file
    pass


def search_contacts(contacts):
    """Search contacts by name (partial, case-insensitive)."""
    # TODO: Get search query
    # TODO: Filter contacts
    # TODO: Display results
    pass


def list_contacts(contacts):
    """Display all contacts in a formatted list."""
    # TODO: Handle empty list
    # TODO: Print each contact nicely
    pass


def edit_contact(contacts):
    """Edit an existing contact."""
    # TODO: Search for the contact
    # TODO: Show current values
    # TODO: Prompt for new values (Enter to keep current)
    # TODO: Save changes
    pass


def delete_contact(contacts):
    """Delete a contact with confirmation."""
    # TODO: Search for the contact
    # TODO: Confirm deletion
    # TODO: Remove and save
    pass


def export_to_csv(contacts):
    """Export contacts to a CSV file."""
    # TODO: Use csv module to write contacts to contacts.csv
    pass


def main():
    """Main menu loop."""
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book ===")
        print("[1] Add contact")
        print("[2] Search contacts")
        print("[3] List all contacts")
        print("[4] Edit contact")
        print("[5] Delete contact")
        print("[6] Export to CSV")
        print("[7] Quit")

        choice = input("\nChoice: ").strip()

        # TODO: Handle menu choices
        # TODO: Handle invalid input


if __name__ == "__main__":
    main()
