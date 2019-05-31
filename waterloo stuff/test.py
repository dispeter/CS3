num = 2
for i in range(0,num+1):
    hand1 = i
    hand2 = num-i
    if hand1 <= 5:
        if hand2 <= 5:
            if hand1 >= hand2:
                print(hand1,hand2)cc