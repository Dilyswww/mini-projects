pwd = ("What is the master password?")

def view():
    pass

def add():
    website = input("Website name: ")
    account = input("Account name: ")
    password = input("Password: ")
    
    # open file in append mode
    with open("password.txt", "a") as f:
        f.write(website + " | " + account + " | " + password + "\n")

while True:
    mode = ("Would you like to add a new password or view existing ones (view, add)? press q to quit.").lower()
    if mode == "q":
        break
    elif mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode")
        continue