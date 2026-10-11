# Write a program to print multiplication table of a given number using for loop.

num=int(input("Enter ypur number:"))

for i in range(11):
    multi=num*i
    print(num ,"x" ,i,"=", multi)


i=1
while(i<11):
    multi=i*num
    print(multi)
    i +=1