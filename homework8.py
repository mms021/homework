# 1. 
class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        return cls(int(date_string.split('-')[0]), int(date_string.split('-')[1]), int(date_string.split('-')[2]))    

    @staticmethod
    def datevalid(date_string):
        return int(date_string.split('-')[0]) in range(1,31) and int(date_string.split('-')[1]) in range(1,12) and int(date_string.split('-')[2]) in range(1990,2040)

date1 = Date.from_string('11-09-2012')
date2 = Date.datevalid('11-09-2012')

# 2. 
class DelForNol:
    @staticmethod
    def delfor(d1, d2):
        if d1 == 0 or d2 ==0 :
            raise Exception("деление на ноль") 
        else:
            return d1 / d2

print(DelForNol().delfor(4,2))

# 3. 
class Error:
    def __init__(self, x = []):
        self.x = x

    def my_input(self):
        while True:
            v = input('Введите значения: ')
            try:
                self.x  += [int(d) for d in v.split(' ')]
                print(f' {self.x} ')
            except:
                if 'stop' in v.split(' '):
                    return f' {self.x} '
                else: 
                    return Error(self.x).my_input()

ex = Error()
print(ex.my_input())

# 4.
# 5. 
# 6. 

class Sklad:
    con = 0 
    dire = []
        
class Orgtehnika(Sklad):
    def __init__(self , name , tip , prise:int , count:int):
        self.name = name
        self.tip = tip
        self.prise =prise 
        self.count = count
        Sklad.con += 1
    
    def priemtehniki(self ):
        Sklad.dire.append({'name' : self.name, 'tip':  self.tip , 'pr':self.prise , 'cou':self.count })
        return Sklad.dire

class Printer(Orgtehnika):
    def __init__(self , name , tip , prise:int , count:int , razmerp):
        super().__init__( name , tip , prise , count)
        self.razmerp = razmerp

class Skaner(Orgtehnika):
    def __init__(self , name , tip , prise:int , count:int, spesf):
        super().__init__( name , tip , prise , count)
        self.spesf = spesf

Printer('HP','good', 10000, 10 , '12/30').priemtehniki()
print(Printer('Canon','good', 10000, 10 , '12/30').priemtehniki())

# 5. 
# 6. 
# 7. 
class Kompleks:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return  f"{self.a + other.a} + {self.b + other.b}i"  

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

print(Kompleks(2 , 3) + Kompleks(3 , 4))
