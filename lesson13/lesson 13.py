#множество
#если во множестве буквы, то они не изменяются
#списки добавлять нельзя, но все остальное можно, буквы в ковычках
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7}
# print(set1 | set2) #объединение | .union()
# print(set1 & set2) #пересечение .intersection
# print(set1 - set2) #разность - что-то уникальное из 1 списка .difference
# print(set1 ^ set2) #симметрическая разность .symmetric.difference


#словарь
# dictionary = {"Ключик1": 1,
#               "Ключик2":"значение",
#               "Ключик3: {"Влож1": -1}}


# from random import randint
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst) #перевод во множество -> удалили повторения
# print(f"{len(unique)} штук: {unique}")


# from random import randint
# size = randint(100, 1000) #сколько раз число генерировалось
# r_start = 0
# r_end = 10000
# lst1 = []
# lst2 = []
#
# for _ in range(size):
#     lst1.append(randint(r_start, r_end))
#     lst2.append(randint(r_start, r_end))
#
# set1 = set(lst1)
# set2 = set(lst2)
# overall = set1 & set2 #set1.intersection(set2)
# print(f"Общих чисел: {len(overall)}")
# print(f"Количество генераций: {size}")
# print(f"Минимальное значение: {min(overall)}")
# print(f"Максимальное значение значение: {max(overall)}")
# print(sorted(overall)) #-> сортированный список

# lst = set() #cоздаем пустое множество
# insert = ""
# while insert != "end":
#     insert = (input("Введи число: "))
#     if insert.lstrip("-").isdigit(): # - тоже буква, .lstrip - убрать символы слева
#         if insert not in lst:
#             print("Нет(")
#             lst.add(insert)
#         else:
#             print("Да)")
#     elif insert == "end":
#         break
#     else:
#         print("Было бы славно получить число, для твоего же блага")


# lst1 = [0, False, 1 - 1, "один", 2, 3.14]
# print(f"{lst1} - возможно, есть повторения")
# set1 = set(lst1)
# print(f"{set1} - повторений нет")
# if len(lst1) != len(set1):
#     print("Повторения есть")
# else:
#     print("Повторений нет")

# phrase = "Я люблю movavi, программирование, а ещё я люблю пельмени!".lower()
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', ',', '.', '?', '>', '<', "'", '"', '/', ':', ';']
# text = ""
# for char in phrase: #перебираем каждый символ фразы
#     if char not in symbols: #если не спец. символ, добавляем в новый список
#         text = text + char
# text = text.split(" ")
# print(text)
# s = set(text) #повторы
# print(s)
# print(f"Различных слов: {len(s)} шт")

# d = {"Антон": ["Сердце"]}
# print(d["Антон"][1])


n = int(input("Кол-во связей деревьев: "))
gen = {}
for _ in range(n):
    child, parent = input("Ребенок Родитель: ").upper().split()
    if parent not in gen: #если родителя еще нет в древе
        gen[parent] = [child]
    else: #если отец уже есть
        gen[parent].append(child) #добавляем ребенка
print(gen)
