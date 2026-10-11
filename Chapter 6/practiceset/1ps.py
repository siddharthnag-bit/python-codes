# Write a program to find the greatest of four numbers entered by the user


num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
num3=int(input("Enter your third number:"))
num4=int(input("Enter your fourth number:"))


if(num1>num2 and num1>num3 and num1>num4):
    print(num1)
elif(num2>num3 and num2>num4):
    print(num2)
elif(num3>num4):
    print(num3)
else:
    print(num4)

