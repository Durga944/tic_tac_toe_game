theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' '}
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+ - +--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+ - +--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
def game():
    value = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your value," + value + ".Move to which place?")
        var = input("Enter the position of 'X' or 'O'= ")
        if theBoard[var] == ' ':
            theBoard[var] = value
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("hurray \U0001F929" +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print(" ** " +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print(" hurray \U0001F929 " +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print(" hurray \U0001F929 " +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print(" hurray \U0001F929 " +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print(" hurray \U0001F929 " +value + " won.","\U0001F929") 
                print("\nGame Over.\n")                
                
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print(" hurray \U0001F929" +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print(" hurray \U0001F929 " +value + " won.","\U0001F929")
                print("\nGame Over.\n")                
                
                break 
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        if value =='X':
            value = 'O'
        else:
            value = 'X'        
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "
        game()
# if name == "main":
game()