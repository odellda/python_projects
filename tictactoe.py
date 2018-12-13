# Python script written by Daniel O'Dell, 2018

import os

# Subroutine to print board on screen using matrix variable board.
def printBoard(board):
    print("")
    print(board[0][0]," | ",board[0][1]," | ",board[0][2])
    print("--------------")
    print(board[1][0]," | ",board[1][1]," | ",board[1][2])
    print("--------------")
    print(board[2][0]," | ",board[2][1]," | ",board[2][2])
    print("")

# Subroutine to make reference board
def MakeBoardRef():
    boardRef = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    return boardRef

# Subroutine to check what the available numbers are on the playing board in the current game
def CheckAvailableNumbers(board):
    availableNums = []
    col = 0
    row = 0
    for row in board:
        for col in row:
            if str(col).isdigit():
                availableNums.append(col)
    print("available numbers: ", availableNums)
    return availableNums

# Subroutine to get user's choice of board reference number.
def AskUserForNumber():
    validNum = 0
    while validNum == 0:
        userChoice = input("Choose which square you want.\n")
        if userChoice.isnumeric():
            userChoice = int(userChoice)
            if userChoice in availableNums:
                print("This is what you chose ", userChoice)
                validNum = 1
            else:
                print(userChoice,"is not a valid number. Please enter one of the following: \n" ,availableNums)
        else:
            print(userChoice,"is not a valid number. Please enter one of the following: \n" ,availableNums)
    return userChoice

# Subroutine to add player's choice to board and check if the player's choice results in a win.
def PlayerPlay(player, winner):
    col = 0
    row = 0
    for row in boardPlay:
        for col in row:
            if col == userChoice:
                break
        if col ==userChoice:
            if turnCount%2 != 0:
                playSymbol = "X"
            else:
                playSymbol = "O"
            print("Replacing ",userChoice," with ",playSymbol)
            boardPlay[(userChoice-1)//3][(userChoice-1)%3] = playSymbol
            player.append(userChoice)
            break
# Check to see if player has winning combination
    for combo in winningCombos:
        comboNumCount = 0
        for comboNum in combo:
            if comboNum in player:
                comboNumCount +=1
        if comboNumCount == 3:
            winner = 1
            print("The winning combination!",combo)
            break
    if winner is 0:
        os.system('cls')
        print("No winner yet.")
    printBoard(boardPlay)
    return player,winner

# Define the winning combinations
winningCombos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# Set up the game - clear players and create new board
playerOne = []
playerTwo = []
boardRef = MakeBoardRef()
if "boardPlay" in locals():
    boardPlay = boardPlay
else:
    boardPlay = boardRef

print("Ready to Play!")
printBoard(boardPlay)

# Play the game!
winner = 0
turnCount = 0
# Begin while loop for each turn.
while winner == 0 or turnCount >=9:
# Determine if it's Player 1 or Player 2's turn
    turnCount += 1
# Check what numbers are available on the board
    availableNums = CheckAvailableNumbers(boardPlay)
    if turnCount%2 != 0:
        print("\nPlayer One's turn.\n")
    else:
        print("\nPlayer Two's turn.\n")

# Ask user to select square to play.
    userChoice = AskUserForNumber()

    if turnCount%2 != 0:
        tmp = PlayerPlay(playerOne,winner)
        playerOne = tmp[0]
        winner = tmp[1]
    else:
        tmp = PlayerPlay(playerTwo,winner)
        playerTwo = tmp[0]
        winner = tmp[1]

# Determine if there is a winner and end the game, or continue while loop until all moves taken
    if winner == 1:
        if turnCount%2 != 0:
            print("Player One Wins!")
            break
        else:
            print("Player Two Wins!")
            break
    if turnCount == 9:
        break

if winner == 0:
    print("Cat's game! It's a tie! No one wins, no one loses!")
