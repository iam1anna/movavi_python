# x = int(input("Введи число: "))
# if x < 0:
#     print("отрицательное")
# elif x > 0:
#     print("положительное")
# else:
#     rint("Ноль")

# year = int(input("Введите год"))
# if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
#     print("високовсный")
# else:
#     print ("Не високосный")

# number_1 = int(input("Первое число: "))
# operation = input("Введите операцию (+, -, *, /)")
# number_2 = int(input("Второе число: "))
# lst = ["+", "-", "*", "/"] #список операций
# if operation in lst:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
# else:
#     print("написал фигню")


# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# number_3 = int(input("Третье число: "))
# count_pol = 0
# count_otr = 0
#
# if number_1 > 0:
#     count_pol += 1
# elif number_1 < 0:
#     count_otr += 1
#
# if number_2 > 0:
#     count_pol += 1
# elif number_2 < 0:
#     count_otr += 1
#
# if number_3 > 0:
#     count_pol += 1
# elif number_3 < 0:
#     count_otr += 1
#
# print("Положительных: ", count_pol)
# print("Отрицательных: ", count_otr)

# hours = int(input("Часы"))
# minutes = int(input("Минуты"))
# seconds = int(input("Секунды"))
# if (hours > 23 or hours < 0) or (minutes > 59 or minutes < 0) or (seconds > 59 or seconds < 0):
#     print("Формат неверный")
# else:
#     print("Формат верный")
#     print(f"{hours}:{minutes}:{seconds}")


# ticket = input("Введи номер билета (6 цифр): ")
# if len(ticket) == 6 and ticket.isdigit():
#     #len - длина строки
#     #isdigit - число ли это
#     first_half = ticket[:3]
#     second_half = ticket[-3:]
#     first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#     second_sum = int(second_half[0]) + int(second_half[1]) + int(second_half[2])
#     if first_sum == second_sum:
#         print("Билет счастливый")
#     else:
#         print("Билет несчастливый")
# else:
#     print("Ну ты что, надо только 6 цифр(")


# month = input("Введи номер месяца").strip()
# #.strip() - убрать пробелы
#
# if month.isdigit() and 12 >= int(month) >= 1:
#     month = int(month)
#     month = int(month)
#     if 3 <= month <= 5:
#         print("Весна")
#     if 6 <= month <= 8:
#         print("Лето")
#     if 9 <= month <= 11:
#         print("Осень")
#     else:
#         print("Зима")

# h = int(input("Часы: "))
# m = int(input("Минуты: "))
# s = int(input("Секунды: "))

hamsters = int(input("Количество хомяков: "))
if 11 <= hamsters <= 19:
    print(hamsters, "хомяков")
elif hamsters % 10 == 1:
    print(hamsters, "хомяк")
elif 2 <= hamsters % 10 <= 4:
    print(hamsters, "хомяка")
else:
    print(hamsters, "хомяков")