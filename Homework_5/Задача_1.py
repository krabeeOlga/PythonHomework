# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as RI

def first_move():
    print('Проведем жеребьёвку...', end='')
    return RI(1, 2)

def next_move(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

def vs_human(all, max_count_on_move):
    player = first_move()
    print(f"Первым ходит игрок {player}")

    while True:
        try:
            num = int(input(f"Игрок {player}, сколько конфет берете? "))
        except:
            num = -1

        if 0 >= num or num > max_count_on_move:
            print(f'Так нельзя, надо брать от 1 до {max_count_on_move} конфет')
            continue

        all = all - num
        print(f'Осталось {all} конфет.')

        if max_count_on_move >= all:
            print(f'Игра окончена! Победил игрок №{next_move(player)}!')
            break

        player = next_move(player)
        print()

def is_bot(player):
    if player == 2:
        player = 'bot'
    return player

def vs_bot(all, max_count_on_move):
    player = is_bot(first_move())
    print(f"Первым ходит игрок {player}")

    while True:
        if player == 'bot':
            num = all % (max_count_on_move + 1)
            if num == 0:
                num = max_count_on_move
            print(f'бот берет {num} конфет')
        else:
            try:
                num = int(input(f"Игрок {player}, сколько конфет берете? "))
            except:
                num = -1

        if 0 >= num or num > max_count_on_move:
            print(f'Так нельзя, надо брать от 1 до {max_count_on_move} конфет')
            continue

        all = all - num
        print(f'Осталось {all} конфет.')

        if max_count_on_move >= all:
            print(f'Игра окончена! Победил игрок {is_bot(next_move(player))}!')
            break

        player = is_bot(next_move(player))
        print()

def game():
    max_count_on_move = 28
    all = int(RI(150, 200))
    print(f'Для игры выдано {all} конфет.')

    print("Выберите тип игры:")
    print("1 - игра с человеком")
    print("2 - игра с ботом")
    play_type = int(input("Ваш выбор: "))

    if play_type == 1:
        vs_human(all, max_count_on_move)
    else:
        vs_bot(all, max_count_on_move)

game()