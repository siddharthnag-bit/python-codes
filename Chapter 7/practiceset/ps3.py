#  Write a program to find whether a given number is prime or not.


num=int(input("enter your number:"))

# for prime in range(2, num):
    # if(num % prime == 0): 
    #  print("Entered number is not prime")
    #  break
# else:
    # print("Entered number is  prime ")

i=2
while(i<num):
    if(num%i == 0):
        print("The number is not prime")
        break

    i = i + 1
        
else:
        print("the number is prime")