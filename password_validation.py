# password_validation.py

import re

def validate_passwords(passwords):
    """Validate passwords based on the given criteria."""
    valid_passwords = []
    for password in passwords:
        if 6 <= len(password) <= 12:
            if re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[A-Z]", password) and re.search("[$#@]", password):
                valid_passwords.append(password)
    return valid_passwords
