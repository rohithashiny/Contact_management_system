# Basic Contact Management System

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
        print("--------------------")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
