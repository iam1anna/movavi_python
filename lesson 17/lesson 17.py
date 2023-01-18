# def add(a, b):
#     return a + b + 1
#
# add_one = lambda a, b: a + b + 1 #аналогичная лямбда функция
#
#
# result = lambda answer: True if answer == "Д" else False
#
# #list comperehension
#
# from random import randint
# lst = []
# for i in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# lst2 = [randint(1, 5) for n in range(5)]
# #1. list comperehension всегда пишется в []
# #2. for n in range() - обычный цикл for -> сколько элементов будет в списке
# #3. Перед for - сам добавляемый элемент
# print(lst2)



# #1 перевод градусов
# c2f = lambda c: 9/5 * c + 32
# print(c2f(200))
#
# f2c = lambda f: (f - 32) * 5/9
# print(f2c(200))
#
# c2k = lambda c: c + 273.15
# k2c = lambda k: k - 273.15
#
# f2k: lambda f: c2k(f2c(f))  #f, потому что там подсказка выыплывает
# degree = 203
# print(f2k(degree))


# #2 кубики
# from random import randint
# while True:
#     k = int(input("Сколько бросаем кубиков?"))
#     lst = [randint(1, 6) for n in range(k)]
#     print(lst)
#
#     vihod = input("Выходим?")
#     exit_code = lambda vihod: True if vihod == "Д" else False
#     if exit_code(vihod) == True:
#             break



# #3 ссылки
# from random import choice  #типа randint
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# a = "httрs://www.google.com"
# dict = {}
# f = [choice(choice(chars)) for i in range(6)]
# b = ''.join(f) #преобразовали строку из типа словря в норм список без пробелов и ковычек
# print(b)
# if a in dict:
#     print("ок", dict[a])
# dict[a] = b
# print("Все ок", dict[a])


#4 Крестики-нолики
field = {"A": ["⬜", "⬜", "⬜"],
         "B": ["⬜", "⬜", "⬜"],
         "C": ["⬜", "⬜", "⬜"]}

cell_letter = ["A", "B", "C"]
cell_number = ["1", "2", "3"]
def drawer() -> None: #функция ничего не вернет
    '''oтрисовывает поле 3х3'''
    print('1, 2, 3')
    for row in range(3):
        print(cell_letter[row], end="")
        for column in range(3):
            print(list(field.values())[row][column],end="")
        print()

def turne(player) -> None:
    '''ход игрока'''
