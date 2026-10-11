# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams

comment=input("Enter your comment:")

if("make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment):
    print("This comment is fake")
else:
    print("This comment is good")