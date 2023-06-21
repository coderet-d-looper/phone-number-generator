import random
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def generate_phone_number(operator, count):
    operator_codes = {
        'GP': ['017', '013', '016', '015'],
        'BL': ['019', '014', '018'],
        'RB': ['017', '018'],
        'AT': ['016']
    }

    operator_prefixes = operator_codes.get(operator.upper())

    if operator_prefixes is None:
        print(Fore.RED + "Invalid operator selection!")
        return None

    phone_numbers = []

    for _ in range(count):
        prefix = random.choice(operator_prefixes)
        number = str(random.randint(10000000, 99999999))
        phone_number = f"+880{prefix}{number}"
        phone_numbers.append(phone_number)

    return phone_numbers

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def show_welcome_message():
    typewriter(Fore.GREEN + "***********************************************************")
    typewriter(Fore.GREEN + "*                                                         *")
    typewriter(Fore.GREEN + "*            Welcome to the Phone Number Generator        *")
    typewriter(Fore.GREEN + "*                                                         *")
    typewriter(Fore.GREEN + "*                 Made by coderet-d-looper                *")
    typewriter(Fore.GREEN + "*                                                         *")
    typewriter(Fore.GREEN + "***********************************************************")
    typewriter("\n")
    typewriter(Fore.GREEN + "Please provide your credentials to proceed.")

def get_user_credentials():
    username = input(Fore.YELLOW + "Username: ")
    password = input(Fore.YELLOW + "Password: ")
    return username, password

def authenticate_user(username, password):
    # Perform authentication logic here
    # You can replace this with your own authentication mechanism
    if username == "admin" and password == "password":
        return True
    return False

def redirect_to_facebook():
    typewriter(Fore.RED + "Redirecting to the owner's Facebook page...")  # Replace with appropriate redirect logic

def clear_previous_texts():
    clear_console()
    print(Fore.GREEN + "Welcome back, admin!")

def generate_and_display_numbers(operator, count):
    typewriter("Generating numbers...")

    phone_numbers = generate_phone_number(operator, count)

    if phone_numbers:
        clear_console()
        print("\nGenerated phone numbers:")
        for number in phone_numbers:
            typewriter(Fore.MAGENTA + number)
            time.sleep(0.5)

        typewriter("\nScanning for active numbers...")
        print("\nValidation results:")
        for number in phone_numbers:
            active = is_active_number(number)
            if active:
                typewriter(Fore.GREEN + f"Active: {number}")
            else:
                typewriter(Fore.RED + f"Inactive: {number}")
            time.sleep(0.5)

def is_active_number(phone_number):
    # Add logic to check if the phone number is active/valid
    # You can use APIs or libraries to perform number validation
    # This is just a placeholder logic
    if phone_number.endswith('000000'):
        return False
    return True

# Example usage:
show_welcome_message()

username, password = get_user_credentials()

if authenticate_user(username, password):
    clear_previous_texts()

    print(Fore.GREEN + "Username and password are correct.")
    while True:
        print("\nSelect an option:")
        print("1. Generate phone numbers")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            operator = input(Fore.CYAN + "Enter the operator (GP, BL, RB, or AT): ")
            count = int(input(Fore.CYAN + "Enter the number of phone numbers to generate: "))

            generate_and_display_numbers(operator, count)

        elif choice == '2':
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

else:
    print(Fore.RED + "Username or password is incorrect.")
    redirect_to_facebook()