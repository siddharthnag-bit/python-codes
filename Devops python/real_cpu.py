import psutil

threshold=int(input("Entter the threshold value:"))
for i in range(5):
    if(psutil.cpu_percent(interval=1)>threshold):
        print("you are unhealthy",psutil.cpu_percent(interval=1))  
    else:
        print("you are healthy",psutil.cpu_percent(interval=1)) 
