import FreeSimpleGUI as sg
from categories import show_second_window
from expenses import show_third_window
from incomes import show_fourth_window
from csv_manager import export_report


def show_main_window():
    layout = [
        [sg.Text("WELCOME TO YOUR RELIABLE MANAGER", font=("Helvetica", 14, "bold"))],

        [sg.Text("PLEASE START WITH A CATEGORY"), sg.Button("CATEGORIES")],

        [sg.Text("Once the information is safe you can export it to CSV"), sg.Button("EXPORT TO CSV")],
    ]

    window = sg.Window("FINANCE MANAGER", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "CATEGORIES":
            show_second_window()
        elif event == "EXPORT TO CSV":
            export_report("report.csv")
            sg.popup("Report exported successfully!")

    window.close()