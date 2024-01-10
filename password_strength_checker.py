# print((lambda x,y:x*y)(5,4))
# Conditions to be fulfilled are:
# Minimum 9 characters and maximum 20 characters.
# Cannot be a newline or a space
# There should not be three or more repeating characters in a row.
# The same string pattern(minimum of two character length) should not be repeating.

import re

def is_strong_password(password):
    # Check minimum and maximum length
    if 9 <= len(password) <= 20:
        # Check for newline or space
        if not re.search(r'[\n\s]', password):
            # Check for repeating characters
            if not re.search(r'(.)\1\1', password):
                # Check for repeating string pattern
                for i in range(2, len(password)//2 + 1):
                    pattern = f'(.{{{i}}})\\1'
                    if re.search(pattern, password):
                        return False, f"Repeating string pattern of length {i} not allowed"
                
                # All conditions met, password is strong
                return True, "Strong password"
            else:
                return False, "Cannot have three or more repeating characters in a row"
        else:
            return False, "Cannot be a newline or a space"
    else:
        return False, "Password length should be between 9 and 20 characters"

# Example usage:
password = input("Enter your password: ")
result, reason = is_strong_password(password)
if result:
    print("Password is strong!")
else:
    print(f"Weak password: {reason}")
