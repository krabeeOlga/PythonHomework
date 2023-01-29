# Создайте программу для игры в 'Крестики-нолики'
from random import randint as RI

def print_board(board):
    for i in range(len(board)):
        print(f" {board[i]} ", end='')
        if (i+1) % 3 == 0:
            print()

def get_board():
    board = []
    available_moves = []
    for i in range(1, 10):
        board.append(i)
        available_moves.append(i)
    return board, available_moves

def first_move():
    my_players = ['O', 'X']
    my_sort = RI(0, 1)
    print(f"Первым ходит игрок {my_players[my_sort]}!")
    return my_players[my_sort]

def next_move(player):
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    return player

def is_win(board, variant, player):
    for v in variant:
        if board[v[0]] == player and board[v[1]] == player and board[v[2]] == player:
            return True
    return False

def win_check(board, player):
    horizontal_index_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    vertical_index_win = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    diagonal_index_win = [[0, 4, 8], [2, 4, 6]]
    win_variants = [horizontal_index_win, vertical_index_win, diagonal_index_win]

    for variant in win_variants:
        if is_win(board, variant, player):
            return True
    return False

def play_game():
    board, available_moves = get_board()
    player = first_move()

    while True:
        print_board(board)
        print()
        try:
            num = int(input(f"Игрок {player}, введите № клетки, куда будете ходить: "))
        except:
            num = -1
        board_index = num -1

        if board_index < 0 or board_index >= 9:
            print("Так нельзя ходить!")
            continue
        if board[board_index] == 'O' or board[board_index] == 'X':
            print("Эта клетка уже занята!")
            continue

        board[board_index] = player
        available_moves.remove(num)

        if win_check(board, player):
            print_board(board)
            print(f"Игрок {player} победил!")
            break

        if not available_moves:
            print_board(board)
            print("Ничья!")
            break

        player = next_move(player)

play_game()


   


