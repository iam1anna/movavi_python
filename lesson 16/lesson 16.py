#1 сложить элементы в списке

# def pelmeni(spisok:list) -> int: #type hinting, list в скобках можно убрать, int - то что в итоге цифры
#     " " " типа описание " " "
#     s = 0
#     for element in spisok:
#         s += element
#     return s


# lst = [5, 4, 8, 9, 3]
# print(pelmeni(lst))


#2 Функция принимает разделитель списка строк и возвращает список разделенным на "|"
# def join(spisok:list, sep:str):
#     resalt = ""
#     for i in spisok:
#         resalt = resalt + i + sep
#     return resalt
#
#
#
# lst = ["Москва", "Новосибирск", "Кемерово"]
# print(join(sep="|", spisok=lst))

#3 написать функцию для вычисления факториала числа
# def factorial(chislo):
#     result = 1
#     for i in chislo(2, chislo + 1):
#         result = result * i
#     return result
#
# print(factorial(chislo=5))

#4 есть строка, надо посчитать кол-во букв верхнего и нижнего регистра

# def python(stroka):
#     dlina = {"Верх": 0,
#              "ниж": 0}
#     for i in stroka:
#         if i.isupper():
#             dlina["Верх"] += 1
#         elif dlina["ниж"] += 1
#         return dlina
#
# stroka = ["Строка"]
# print(python(stroka))

from pictures import box_carrot, box_empty, box_close
from random import choice

def generate_boxes(status1, status2):
    result = ""
    if status1 == "ПУСТОТА":
        box1 = box_empty.format(COLOR1.center(13).split).split("\n")
    elif status1 == "МОРКОВКА":
            box1 = box_carrot.format(COLOR1.center(13).split).split("\n")
    else:
        box1 = box_close.format(COLOR1.center(13).split).split("\n")



    if status2 == "ПУСТОТА":
        box2 = box_empty.format(COLOR2.center(13).split).split("\n")

    elif status2 == "МОРКОВКА":
            box2 = box_carrot.format(COLOR2.center(13).split).split("\n")
    else:
        box2 = box_close.format(COLOR2.center(13).split).split("\n")
    for element in zip(box1, box2): #склеиваем коробки:
        result += "   ".join(element) + ("\n")
    result += p1Name[:10].center(13) + " " * 7 + p2Name[:10].center(13) + "\n"
    return result



COLORS = ["ФИОЛЕТОВАЯ", "КАЙФОВАЯ", "ЗОЛОТАЯ", "МАГАДАНСКАЯ"]
COLOR1 = choice(COLORS)
COLOR2 = choice(COLORS)
while COLOR1 == COLOR2:
    COLOR2 = choice(COLORS)
p1Box = "ЗАКРЫТО"
p2Box = "ЗАКРЫТО"




p1Name = input("Имя первого игрока:")
while p1Name.strip() == "": #если убрав пробелы остается пустота
    p1Name = input("Имя первого игрока")

p2Name = input("Имя второго игрока:")
while p2Name.strip() == "": #если убрав пробелы остается пустота
    p2Name = input("Имя второго игрока")
print(generate_boxes("ПУСТОТА", "МОХ"))


while True:
    print(f"{p2Name}, в твоей коробке {p2Box}")

    #ПРАВДА / БЛЕФ
    action = input(f"Иногда нам приходится принять решение... \n"
                   f"1. Блеф: сказать, что в коробке {p1Box}\n"
                   f"2. Правда: не сказать, что в коробке {p1Box}\n"
                   f" (Б - блеф, П - правда) ").upper()

    while action != "Б" and action != "П":
        action = input((f" (Б - блеф, П - правда) ")).upper()
    print("\n" * 70)
    input(f"{p1Name} открывает глаза(Enter)")
    if action == "Б":
        print(f"{p2Name} сообщает, что в его коробке {p1Box}")
    else:
        print(f"{p1Name} сообщает, что в его коробке {p2Box}")

