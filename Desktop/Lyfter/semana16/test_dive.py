import pytest
from division import divide

def test_division_input_number():
    result = divide(10, 2)
    
    
    assert result == 5.0

def test_division_zero_error():
    
    with pytest.raises(ValueError):
        divide(10, 0)

def test_division_string_error():

    with pytest.raises(TypeError):
        divide("10", 2)
    
    with pytest.raises(TypeError):
        divide(10, "2")
    
    with pytest.raises(TypeError):
        divide("10", "2")

if __name__ == "__main__":
    test_division_input_number()
    print("Test passed: divison is ok")
    
    test_division_zero_error()
    print(" Test passed: cannot divide by zero")
    
    test_division_string_error()
    print(" Test passed: Strings are not accepted")