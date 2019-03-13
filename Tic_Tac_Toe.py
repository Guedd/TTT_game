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

def answering(just_play=True):
    global Tgame,  L2, C2
    answer=str(input("Your answer PLZ: Y/N"))
    if(answer=="Y") or (answer=="y") or (answer=="yes") or (answer=="YES"):
        print(board(game=Tgame,just_play=play,line=L2,colon=C2))
    else:
        just_play=False
    return just_play


def board(game,just_play,line=0,colon=0):
    global Tgame, L1, L2, C1,C2,cnt
    cnt=+1
    try:
        if (cnt % 2==0) and (just_play==True):
            print("player 1, chose index now")
            line=input("witch line: ")
            L1=line
            colon=input("witch colun: ")
            print("   0  1  2")
            if just_play:
                    game[int(L1)][int(C1)]=1
            for count, row in enumerate(game):
                print(count,row)
            print("   0  1  2")
            just_play=False
            return game,int(L1),int(C1)

    except IndexError as er:
        print("Error: did you input line\colon  as 0,1 or 2??.",er)

    try:
        if cnt % 2!=0 and just_play:
             print("player 2, chose index now")
             line=input("witch line: ")
             L2=line
             colon=input("witch colun: ")
             C2=colon
             if just_play:
                 print("   0  1  2")
                 game[int(L2)][int(C2)]=2
             for count, row in enumerate(game):
                 print(count,row)
             print("   0  1  2")
             return game,int(L2),int(C2)

    except IndexError as er:
        print("Error: did you input line\colon  as 0,1 or 2??.",er)
        answering(just_play=just_play)
        if just_play==True:
            return game,int(L2),int(C2)
        else:
             return 0



play=True
while play==True:
    #player 1
        print(board(game=Tgame,just_play=play,line=0,colon=0))

    #player 2
        print(board(game=Tgame,just_play=play,line=0,colon=0))

    #test of indexing coosing
        if play==True:
           if (Tgame[int(L1)][int(C1)] == Tgame[int(L2)][int(C2)]):
                print("the choix of player 2, is  the same of player 1.\n Would you like to make other choix?.")
                answering(just_play=play)
