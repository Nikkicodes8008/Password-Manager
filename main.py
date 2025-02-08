import random
import string
import json
from pathlib import Path
data={}
file_path = Path(__file__).parent /"passwords.json"
try:
    with file_path.open("r") as f:
        data=json.load(f)
except:
    print("No saved passwords or")
    print("Error loading passwords file")
print("Welcome to Nikhil's Password Manager")

def password_generator():
    description=input("Enter description\ni.e Instagram/Facbook etc... \n").strip()
    username=input("Enter Username: ").strip()
    length=int(input("Enter the length of the password: ").strip())

    if length < 4:
        print("Password length too small")
        return
    
    upper_case=input("Should the password contain uppercase letters (y/n) : ").lower().strip()
    lower_case=input("Should the password contain lower letters (y/n) : ").lower().strip()
    special_char=input("Should the password contain special characters (y/n) : ").lower().strip()
    numbers=input("Should the password contain digits (y/n) : ").lower().strip()
    pool=""
    LOWER_CASE=string.ascii_lowercase
    UPPER_CASE=string.ascii_uppercase
    SPECIAL_CHAR=string.punctuation
    DIGITS=string.digits
    password=[]
    len_pass=0
    if lower_case=="y":
        password.append(random.choice(LOWER_CASE))
        len_pass+=1
        pool+=LOWER_CASE     
    if upper_case=="y":
        password.append(random.choice(UPPER_CASE))
        len_pass+=1
        pool+=UPPER_CASE
    if special_char=="y":
        password.append(random.choice(SPECIAL_CHAR))
        len_pass+=1
        pool+=SPECIAL_CHAR
    if numbers=="y":
        password.append(random.choice(DIGITS))
        len_pass+=1
        pool+=DIGITS
    if pool=="":
        print("You did not select any characters for password ")
        return

    for _ in range (length-len_pass):
        password.append(random.choice(pool))
 
    random.shuffle(password)
 
    str_password="".join(password)

    usr_pass={username:str_password}

    data[description]=usr_pass
    with file_path.open("w") as f:
        json.dump(data,f,indent=4)

    return str_password

def save_existing_credentials():
    description=input("Enter description\ni.e Instagram/Facbook etc... \n").strip()
    username=input("Enter Username: ").strip()
    password=input("Enter Password: ").strip()
    usr_pass={username:password}
    data[description]=usr_pass
    try:
        with file_path.open("w") as f:
            json.dump(data,f,indent=4)
        print("Credentials saved sucessfully!!!")
    except Exception as e:
        print("Error saving files")
        print(e)
    
while True:
    try:
        operation=int(input("\nWhat do you want to do? \n1.Genterate Random Password \n2.View Stored Passwords\n3.Save Existing Credentials\n4.Remomve Saved Credentials \n5.Delete all saved passwords \n6.Exit \nEnter your choice(1/2/3): "))
    except:
        print("Enter an integer")
        continue
    if operation==1:
        password=password_generator()
        print(f"Your randomly generated password is: {password}")

    elif operation==2:
        print(data)
    
    elif operation==3:
        save_existing_credentials()

    elif operation==4:
        print(data)
        try:
            description=input("Enter description for credentials to be deleted: ").strip()
            del data[description]
            print("Credentials deleted sucessfully")
        except:
            print("Error Occured")

    elif operation==5:
        data.clear()
        try:
            with file_path.open("w") as f:
                json.dump(data,f,indent=4)
            print("Data deleted sucessfully")
        except:
            print("An error occured ")
    elif operation==6:
        print("Program exited sucessfully")
        break
    else:
        print("Invalid Choice")
            