import pytest
from eje7 import qualifying_prime, numberlist

def test_ex_7():
    prime_list = [1,4,6,7,13,9,67]

    result = numberlist(prime_list)

    assert result == [7,13,67]

if __name__ == "__main__":
    test_ex_7()
    print("✓ Test passed: Los números primos se identificaron correctamente")
