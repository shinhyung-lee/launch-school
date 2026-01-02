import random
import os 

def display_board(board):
    os.system('clear')
    
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)} # 1 ~ 9

def prompt(message):
    print(f'==> {message}')
    
# Bonus feature: join_or 
'''
Input:  A list, delimiter, and word 
Output: A string. 

Data Structures
- List : list comprehension
- list slicing
- string: join list back into a string 

Algorithms: 
IDEA
- if list is empty, return an empty string
- Join list into a string using delimieter from 0th index to [-2] index
- for last index, use delimiter and word and add to string
- return result
Pseudocode:
- if list == []:
    - return ''
- Initialize "return_str". Use delimiter and delimiter.join(lst) to form a string.
    - use str slicing[:-1]
- Concatenate last element to "return_str" with delimiter and word
- Return return_str
'''
def join_or(lst, delimiter=', ', word='or'):
    match len(lst):
        case 0:
            return ''
        case 1:
            return f'{lst[0]}'
        case 2:
            return f'{lst[0]} {word} {lst[1]}'
    
    leading_items = delimiter.join([str(elem) for elem in lst[:-1]])
    return f'{leading_items}{delimiter}{word} {lst[-1]}'

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_choose_square(board):
    while True: 
        valid_choices = [str(num) for num in empty_squares(board)]
        # prompt(f"Choose a square ({', '.join(valid_choices)})")
        prompt(f"Choose a square: ({join_or(valid_choices)})")
        # input trimmed to allow spaces in input
        square = input().strip()
        if square in valid_choices:
            break # break if it's a valid square
        
        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_choose_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER
    
def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won(board):
    return bool(detect_winner(board))

WINNING_SCORE = 2
def play_tic_tac_toe():
    player_score, computer_score = 0, 0
    while True:
        board = initialize_board()
        while True:
            display_board(board)
            
            player_choose_square(board)
            if someone_won(board) or board_full(board):
                break 
            
            computer_choose_square(board)
            if someone_won(board) or board_full(board):
                break 
        
        display_board(board)
        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
            winner = detect_winner(board)
            if winner == 'Player':
                # player_score, computer_score
                player_score += 1
            else:
                computer_score += 1
        else:
            prompt("It's a tie!")
        if player_score == WINNING_SCORE:
            print('Player won the game!')
        elif computer_score == WINNING_SCORE:
            print('Computer won the game!')
        prompt("Play again? (y or n)")
        answer = input().lower() 
        
        if answer[0] != 'y':
            break 
    
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
