# while True:
#     try:
#         x = int(input("Ярусов: "))
#         if x < 1:
#             raise Exception("🐏 Да ты баран, положительное хочу.")
#     except ValueError:
#         print("Ну блин.")
#         continue
#     except Exception as error_message:
#         print("Низя.", error_message)
#         continue
#     else:  # если ошибок нет
#         break  # выход из while True
#
# while True:
#     char = input("Символ: ").strip()
#     if len(char) != 1:
#         print("Хочу один символ. И кильку.")
#     else:  # если всё хорошо
#         break  # выход из while True
#
# for super_anton in range(1, x + 1):
#     # левая половина
#     print(" " * (x - super_anton), end="")
#     print(char * super_anton, end="||")
#
# # правая половина
#     print(char * super_anton)


# x = int(input("Число"))
# for anton in range(1, 11):
#     print(x, "x", anton, "=", x * anton)

# shirina = int(input("Ширина"))
# visota = int(input("Высота"))
#
# for _ in range(0, visota):
#     print("# " * shirina) #после решетки пробел



# import random
# import viselica
# intro = """
#    ▓▀▀▀▀▄   ▐█    ██   ▄▓▀▀▀▀▄   █▒▀▀▀▒      ▓▀▓      ▐█    ██                  ▓▀▓
#    ▒▌▄▄▄▀   ▐█  ▄█▀█  ▓▌         █▌         ▓▌ ▐▓     ▐█  ▄█▀█                 ▓▌ ▐▓
#    ▒▌  ▀█▄  ▐█╔▓▀ ▐█  █          █▌█▌█▌    ▓▌   ▐▓    ▐█╔▓▀ ▐█                ▓▌▄▄▄▐▓
#    ▒▌  ▄█▀  ▐██   ▐█  ▀▓▄    ▄   █▌       ▓▌     ▐▓   ▐██   ▐█               ▓▌     ▐▓
#    ▀▀▀▀     ▀▀     ▀     ▀▀▀▀    ▓▒▄▄▄▒  ▐█       █▌  ▀▀     ▀  ▄▄▄▄▄▄▄▄▄▄  ▐█       █▌
# """
# print(intro)
# vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
#
#
# word_answer = random.choice(vocabulary).lower()
# word_display = []
#
# for _ in range(len(word_answer)):
#     word_display.append("_")
# print(word_display)
# life = 6
# counter = 0 # счетчик проявленных букв
# while life > 0 and counter != len(word_answer):
#     letter = input("Буква: ")
#     letter_is_be = False #наличие букв в слове
#     for i in range(len(word_answer)): #пробегаемся по слову
#         if letter == word_answer[i]:
#             if word_display[i] != "_":
#                 letter_is_be = True
#
#             else:
#                 word_display[i] = letter #переворачивааем букву
#                 letter_is_be = True
#                 counter += 1 #counter = counter + 1
#     if letter_is_be == False: #если нет нужной буквы
#         life -= 1
#     print(word_display)
#
# if counter == len(word_answer):
#     print("Это победа! Мой друг именно так бы и сказал...")
# else:
#     print(viselica.stages[life])
#     print("На этот случай мой друг не припас фраазы, но, думаю, ты и сам знаешь")




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_end = False

while not should_end:
    text = input("Введи сообщение")
    text = list(text)
    shift = int(input("Сдвиг: "))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    elif shift < -len(alphabet):
        shift = shift % -len(alphabet)



    #механизм сдвига
    cifer_text = ""
    for letter in text:
        if letter == " ":
            cifer_text += letter #ну тип пробел не нужен
        else:
            position = alphabet.index(letter) #позволяет определить индекс letter
            if position + shift > len(alphabet): #вышел за пределы вверх
                new_position = position + shift - len(alphabet)
            elif position + shift < -len(alphabet): #вышли за низ алфавита
                new_position = position + shift + len(alphabet) #вышел за пределы вниз
            else:
                new_position = position + shift
            cifer_text += alphabet[new_position]

    print(cifer_text)
restart = input("Еще раз? y - да, n - нет")
if restart == "n":
