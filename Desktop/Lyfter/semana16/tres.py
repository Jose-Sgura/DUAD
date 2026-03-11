import pytest

class operations:
    def sum(self, a, b):
        return a + b
    
    def average(self, numbers):
        total = sum(numbers)
        
        
        spaces = len(numbers)
        
        
        avg = total / spaces
        
        return avg
    
    def conversion(self, kg):
        pound = 2.20462262185

        total = kg * pound

        return total




if __name__ == "__main__":
    calculate = operations()
    
    result = calculate.sum(2, 3)
    print(f"the sum is: {result}")
    
    numbers = [10, 20, 30, 40]
    average_result = calculate.average(numbers)
    print(f"the average of = {numbers} es: {average_result}")

    convert = calculate.conversion(10)
    print(f"the amount in pounds is = {convert}")
        