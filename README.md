# Password--Genreator

👉The generate_password function creates random passwords based on user-specified criteria, such as minimum length, inclusion of uppercase letters, lowercase letters, numbers, and special characters. It also allows users to exclude certain characters like 'l', '1', 'I', '0', and 'O' to avoid confusion. The generated passwords are guaranteed to meet the specified requirements, ensuring a strong password.
Password Strength Checker and Generator
This Python script provides tools for both checking the strength of passwords and generating secure passwords.

Features:
Password Strength Checker:
This function checks the strength of a given password and returns a rating based on its composition:

Strong 💪: Length >= 12 and contains at least one uppercase letter, one lowercase letter, one digit, and one special character.

Medium 🔐: Length >= 8 and contains at least three of the required components.

Weak ⚠️: Otherwise.

Password Generator:
This function generates secure passwords with customizable options:

Minimum Length: Set the minimum length for the generated password.

Character Options: Choose whether to include uppercase letters, lowercase letters, numbers, and special characters.

Avoid Similar Characters: Option to avoid characters like 'l', '1', 'I', '0', 'O' to avoid confusion.
