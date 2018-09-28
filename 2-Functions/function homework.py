
a = 0
b = 0
number = 0

fraction = 0
#Question 1
def division(a ,b):
	number = a//b
	fraction = a%b
	print("Answer: " + str(number) +" "+ str(fraction) + "/" + str(b))

division(100,3)
vowel = 0
counter = 0 
#Question 2
def vowel_count1(word):
	counter = 0
	vowel=["a","e","i", "o", "u","A", "E","I", "O","U"]
	word=str(word)
	for i in range(0,len(word)):
		for x in range(0,4):
				if word[i]==vowel[x]:
					counter = counter+1
	print(counter)

vowel_count1("aki")
#Question 3
def vowel_count2(word1):
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
	print(acount,ecount,icount,ocount,ucount)
	print("A" ,"E","I","O","U")

radius=2
def volume(radius):
	volume=(4/3)*3.14*pow(radius,3)
	return int(volume)

def surface(radius):
	surface = 4*3.14*radius*radius
	return int(surface)

def pretty():
	print("The volume of a sphere is" , volume(radius) , "The surface area of a sphere is ", surface(radius))

pretty()

def homo_sapiens(height, age, weight):
	print(age, weight, height)

rgb = [255,255,255]

def convert_rbg_hex(rgb):
	for p in range(len(rgb)):
		print(hex(rgb[p]), end = " ")

convert_rbg_hex(rgb)

hex1 = "a"
def convert_hex_rgb(hex):
	print(int(hex1, 16))

convert_hex_rgb(rgb)







