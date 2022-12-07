# lst = [5, 7, "7", True]
# lst.append(9)
# lst.pop(-2) # .pop() - удалить True
# lst.remove() # .remove удалить по значению

# lst1 = [0, 1, 2]
# lst2 = ["А", "Б", "В"]
# lst1.extend(lst2) #extend() - расширить список
# print(lst1)

# lst = [1, 2, 3]
# lst.insert(1, 1.5) #insert - вставить какое-то значение: сначала - индекс, потом - значение
# print(lst)

# lst = [0, 3, 2, 15, -3]
# lst.sort() #сортируем по возрастанию
# print(lst)
#
# lst = [0, 3, 2, 15, -3]
# lst.sort(reverse=True) #сортируем по убыванию
# print(lst)
#
# lst.clear()
# print(lst)


# lst = [5, 4, 3, 2, 1]
# lst.reverse() # .reverse() перевернуть список
# print(lst)


#КОРТЕЖИ
#типы данных = мутабельные(изменяемые) + немутабельные(неизменяемые)


# x = "mavavi" #str - неизменяемый тип данных
# #x[1] = "о" #так нельзя!
# x = "movavi"
# print(x)

tup = (1, 2, 3)
tup1 = 1, 2, 3
tup2 = 1,

print(max(tup))