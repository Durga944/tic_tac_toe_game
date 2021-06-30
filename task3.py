grid = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
board_keys = []
for key in grid:
    board_keys.append(key)
def making_box(box):
    print(box['1'] +    ' | '  + box['2'] +   '  | '  + box['3'])
    print('--+ -- +--')
    print(box['4'] +    ' | '  + box['5'] +   '  | '  + box['6'])
    print('--+ -- +--')
    print(box['7'] +    ' | '  + box['8'] +   '  | '  + box['9'])
def game_opening():
    value = 'X'
    count = 0
    print("chance 1 is  X  and chance 2 is 0")
    for i in range(9+1):
        making_box(grid)
        print("It's your value," + value + ".Move to which place?")
        print("*********")
        move = input("Enter The position of your 0 or X=")
       
        if grid[move] == ' ':
            grid[move] = value
            count += 1
        else:
            print("You already used this place.\nMove to which place?")
            continue 
        if count >= 5:
            if grid['7'] == grid['8'] == grid['9'] != ' ': 
                making_box(grid)
                print("*************")
                print( " \U0001F929 " ,  value + " won the game","\U0001F929")
                print( " \nGame Over.\n            ")                
                print("*************")             
                break
            elif grid['4'] == grid['5'] == grid['6'] != ' ': 
                making_box(grid)
                print("*************")
                print("\U0001F929" ,  value + " won the game","\U0001F929")
                print("\nGame Over.\n")                
                print("*************")
                break
            elif grid['1'] == grid['2'] == grid['3'] != ' ': 
                making_box(grid)
                print("*************")
                print( "\U0001F929" ,  value + " won the game","\U0001F929") 
                print(" \nGame Over.\n")
                print("*************")
                break
            elif grid['1'] == grid['4'] == grid['7'] != ' ': 
                making_box(grid)
                print("*************")
                print("  \U0001F929" +  value + " won the game ","\U0001F929") 
                print( "   \nGame Over.\n")    
                print("*************")           
               
                break
            elif grid['2'] == grid['5'] == grid['8'] != ' ': 
                making_box(grid)
                print("*************")
                print("\U0001F929" , value + " won. ","\U0001F929")
                print( "\nGame Over.\n")   
                print("*************")            
                
                break
            elif grid['3'] == grid['6'] == grid['9'] != ' ': 
                making_box(grid)
                print("*************")
                print("\U0001F929" , value + " won. ","\U0001F929")
                print("\nGame Over.\n")                
                print("*************")
                break 
            elif grid['7'] == grid['5'] == grid['3'] != ' ': 
                making_box(grid)
                print("*************")
                print("\U0001F929" , value + " won. ","\U0001F929")
                print("\nGame Over.\n")                
                print("*************")
                break
            elif grid['1'] == grid['5'] == grid['9'] != ' ':
                making_box(grid)
                print("*************")
                print("\U0001F929" ,  value + " won. ","\U0001F929")
                print("\nGame Over.\n")                
                print("*************")
                break 
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Draw!!")
        if value =='X':
            value = 'O'
        else:
            value = 'X'        
    restart = input("Do You want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            grid[key] = " "
        game_opening()
game_opening()