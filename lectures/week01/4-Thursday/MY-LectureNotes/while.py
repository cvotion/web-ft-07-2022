
#1. Create a program that will print from 1-10 using a while loop.

# count = 1

# while count <= 10:
#     print(count)
#     count += 1

# #2. Create a program that will print from 10-1 using a while loop.

# count = 10

# while count > 0:
#     print(count)
#     count -= 1

# #3. Create a program that prompts the user to enter a word.  The program doesn't stop asking the user to enter a word until the user enters the word "stop"

# question = input("enter a word >> ")



# while question.lower() != "stop" :
#     question = input("enter a word >> ")

# # #4a. Create a program that has a variable named username and another variabled named password with values of your choice.
username = "c_votion"
password = "pass_word123"
pass_attempt = 0

# # #4b. Prompt the user for a username and then a password.
username_input = input("Create a username >> ")
password_input = input("Create a password >> ")
# #4c. If the both match continue on with the program and give a welcome message.
if (username_input == username and password_input == password):
    print("Welcome")
# #4d. If not it prompts the user for the username and password until they get it correct.
else:
    while (username_input != username or password_input != password):
        print("That is incorrect")
        username_input = input("Create a username >> ")
        password_input = input("Create a password >> ")
        pass_attempt += 1
        if (pass_attempt > 3):
            print("too many attempts!")
            break
#4e. (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.
