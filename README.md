#Encrypted Password Manager (with Strength Checker)

A beginner-friendly Python project that securely stores and retrieves website passwords using encryption, with a built-in password strength checker.

# Features

- ✅ Encrypts passwords using **Fernet** (from the `cryptography` library)
- ✅ Stores credentials locally in an encrypted file
- ✅ Checks password strength based on:
  - Length (min. 8 characters)
  - Uppercase and lowercase letters
  - Numbers
  - Special characters
- ✅ Simple command-line interface
- ✅ Secure password input using `getpass`
 
# Requirements

- Python 3.6+
- `cryptography` library

Install dependencies:
```bash
pip install cryptography

 How to Use
Clone the repo:
git clone https://github.com/yourusername/password-manager.git
cd password-manager
Run the script:
python password_manager.py
Choose an option from the menu:
(1) Add password
(2) Get password
(3) Exit

#What I Learned
Basics of encryption with symmetric keys

Password validation logic in Python

Managing secure input and file I/O

How to build simple but useful security tools

#Notes
All passwords are encrypted and stored locally.

Make sure to keep your encrypted_key file safe.

For now, this is a local-only tool and does not sync or share data.

 Future Improvements
Add a password generator

GUI interface (e.g., Tkinter)

Delete and update entries

Multi-user support

 Disclaimer
This tool is built for educational purposes and local use only. Do not use it to store real, sensitive data in production environments.

👩🏽‍💻 Author
Victoria Ogbeide

