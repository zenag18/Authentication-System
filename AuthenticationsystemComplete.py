# Authentication System Project

# Step 1: Create menu
# Step 2: SignUp
'''
SignUp requirements:
Ask the Name of person
User must enter a valid email as a userName
password must be at-least 8 character.

name,email,password\n
'''

def signUp():
    # This function is used to register the user
    print("\n***** Registration Menu *****")
    name = input("Enter your name :")
    email = input("Enter your email :")  # zenagmail.com
    while "@" not in email:
        email = input("Invalid Email - Please enter a valid Email Again:")
    password = input("Enter your password (at-least 8 char):") #zena123
    while len(password) < 8:                                       # len()  used to count the string characters
        password = input("Invalid Password - Please enter a valid Password Again :")
    file = open("users.txt","a")

    file.write(name+","+email+","+password+"\n")
    file.close()
    print(name,"you have been registered Successfully !")


def login():
    email = input("Enter your email :")
    password = input("Enter your password :")
    file = open("users.txt","r")
    found = False
    for x in file:   # x is holding each line in each iteration
        name,actualEmail,actualPass = x.split(",")
        if actualEmail.lower() == email.lower() and actualPass.strip() == password:
            print("Login successful as",name)
            found = True
            break
    if not found :
        print("Invalid user !!!")

while True:
    print("**** Fun Time World *****\n")
    print("1. SignUp")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Choose :"))
    if choice==1:
        signUp()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Thanks for using this Application !")
        break




