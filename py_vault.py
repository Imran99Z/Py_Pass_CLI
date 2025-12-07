import sys
import time 
import json 
import os 
from getpass import getpass

from cryptography.fernet import Fernet
import keyring 

vault_f = "vault"
log_f = "login.csv"
key_f= "vault.key"
serv_n = "password_cli"
master = "admin"

def main():
    while True:
        choice = show_home_menu()
        if choice == "1":
            handle_login_flow()
        elif choice == "2":
            print("Exiting program.")
            sys.exit(0)
        else:
            print("Invalid choice. Exiting.")
            sys.exit(0)

def show_home_menu():
    print("\n=== Password Vault CLI ===")
    print("1) Log in")
    print("2) Exit")
    return input("Select an option (1-2): ").strip()

def show_home_menu():
    print("\n=== Password Vault CLI ===")
    print("1) Log in")
    print("2) Exit")
    return input("Select an option (1-2): ").strip()

def handle_login_flow():
    print("\n--- Login Required ---")
    print("Type 'login' to continue or 'exit' to return home.")
    print("Anything else = quit program.")
    
    attempts = 0
    while attempts < 3:
        user_input = input("Your choice: ").strip().lower()
        
        if user_input == "exit":
            print("Returning to home...")
            return  # back to main menu
        
        elif user_input != "login":
            print("Unrecognized input. Quitting.")
            sys.exit(0)
        
        # Simulate password check (real one later)
        password = getpass("Enter master password: ")
        print("✅ Password correct! (simulated)")
        print("Logging in...")
        time.sleep(1)  # fake delay
        print("🔐 Access granted. Loading vault...")
        vault_menu()  # we'll build this next
        return
        
        # Wrong password (uncomment later)
        # attempts += 1
        # print(f"❌ Incorrect password. {3-attempts} attempts left.")
    
    print("🚫 Too many failed attempts. Closing program.")
    sys.exit(0)

def vault_menu():
    print("\n=== Secure Password Manager ===")
    print("Access enabled for all files.")
    print("1) Add files  2) List files  3) Search files  4) Delete  5) Logout")
    input("Press Enter to continue building...")
    print("Logging out...")

if __name__ == "__main__":
    main()
