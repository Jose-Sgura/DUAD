import FreeSimpleGUI as sg
from categories import show_second_window
from csv_manager import export_report, data_load


def load_movements():
    expenses = data_load("expenses.csv")
    incomes = data_load("incomes.csv")
    movements = []
    total_expenses = 0
    total_incomes = 0
    for row in expenses:
        movements.append(row + ["Expense"])
        total_expenses += float(row[3])
    for row in incomes:
        movements.append(row + ["Income"])
        total_incomes += float(row[3])
    return movements, total_expenses, total_incomes


def show_main_window():
    movements, total_expenses, total_incomes = load_movements()

    layout = [
        [sg.Text("WELCOME TO YOUR RELIABLE MANAGER", font=("Helvetica", 14, "bold"))],
        [sg.Text("PLEASE START WITH A CATEGORY"), sg.Button("CATEGORIES")],
        [sg.Text("Once the information is safe you can export it to CSV"), sg.Button("EXPORT TO CSV")],
        [sg.Text("ALL MOVEMENTS", font=("Helvetica", 12, "bold"))],
        [sg.Table(values=movements,
                headings=["DATE", "TITLE", "TYPE", "AMOUNT", "MOVEMENT"],
                key="-MOVEMENTS-", size=(60, 15),
                col_widths=[12, 12, 12, 12, 10],
                auto_size_columns=False)],
        [sg.Text(f"Total Expenses: {total_expenses} | Total Incomes: {total_incomes} | Balance: {total_incomes - total_expenses}", key= "-TOTALS-")]
        ]

    window = sg.Window("FINANCE MANAGER", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "CATEGORIES":
            show_second_window()
            movements, total_expenses, total_incomes = load_movements()
            window["-MOVEMENTS-"].update(values=movements)
            window["-TOTALS-"].update(f"Total Expenses: {total_expenses}  |  Total Incomes: {total_incomes}  |  Balance: {total_incomes - total_expenses}")
        elif event == "EXPORT TO CSV":
            export_report("report.csv")
            sg.popup("Report exported successfully!")

    window.close()
