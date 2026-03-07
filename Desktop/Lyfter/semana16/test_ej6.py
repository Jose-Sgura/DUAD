import pytest
from eje6 import word_order

def test_exe_6():
    test_list = 'python-variable-funcion-computadora-monitor'

    result = word_order(test_list)

    assert result == "computadora-funcion-monitor-python-variable"

if __name__ == "__main__":
    test_exe_6()
    print("✓ Test passed: Las palabras se ordenaron correctamente")