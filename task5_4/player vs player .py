from operator import or_
import os
import random

from sys import flags


def clear(): return os.system('clear')


clear()
print("Игра в конфеты (правила)\n")
print("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.")
print("Первый ход определяется жеребьёвкой. ")
print("За один ход можно забрать не более чем 28 конфет. ")
print("Все конфеты оппонента достаются сделавшему последний ход. ")
print("Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?\n")
start = input("Нажминие Enter для продолжения\n")
# Цикл ввода имени первого игрока
clear()
candies = input("Введите количество конфет с которым будете играть?\n\nНажминие Enter если не хотите вводить количеcтво\n")
if not candies:
    candies = 2021
else:
    candies = int(candies)
print(candies)
flags = True
clear()
while flags:
    name_player1 = input("Введите имя первого игрока: \n")
    clear()
    if not name_player1:
        print("Имя игрока не введено, прошу ввести имя первого игрока")
    else:
        flags = False
# Цикл ввода имени второго игрока
flags = True
clear()
while flags:
    name_player2 = input("Введите имя вторго игрока: \n")
    clear()
    if not name_player2:
        print("Имя игрока не введено, прошу ввести имя второго ")
    else:
        flags = False
clear()
# На данном моменте уже введы имена игроков.
flags_winners = True
flags = True
move = 0
quantity_candies_player1 = 0
quantity_candies_player2 = 0
while candies > 0:
    clear()
    move += 1
    flags = True
    while flags:
        part = 1
        print(f"Раунд {move} /({part})\n")
        print(f"Конфет у игрока {name_player1}, всего {quantity_candies_player1}")
        print(f"Конфет у игрока {name_player2}, всего {quantity_candies_player2}\n")
        print(f"Осталось конфет {candies}")
        try: 
            player1_candies = int(input(f"Игрок {name_player1} введите сколько хотите взять конфет от 1 до 28 \n"))
            clear() 
            if 1 <= player1_candies <= 28 and player1_candies <= candies:
                candies -= player1_candies
                quantity_candies_player1 += player1_candies
                flags = False
            else:
                print("Ошибка, введено некорректное количество конфет или ввели не число")         
        except ValueError:
                print("Ошибка, введено некорректное количество конфет или ввели не число")         
    flags = True
    if candies == 0:
        flags = False
    while flags:
        part = 2
        print(f"Раунд {move} /({part})\n")
        print(f"Конфет у игрока {name_player1}, всего {quantity_candies_player1}")
        print(f"Конфет у игрока {name_player2}, всего {quantity_candies_player2}\n")
        print(f"Осталось конфет {candies}")
        try: 
            player2_candies = int(input(f"Игрок {name_player2} введите сколько хотите взять конфет от 1 до 28 \n"))
            clear() 
            if 1 <= player2_candies <= 28 and player2_candies <= candies:
                candies -= player2_candies
                quantity_candies_player2 += player2_candies
                flags = False
            else:
                print("Ошибка, введено некорректное количество конфет или ввели не число")         
        except ValueError:
                print("Ошибка, введено некорректное количество конфет или ввели не число")             
        if candies == 0:
            flags_winners = False
clear()
if flags_winners == True:
    print(f"Выиграл игрок {name_player1}\n")
    print(f"Все конфеты переходят игроку {name_player1}")
    print(
        f"Конфеты всего конфеты игрока {name_player1}, всего  {player1_candies}")
else:
    print(f"Выиграл игрок {name_player2}")
    print(f"Все конфеты переходят игроку {name_player2}")
    print(
        f"Конфеты всего конфеты игрока {name_player2}, всего  {player2_candies}")

print(f"Сыгранно раундов за игру {move}\n")
