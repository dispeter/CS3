# # #Question 1 
# print(9%7)

# print(8*4-4)

# print(bool(4/4))

# print(abs(-1)*4+10)

# print(pow(4,3)%3)

# print(20-int(14.5))

# print(bool(int(2.2)*5)-10)

# print(divmod(19,4))

# print(str(10*5-18))

# print(float(15%4-int(True)))

# #Question 5
# print((4>3)and(1<2))

# print(len("Hi")<30)

# print((6<8)or(12>10))

# print(not(7>10))

# print((5>6)and(8<7))

# print(not(6<5)and(7<8))

# print(10/2==5 and "A" != "B")

# print(10/2!=5 and "A" == "B")

# #Question 6
# # a)b is not defined 
# # 	Syntax error

# # b)you cannot print a function
# # 	Syntax error
# # c)no error 
# # 	Output: HiHiByeHiBye
# # d)cannot use arithmetic equation with 2 strings 
# # 	Syntax error
# # e) Missing a bracket for the last print
# # 	Syntax error

# #Question 7
# a= 0
# b= 0
# c= 0
# x_plus = (-b+pow((pow(b,2)-4*a*c),0.5))/2*a
# x_minus = (-b-pow((pow(b,2)-4*a*c),0.5))/2*a

#Question 8
print("A", "B", "C", "X")
for A in range(0,2):
	for B in range(0,2):
		for C in range(0,2):
			AandB= A*B
			AnandC= 1-(A*C)
			X= AandB+AnandC
			if X==2:
				X=1
			print(A,B,C,X)