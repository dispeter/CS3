
def foo(count):
	if count < 0:
		return
	print(count)
	foo(count - 1)
	print(count)	
#####################################
from random import randint

def bar(num, count):
	if num < 10:
		return count
	for i in range(5):
		bar(randint(0, 20), count + 1)
		
# print(bar(11, 0))

#####################################

def test(num):
	if num <= 0:
		return 0
	return num + test(num - 1)	

# print(test(10))

#######################################


def move(lst, count):
	if count == 0:
		return lst
	for i in range(len(lst)):
		if lst[i] == 0:
			lst[i] = 1
			return move(lst, count - 1)
	return lst

lst = [0, 0, 0, 0, 0]
# print(move(lst, 3))

##########################################
list2 = [[0,0,0], [0,0,0], [0,0,0]]
def grid(list2,count):
    if count ==0: 
        return list2
    for i in range(len(list2)):
        for z in range(len(list2)):
            if list2[i][z] == 0:
                list2[i][z]=1
                return grid(list2, count-1)
    return list2

print(grid(list2,5))