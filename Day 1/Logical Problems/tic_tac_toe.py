from random import randint
def print_board(board):
    c=0
    for row in board:
        print(" | ".join(row))
        if c<2:
            print("-"*9)
        c+=1
    
def check_winner(board):
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]!=' '):
            return board[i][0]
        if(board[0][i]==board[1][i]==board[2][i]!=' '):
            return board[0][i]
    
    if(board[0][0]==board[1][1]==board[2][2]!=' '):
        return board[0][0]
    if(board[2][0] == board[1][1] == board[0][2]!=" "):
        return board[0][2]

    return None

def is_draw(board):
    return all(cell!=" " for row in board for cell in row)

def computer_move(board):
    while True:
        row = randint(0,2)
        col = randint(0,2)
        if(board[row][col]==" "):
            board[row][col] = "O"
            print (f"Computer chose: ({row},{col})")
            break
        
def tic_tac_toe():
    board=[[" " for _ in range(3)] for _ in range(3)]
    print("Starting a game of Tic-Tac-Toe where you are : \"X\"  and the computer is \"O\".")
    print_board(board)
    
    while True:
        while True:
            try: 
                row = int(input("Enter a row in the range 0-2: "))
                col = int(input("Enter a col in the range 0-2: "))
                if 0<=row<3 and 0<=col<3 and board[row][col]==" ":
                    board[row][col] = "X"
                    break
                else:
                    print("Position Already filled, Try again")
            except(ValueError, IndexError):
                print("Enter Valid Row and col")
        print_board(board)
        
        winner = check_winner(board)
        if winner: 
            print(f"Player {winner} wins!!!")
            break
        if is_draw(board):
            print("Its a Draw!")
            break
        
        computer_move(board)
        print_board(board)
        
        winner= check_winner(board)
        if winner:
            print(f"Player {winner} wins!!")
            
        if is_draw(board):
            print("Its a draw.")    
            break
        
tic_tac_toe()