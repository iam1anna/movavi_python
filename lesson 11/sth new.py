# a = int.input("Число:")
# b= int.input("Число:")
# lst = []
# for jojo in range(a + 1, b): #чтоба а не включалось
#
#     lst.append(jojo ** 2) #** - степень
# print(lst)

# phrase = print(input("Введи фразу"))
# lst = phrase.split(" ") #раскалывает фразу
# list.reverse()
# print(lst)

# chet = 0
# nechet = 0
# lst = []
# number = "" #начальное значение
#
# while number != "end":
#     number = input("Число: ")
#     if number.lstrip("-").isdigit(): #дабы отрицательные прошли проверку
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break #выйти
#     else:
#         print("Число и только число!")
#         continue #перезапустить
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
#
# print(f"Четных:{chet}шт")
# print(f"Нечетных:{nechet}шт")

# phrase = input(">>> ")
# lst = phrase.split(" ")
# print(lst)
#
# for i in range(1, len(lst)):#у первого числа нет предыдущего, поэтому начинаем со 2-го
#     if int(lst[i]) < int(lst[i-1]):
#         print(f"Я считаю, что {lst[i]} больше, чем {lst[i-1]}")

# lst = [-5, 14, 2, -8, 1]
# mini = min(lst)
# maxi = max(lst)
#
# lst[lst.index(max)], lst[lst.index(mini)] = lst[lst.index(mini)], lst[lst.index(max)]
# print(lst)


# import random
# lst = []
# count = int(input("Сколько учеников в строю?"))
# for _ in range(count):
#     lst.append(random.randint(150, 200))
# lst.sort(reverse=True) #от больших к мелким
# print("Было: ", lst)
#
# peter = int(input("Рост Пети: "))
# lst.append(peter)
# lst.sort(reverse=True)
# print("Стало: ", lst)
#
# revers = lst[::-1] #переворачиваем
# peter_position = len(lst) - revers.index(peter)
# print(f"Петя встает {peter_position} по счету")

nums = [4, 5, 6, 7, 8, 9, 10]
shift = int(input("Сдвиг: "))
if shift < 0:
    shift = abs(shift) #модуль числа
    for i in range(shift):
        nums.append(nums.pop(0)) #удаляем первую цифру и добавляем ее в конец
    else:
        for i in range(shift):
            nums.insert(0, nums.pop(-1)) #.pop() - изъятие последнего элемента
            print(nums)