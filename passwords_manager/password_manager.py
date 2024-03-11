from cryptography.fernet import Fernet
from password_generator import generate_psw

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""

# write_key()

def load_key():
    # open file in read byte mode
    file = open("key.key", "rb")
    key = file.read()
    file.close()   
    return key

# write_key()
# master_pwd = input("What is the master password?")
key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            website, account, password = data.split("|")
            print("Website:", website, " Account:", account, " Password:", fer.decrypt(password.encode()).decode())
            
def add():
    website = input("Website name: ")
    account = input("Account name: ")
    
    # Ask user for password length and preferences
    min_length = int(input("Enter the minimum length of the password: "))
    has_number = input("Do you want numbers in the password? (y/n): ").lower() == "y"
    has_special = input("Do you want special characters in the password? (y/n): ").lower() == "y"
    password = generate_psw(min_length, has_number, has_special)
    
    # open file in append mode
    with open("passwords.txt", "a") as f:
        f.write(website + "|" + account + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? press q to quit.").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue