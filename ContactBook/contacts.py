contacts = []

class Contact:
    def __init__(self, phone_number, name, email):
        self.phone_number = phone_number
        self.name = name
        self.email = email

    def view_contacts(array):
        for contact in array:
            print("---")
            print(contact.name)
            print(contact.phone_number)
            print(contact.email)
            print("---\n")
    
    def add_contact(array):
        phone_number = input("Enter a phone number: ")
        name = input("Ente a name: ")
        email = input("Enter an email: ")

        contact = Contact(phone_number, name, email)
        array.append(contact)
    
    def remove_contact(array):
        name = input("Which contact would you like to remove? ")
        for contact in array:
            if contact.name != name:
                continue
            else:
                print("---")
                print(contact.name)
                print(contact.phone_number)
                print(contact.email)
                print("---")

                option = input("Do you really want to remove this contact? (Y/n)")
                if option == 'y':
                    array.remove(contact)
    
    def edit_contact(array):
        contact = input("Which contact would you like to edit? (enter name) ")
    
                    

print("--------Contact Book--------")

while True:

    option = input("\nWhat would you like to do? (view (v), add (a), remove (r), edit (e), quit (q) )")

    if option == 'q':
        break

    elif option == 'v':
        Contact.view_contacts(contacts)
    
    elif option == 'a':
        Contact.add_contact(contacts)

    elif option == 'r':
        Contact.remove_contact(contacts)

    elif option == 'e':
        Contact.edit_contact(contacts)

    else:
        print("Invalid option!")