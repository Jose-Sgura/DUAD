import math
class Circle:
    def __init__(self, radius):
        self.radius=radius

    def Get_Area(self):
        return math.pi*(self.radius**2)
    
mycircle=Circle(7)
print("Radio", mycircle.radius)
print("Area", mycircle.Get_Area())


class People():
	def __init__(self, name):
		
		self.name = name

person1=People("Ana")
person2=People("Marvin")
person3=People("Juan")
person4=People("Marta")

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers= max_passengers
        self.passenger=[]
        
    def adding(self, person):
        if len(self.passenger)<self.max_passengers:
            self.passenger.append(person)
            print(f"The person {person.name}  has get into the bus")
        else:
            print("Bus is full, w8 for next trip")
    
    def getting_out(self, person):
        if person in self.passenger:
            self.passenger.remove(person)
            print(f"{person.name} has left the bus")
        else:
            print(f"{person.name} is not in the bus")

limit= Bus(2)
limit.adding(person1)
limit.adding(person3)
limit.getting_out(person3)
limit.getting_out(person4)
    


    


    
    
    

