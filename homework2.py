#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
tub = [1,'2',3.0, True ,{'a':"f"}]
for i in tub:
    print(type(i),i)
#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
#a = input("ведите значения")
a = 'a b c d e f c'
a = a.split(' ')
b = len(a) if len(a) % 2 == 0 else len(a) -1
for i in range(0,b,2):
    a[i] , a[i+1] = a[i+1] , a[i]
print(a)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
#a = input('Месяц:')
a = '1'
b = { ('11','12' ,'1'):'Зима',('2','3','4'):'Весна',('5','6','7'):"Лето",('8','9','10'):"осень"}
monf = {'1':['января','Зима'], '2':['февраля','Весна'],'3':['марта','Весна'],'4':['апреля','Весна'],'5':['мая','Лето'],'6':['июня','Лето'],'7':['июля','Лето'],'8':['августа','Лето'],'9':['сентябрь','Осень'],'10':['октябрь','Осень'],'11':['ноябрь','Осень'],'12':['Декабрь',"Зима"]}
print(monf[a][0] , monf[a][1] )
#print(b[('1')])
#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
#a = input("Строку :")
a = "1234567891011 12345 Привет"
n = 1
for i in a.split(' '):
    print(n, i[:10])
    n +=1

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#a = int(input('Число :'))
a = 8
my_list = [7, 5, 4, 2, 3, 2]
my_list.append(a)
print(sorted(my_list, reverse=True))

my_list = [7, 5, 3, 3, 2]
my_list2 = []
b = 8
for i in range(len(my_list)):
    #print(my_list[i] ,b, i)
    if my_list[i] > b :
        my_list2.append(my_list[i])
    elif my_list[i] < b :
        my_list2.append(b)
        my_list2.append(my_list[i])
        b= 0
    else:
        my_list2.append(my_list[i])
print(my_list2)


#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.



d = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}), 
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
    ]

while True:
    f = input("Добавить продукт - 1, вывести аналитику - 2, Выйти: 3 ")
    if f == "1":
        m = input('Название: Цена: Колличество: ')
        m = m.split(' ')
        tup  = (int(d[-1][0] +1) , {"название": m[0], "цена": int(m[1]), "количество": int(m[2]), "eд": "шт."})
        dic = d.append(tup)
        print(d)
    elif f == '2':
        hov= d[0][1].keys()
        dictr = {'название':[],"цена":[] ,"количество":[] ,'eд':[]}
        for i in d:

            dictr['название'].append(i[1]["название"]) 
            dictr["цена"].append(i[1]["цена"]) 
            dictr["количество"].append(i[1]["количество"]) 
            dictr['eд'].append(i[1]["eд"]) 

        print(dictr)
    elif f =='3':
        break




