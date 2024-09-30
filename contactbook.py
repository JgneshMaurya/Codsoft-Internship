contact_book = []

def display_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contact_book, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Location: {contact['location']}")
    print()

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    location = input("Enter contact location: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'location': location
    }
    
    contact_book.append(contact)
    print(f"Contact '{name}' added!\n")

def update_contact():
    display_contacts()
    if contact_book:
        try:
            contact_num = int(input("Enter the serial number of the contact to update: "))
            contact = contact_book[contact_num - 1]
            
            print(f"Updating contact: {contact['name']}")
            contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
            contact['location'] = input(f"Enter new location ({contact['location']}): ") or contact['location']
            
            print(f"Contact '{contact['name']}' updated!\n")
        except (ValueError, IndexError):
            print("Invalid contact number!\n")
def delete_contact():
    display_contacts()
    if contact_book:
        try:
            contact_num = int(input("Enter the serial number of the contact to delete: "))
            removed_contact = contact_book.pop(contact_num - 1)
            print(f"Contact '{removed_contact['name']}' deleted!\n")
        except (ValueError, IndexError):
            print("Invalid contact number!\n")

def show_menu():
    print("Contact Book Menu:")
    print("1. View All Contacts")
    print("2. Add a New Contact")
    print("3. Update a Contact")
    print("4. Delete a Contact")
    print("5. Exit")
def contact_book_app():
    while True:
        show_menu()
        choice = input("Enter your choice between 1 to 5 : ")
        
        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice! Please give valid input !.\n")
contact_book_app()
