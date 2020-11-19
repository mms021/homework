import time
import itertools
# 1. 
class TrafficLight:
    _cl = ["красный" , "желтый" , "зеленый"]
    ti = {"красный": 7, "желтый": 5, "зеленый": 8 }
    def running(self):
        for i in itertools.cycle(self._cl):
            print(i)
            time.sleep(self.ti[i])

lit = TrafficLight()
lit.running()

# 2. 
class Road:
    def __init__(self,length, width ):
        self.length = length
        self.width = width

    def get_road(self , tolsh):
        return self.length * self.width * ( self.width /self.length /10) * tolsh

roa = Road(length= 20, width = 5000)
print(roa.get_road(5))
    


# 3. 
class Worker:
    def __init__(self,name, surname , position , _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
    
class Position(Worker):
    def get_full_name(self):
        return f'Полное ФИО: {self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus'] 

pos = Position('Ivan','Petrov', 'SEO' , {"wage": 1000, "bonus": 500})
print(pos.get_full_name())
print(pos.get_total_income())
# 4. 
class Car:
    def __init__(self ,speed , color , name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return('Go')
    def stop(self):
        return('Stop')
    def turn(self , direction):
        return(direction)
    def show_speed(self):
        return(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed >60:
            return(f'Превышении скорости! {super().show_speed()}')
        else:
            return(super().show_speed())

class WorkCar(Car):
    def show_speed(self):
        if self.speed >40:
            return(f'Превышении скорости! {super().show_speed()}')
        else:
            return(super().show_speed())

class PoliceCar(Car):
    def __init__(self , speed , color , name , is_police=True):
        super().__init__(speed , color , name)
        self.is_police = is_police
    def show_speed(self):
        if self.speed >80:
            return(f'Погоняяя! {super().show_speed()}')
        else:
            return(super().show_speed())

class SportCar(Car):
    pass


tc = TownCar(80 ,'read','x1')
print(tc.show_speed())

sp = SportCar(80 ,'read','x5')
print(sp.turn('left'))
# 5. 
class Stationery:
    def __init__(self , title , ):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'

class Pen(Stationery):
    def draw(self):
        return  f'{super().draw()} PEN'

class Pencil(Stationery):
    def draw(self):
        return  f'{super().draw()} Pencil'

class Handle(Stationery): 
    def draw(self):
        return  f'{super().draw()} Handle'

d =  Pen(title=1)
print(d.draw())



































