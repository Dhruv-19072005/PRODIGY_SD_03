import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"\n✅ Contact '{name}' added successfully!")


def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        choice = int(input("\nEnter the contact number to edit: "))
        if 1 <= choice <= len(contacts):
            contact = contacts[choice - 1]
            print(f"Editing '{contact['name']}'. Leave field blank to keep existing value.")

            new_name = input(f"New name ({contact['name']}): ").strip()
            new_phone = input(f"New phone ({contact['phone']}): ").strip()
            new_email = input(f"New email ({contact['email']}): ").strip()

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)
            print("\n✅ Contact updated successfully!")
        else:
            print("\n❌ Invalid contact number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        choice = int(input("\nEnter the contact number to delete: "))
        if 1 <= choice <= len(contacts):
            removed = contacts.pop(choice - 1)
            save_contacts(contacts)
            print(f"\n✅ Contact '{removed['name']}' deleted successfully!")
        else:
            print("\n❌ Invalid contact number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")


def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nGoodbye! Your contacts have been saved.")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
