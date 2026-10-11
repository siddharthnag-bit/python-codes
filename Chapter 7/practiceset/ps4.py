#  Write a program to find the sum of first n natural numbers using while loop.

num=int(input("Enter the number:"))

# i=1
# sum=0
# while(i<=num):
    # sum=sum+i
    
    # i = i + 1

# print(sum)

sum=0
for i in range(1,num+1):
    # if(i <= num):
        sum=sum+i
print("Sum is :",sum)