# main_menu.py
# Home Screen, Login Loop, and Program Connector

import sys
from getpass import getpass
from master_password_manager import retrieve_master_password, set_master_password
from vault_loop import vault_main


def home_menu():
    """Home screen for user."""
    print("\n=== Password Vault CLI ===")
    print("1) Login")
    print("2) Exit")
    return input("Select an option (1 or 2): ").strip()


def login_loop():
    """Simple login using stored master password."""
    stored = retrieve_master_password()

    if stored is None:
        print("No master password found. You must set one.")
        set_master_password()
        stored = retrieve_master_password()

    attempts = 3
    while attempts > 0:
        password = getpass("Enter Master Password: ")
        if password == stored:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")

    print("Too many failed attempts. Exiting.")
    return False


def main():
    """Main connector controlling program flow."""
    while True:
        choice = home_menu()

        if choice == "1":
            success = login_loop()
            if success:
                print("\nEntering Vault Menu...")
                vault_main()
        elif choice == "2":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Program will close.")
            sys.exit()


if __name__ == "__main__":
    main()
