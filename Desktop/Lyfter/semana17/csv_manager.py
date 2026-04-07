import csv
class Expense:
    def __init__(self, date, title, type, amount):
        self.date = date
        self.title = title
        self.type=type
        self.amount=amount
    def to_row(self):
        return [self.date, self.title, self.type, self.amount]
class Income:
    def __init__(self, date,title, category, amount):
        self.date=date
        self.title=title
        self.category=category
        self.amount=amount
        
    def to_row(self):
        return [self.date, self.title,self.category, self.amount]
class Category:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def to_row(self):
        return [self.name, self.color]


def save_data(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
        
def data_load(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def export_report(filename):
    expense = data_load("expenses.csv")
    incomes = data_load ("incomes.csv")

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Title", "Amount", "Category", "Type"])

        total_expenses = 0
        for row in expense:
            writer.writerow([row[0], row[1], row[3], row[2], "", "Expense"])
            total_expenses += float(row[3])
        total_incomes = 0
        
        for row in incomes:
            writer.writerow([row[0], row[1], row[3],row[2], "", "Income"])
            total_incomes += float(row[3])
    
        writer.writerow([])
        writer.writerow(["Totals:"])
        writer.writerow(["Incomes:", total_incomes])
        writer.writerow(["Expense:", total_expenses])
        writer.writerow(["Total balance:", total_incomes - total_expenses])

