with open ("tempinit") as f:
    l=f.readlines()
lines= []
num_of_lines = l[0].strip()#input()
for i in range(1,int(num_of_lines)+1):
    line = l[i].split(" ")#input.split(" ")
    lines.append([int(line[0]),line[1].strip()])
print(lines)
# lst = [4,9,"+",3,"-",12,"A",2,"X"]
# times = []
# symbol = []
# for i in range(0,len(lines)):
#     if i%2==1:
#         times.append(lines[i])
#     elif i%2==0:
#         symbol.append(lines[i])

# symbol.pop(0)
for i in range(0,len(lines)):
    print(lines[i][1]*lines[i][0])



