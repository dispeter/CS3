total = 0 
num = 28
for i in range(1,num-1):
    if num % i == 0:
        total=total+i
        if total==num:
            print("Perfectnumber")