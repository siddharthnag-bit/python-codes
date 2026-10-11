# Write a program which finds out whether a given name is present in a list or not.

name_list=["rohan","ayush","siddharth","shruti"]

name=input("Enter your name:")

if(name in name_list):
    print("your name is in the list")
else:
    print("your name is not in the list")