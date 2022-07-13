# Bank (class)
    # properties
        # name 
        # address 
        # list all of members
    #methods
        #* add an account holder to the account_holders list
        #* searchBy Name
        #* total bank balance 
        #* see all of our members 
        #* hightest account holder 
        
# Account
    # name 
    # balance
    
    
class Bank:
    def __init__(self, name, address):
        self.name = name
        self.account_holders = 0
        self.total_balance = 0.00
        self.address = address
        self.members = []
        
    def add_member(self, name, balance):
        name = Account(name, balance)
        self.account_holders += 1
        self.members.append(name)
        self.total_balance += balance
        
    def search(self, member):
        for each_account in self.members:
            if each_account.name == member:
                print(f"{each_account.name}'s balance is ${each_account.balance}")   
    def print_balance(self):
        print(f"The total bank balance is : ${self.total_balance}")      
    def print_members(self):
        for member in self.members:
            print(f"{member.name}:${member.balance}")      
    def richest_member(self):
        rich_member = 0
        rich_member_name = ''
        print(rich_member)
        for member in self.members:
            if member.balance > rich_member:
                rich_member = member.balance 
                rich_member_name = member.name   
        print(f"{rich_member_name} is the richest member with a balance of ${rich_member}") 
        
           
class Account:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance        
        
        
        
rbfcu = Bank('RBFCU', '1 RBFCU Pkwy, Live Oak, TX, 78233')

rbfcu.add_member('Shannon', 100.00) 
rbfcu.add_member('Dan', 50.00)
rbfcu.add_member('Ryan', 1.00)
rbfcu.add_member('Peyton', 115.00)
rbfcu.add_member('Thommas', 20.00)
rbfcu.add_member('Tommy', 13.00)  

rbfcu.search('Shannon')
rbfcu.print_balance() 
rbfcu.print_members() 
rbfcu.richest_member()