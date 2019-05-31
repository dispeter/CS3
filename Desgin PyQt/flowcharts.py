count  = 0
num = 8 
while count!=num:
    if num == int(num):
        if num<1 or num==1:
            print("Prime numbers are integers > 1")
        else:
            count+=1
            if count > num or count== num:
                print("input number is a prime number")
            else:
                remainder = num%count
                if remainder == 0:
                    count+=1
                else:
                    print("The input number was evenly divided by count so it is not a prime")
                    print("The input number is not a prime  number")
                    break
    else:
        print("Prime numbers are integers > 1")

 
