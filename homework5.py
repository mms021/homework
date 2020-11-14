# 1. 
my_file = open("some.txt", "a")
w = ''
while w != "" :
    w = input('Ведите строку    ')
    my_file.write(f"{w} \n")
my_file.close()

# 2. 
f = open('test.txt', 'r')
com = f.readlines()
n = 1 
g = {}
for i in com:
    g[n] = len(i.split(' '))
    n +=1
print('Строк:',len(com), g)
f.close()

# 3. 
fil = open('test.txt', 'r')
com = fil.readlines()
f = [int(f.split(' ')[1]) for f in com  ]
print("Минимальная ЗП у", [f.split(' ')[0] for f in com if int(f.split(' ')[1]) < 20000 ])
print('Средняя зп' , sum(f)/len(f))
fil.close()

# 4. 
slov = {"One" : 'Один' , "Two" :"Два", "Three" : 'Три' , "Four" :'Четыре' }
fo = open('some2.txt', 'a')
with open('some.txt', 'r') as fl:
    for i in fl:
        try:
            fo.writelines(f"{ slov[i.split(' ')[0]]  }  {i.split(' ', maxsplit=1)[1]}")
        except :
            fo.writelines(f"\n")    
fo.close()   

# 5. 
my_file = open("some222.txt", "a")
my_file.write('1 2 3 4 5 6 7')
my_file.close()
my_file = open("some222.txt", "r")
sed =  my_file.read()
print( 'Сумма',sum([int(s) for s in sed.split(' ')]))
my_file.close()

# 6. 
dire = {}
with open('some23.txt', 'r') as flr:
    for sen in flr.readlines():
        dire[sen.split(": ")[0]] = sum([int(s) for s in sen.replace('(', ' ').split() if s.isdigit()])
print(dire)

# 7. 
dire = {}
ybit = []
with open('firm.txt', 'r') as flr:
    for sen in flr.readlines():
        dire[sen.split(' ')[0]] = int(sen.split(' ')[2]) - int(sen.split(' ')[3])
        if int(sen.split(' ')[2]) - int(sen.split(' ')[3]) > 0 :
            ybit.append(int(sen.split(' ')[2]) - int(sen.split(' ')[3]))
data = [dire , {'average_profit': sum(ybit)/len(ybit) } ]
import json
with open("json_ex.json" , 'w') as json_ex:
    json.dump(data, json_ex)










