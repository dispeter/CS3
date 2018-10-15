string1 = "aeiou"
string2 = "qwerty"

if type(string1) == int:
	print("is int")
else:
	print("no no no")


#Hard
	a="a"
	A="A"
	e="e"
	E="E"
	i="i"
	I="I"
	o="o"
	O="O"
	u="u"
	U="U"
	acount=0
	ecount=0
	icount=0
	ocount=0
	ucount=0

	if A or a in word1:
		acount+=1
	if e or E in word1:
		ecount+=1
	if i or I in word1:
		icount+=1
	if o or O in word1:
		ocount+=1
	if u or U in word1:
		ucount+=1
if acount==1 and ecount==1 and icount==1 and ocount==1 and ucount==1:
	print("contain all vowels")
elif acount==0 and ecount==0 and icount==0 and ocount==0 and ucount==0:
	print("no vowels")
else:
	print("some vowels")
a = 0
b = 10
print("Yes") if a< b else print("No")

from math import sqrt
c = 0
if sqrt(c)<5 or sqrt(c)>10:
	print("qwerty")
elif sqrt(c) ==10:
	print("equal to 10 ")
	

	
