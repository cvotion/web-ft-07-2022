import contacts

contacts_data = contacts.data

# name
# address (street, suite, city, zip)

for i in range(len(contacts_data[0])):
    print(f"""\n
          Name : {contacts_data[i]['name']}
          Street :
          
          
          """)