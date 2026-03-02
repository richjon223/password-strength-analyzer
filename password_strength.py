password = input("Enter your password: ")

score = 0
suggestions = []

# Check length
if len(password) >= 8:
    print("✓ Password length is good")
    score += 1
else:
    print("✗ Password is too short (minimum 8 characters)")
    suggestions.append("Use at least 8 characters")

# Check lowercase
if any(char.islower() for char in password):
    print("✓ Contains lowercase letter")
    score += 1
else:
    print("✗ Missing lowercase letter")
    suggestions.append("Add lowercase letters")

# Check uppercase
if any(char.isupper() for char in password):
    print("✓ Contains uppercase letter")
    score += 1
else:
    print("✗ Missing uppercase letter")
    suggestions.append("Add uppercase letters")

# Check numbers
if any(char.isdigit() for char in password):
    print("✓ Contains number")
    score += 1
else:
    print("✗ Missing number")
    suggestions.append("Add numbers")

# Check special characters
special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(char in special_characters for char in password):
    print("✓ Contains special character")
    score += 1
else:
    print("✗ Missing special character")
    suggestions.append("Add special characters like !@#$")

print("\nPassword Score:", score, "/5")

# Determine strength
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength:", strength)

# Show suggestions
if suggestions:
    print("\nSuggestions to improve your password:")
    for s in suggestions:
        print("-", s)
else:
    print("\nYour password is very strong.")

