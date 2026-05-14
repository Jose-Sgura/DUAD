import FreeSimpleGUI as sg
from csv_manager import save_data, data_load
from datetime import datetime
from finance_logic import validate_income, add_income, delete_row, filter_my_date, validate_date

def show_fourth_window():
    data = data_load("incomes.csv")
    categories = data_load("categories.csv")
    color_map = {}
    for row in categories:
        color_map[row[0]] = row[1]

    category_name = [row[0] for row in categories]

    row_colors = []
    for i, row in enumerate(data):
        category = row[2]
        if category in color_map:
            row_colors.append((i, color_map[category]))

    if not categories:
        sg.popup_error("You must create at least one category before adding incomes!")
        return

    layout = [
        [sg.Text("Title"), sg.Input(key="TITLE_ITEM")],
        [sg.Text("Category"), sg.Combo(category_name, key="CATE", readonly=True)],
        [sg.Text("Income"), sg.Input(key="ADDS")],
        [sg.Button("ADD"), sg.Button("DELETE")],
        [sg.Text("DATE:"), sg.Input(datetime.today().strftime("%d/%m/%Y"), key="DATE")],
        [sg.Text("START DATE"), sg.Input(key="FIRST DATE")],
        [sg.Text("END DATE"), sg.Input(key="LAST DATE")],
        [sg.Button("FILTER")],
        [sg.Table(values=data, headings=["DATE", "TITLE", "CATEGORY", "INCOMES"],
            key="-TABLE-", size=(40, 10),
            col_widths=[12, 12, 12, 12],
            auto_size_columns=False, row_colors=row_colors)]
    ]

    window = sg.Window("INCOMES", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            save_data("incomes.csv", data)
            break
        elif event == "ADD":
            title = values["TITLE_ITEM"]
            cat = values["CATE"]
            inc = values["ADDS"]
            valid, error = validate_income(title, cat, inc, values["DATE"])
            if not valid:
                sg.popup_error(error)
            else:
                data = add_income(data, values["DATE"], title, cat, inc)

                row_colors = []
                for i, row in enumerate(data):
                    category = row[2]
                    if category in color_map:
                        row_colors.append((i, color_map[category]))

                window["-TABLE-"].update(values=data, row_colors=row_colors)
                window["CATE"].update(value=category_name[0] if category_name else "")
                window["ADDS"].update("")
        elif event == "FILTER":
            start = values["FIRST DATE"]
            end = values["LAST DATE"]
            if not validate_date(start) or not validate_date(end):
                sg.popup_error("Format not correct, use dd/mm/yyyy")
            else:
                filtered = filter_my_date(data, start, end)
                window["-TABLE-"].update(values=filtered)
        elif event == "-TABLE-":
            picked = values["-TABLE-"]
        elif event == "DELETE":
            picked = values["-TABLE-"]
            if not picked:
                sg.popup_error("Please pick the row you wanna delete")
            else:
                index = picked[0]
                data = delete_row(data, index, "incomes.csv")
                row_colors = []
                for i, row in enumerate(data):
                    category = row[2]
                    if category in color_map:
                        row_colors.append((i, color_map[category]))
                window["-TABLE-"].update(values=data, row_colors=row_colors)

    window.close()
