#  Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]


# i=0
# while(i<len(l)):
    # if(l[i].startswith("S")):
    #   print("Good mroning",l[i])
    #   i +=1
# 
    # else:
    #    print("morning")
    #    i+=1

for i in l:
    if(i.startswith("S")):
      print("Good morning",i)
    else:
       print("morning",i)

