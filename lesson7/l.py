#x = 7/0
#ZeroDivisionError

# x = 15 + "а"
#unsupported operand type(s) for +: 'int' and 'str'

# x = [0, -5,5, "пять"]
# print(x[3])
#IndexError

# x = "Привет
#SyntaxError

# int("А")
# ValueError

# print(x)
# NameError

#assert
# def summa(numbers):
# return sum(numbers)
#
# assert summa([1, 2]) == 3
# assert summa([1, 2]) == 4
# try:
# div = int(input("Введи число для деления")
# x = 5/div
#
# except ZeroDivisionError
# # print("Ошибка")
# # except Exception:
# # print("Я сработал")
# except ValueError:
# print("Введи цифру!")
# else:
# print("Все хорошо")
# finally

# lst = []
# f = open("lessons.txt")
# try:
# for line in f
# lst.append(int(line))
# except ValueError
# print("Я хочу только цифры")
# else:
# try:
# for line in f: #для каждой строчки в файле
#  lst.append(int(line))
#
#
#
# f.close()
# print(lst)

# try:
#    x = 5/0
# except ZeroDivisionError as error_message:
#    print("Ошибка", error_message)
# raise x

try:
    x = 5 / 0
except ZeroDivisionError:
    pass #ничего
if 5 == 2:
    pass