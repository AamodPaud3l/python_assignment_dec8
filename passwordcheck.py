#Program to define a global static password value and a function to check if the passwords match
def passcheck(passw):
    if (passw == passw1):
        print("Password Match")
    else:
        print("Password doesn't match")
passw1 = "admin"
password = str(input("Enter your password: "))
passcheck(password)