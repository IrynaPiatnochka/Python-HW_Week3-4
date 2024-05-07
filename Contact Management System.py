import re

def export_data(contact_data):
        with open('contacts.txt', 'w') as file:
            for contact in contact_data.values():
                line = '\t'.join([contact["name"], contact["phone"], contact["email"], contact["additional_info"]])
                file.write(line + '\n')
        print("Data was exported.")
    
def import_data(contact_data):
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, phone, email, additional_info = line.strip().split('\t')
                contact_data[name] = {"name": name, "phone": phone, "email": email, "additional_info": additional_info}
                name = re.search(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', line)
                email = re.match(r"[^@]+@[^@]+\.[^@]+", email)
        print("Data was imported.")
    except FileNotFoundError:
        print("File not found.")

def add_new(contact_data):
    name = input('Enter name: ')
    phone = input('Phone number: ')
    email = input('Email: ')
    additional_info = input('Enter additional information (optional): ')
    
    contact_data[name] = {"name": name, "phone": phone, "email": email, "additional_info": additional_info}
    print(f'Added {name} to the contact list.')

def edit(contact_data):
    name = input('Enter the name of the contact you want to edit: ')
    if name in contact_data:
        print("Name:", contact_data[name]["name"])
        print("Phone:", contact_data[name]["phone"])
        print("Email:", contact_data[name]["email"])
        print("Additional Info:", contact_data[name]["additional_info"])
        
        choice = input("What do you want to edit: name, phone, email or additional info)? ").lower()
        if choice in contact_data[name]:
            new_value = input(f'Enter new {choice}: ')
            contact_data[name][choice] = new_value
            print("Contact details updated.")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")

def delete(contact_data):
    name = input('Enter the name of the contact you want to delete: ')
    if name in contact_data:
        del contact_data[name]
        print(f'{name} deleted from the contact list.')
    else:
        print("Contact not found.")

def search(contact_data):
    search_contact = input("Enter the name to find: ")
    found_contact = [contact for contact in contact_data.values() if search_contact.lower() in contact["name"].lower()]
    if found_contact:
        print("Contact found.")
        for contact in found_contact:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Additional Info:", contact["additional_info"])
            print()
    else:
        print("No contact found.")

def display_all(contact_data):
    if not contact_data:
        print("No contacts found.")
    else:
        for contact in contact_data.values():
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Additional Info:", contact["additional_info"])
            print()

def runner():
    contact_data = {}
    print("Welcome to the Contact Management System!")
    while True:
        action = input('''
Menu
*************************************
1.) Add a new contact
2.) Edit an existing contact
3.) Delete a contact
4.) Search for a contact
5.) Display all contacts
6.) Export contacts to a text file
7.) Import contacts from a text file
8.) Quit
> ''')
        if action == '1':
            add_new(contact_data)
        elif action == '2':
            edit(contact_data)
        elif action == '3':
            delete(contact_data)
        elif action == '4':
            search(contact_data)
        elif action == '5':
            display_all(contact_data)
        elif action == '6':
            export_data(contact_data)
        elif action == '7':
            import_data(contact_data)
        elif action == '8':
            print('Quit')
            break
        else:
            print('Invalid selection.')

runner()