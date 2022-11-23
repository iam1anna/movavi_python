import random
import  datetime

while True:
    number = input("Сколько дней недели мы генерируем (до 70)")
    if not number.isdigit() or int(number) > 70 or int(number) < 2:
        print("Для твоего же блага - до 70!")
        print("-" * 8)
    else: #если все правильно
        number = int(number) #переводим строчку в число
        break

birdhdays = []
startofyear = datetime.date(2022, 1, 1)
for _ in range(number):
    shift = random.randint(0, 364)
    shiftofdays = datetime.timedelta(shift)
    birdhday = startofyear + shiftofdays
    birdhdays.append(birdhday)

for index in range(number):
    print(f"{index + 1}) {birdhdays[index]}") #string(?)

print("=" * 10)
for i in set(birdhdays): #set - это множества, где повторений нет
    if birdhdays.count(i) > 1: #два и более совпадения, повторяющиеся др
        print(f"- {i.strftime('%d.%m.%y')} встречается {birdhdays.count(i)} раза.")