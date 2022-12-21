# множества
# s = {1, 2, 3}
# nad = {0, 1, 2, 3}
# pod = {1, 3}
# miss = {4, 5}
#
# if miss < s:
#     print("Это подножество s")

# person1 = {"Python", "C#", ""}
# person2 = {"YoptaScript", "Kotlin", "BrainFuck", "C++"}
#
# if person1 < person2:
#     print("Второй круче")
# elif person2 < person1:
#     print("Первый круче")
# else:
#     print("Стеки разработки отличаются")

# def - ФУНКЦИИ
# def nazvanie_function(): #мы обозначили функцию
#     print("5")
#     print("4")
#     print("3")
#     print("2")
#     print("1")
# nazvanie_function() #мы призвали функцию

# def koren(number, stepen): #функция с двумя аргументами
#     return number ** (1/stepen) #возвращение результата


# 1 дан список и если цифры возрастают, то True


# def roflan(spisok):
#     sorted_l = sorted(l)
#     if sorted_l == spisok:
#         return True
#
# l = [1, 2, 3]
# #roflan - сама функция
# #roflan(spisok=l)
# if roflan(l):
#     print("отсортирован")
# else:
#     print("No")

# 2 найти список с максимальной длиной
# def find_longest(words):
#     chisla = []
#     for i in words: #i - значение каждого слова
#         chisla.append(len(i)) #добавляем в список значение каждого слова
#     maxi = max(chisla)  # максимальная длина всех слов списка
#     ind = chisla.index(maxi)  # индекс наибольшей длины
#     return words[ind]
# spisok = ["да", "нет", "семнадцать", "аннушка", "новикова"]
# print(find_longest(words=spisok))

# 3 вывести минимальное и максимальное значение (min и max использовать нельзя)

# def min_max(spisok):  # spisok - имя нашей функции
#     mini = spisok[0]
#     maxi = spisok[0]
#     for i in spisok:
#         if i > maxi:  # нахождение нового максимума
#             maxi = i  # записываем этот максимум
#         if i < min:
#             mini = i
#
#     return {"максимум": maxi, "минимум": mini}
#
#
# l = [9, 5, 3, 0]
# print(min_max(spisok=l))
#
#
# 4 складываем позиционно каждое из значений двух списков, а потом это тоже складываем. Но сначала нужно получить список первичных сумм
# def list_sum(l1, l2):
#     if len(l1) != len(l2): #если разные длины
#         if len(l1) > len(l2): #если первый список больше
#             for index in range(len(l2)): #проходимся по второму списку
#                 l1[index] += l2[index] #складываем элементы
#             return l1
#         else:
#             if len(l2) > len(l1):
#                 for index in range(len(l1)):  # проходимся по второму списку
#                     l2[index] += l1[index]  # складываем элементы
#                 return l2
#
#
#
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [5, 6, 7]
# print(list_sum(lst1, lst2))


#нужно проверить, является ли число простым (делится на 1 и на себя)
# def anya(number):
#     for i in range(2, number + 1):
#         if i == number:
#             return True
#         elif number % i == 0:
#             break
# print(anya(523))
