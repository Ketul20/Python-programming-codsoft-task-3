import random
import string


def generate_password(length, complexity):
    characters = ""
    if 'l' in complexity:
        characters += string.ascii_lowercase
    if 'u' in complexity:
        characters += string.ascii_uppercase
    if 'd' in complexity:
        characters += string.digits
    if 's' in complexity:
        characters += string.punctuation

    if not characters:
        print("No complexity options selected. Using default characters.")
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_complexity():
    print("\nPassword complexity options:")
    print("l - Include lowercase letters")
    print("u - Include uppercase letters")
    print("d - Include digits")
    print("s - Include symbols")

    while True:
        complexity = input("Enter desired complexity (e.g., 'luds' for all options): ").lower()
        if all(c in 'luds' for c in complexity):
            return complexity
        else:
            print("Invalid complexity options. Please enter only 'l', 'u', 'd', or 's'.")


def password_strength(password):
    """Evaluate the strength of the password."""
    strength = "Weak"
    if len(password) >= 12 and (any(c.islower() for c in password) and
                                any(c.isupper() for c in password) and
                                any(c.isdigit() for c in password) and
                                any(c in string.punctuation for c in password)):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Moderate"
    return strength


def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Password length should be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    complexity = get_complexity()

    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate? "))
            if num_passwords <= 0:
                print("Please enter a positive number for the number of passwords.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(length, complexity)
        strength = password_strength(password)
        print(f"{password} (Strength: {strength})")


if __name__ == "__main__":
    main()