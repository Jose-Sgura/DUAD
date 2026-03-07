import pytest
from bubble import bubble_right_to_left

def test_short_list():
    my_test_list= [2,4,3,5]

    bubble_right_to_left(my_test_list)

    assert my_test_list == [2,3,4,5]
    


if __name__ == "__main__":
    test_short_list()
