# master_password_manager.py
# Handles Master Password Storage and Update

import os
from getpass import getpass

MASTER_PW_FILE = "master_password.txt"


def set_master_password():
    """Set the Master Password (only if not created)."""
    if os.path.exists(MASTER_PW_FILE):
        print("Master password already exists.")
        return

    while True:
        pw = getpass("Set Master Password: ")
        confirm = getpass("Confirm Master Password: ")

        if pw == confirm:
            with open(MASTER_PW_FILE, "w") as f:
                f.write(pw)
            print("Master password set successfully.")
            break
        else:
            print("Passwords do not match. Try again.")


def change_master_password():
    """Allows the user to update the master password."""
    if not os.path.exists(MASTER_PW_FILE):
        print("No master password found. Run set_master_password first.")
        return

    with open(MASTER_PW_FILE, "r") as f:
        current = f.read()

    old = getpass("Enter current Master Password: ")
    if old != current:
        print("Incorrect password. Cannot change password.")
        return

    while True:
        new = getpass("Enter new Master Password: ")
        confirm = getpass("Confirm new Master Password: ")
        if new == confirm:
            with open(MASTER_PW_FILE, "w") as f:
                f.write(new)
            print("Master password updated.")
            break
        else:
            print("Passwords do not match. Try again.")


def retrieve_master_password():
    """Retrieve existing master password."""
    if not os.path.exists(MASTER_PW_FILE):
        return None

    with open(MASTER_PW_FILE, "r") as f:
        return f.read()
