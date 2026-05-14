from unittest.mock import patch, mock_open
from csv_manager import save_data, data_load

def test_save_data():
    data= [["01/07/2025", "Pizza", "Comida", "2000"]]

    with patch("builtins.open",mock_open()) as mock_file:
        save_data("test.csv",data)
        mock_file.assert_called_once_with("test.csv","w", newline="")
        print("Test passed, save_data called correctly")

def test_data_load():
    fake= "01/07/2025,Pizza,Comida,2000\n"

    with patch("builtins.open", mock_open(read_data=fake)):
        result=data_load("test.csv")
        assert result == [["01/07/2025", "Pizza", "Comida", "2000"]]
        print("Test passed, data_load working correctly")

if __name__ == "__main__":
    test_save_data()
    test_data_load()





