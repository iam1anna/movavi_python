
# import random
# logo = """
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |
#       `------'                           |__/
# """
# print("logo")
# cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# hand_player = [random.choice(cards)]
# hand_computer = [random.choice(cards)]
# score_player = 0
# score_computer = 0
# get_card = "y"
# while get_card == "y":
#     hand_player.append(random.choice(cards))
#
#     if sum(hand_player) > 21 and 11 in hand_player:
#         for i in range(0, len(hand_player)):
#             if hand_player[i] == 11:
#                 hand_player[i] = 1
#                 break
#     score_player = sum(hand_player)
#     print(f"Твоя рука: {hand_player}. Очков: {score_player}")
#     print(f"Первая карта диллера: {hand_computer[0]}")
#     if score_player > 21:
#         get_card = "n"
#     else:
#          get_card = input("Добираем карту? y - да, n - нет")
# while sum(hand_computer) < 17:
#     hand_computer.append(random.choice(cards))
#     if sum(hand_computer) > 21 and 11 in hand_computer:
#         for i in range(0, len(hand_computer)):
#             if hand_computer[i] == 11:
#                 hand_computer[i] = 1
#                 break
# score_computer = sum(hand_computer)
#
# print("=" * 10)
# print(f"Итоговая рука диллера: {hand_computer}. Очков: {score_computer}")
# print(f"Твоя рука: {hand_player}. Очков: {score_player}.")
# if score_player > 21 and score_computer > 21:
#     print("Перелет обоих. Ничья.")
# elif score_player > 21:
#     print("Твой перелет. Проиграл.")
# elif score_computer > 21:
#     print("Ничья")
# elif score_computer > score_computer:
#     print("Победа")
# elif score_player == score_computer:
#     print("Ничья")
# else:
#     print("Проиграл")


# import random
#
# length = 3
# life = 10
#
# answer = random.randint(100, 999)
# answer = str(answer) #число преобразуем в строчку
# answer = list(answer) #строчку преобразуем в список
#
# print(answer)
#
# is_guessed = False #отгадано?
#
# while life: #while life != 0
#     print("=" * 10)
#     # print("Жизней:", life)
#     print("Жизней:", end=" ")
#     for _ in range(0, life):
#         print("♥", end="")
#
#     guess = input("Предположение: ")
#     if len(guess) != 3 or guess.isdigit():
#     #если длина не равна 3 или это не число
#     print("Число от 100 до 999, пожалуйста!")
#         continue
#     if list(guess) == answer:
#         print("Это победа!!!")
#         is_guest = True
#         break
#         #выход из while
#
#     if not is_guessed:
#         for i in range(0,length):
#             if guess[i] == answer[i]: #совпадение позиции и значения # print("Bagels")
#                 is_guested = True
#                 break #выход из for
#     if not is_guessed:
#         for char in guess:
#             if char not in answer:
#                 print("Ошибка")
#             else:  #овпадение значения
#                 print("Fermi")
#                 break #выход из for
#     print("Pico")    #мимо
#     life -= 1

for i in range(0, level)
    print(symbol)
