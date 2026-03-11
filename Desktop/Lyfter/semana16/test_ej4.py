import pytest
from eje4 import backingoff

def test_ejercicio_4_backwardswords():
    check_string = "Hola Mundo"
    
    result = backingoff(check_string)
    
    assert result == "odnuM aloH"

if __name__ == "__main__":
    test_ejercicio_4_backwardswords()
    print("Test passed")

