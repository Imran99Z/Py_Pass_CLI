# vault_loop.py
# Encrypted Vault File & Menu

import json
import os
from cryptography.fernet import Fernet
from getpass import getpass

VAULT_FILE = "vault_data.enc"
KEY_FILE = "vault_key.key"


# ========== KEY MANAGEMENT ==========

def load_or_create_key():
    """Loads vault key if it exists, otherwise creates one."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print("New encryption key created.")
        return key

    with open(KEY_FILE, "rb") as f:
        return f.read()


# ========== VAULT LOAD / SAVE ==========

def load_vault(fernet):
    """Decrypt and load stored vault entries."""
    if not os.path.exists(VAULT_FILE):
        return []

    with open(VAULT_FILE, "rb") as f:
        encrypted_data = f.read()

    if not encrypted_data:
        return []

    try:
        decrypted = fernet.decrypt(encrypted_data)
        return json.loads(decrypted.decode())
    except:
        print("Vault corrupt or unreadable. Starting empty.")
        return []


def save_vault(fernet, entries):
    """Encrypt and save vault entries."""
    data = json.dumps(entries, indent=2).encode()
    encrypted = fernet.encrypt(data)

    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)

    print("Vault saved.")


# ========== MENU ACTIONS ==========

def add_entry(entries):
    print("\n--- Add Entry ---")
    name = input("Account/Service Name: ").strip()
    username = input("Username: ").strip()
    password = getpass("Password: ")

    if name and username and password:
        entries.append({"name": name, "username": username, "password": password})
        print("Entry added!")
    else:
        print("All fields required.")


def list_entries(entries):
    print("\n--- Stored Entries ---")
    if not entries:
        print("No entries.")
        return

    for i, entry in enumerate(entries, 1):
        print(f"{i}. {entry['name']} - {entry['username']}")


def search_entries(entries):
    term = input("Search term: ").strip().lower()
    results = [e for e in entries if term in e["name"].lower()]

    if not results:
        print("No matches found.")
        return

    print("\n--- Search Results ---")
    for entry in results:
        print(f"{entry['name']} — {entry['username']} (Password: {entry['password']})")


def delete_entry(entries):
    list_entries(entries)
    if not entries:
        return

    try:
        index = int(input("Entry number to delete: ")) - 1
        if 0 <= index < len(entries):
            removed = entries.pop(index)
            print(f"Deleted {removed['name']}.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


# ========== MAIN VAULT LOOP ==========

def vault_main():
    key = load_or_create_key()
    fernet = Fernet(key)

    entries = load_vault(fernet)

    while True:
        print("\n=== Vault Menu ===")
        print("1) Add Entry")
        print("2) List Entries")
        print("3) Search Entries")
        print("4) Delete Entry")
        print("5) Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_entry(entries)
            save_vault(fernet, entries)
        elif choice == "2":
            list_entries(entries)
        elif choice == "3":
            search_entries(entries)
        elif choice == "4":
            delete_entry(entries)
            save_vault(fernet, entries)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid input.")
