password = input("Enter your password: ")

# Check if the password is empty
if password == "":
    print("Error: Password cannot be empty.")
    exit()

# Check for common passwords
common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "admin"
]

is_common = password.lower() in common_passwords

if is_common:
    print("Warning: This is a common password.")

# Password length
length = len(password)
print("Password length:", length)

# Check uppercase letters
has_uppercase = any(char.isupper() for char in password)
print("Contains uppercase:", has_uppercase)

# Check lowercase letters
has_lowercase = any(char.islower() for char in password)
print("Contains lowercase:", has_lowercase)

# Check numbers
has_digit = any(char.isdigit() for char in password)
print("Contains number:", has_digit)

# Check special characters
special_characters = "!@#$%^&*"
has_special = any(char in special_characters for char in password)
print("Contains special character:", has_special)

# Calculate score
score = 0

if length >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

# A common password cannot be considered strong
if is_common:
    strength = "Weak"
elif score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Score:", score)
print("Password Strength:", strength)

# Suggestions
print("Suggestions:")

if length < 8:
    print("- Use at least 8 characters.")

if not has_uppercase:
    print("- Add an uppercase letter.")

if not has_lowercase:
    print("- Add a lowercase letter.")

if not has_digit:
    print("- Add a number.")

if not has_special:
    print("- Add a special character.")

if is_common:
    print("- Avoid common passwords.")
