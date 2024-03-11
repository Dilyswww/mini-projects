import random
import string

def generate_psw(min_length, numbers = True, special_chars = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special
        
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        # pwd = ''.join(random.choice(characters) for i in range(min_length))
        # for char in pwd:
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
    return pwd
            
pw = generate_psw(8, True, True)
print(pw)