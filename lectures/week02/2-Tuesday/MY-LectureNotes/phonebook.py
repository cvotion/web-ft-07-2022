import pickle
from secrets import choice
from webbrowser import get #allows you to export data to pickle file (filename.pickle)


#!loading
try:
# reading from a file
    with open('phonebook.pickle', 'rb') as fh:
        phonebook = pickle.load(fh)
except:
    phonebook = {}        

#todo ### Global Vars    
running = True



#todo ### Functions
def menu(): #* Working
    print(f"""\n\n
          Electronic Phone Book
          ---------------------
          1. Look up an entry
          2. Set an entry
          3. Delete an entry
          4. List all entries
          5. Quit
          
          Choose an option 1 - 5.
          
          ---------------------
          """)
    
    
def find_entry(): #* Working
    name = input("What is the name of the contact you are looking for? >> ")
    number = phonebook[name]
    if name in phonebook:
        print(f"""
              Name : {name}
              Phone : {number}
              """)
    else:
        print(f"{name} does not exist in your contacts")
           

     
def set_entry(): #* Working
    name = input("Enter the name of your new contact >> ")
    number = input("Enter the phone number of your new contact >> ")
    phonebook[name] = number 
    print(f"{name} has been added to your contacts.")
              


def delete_entry(): #* Working
    name = input("Which contact would you like to delete? >> ")
    
    del phonebook[name]
    print(f"{name} has been deleted form your contacts.")
    


def print_entries(): #* Working
    for i, j in phonebook.items():
        print(f"""
              Name : {i}
              Phone Number : {j}
              """) 
    
    
def quit(): #* Working
    print("see you later!")
    #!save
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook, fh)


while running:
    menu()
    choice = int(input("What would you like to do? >> "))
    
    if choice == 1:
        find_entry()
        
    elif choice == 2:
        set_entry()
        
    elif choice == 3: 
        delete_entry()
        
    elif choice == 4: 
        print_entries() 
                
    elif choice == 5:
        quit() 
        running = False        
    
    else:
        print("Sorry, that is not a valid input!")
        menu()
    