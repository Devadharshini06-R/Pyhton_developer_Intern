def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def is_winner(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True 
    return False
def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)
def tic_tac_toe():
    print("WELCOME TO TIC TAC TOE")
    print("ABC IS X AND DEF IS O")
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        while True:
            print_board(board)
            print(f"{current_player}'s turn.")
            try:
                row,col =  map(int, input("ENTER ROW AND COLUMN (0-2 SEPERATED BY A SPACE):").split())
                if row < 0 or row > 2 or col < 0 or col > 2:
                    raise ValueError
                if board[row][col] != " ":
                    print("THAT SPOT IS ALREADY TAKEN. TRY AGAIN.")
                    continue
                board[row][col] = current_player
            except ValueError:
                print("INVALID INPUT. PLEASE ENTER TOW NUMBER BETWEEN 0 AND 2.") 
                continue
            if is_winner(board,current_player):
                print_board(board)
                print(f"PLAYER {current_player} WINS!")
                break
            if is_full(board):
                print_board(board)
                print("IT'S A DRAW")
                break
            current_player = "O" if current_player == "X" else "X"
        play_again =input ("DO YOU WANT TO PLAY AGAIN? (yes/no):").lower()
        if play_again != "yes":
            print("THNAKS FOR PLAYING!")
            break
if __name__ == "__main__":
    tic_tac_toe()
