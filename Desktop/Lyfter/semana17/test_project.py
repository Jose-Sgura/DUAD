import unittest
from csv_manager import Expense

class TestExpense(unittest.TestCase):

    def test_to_row(self):
        item=Expense("01/07/2025", "Pizza", "Comida", "2000")
        result= item.to_row()
        self.assertEqual(result, ["01/07/2025", "Pizza", "Comida", "2000"])
    
    def test_valid_date(self):
        self.assertTrue(validate_date("01/07/2025"))

    def test_invalid_date(self):
        self.assertFalse(validate_date("01/07/2025"))
    
    def test_invalid_text(self):
        self.assertFalse(validate_date("Hello"))


if __name__ == "__main__":
    unittest.main()