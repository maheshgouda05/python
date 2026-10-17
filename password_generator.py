
import string
import random

def generate_password():
    print("===== Random Password Generator =====")

    try:
        # Get password length from the user
        length = int(input("Enter password length (minimum 12): "))

        if length < 12:
            print("Error: Password must contain at least 12 characters.")
            return

        # Ask for character preferences
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower()
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower()
        use_digits = input("Include numbers? (yes/no): ").lower()
        use_symbols = input("Include special characters? (yes/no): ").lower()

        # Validate user preferences
        preferences = [
            use_lowercase, use_uppercase, use_digits, use_symbols
        ]

        if any(choice not in ("yes", "no") for choice in preferences):
            print("Error: Please enter only 'yes' or 'no'.")
            return

        # Build character sets
        characters = ""
        required_characters = []

        if use_lowercase == "yes":
            characters += string.ascii_lowercase
            required_characters.append(random.choice(string.ascii_lowercase))

        if use_uppercase == "yes":
            characters += string.ascii_uppercase
            required_characters.append(random.choice(string.ascii_uppercase))

        if use_digits == "yes":
            characters += string.digits
            required_characters.append(random.choice(string.digits))

        if use_symbols == "yes":
            characters += string.punctuation
            required_characters.append(random.choice(string.punctuation))

        if not characters:
            print("Error: Select at least one character type.")
            return

        if len(required_characters) > length:
            print("Error: Password length is too short for your preferences.")
            return

        # Generate remaining characters
        remaining_length = length - len(required_characters)
        password_characters = required_characters + [
            random.choice(characters)
            for _ in range(remaining_length)
        ]

        # Shuffle the characters
        random.shuffle(password_characters)

        # Display the password
        password = "".join(password_characters)

        print("\nYour generated password is:")
        print(password)

    except ValueError:
        print("Error: Please enter a valid whole number for the length.")

generate_password()
