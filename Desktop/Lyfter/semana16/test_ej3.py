import pytest
from ej3 import sum

def test_sum_three():
    plist = [4,6,2,29]
    
    result = sum(plist)
    
    assert result == 41

if __name__ == "__main__":
    test_sum_three()