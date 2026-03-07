import pytest
from eje5 import indentifier

def test_exe_5():
    
    test_letter = "I love Nación Sushi"
    
    
    capital, lower = indentifier(test_letter)
    
    assert capital == 3
    assert lower == 13 

if __name__ == "__main__":
    test_exe_5()
    print("Test passed")
        