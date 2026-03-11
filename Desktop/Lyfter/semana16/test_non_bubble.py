import pytest
from bubble import bubble_right_to_left

def test_non_list():
    my_test_tuple = (2,4,5,3)

    with pytest.raises(TypeError):
        bubble_right_to_left(my_test_tuple)


if __name__ == "__main__":
    test_non_list()
    print(" Test passe")

