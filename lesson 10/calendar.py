import datetime

MONTH = ("Январь", "Февраль, ""Март", "Апрель, ""Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
DAYS = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

while True:
    year = input("Год:")
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break

while True:
    month = input("Месяц:")
    if month.isdigit() and int(month) > 0:
        month = int(month)
        break

caltext = ""
caltext += (" " * 34) + MONTH[month - 1] + " " + str(year) + "\n" #для пользователя январь - первый песяц, но в списке он нулевой

for i in range(7):
    caltext += DAYS[i]
print(caltext)


weekSeparator = ("+----------" * 7) + "\n" #\n - gthtyjc yf yjde. cnhhjre
blankRow = ("          " * 7) + "|\n"