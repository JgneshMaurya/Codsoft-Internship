import random
import string

def generate_password(length, use_letters, use_digits, use_special_chars):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters 
    if use_digits:
        characters += string.digits  
    if use_special_chars:
        characters += string.punctuation 
    if not characters:
        return "Error: No character types selected for password generation."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length (minimum 4): "))
    
    if length < 4:
        print("Error: Password length must be at least 4 characters.")
    else:
        use_letters = input("Do you want to include letters? (y/n): ").lower() == 'y'
        use_digits = input("Do you want to include numbers? (y/n): ").lower() == 'y'
        use_special_chars = input("Do you want to include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_digits, use_special_chars)
        print(f"Generated password: {password}")
except ValueError:
    print("Error: Please enter a valid number for the password length.")
