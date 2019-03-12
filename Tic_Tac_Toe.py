Tgame=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
L1=0
L2=0
C2=0
C1=0
cnt=0

def board(game,just_play,line=0,colon=0):
    global Tgame, L1, L2, C1,C2,cnt
    cnt=+1
    try:
        if (cnt % 2==0) and (just_play==True):
            print("player 1, chose index now")
            line=input("witch line: ")
            L1=line
            colon=input("witch colun: ")
            C1=colon
            return game
            print("   0  1  2")
            if just_play:
                    game[int(L1)][int(C1)]=1
            for count, row in enumerate(game):
                print(count,row)
            print("   0  1  2")
            just_play=False
            return game,int(L1),int(C1)

        if cnt % 2!=0 and just_play:
             print("player 2, chose index now")
             line=input("witch line: ")
             L2=line
             colon=input("witch colun: ")
             C2=colon
             return game
             print("   0  1  2")
             if just_play:
                 game[int(L2)][int(C2)]=2

             for count, row in enumerate(game):
                 print(count,row)
             print("   0  1  2")
             just_play=False
             return game,int(L2),int(C2)
    excepte indexerror as er:
        print("Error: did you input line\colon  as 0,1 or 2??.",er)

play=True
while play:
    #player 1
    print(board(game=Tgame,just_play=play,line=0,colon=0))

    #player 2
    print(board(game=Tgame,just_play=play,line=0,colon=0))

    #test of indexing coosing
    if (Tgame[int(L1)][int(C1)] == Tgame[int(L2)][int(C2)]):
        play =False
        print("game over")

