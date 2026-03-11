import pytest
from bubble import bubble_right_to_left

def test_empty_list():
    my_test_list = []

    bubble_right_to_left(my_test_list)

    assert my_test_list == []
    


if __name__ == "__main__":
    test_empty_list