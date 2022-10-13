# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
#     Добавьте игру против бота
#     Подумайте как наделить бота "интеллектом"


from random import shuffle

# candies = 2021
candies = 117
candies_limit = 28


def bot_init(cnds: int) -> int:
    if cnds <= candies_limit:
        result = cnds
    else:
        result = candies_limit
        cnd_step = cnds // candies_limit
        if cnds % candies_limit > 0:
            cnd_step += 1

        if cnd_step % 2 == 0:
            if cnds - candies_limit < candies_limit:
                result = cnds - (candies_limit - 1)
    return result


rest_candies = candies

players = ['Человек', 'bot' if int(
    input('Игра с ботом 1 - да, 0 - нет?')) else 'Человек_2']
shuffle(players)

active_player = players[0]
print(f'1 player - {players[0]}, 2 player - {players[1]}')

while rest_candies > 0:
    print(f'\nСейчас {rest_candies} есть, можно взять [1 .. {candies_limit}]')
    print(f'Ходит {active_player}')

    if active_player == 'bot':
        get_candies = bot_init(rest_candies)
        print(f'bot взял {get_candies} конфет')
    else:
        get_candies = int(input(f'Сколько конфет хотите, {active_player}: '))

    if get_candies not in range(1, candies_limit + 1):
        print('Неверный ход!')
    else:
        rest_candies -= get_candies
        if rest_candies > 0:
            if 'bot' in players:
                active_player = 'Человек' if active_player == 'bot' else 'bot'
            else:
                active_player = 'Человек' if active_player == 'Человек_2' else 'Человек_2'
        else:
            print(f'Выиграл {active_player}!')
