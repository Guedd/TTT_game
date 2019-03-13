Tgame=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
L1=0
L2=0
C2=0
C1=0
count_One = 0
count_Two = -1

def answering(just_play=True , gamer=0):
    if gamer == 1:
        answer = str(input("Your answer Player 1: Y/N\n"))
        if(answer == "Y") or (answer == "y") or (answer == "yes") or (answer == "YES"):
            print(board(game=Tgame,player=1,just_play=play))
        else:
            exit()
    elif gamer == 2:
        answer = str(input("Your answer Player 2: Y/N\n"))
        if(answer == "Y") or (answer == "y") or (answer == "yes") or (answer == "YES"):
            print(board(game=Tgame,player=2,just_play=play))
        else:
            exit()



def board(game , player=0 , just_play=True , line=0 , colon=0):
    global Tgame, L1, L2, C1,C2 , count_One , count_Two
    count_One += 1
    count_Two += 1

    #the trn of player 1 for making his choix
    if player == 1 and just_play and ((count_One < 6) and (count_One > 0)):
        try:
            print("player 1, chose index now:")
            line=input("witch line: ")
            L1=line
            colon=input("witch colun: ")
            C1=colon
            if just_play:
                  game[int(L1)][int(C1)]=1
                  print("   0  1  2")
                  for count, row in enumerate(game):
                      print(count,row)
                  print("   0  1  2\n")
            just_play=False
        except IndexError as er:
            print("Error: did you input line\colon  as 0,1 or 2??.\n",er)
            answering(just_play= just_play , gamer=player)

    #the trn of player 2 for making his choix
    elif player == 2 and just_play and ((count_Two < 5) and (count_Two >= 0)):
        try:
                 print("player 2, chose index now:")
                 line=input("witch line: ")
                 L2=line
                 colon=input("witch colun: ")
                 C2=colon
                 if just_play:
                     print("   0  1  2")
                     game[int(L2)][int(C2)]=2
                     for count, row in enumerate(game):
                          print(count,row)
                     print("   0  1  2\n")
                     return game

        except IndexError as er:
            print("Error: did you input line\colon  as 0,1 or 2??.\n",er)
            answering(just_play=just_play,gamer=player)

play=True
while play:
    #player 1
        print(board(game=Tgame , player=1 , just_play=play , line=0 , colon=0))

    #player 2
        print(board(game=Tgame , player=2 , just_play=play , line=0 , colon=0))

    #test of indexing coosing
        if play:
           if (Tgame[int(L1)][int(C1)] == Tgame[int(L2)][int(C2)]):
                print("the choix of player 2, is  the same of player 1.\n Would you like to make other choix?.")
                answering(just_play=play , gamer = 2)
