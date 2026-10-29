contact = {}

while True:
    print("\n'1' : Add Contact '2' : Search Contact '3' : List '4' : Exit")
    choice = input("Enter Your Choice : ")
    if choice == "1":
        name = input("Enter Name : ")
        phone = input("Enter Phone : ")
        email = input("Enter Email : ")        
        contact[name] = [phone, email]
        print(f"Contact '{name}' added successfully!")
    elif choice == "2":
        search = input("Enter name to Search : ")
        found = False
        for name in contact:
            if search.lower() == name.lower():
                print(f"Name: {name} \nPhone: {contact[name][0]} \nEmail: {contact[name][1]}")
                found = True
                break 
        if not found:
            print("Contact not found.")
    elif choice == '3':
        if not contact:
            print("Contact book is empty.")
        else:
            print("\n*Contact List*")
            for name in contact:
                print(f"Name: {name} \nPhone: {contact[name][0]} \nEmail: {contact[name][1]}")
               
    elif choice == "4":
        print("Exiting contact book. Goodbye!")
        break
    else:
        print(f"{choice}Invalid choice. Please enter a number between 1 and 4.")
        break