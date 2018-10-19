length = 9
for x in range(0,length):
   for y in range (0,length):
       if x==0 or x==length-1:
           print("*",end="")
       elif y==0 or y==length-1:
           print("*",end="")
       elif x==y:
            print("*", end="") 
       elif x==(y*-1)+length-1:
            print("*", end="") 
       else:
           print(" ",end="")
   print()
