#x = input("Введи что-то")
#temp = x[-1]
#print(x.index(temp) + 1)
#print(len(x))

# name_1 = "Антон"

# path = "C:/Python3/python.exe"
# print("Имя файла:", path[11:])
# print("Расширение:", path[-3:])
# print("Имя каталога:", path[3:10])
# print("Полный путь к каталогу:", path[0:10])

# path = "C:/Python3/python.exe"
# temp = path.split("/")
# print("Имя файла:", temp[-1][-3:])
# print("Расширение:", )
# print("Имя каталога:", temp[1])
# print("Полный путь к каталогу:", temp[0] + "/" + temp[1])

# chapter_1 = input("Глава 1: ")
# page_1 = input("Страница: ")
#
# chapter_2 = input("Глава 2: ")
# page_2 = input("Страница: ")
#
# chapter_3 = input("Глава 3: ")
# page_3 = input("Страница: ")
#
# print(chapter_1.ljust(15), page_1.rjust(15))
# print(chapter_2.ljust(15), page_2.rjust(15))
# print(chapter_3.ljust(15), page_3.rjust(15))


# x = "123456789"
# print(x[::2])  #через один
# print(x[::-1])   #в обратном порядке
# print(x[::-2])    #в обратном порядке через один

x = "12'345'678"

# temp = x[:2] + x[3:5] + x[-3:]
# number = int(temp)
# print(number)

# temp = x.split("'")
# temp2 = temp[0] + temp[1] + temp[2]
# number = int(temp2)
# print(number)

temp = x.replace("'", "")
number = int(temp)
print(temp)


print(1)
