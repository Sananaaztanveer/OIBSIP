import secrets

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!&*"

try:
    length = int(input("Enter password length: "))

    if length < 8:
        print("Password length must be at least 8 characters!")
    else:
        password = ""

        for i in range(length):
            password += secrets.choice(characters)

        print("Your generated password is:", password)

except ValueError:
    print("Invalid input! Please enter numbers only.")