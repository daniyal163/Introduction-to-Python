contact = {
    "Joe": ["09811", "joe@gmail.com"],
    "Harry": ["11223", "harry@gmail.com"]
}

search = input("Enter name to search details: ")
found = False

for name in contact:
    if search.lower() == name.lower():
        print(f"Name: {name} \nPhone: {contact[name][0]} \nEmail: {contact[name][1]}")
        found = True
        break

if not found:
    print("Contact not found.")
    choice = input("Do you want to add this contact? (y/n): ").lower()
    
    if choice == 'y':
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        
        # Add the new contact to the dictionary
        contact[search] = [phone, email]
        print(f"Contact added successfully!")
        print(f"Name: {search} \nPhone: {phone} \nEmail: {email}")
    else:
        print("Thank you for using the contact book!")
else:
    print("Thank you")