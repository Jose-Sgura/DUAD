import pytest
from tres import operations

def test_tres_sum():
    
    calc = operations()
    
    
    result = calc.sum(10, 20)
    
    
    assert result == 30
def test_average_minus():
    avr = operations()
    
    numbers = [-10, -20, -30, -40]
    total = avr.average(numbers)
    
    assert total == -25
def test_zero():
    conver = operations()

    
    equal = conver.conversion(0)

    assert equal == 0





if __name__ == "__main__":
    test_tres_sum()
    print(" Test passed the sum is ok")
    test_average_minus()
    print("Test passed negative average is correct")
    test_zero()
    print("Test passed worked with zero")

