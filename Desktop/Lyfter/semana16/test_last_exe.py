import pytest
from unittest.mock import mock_open, patch
from last_exe import read_lines

def test_read_lines_with_content():
    
    fake_content = "Line 1\nLine 2\nLine 3\n"
    

    with patch('builtins.open', mock_open(read_data=fake_content)):
        
        result = read_lines('fake_file.txt')
        
        
        assert result == ["Line 1\n", "Line 2\n", "Line 3\n"]

def test_read_lines_file_not_found():

    with patch('builtins.open', side_effect=FileNotFoundError):
        
        with pytest.raises(FileNotFoundError):
            read_lines('non_existence_file.txt')



def test_read_lines_empty_file():
    
    with patch('builtins.open', mock_open(read_data="")):
        result = read_lines('void_file.txt')
        
        
        assert result == []


if __name__ == "__main__":
    test_read_lines_with_content()
    print(" Test 1 passed: read lines correctly")
    
    test_read_lines_file_not_found()
    print(" Test 2 passed: raise an error ")
    
    test_read_lines_empty_file()
    print(" Test 3 passed: Manage empty lines")
