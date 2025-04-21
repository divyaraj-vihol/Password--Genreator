import random
import string

def calculate_strength(pwd):
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if length >= 12 and score == 4:
        return "Strong 💪"
    elif length >= 8 and score >= 3:
        return "Medium 🔐"
    else:
        return "Weak ⚠️"

def generate_password(min_length=8, use_upper=True, use_lower=True,
                      use_numbers=True, use_specials=True,
                      avoid_similar=False):
    similar_chars = 'l1I0Oo'
    characters = ''
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if avoid_similar:
        characters = ''.join(c for c in characters if c not in similar_chars)

    if not characters:
        return "Error: No character types selected!"

    pwd = ""
    has_number = False
    has_special = False

    while len(pwd) < min_length or \
          (use_numbers and not has_number) or \
          (use_specials and not has_special):

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in string.digits:
            has_number = True
        if new_char in string.punctuation:
            has_special = True

    return pwd


min_length = int(input("Enter the minimum password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_specials = input("Include special characters? (y/n): ").lower() == 'y'
avoid_similar = input("Avoid similar characters (l, 1, I, 0, O)? (y/n): ").lower() == 'y'
how_many = int(input("How many passwords to generate? "))

print("\nGenerated Password(s):")
for _ in range(how_many):
    pwd = generate_password(min_length, use_upper, use_lower, use_numbers, use_specials, avoid_similar)
    strength = calculate_strength(pwd)
    print(f"{pwd}  -->  {strength}")

