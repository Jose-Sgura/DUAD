class Car:
    def __init__(self, brand, model, speed=0):
        self.brand=brand
        self.model=model
        self.speed=speed
    
    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed= max(0, self.speed-amount)
    
    def __str__(self):
        return f"{self.brand} {self.model} - Speed: {self.speed} km/h"
    
my_car=Car("Toyota", "Hilux")
print(my_car)
my_car.accelerate(60)
print(my_car)
my_car.brake(50)
print(my_car)


        