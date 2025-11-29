from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, salary):
        self._name=name
        self.salary=salary
    
    @property
    def name(self,value):
        self._name
    
    @name.setter
    def name(self,value):
        self._name=value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("The amount can not be negative")
        self._salary=value

    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("The amount can not be negative")
    
        increase= self.salary*percentage
        self.salary+=increase

if __name__=="__main__": 
    employee= Employee("Ana", 1000)
    employee.promote(0.1)
    print(employee.salary)
    
class User(ABC):
    def __init__(self, name):
        self._name=name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def get_role(self):
        return "admin"
    
    def has_permission(self, permission):
        return True
    
class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self._allowed_permissions={"read"}

    def get_role(self):
        return "regular"
    
    def has_permission(self, permission):
        return permission in self._allowed_permissions
    
if __name__== "__main__":
    user1= AdminUser("Ana")
    user2= RegularUser("Fernando")

    print(user1.has_permission("delete"))
    print(user1.has_permission("comment"))
    print(user2.has_permission("delete"))
    print(user2.has_permission("read"))

class Vehicle:
    def __init__(self, brand, year):
        self._brand=brand
        self._year=year
    
    def get_info(self):
        return f"{self._brand} ({self._year})"
    
class Car(Vehicle):
    def __init__(self, brand, year,  doors):
        super().__init__(brand,year)
        self._doors=doors
    def get_info(self):
        return f"{self._brand} ({self._year}) - {self._doors} doors"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year, motorcycle_type):
        super().__init__(brand, year)
        self._motorcycle_type=motorcycle_type
    def get_info(self):
        return f"{self._brand} ({self._year}) - Type: {self._motorcycle_type}"


vehicle1=Car("Honda", 1995, 2)
vehicle2=Motorcycle("Yamaha", 2022, "Sport")

print(vehicle1.get_info())
print(vehicle2.get_info())