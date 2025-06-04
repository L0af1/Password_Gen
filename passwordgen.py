import secrets
import string
import time

def generate_password(length=15, exclude_special=False, prefix=""):
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # Modify character pool based on the option
    if exclude_special:
        character_pool = letters + digits
    else:
        character_pool = letters + digits + special_characters

    # Ensure the password includes at least one character from each active category
    password = []
    password.append(secrets.choice(letters))  # At least one letter
    password.append(secrets.choice(digits))  # At least one digit
    if not exclude_special:
        password.append(secrets.choice(special_characters))  # At least one special character

    # Fill the rest of the password length
    remaining_length = length - len(prefix) - len(password)
    if remaining_length < 0:
        raise ValueError("Prefix length is too long for the specified password length.")

    password += [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Shuffle the password to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    return prefix + ''.join(password)

def save_password_to_file(password, file_name="passwords.txt"):
    try:
        with open(file_name, "a") as file:
            file.write(password + "\n")
        print(f"Password saved to {file_name}")
    except Exception as e:
        print(f"An error occurred while saving the password: {e}")

if __name__ == "__main__":
    print("\033[91m" + """
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗  -██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗-██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║-██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║-██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝-╚██████╔╝███████╗██║ ╚████║ 
                      by xavi  #ANSI SHADOW                     
    """ + "\033[0m")

    print("Make sure of the following:")
    print("1. Disregard capital letters (at the beginning of words)")
    print("2. Write two-letter words as two words or one word if you like (e.g., \"New York\")")

    print("\n[*] Password properties")
    print("=> 12 <= length <= 20")
    print("amount of digits >= 20 Max")
    print("amount of uppercase characters >= ∞")
    print("amount of lowercase characters >= ∞")
    print("amount of special characters >= ∞")
    print("add capitalized/un-capitalized versions of words => True")

    # User inputs two words for the prefix
    prefix = input("\nChoose 2 words to include in your password or one word if you like (e.g., NewYork): ").replace(" ", "")

    # User selects password length
    while True:
        try:
            length = int(input("\nEnter the desired password length (12-20): "))
            if 12 <= length <= 20:
                break
            else:
                print("Please enter a valid length between 12 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number between 12 and 20.")

    print("\n[+] Options")
    print("1. Generate password with special characters (e.g., !@#$%)")
    print("2. Generate password with only letters and numbers")
    choice = input("Pick option 1 or 2: ")

    # Validate user choice and generate the password
    if choice == "1":
        print("\nYou selected: Password with special characters.")
        generated_password = generate_password(length=length, exclude_special=False, prefix=prefix)
    elif choice == "2":
        print("\nYou selected: Password with only letters and numbers.")
        generated_password = generate_password(length=length, exclude_special=True, prefix=prefix)
    else:
        print("\nInvalid choice. Please run the program again and select either 1 or 2.")
        exit()

    # Display the generated password with progress simulation
    print("\nStarting to generate password...")
    for i in range(0, 101, 10):
        time.sleep(0.2)  # Simulate loading time
        print(f"Status: generating [{i}% completed]")

    print("\nGenerated Password:", generated_password)
    save_password_to_file(generated_password)
    print("\nPassword saved to passwords.txt")
