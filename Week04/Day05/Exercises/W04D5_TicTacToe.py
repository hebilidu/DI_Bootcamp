# Week04 Day05 - Mini-Project # 1 : Tic Tac Toe
# Created on  : 210429 by : lidu
# Modified on : 210430 by : lidu
''' Tic Tac Toe game '''
# board. 0: empty / 1: X(player 1) / 2: O(palyer 2)
board_init = [
    [' ', '|', ' ', '|', ' '],
    ['-', '.', '-', '.', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '.', '-', '.', '-'],
    [' ', '|', ' ', '|', ' '],
]
corresp = [' ', 'X', 'O']
offsets = {'1': 0, '2': 2, '3':4}

def display_board(board):
    '''Displays the Tic Tac Toe board (GUI)'''
    print('\n')
    print('TIC TAC TOE')
    for row in board:
        print(''.join(row))
    print('\n')

def player_input(player, board):
    '''Gets a new position from the player'''
    print("Player {}'s turn ({})...\n".format(player, corresp[player]))
    while True:
        row = input("Enter row    (1/2/3): ")
        col = input("Enter column (1/2/3): ")
        if not(row in ['1', '2', '3'] and col in ['1', '2', '3']):
            print('Invalid input.')
            continue
        elif board[(int(row)-1)*2][(int(col)-1)*2] != ' ':
            print('Spot already occupied !')
            continue
        board[(int(row)-1)*2][(int(col)-1)*2] = corresp[player]
        break
    return board

def check_win(board):
    '''To check whether there is a winner or not.  Returns '0'(no winner)/'1'/'2' '''
    # Check rows
    for row in board:
        if row[0] != ' ' and row[0] != '-' and row[0] == row[2] and row[0] == row[4]:
            if row[0] == 'X' :
                return '1'
            else:
                return '2'
    # Check columns
    for col in range(4):
        if board[0][col] != ' ' and board[0][col] != '|' and board[0][col] == board[2][col] and board[0][col] == board[4][col]:
            if board[0][col] == 'X' :
                return '1'
            else:
                return '2'
    # Check diagonals
    if board[0][0] != ' ' and ((board[0][0] == board[2][2] and board[0][0] == board[4][4]) or (board[0][4] == board[2][2] and board[0][0] == board[4][0])):
        if board[2][2] == 'X':
            return '1'
        else:
            return '2'
    return '0'

def play():
    '''Main function'''
    board_current = board_init.copy()
    turns = 0
    player = 1
    while turns < 9:
        turns += 1
        display_board(board_current)
        board_current = player_input(player, board_current)
        winner = check_win(board_current)
        if turns == 9 and winner == '0':
            winner = 'No one'
        elif winner in ['1', '2']:
            turns = 9
            winner = 'Player ' + winner
        player = 1 * (player == 2) + 2 * (player == 1)
    display_board(board_current)
    print('GAME OVER. {} wins.\n'.format(winner))

play()
