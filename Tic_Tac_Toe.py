Tgame=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
print("   0  1  2")
for colun,line in enumerate(Tgame):
    print(colun,line,colun)
print("   0  1  2")
play=True
while play:
    #player 1
    print("player I, chose index now")
    L1=input("witch line: ")
    C1=input("witch colun: ")
    Tgame[int(L1)][int(C1)]=1

    #player 2
    print("player II, chose index now")
    L2=input("witch line: ")
    C2=input("witch colun: ")
    Tgame[int(L2)][int(C2)]=2;
    #test of indexing coosing
    if (Tgame[int(L1)][int(C1)] == Tgame[int(L2)][int(C2)]):
        play =False
    else:
        print("   a  b  c")
        for colun,line in enumerate(Tgame):
            print(colun,line,colun)

print("   a  b  c")


