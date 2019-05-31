import random

totalpeople=100
people=totalpeople
entrytimestanding=3
entrytimewalking=1

ratio=30
walkup=entrytimewalking*ratio
liftup=entrytimestanding*ratio

walk=0
lift=0

time = 0
currenttime = liftup

while currenttime>1:
    if time%entrytimewalking==0 and people >0:
        people -= 1
        walk+=1

    if time%entrytimestanding==0 and people>0:
        people-=1
        lift+=1
        currenttime=liftup

    time+=1
    currenttime-=1



print(time,'seconds')
print(time-60,'seconds without 60')
print(walk,'walked',lift,'lifted')