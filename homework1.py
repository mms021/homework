#1 Задание 
# в целом все это делается и дальше 

#2 Задание Перевод секунд в время 
#a = int(input("Время в секундах:"))
a = 121
print("%s:%s:%s"% ( a//360, a//60, a%60))

# 3 Задание 
#b = int(input("Сумма чисел:"))
b = 31
print(b + int(f"{b}{b}") + int(f"{b}{b}{b}"))

# 4 Задание 
#c = int(input("Наибольшее число:"))
c = 14070
d = 0
while c != 0:
    if c%10 >= d:
        d = c%10
        c = c//10
    else: 
        c = c//10
print('Число',d)

# 5 Задание
#r = int(input("Выручка:"))
#t = int(input("Издержки:"))
r = 100
t = 90
if r > t:
    print('Прибль:%s , Рентабельность: %s'% (r-t ,r/t*100 ))
elif r <t:
    print('Убыток:', r-t)
else:
    print("Вы вышли в 0")

# 6 Задание
#a = float(input("факт:"))
#b = float(input("план:"))
a = 2.0
b = 3.0
day = 1
print('%s-й день: %s'% (day, round(a,2)))
while b > a:
    a *= 1.1
    day += 1
    print('%s-й день: %s'% (day, round(a,2)))

