
password = input("Enter password: ")
if len(password) >= 8 and "@" in password and "123" not in password:
        print("Strong Password")
else:
        print("Weak Password")

    