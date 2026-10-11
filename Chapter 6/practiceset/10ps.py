# Username aur password input lo.
# Agar username "admin" and password "1234" hai → Login successful, otherwise failed.


username=input("enter your username:")
password=input("enter your password:")

if(("admin" in username) and ("1234" in password)):
    print("logged in")
else:
    print("no match")