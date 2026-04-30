phonebook = {}

print("------- Phonebook Menu ------")
print("1. Add new contact ")
print("2. Search for a contact ")
print("3. Delete a contact ")
print("4. List all contacts ")
print("5. Exit ")

while True:
    x = input("Enter your choice (1-5) : ")

    if x == '1':
        name = input("Enter contact name : ")
        if name in phonebook:
            print(f"{name} already exists.")
        else:
            number = input("Enter number : ")
            phonebook[name] = number
            print("Contact successfully added.")

    elif x == '2':
        name = input("Enter contact name : ")
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print("Contact not found.")

    elif x == '3':
        name = input("Enter contact name : ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif x == '4':
        print(" ------ All Contacts ------")
        if phonebook:
            for name, number in phonebook.items():
                print(f"{name} : {number}")
        else:
            print("Phonebook is empty.")

    elif x == '5':
        print("Exiting Phonebook. Goodbye!")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 5.")

