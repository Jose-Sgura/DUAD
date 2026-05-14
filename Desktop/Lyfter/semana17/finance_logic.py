from datetime import datetime
from csv_manager import save_data, data_load, Expense, Income, Category

def is_valid_amount(amount_str):
    try:
        value = float(amount_str)
        return value > 0
    except ValueError:
        return False

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
#Validations
def validate_expense(title, type, expense, date_str):
    if not title.strip() or not type.strip() or not expense.strip():
        return False, "Please fill all fields"
    if not is_valid_amount(expense):
        return False, "Amount must be a valid positive number"
    if not validate_date(date_str):
        return False, "Format not correct, use dd/mm/yyy"
    if datetime.strptime(date_str, "%d/%m/%Y") > datetime.today():
        return False, "Date cannot be in the future"
    return True, None

def validate_income(title, cat, inc, date_str):
    if not title.strip() or not cat.strip() or not inc.strip():
        return False, "Please fill all fields"
    if not is_valid_amount(inc):
        return False, "Amount must be a valid positive number"
    if not validate_date(date_str):
        return False, "Format not correct, use dd/mm/yyyy"
    if datetime.strptime(date_str, "%d/%m/%Y") > datetime.today():
        return False, "Date cannot be in the future"
    return True, None

#operations
def add_expense(data, date, title, type,expense ):
    item =  Expense(date, title, type, expense)
    data.append(item.to_row())
    save_data("expenses.csv", data)
    return data
def add_income(data, date, title, cat, inc):
    item = Income(date, title, cat, inc )
    data.append(item.to_row())
    save_data("incomes.csv", data)
    return data
def add_category(data, name, color):
    item = Category(name, color)
    data.append(item.to_row())
    save_data("categories.csv", data)
    return data
def delete_row(data, index, filename):
    data.pop(index)
    save_data(filename, data)
    return data
def filter_my_date(data, start_str, end_str):
    start = datetime.strptime(start_str, "%d/%m/%Y")
    end = datetime.strptime(end_str, "%d/%m/%Y")
    filtered = []
    for row in data:
        row_date = datetime.strptime(row[0], "%d/%m/%Y")
        if start <= row_date <= end:
            filtered.append(row)
    return filtered