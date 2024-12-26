import re

# Function to analyze one password
def analyze_password_strength(password):
    # Step 1: Check the length of the password
    if len(password) < 8:
        return "Weak", "Password is too short. Use at least 8 characters."


    has_upper = re.search(r'[A-Z]', password)  # Uppercase letters
    has_lower = re.search(r'[a-z]', password)  # Lowercase letters
    has_digit = re.search(r'\d', password)     # Digits
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  # Special characters


    diversity = sum([bool(has_upper), bool(has_lower), bool(has_digit), bool(has_special)])


    if diversity == 4:
        return "Strong", "Password is long and diverse."
    elif diversity == 3:
        return "Moderate", "Password is fairly diverse."
    else:
        return "Weak", "Password lacks diversity in characters."


password = input("Enter a password to analyze: ")
strength, message = analyze_password_strength(password)
print(f"Strength: {strength}\nReason: {message}")


