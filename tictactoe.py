cboardpos=[]
xoboard=[" "]*10

def main1():
    winner=''
    turn =0
    player_choice=input('Player 1 Choose X or O:')
    if player_choice.lower()=='x':
        player1="X"
        player2="O"
        print('Player 1 is X Player 2 is O')
    elif player_choice.lower()=='o':
        player1="O"
        player2="X"
        print('Player 1 is O Player 2 is X')
    else:
        print('Please restart and enter valid input')

    while winner=='' and turn<9:
        if turn%2==0:
            player=1
        else:
            player=2
        player_in(player,player1,player2)
        winner=game_over(turn,player)
        printboard()
        turn+=1
        print('\n'*2)
    else:
        printboard()
        if winner=="":
            print("Stalemate")
        else:
            print(f"Congratulations Player {winner} won")

def player_in(player,player1,player2):
    global cboardpos
    global xoboard
    if player==1:
        xoin=player1
    else:
        xoin=player2

    while True:
        if player==1:
            posadd=int(input('Player1 please choose position(1-9):'))
        elif player==2:
            posadd=int(input('Player2 please choose position(1-9):'))
        else: 
            print('player_in error 1')
        if posadd in cboardpos:
            print("Position already in use!")
            pass
        else:
            cboardpos.append(posadd)
            xoboard[posadd]=xoin
            break
    return cboardpos,xoboard


def printboard():
    print(f"{xoboard[7]} | {xoboard[8]} | {xoboard[9]}\n---------\n{xoboard[4]} | {xoboard[5]} | {xoboard[6]}\n---------\n{xoboard[1]} | {xoboard[2]} | {xoboard[3]}\n")
    pass


def game_over(turn,player):
    #win conds- (1,2,3) (4,5,6) (7,8,9) (1,4,7) (2,5,8) (3,6,9) (1,5,9) (3,5,7)
    if xoboard[1]==xoboard[2]==xoboard[3]!=" ":
        winner=str(player)
    elif xoboard[4]==xoboard[5]==xoboard[6]!=" ":
        winner=str(player)
    elif xoboard[7]==xoboard[8]==xoboard[9]!=" ":
        winner=str(player)
    elif xoboard[1]==xoboard[4]==xoboard[7]!=" ":
        winner=str(player)
    elif xoboard[2]==xoboard[5]==xoboard[8]!=" ":
        winner=str(player)
    elif xoboard[3]==xoboard[6]==xoboard[9]!=" ":
        winner=str(player)
    elif xoboard[1]==xoboard[5]==xoboard[9]!=" ":
        winner=str(player)
    elif xoboard[3]==xoboard[5]==xoboard[7]!=" ":
        winner=str(player)
    else:
        winner=""
    return winner
        
main1()
