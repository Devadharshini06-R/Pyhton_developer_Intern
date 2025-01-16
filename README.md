# Pyhton_developer_Intern


## Task 2 Tic Tac Toe Game

### python - VS Code
---

## Overview
This is a simple interactive Tic-Tac-Toe game where two players take turns to play. The game continues until there is a winner or a draw. Players are prompted to input their moves (row and column), and the board is displayed after each turn. The game also asks if the user wants to play again after the game ends.

## Features
- Player "X" uses the alphabet "ABC" and player "O" uses "DEF" for their moves.
- Players alternate turns and input row and column (0-2).
- The game checks for a winner after each move, and ends when a player wins or the board is full (draw).
- Players are prompted to play again after each game.

## Functions
### `print_board(board)`
- Purpose: Prints the current state of the Tic-Tac-Toe board.
- Displays the board as a grid with row and column numbers, and the positions occupied by players.

### `is_winner(board, player)`
- Purpose: Checks if the specified player has won the game.
- Logic: 
  - Checks if all cells in any row or column are occupied by the player's symbol.
  - Checks both diagonals for a win.
  - Returns `True` if the player has won, otherwise `False`.

### `is_full(board)`
- Purpose: Checks if the Tic-Tac-Toe board is completely filled.
- Logic: Returns `True` if there are no empty cells left on the board, otherwise `False`.

### `tic_tac_toe()`
- Purpose: Manages the game flow.
- Components:
  - Initializes the game and the board.
  - Alternates between the two players, asking for row and column input.
  - Checks for invalid input (out of range or already taken spots).
  - Calls `is_winner()` and `is_full()` to check if the game is over.
  - Displays the final outcome (win/draw).
  - Prompts the player to play again after each game.

## Usage
1. Run the program.
2. The game will print the board and prompt the current player for their move.
3. Players will input the row and column where they want to place their symbol (X or O).
4. The game checks after each move whether there is a winner or if the game is a draw.
5. After the game ends, players will be asked if they want to play again.

### Example Game Flow:
```
WELCOME TO TIC TAC TOE
ABC IS X AND DEF IS O

 | | 
-----
 | | 
-----
 | | 
X's turn.
ENTER ROW AND COLUMN (0-2 SEPERATED BY A SPACE): 1 1
 | | 
-----
 |X| 
-----
 | | 
O's turn.
ENTER ROW AND COLUMN (0-2 SEPERATED BY A SPACE): 0 0
 | | 
-----
X|X| 
-----
 | | 
PLAYER X WINS!
DO YOU WANT TO PLAY AGAIN? (yes/no): no
THNAKS FOR PLAYING!
```

## Notes
- Ensure you enter valid row and column numbers (0, 1, or 2). If an invalid choice is made (such as a number outside the range or a spot already taken), the program will prompt you to try again.
- The game checks for a winner or a draw after each turn.
- After the game ends, players can choose to play again.

## License
This project is open-source and available for personal use and learning purposes.
