import random
import string

def generate_psw(min_length, numbers = True, has_special = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if numbers:
        characters += digits
    if has_special:
        characters += special
        
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if has_special:
            meets_criteria = meets_criteria and has_special
    return pwd
            
'''
if __name__ == "__main__":
    min_length = int(input("Enter the minimum length of the password: "))            
    has_number = input("Do you want numbers in the password? (y/n): ").lower() == "y"
    has_special = input("Do you want special characters in the password? (y/n): ").lower() == "y"

    pwd = generate_psw(min_length, has_number, has_special)
    # print(pwd)
'''