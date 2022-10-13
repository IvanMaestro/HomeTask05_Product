# 3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

def draw_board(b):
    print("-" * 13)
    for i in range(3):
        print("|", b[0 + i * 3], "|", b[1 + i * 3], "|", b[2 + i * 3])
        print("-" * 13)


def take_move(player_symbol):  # ход игрока с проверками
    valid = False
    while not valid:
        player_step = input("Куда поставим " + player_symbol + "? ")
        try:
            player_step = int(player_step)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число? ")
            continue
        if player_step >= 1 and player_step <= 9:
            if (str(board[player_step - 1]) not in "XO"):
                board[player_step - 1] = player_symbol
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9")


def chek_win(b):
    win_lines = [[0,1,2],
                 [3,4,5],
                 [6,7,8],
                 [0,3,6],
                 [1,4,7],
                 [2,5,8],
                 [0,4,8],
                 [2,4,6]]
    win = ""
    for i in win_lines:
        if b[i[0]] == "X" and b[i[1]] == "X" and b[i[2]] == "X":
            win = "X"
        if b[i[0]] == "O" and b[i[1]] == "O" and b[i[2]] == "O":
            win = "O"
    return win


def main_game(b):
    counter = 0
    winner = False
    while not winner:
        draw_board(b)
        if counter % 2 == 0:
            take_move("X")
        else:
            take_move("O")
        counter += 1
        if counter > 4:
            tmp = chek_win(b)
            if tmp:
                print("\n" + tmp, "выиграл!")
                winner = True
                break
            if counter == 9:
                print(f'Ничья!')
                break
    draw_board(b)


print("\nИгра Крестики-нолики для двух игроков ")
board = [1,2,3,
         4,5,6,
         7,8,9]

main_game(board)
input("Нажмите Enter для выхода!")

#============================================================

# board = list(map(str, range(1, 10)))
#
# def draw_board():
#     print('-' * 20)
#     for i in range(3):
#         for k in range(3):
#             print(f'{board[k + i * 3]:^5}', end=' ')
#         print(f'\n{"-" * 20}')
#     print()
#
#
# def seleckt_position(symbol):
#     global board
#     while True:
#         answer = input(f'Введите номер ячейки от 1 до 9.\nВыберите позицию {symbol}: ')
#         if answer.isdigit() and int(answer) in range(1, 10):
#             answer = int(answer)
#             pos = board[answer - 1]
#             if pos not in (chr(10060), chr(11093)):
#                 board[answer -1] = chr(10060) if symbol == "X" else chr(11093)
#                 break
#         else:
#             print(f'Эта ячейка занята{chr(9995)}{chr(129292)}')
#     else:
#         print(f'Неверный ввод{chr(9940)}. Введите корректное число!')
#
#
# def check_win():
#     win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
#     return n[0] if n else n
#
#
# def main():
#     counter = 0
#     draw_board()
#     while True:
#         seleckt_position('0') if counter % 2 else seleckt_position('X')
#         draw_board()
#
#
#         if counter > 3:
#             if check_win():
#                 print(f'{check_win()} - "выиграл!"{chr(127942)}{chr(127881)}!')
#                 break
#         if counter == 8:
#             print(f'Ничья {chr(129318)}{chr(129309)}')
#             break
#         counter += 1
#
# main()