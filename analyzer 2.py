#list of common passwords
COMMON_PASSWORDS = ["123456", "password", "123456789", "qwerty", "abc123", "111111", "iloveyou"]

def analyze_password_strength(password):
    # Step 1: Check if the password is common
    if password in COMMON_PASSWORDS:
        return "Weak", "Password is commonly used and easy to guess."

    #length of the password
    if len(password) < 8:
        return "Weak", "Password is too short. Use at least 8 characters."

    #diversity of characters
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

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