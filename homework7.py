

# 1. 
class Matrix:
    def __init__(self, x ):
        self.x = x 

    def __str__(self):
        d = []
        for n in self.x:
            d.append(' '.join(str(i) for i in n ))
        return '\n'.join(d)

    def __add__(self , nextof):
        d = [ ]
        nom = 0 
        for s  in self.x :
            d.append([ y+i for y , i in zip(s , nextof.x[nom])])
            nom +=1
        return Matrix(d)
                

m1 = Matrix([[1,2,4],[1,2,4],[1,2,4]])
m2 = Matrix([[1,2,4],[1,2,4],[1,2,4]])

m3= m1 + m2
print(m3 + m2)

# 2
class Odejda:
    def __init__(self, title ):
        self.title = title

class Palto(Odejda):
    def __init__(self, title,  V ):
        super().__init__(title)
        self.V = V

    @property
    def razmeri(self):
        return (self.V/6.5 + 0.5)

class Kostym(Odejda):
    def __init__(self, title,  H ):
        super().__init__(title)
        self.H = H

    @property
    def razmeri(self):
        return  (2*self.H + 0.3)

d = [Kostym('kostum', 10 ), Kostym('kostum', 20 )  , Palto('Palto', 15 ) ]
print( sum([i.razmeri for i in d]) )

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Kletka:
    def __init__(self, nom:int):
        self.nom = nom

    def make_order(self, kol):
        j = '\n'.join(['*'*kol for i in range(self.nom // kol)])
        return f"{j}\n{'*' * (self.nom % kol)}"

    def __add__(self , kl):
        return Kletka(self.nom + kl.nom)

    def __sub__(self , kl):
        if (self.nom - kl.nom) > 0:
            return Kletka(self.nom - kl.nom)
        else:
            raise Exception('исключение')
    def __mul__(self , kl):
        return Kletka(self.nom * kl.nom)

    def __truediv__(self , kl):
        if (self.nom / kl.nom) > 0:
            return Kletka(round(self.nom / kl.nom) )
        else:
            raise Exception('исключение')


kl1  = Kletka(11)
kl2  = Kletka(2)
print(kl1.make_order(3))
kl3 = kl1 * kl2
print(kl3.make_order(3))

