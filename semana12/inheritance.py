
from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def Add_Money(self, add):
        if add < 0:
            raise ValueError ("Transaction not valid--Please enter an amount over 0")
        self.balance+=add
        return self.balance
    def Withdraw(self, add):
        if add<0:
            raise ValueError ("Transaction not valid--Please enter an amount over 0")
        if add > self.balance:
            raise ValueError("Insufficient funds")
        self.balance-=add
        return self.balance
        
    
class Savings_Account(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance=min_balance
        if self.balance< self.min_balance:
            raise ValueError("The balance can not be less than the minor ")
    def Withdraw(self, add):
        if add <= 0:
            raise ValueError("Transaction not valid--Please enter an amount over 0")
        if self.balance-add< self.min_balance:
            raise ValueError("Invalid transaction: the amount is less than the minor")
        self.balance-=add
        return self.balance

class Shape(ABC):
    def calculate_perimeter(self):
        pass
    def calculate_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        if radius<=0:
            raise ValueError("The value must be over 0")
        self.radius=radius
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius
    def calculate_area(self):
        return 3.14159 * self.radius * self.radius
class Square(Shape):
    def __init__(self, side):
        if side <=0:
            raise ValueError("The value must be over 0")
        self.side=side
    
    def calculate_perimeter(self):
        return 2 * self.side
    
    def calculate_area(self):
        return self.side * self.side
class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise("The value must be over 0")
        self.width=width
        self.height=height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    def calculate_area(self):
        return self.width * self.height
    
if __name__ == "__main__":
    bank= BankAccount(150)
    bank.Add_Money(50)
    bank.Withdraw(20)

    safe= Savings_Account(balance=100, min_balance=50)
    safe.Withdraw(20)

    cir = Circle(5)
    sq = Square(7)
    rect = Rectangle(2, 5)
    print(cir.calculate_area())
    print(sq.calculate_perimeter())
    print(rect.calculate_area())

#multiples
class Student:
    def __init__(self, name, major):
        self.name=name
        self.major=major

    def study(self):
        print(f"{self.name} is studying {self.major}")

class Worker:
    def __init__(self, enterprise, salary):
        self.enterprise=enterprise
        self.salary=salary
    
    def work(self):
        print(f"working in {self.enterprise} earning {self.salary}")

class StudentWorking(Student, Worker):
    def __init__(self, name, major, enterprise, salary):
        Student.__init__(self, name, major)
        Worker.__init__(self, enterprise,salary)
    def introduction(self):
        print(f"Hello, I´m {self.name}, I am studying {self.major} and I´m working in {self.enterprise}")

People=StudentWorking("Jose","Ing.Software","Coopelesca","$3.000")
People.introduction()
People.study()
People.work()
