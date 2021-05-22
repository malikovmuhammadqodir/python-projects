import os

class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        print(f'{self.first} {self.last}')    


    def __str__(self):
        return f'{self.first} {self.last} : {self.age} : {self.phone_number}'

contacts = list()        


if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_lsit = f.readlines()
        for contact_line in csv_lsit:
            contact_data = contact_line.rstrip().split(",")
            contact = Person(contact_data[0],
                             contact_data[1],
                             contact_data[2],
                             contact_data[3])
            contacts.append(contact)  


users_input = ""

print('welome to address book information program')

while users_input != 'q':
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contacts")
    print("3 - Find conact")
    print("q - quit program")
    users_input = input("Select option: ")

    if users_input == '1':
        print('Enter your contact\'s below')

        first_name = input('first name = ')
        last_name = input('last name = ')
        age = input('your age = ')
        phone_number = input('your phone number ')
        our_contact = Person(first_name, last_name, age, phone_number)
        contacts.append(our_contact)
        print('thank you')

    
    elif users_input == '2':
        for contact in contacts:
            print(contact)
        input('Contacts displayed. Hit enter to contine')
    elif users_input == '3':
        to_lookup = input("Enter contact's name to lookup: ")
        for to_lookup in contacts:
            if to_lookup in contact.full_name():
                print(contact)
    elif users_input.lower() == 'q':
        break


with open('contacts.csv', 'w') as f:
    for contact in contacts:
        f.write(f'{contact.first},{contact.last},{contact.age},{contact.phone_number}\n')

print('thank you we have recieved your inforamtion!')
