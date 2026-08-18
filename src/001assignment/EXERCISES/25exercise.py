password = input("Enter a password to validate: ")


length_ok = len(password) >= 8


has_num = any(char.isdigit() for char in password)


has_special = any(not char.isalnum() for char in password)

if length_ok and has_num and has_special:
    print("Strong password!")
else:
    print("Weak password. Ensure it has 8+ characters, a number, and a special character.")
