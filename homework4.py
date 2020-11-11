
#1. 
from sys  import argv
def priseofmywork(h,stavka = 300,premia = 0):
    return (h*stavka)+ premia

#file_name, h , stavka = argv
h = 10
stavka = 10
print(priseofmywork(int(h), int(stavka) ))

# 2. 
a  = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([j for i, j in zip(a, a[1:]) if j > i])


#3. 
print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])

#4. 
no  = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([f for f in no if no.count(f) == 1 ])

#5. 
from functools import reduce

def summofval(a,b):
    return a * b

print(reduce(summofval , [x for x in range(100 , 1001) if x % 2 == 0 ]))

#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count , cycle
from time import sleep

for n in count(4):
    print(n, end=" ")
    sleep(0.1)
    if n == 10:
        break


z  = [12, 44, 4, 10, 78, 123]
cy = cycle(z)
q = 0

while q != 10:
    print(next(cy), end=" ")
    q += 1 


#7.
def fact(n):
    start  = 1
    while n >= start:
        yield start
        start +=1

print([el for el in fact(4)])

#for el in fact(n)]




