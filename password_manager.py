import os  # Provides functions for interacting with the operating system
import getpass  # Provides a way to securely get user input for passwords
from cryptography.fernet import Fernet  # Imports Fernet for encryption and decryption

KEY_FILE = "key.key"  # File name where the encryption key will be stored
PASSWORDS_FILE = "passwords_encrypted.txt"  # File name where encrypted passwords will be saved

def load_key():
    # Checks if the key file exists
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()  # Generates a new encryption key
        with open(KEY_FILE, "wb") as key_file:  # Opens the key file in write-binary mode
            key_file.write(key)  # Writes the key to the file
    else:
        with open(KEY_FILE, "rb") as key_file:  # Opens the key file in read-binary mode
            key = key_file.read()  # Reads the key from the file
    return key  # Returns the encryption key

def add_password(site, username, password, fernet):
    entry = f"{site},{username},{password}\n".encode()  # Combines site, username, and password, then encodes to bytes
    encrypted = fernet.encrypt(entry)  # Encrypts the entry using Fernet
    with open(PASSWORDS_FILE, "ab") as f:  # Opens the password file in append-binary mode
        f.write(encrypted + b"\n")  # Writes the encrypted entry to the file, followed by a newline

def get_password(site, fernet):
    # Checks if the password file exists
    if not os.path.exists(PASSWORDS_FILE):
        print("No passwords stored yet.")  # Prints message if file doesn't exist
        return
    with open(PASSWORDS_/. FILE, "rb") as f:  # Opens the password file in read-binary mode
        for line in f:  # Iterates through each line in the file
            try:
                decrypted = fernet.decrypt(line.strip()).decode()  # Decrypts the line and decodes it to a string
                s, u, p = decrypted.split(",", 2)  # Splits the decrypted line into site, userna/. /. me, and password
                if s == site:  # Checks if the site matches the requested site
                    return u, p  # Returns the username and password
            except Exception:
                continue  # If decryption fails, continues to the next line
    return None  # Returns None if no matching site is found

def main():
    key = load_key()  # Loads or generates the encryption key
    fernet = Fernet(key)  # Creates a Fernet object for encryption/decryption

    while True:  # Infinite loop for user menu
        print("Options: (1) Add password (2) Get password (3) Exit")  # Prints menu options
        choice = input("Choose option: ")  # Gets user's menu choice
        if choice == "1":
            site = input("Site: ")  # Gets the site name from the user
            username = input("Username: ")  # Gets the username from the user
            password = getpass.getpass("Password: ")  # Securely gets the password from the user
            add_password(site, username, password, fernet)  # Saves the encrypted password
            print("Password added and encrypted.")  # Confirms success
        elif choice == "2":
            site = input("Site to retrieve: ")  # Gets the site name to retrieve password for
            result = get_password(site, fernet)  # Retrieves the username and password for the site
            if result:
                print(f"Username: {result[0]}, Password: {result[1]}")  # Prints the retrieved credentials
            else:
                print("No password found for that site.")  # Informs if no password was found
        elif choice == "3":
            break  # Exits the loop and ends the program

if __name__ == "__main__":
    main()  # Runs the main function if the script is executed directly
