import pprint
from random import randint
theBoard = {
   'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
   'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
   'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}

def printBoard(board):
    print(f"""
    {board['top-L']}|{board['top-M']}|{board['top-R']}
    -+-+-
    {board['mid-L']}|{board['mid-M']}|{board['mid-R']}
    -+-+-
    {board['low-L']}|{board['low-M']}|{board['low-R']}
    """) 

choiceBoard = {
    '1': 'low-L',
    '2': 'low-M',
    '3': 'low-R',
    '4': 'mid-L',
    '5': 'mid-M',
    '6': 'mid-R',
    '7': 'top-L',
    '8': 'top-M',
    '9': 'top-R', }

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    if turn == 'X':
        move = input(f"Ruch gracza {turn}. W Którym kierunku stawiasz znak?")
        theBoard[move] = turn
        turn = 'O'
    else:
        ran = str(randint(1,9))
        move = choiceBoard[ran]
        theBoard[move] = turn
        turn = 'X'

printBoard(theBoard)