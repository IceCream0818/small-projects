status = '123456789'
i = 1

def updateBoard():

    board = f"{status[0]}|{status[1]}|{status[2]}\n{status[3]}|{status[4]}|{status[5]}\n{status[6]}|{status[7]}|{status[8]}"
    print(board)

def playerName(turn):
    
    if turn == 1:
        return "X"
    else:
        return "O"
    
def restart():
    temp2 = input("restart? Y/N ")
    if temp2.capitalize().rstrip() == "Y":
        global status
        status = "123456789"
        global i
        i = 1
        playGame()
    else:
        pass
    
def playGame():
    updateBoard()
    playerTurn = 1
    
    #check if input is valid
    global i
    global status
    while i < 10:
        temp = (input(f'{playerName(playerTurn)} Turn:'))

        if not temp.isdigit() or status[int(temp)-1] != temp:
            print('invalid')
        elif playerTurn == 1:
            temp = int(temp)
            playerTurn +=1
            status = status.replace(str(temp), 'X')
            i +=1
            updateBoard()
        else:
            temp = int(temp)
            playerTurn -=1
            status = status.replace(str(temp), 'O')
            i +=1
            updateBoard() 
    
        if status[0] == status[4] == status[8] or status[2] == status[4] == status[6]:
            print(f"{playerName(playerTurn%2 + 1)} wins")
            i = 11
        if len(set(status[0::3]))== 1 or len(set(status[1::3]))== 1 or len(set(status[2::3]))== 1 :
            print(f"{playerName(playerTurn%2 + 1)} wins")
            i = 11
        if len(set(status[0:3]))== 1 or len(set(status[3:6]))== 1 or len(set(status[6:9]))== 1 :
            print(f"{playerName(playerTurn%2 + 1)} wins")
            i = 11
        if i == 10:
            print("ties")
    restart()

playGame()
