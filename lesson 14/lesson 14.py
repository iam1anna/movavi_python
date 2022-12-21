# #сколько повторяющихся символов в тексте
# text = input("Ветер, ветер, ты могуч, ты гоняешь стаю туч").lower()
# symbols = list(".,!?")
# d = {} #словарь
# text_clear = ""
# #очищаем от символов
# for i in text:
#     if i not in symbols:
#         text_clear += i
#
# text_prepared = text_clear.split(" ")
# print(text_prepared)
#
# for word in text_prepared:
#     if word not in d: #если такого слова еще нет в словаре
#         d[word] = 1 #первое повторение
#     else:
#         d[word] += 1
#     print(d)

#посчитать итоговую сумму товаров
# d = {"Бананы": 50,
#      "Богдан": 999,
#      "Чипсы": 0,5}
#
# s = 0
# for i in d.values(): # .values - значения
#     s += 1
# print("Итог:", s)

# DIE_SIDES = 6
# DIE_COUNDS = 2
# die_dicts = {}
# #записываем цифры в столбик
# for first in range(1, DIE_SIDES + 1):
#     for second in range(1, DIE_SIDES + 1):
#        if first + second not in die_dicts: #если сумма еще не обозначена
#            die_dicts[first + second] = [(first, second)] #ох разные типы словарь \ несловарь
#        else:
#            die_dicts[first + second].append((first, second))
#        #print(die_dicts)
#        for key in die_dicts:
#            print(f"{key}: {die_dicts[key]}")


# #сколько повторяющихся символов в тексте
# text = input("Ветер, ветер, ты могуч, ты гоняешь стаю туч").lower()
# symbols = list(".,!?")
# d = {} #словарь
# text_clear = ""
# #очищаем от символов
# for i in text:
#     if i not in symbols:
#         text_clear += i
#
# text_prepared = text_clear.split(" ")
# print(text_prepared)
#
# for word in text_prepared:
#     if word not in d: #если такого слова еще нет в словаре
#         d[word] = 1 #первое повторение
#     else:
#         d[word] += 1
#     print(d)
# maxi = max(d.values()) #максимум среди значений
# print(maxi)
# for key, values in d.items(): # key = "ветер", value = 2
#     if values == maxi:
#         print(f"Ключ: {key} | Значение: {values}")
#         break #так выведется только 1-й максимум

d = {"ключ1": 1,
     "ключ2": 2,
     "ключ3": 3,
     "ключ4": 4,
     "ключ5": 5}
word = d.values()
del d["ключ2"]
del d["ключ1"]
del d["ключ3"]
del d["ключ4"]
d.update(["ключ3", "ключ4", "ключ1"])
print(d)







