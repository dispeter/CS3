grid = []
step = 0
game = True
for y in range(0,3):
    for x in range(0,3):
        grid.append("0")
print(grid)
while game==True:
    choice=int(input("what gird number do you want"))
    list_used = choice-1
    grid[list_used]= 1
    # if step>6:
    if grid[0] and grid[1] and grid[2] == 1:
        print("win")
        game=False
    elif grid[3] and grid[4] and grid[5]==1:
        print("win")
        game=False
    elif grid[6] and grid[7] and grid[8]==1:
        print("win")
        game=False
    elif grid[0] and grid[3] and grid[6] ==1:
        print("win")
        game=False
    elif grid[1] and grid[4] and grid[7] ==1:
        print("win")
        game=False
    elif grid[2] and grid[5] and grid[8] ==1:
        print("win")
        game=False
    elif grid[0] and grid[4] and grid[8]==1:
        print("win")
        game=False
    elif grid[2] and grid[4] and grid[6]==1:
        print("win")
        game=False
    # else:
    #     print("tie")
        game=False
    step+=1
    print(grid)
    priut(step)
    print("---------------")