# Write a program to find whether a given username contains less than 10 characters or not.

name=input("Enter your name:")

length=len(name)

if(length<10):
    print("The username contains less then 10 character")
else:
    print("the username contains more then 10 character")