import FreeSimpleGUI as sg
from csv_manager import save_data, data_load, Income
from datetime import datetime

def validate_date(date_user):
    try:
        datetime.strptime(date_user, "%d/%m/%Y")
        return True
    except ValueError:
        return False

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
    
    layout = [
        [sg.Text("Title"), sg.Input(key="TITLE_ITEM")],
        [sg.Text("Category"), sg.Combo(category_name,key="CATE",readonly=True)],
        [sg.Text("Income"), sg.Input(key="ADDS")],
        [sg.Button("ADD"),sg.Button("DELETE")],
        [sg.Text("DATE:"), sg.Input(datetime.today().strftime("%d/%m/%Y"), key = "DATE")],
        [sg.Text("START DATE"), sg.Input(key="FIRST DATE")],
        [sg.Text("END DATE"), sg.Input(key="LAST DATE")],
        [sg.Button("FILTER")],
        [sg.Table(values=data, headings=["DATE","TITLE","CATEGORY", "INCOMES"],
            key="-TABLE-", size=(40, 10),
            col_widths=[12,12, 12, 12],
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
            date_input = datetime.strptime(values["DATE"], "%d/%m/%Y")
            if not title or not cat or not inc:
                sg.popup_error("PLEASE FILL UP THE INFORMATION REQUIRED")
            elif date_input > datetime.today():
                sg.popup_error("Date cannot be in the future")
            
            else:
                item = Income(values["DATE"],title,cat, inc)
                data.append(item.to_row())
                save_data("incomes.csv", data)

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
                start = datetime.strptime(start, "%d/%m/%Y")
                end = datetime.strptime(end, "%d/%m/%Y")
                filtered = []
                for row in data:
                    register_date = datetime.strptime(row[0], "%d/%m/%Y")
                    if start <= register_date <= end:
                        filtered.append(row)
                window["-TABLE-"].update(values=filtered)
        elif event == "-TABLE-":
            picked =  values["-TABLE-"]
        elif event == "DELETE":
            picked =  values["-TABLE-"]
            if not picked:
                sg.popup_error("Please pick the row you wanna delete")
            else:
                index = picked[0]
                data.pop(index)
                save_data("incomes.csv", data)

                row_colors = []
                for i, row in enumerate(data):
                    category = row[2]
                    if category in color_map:
                        row_colors.append((i, color_map[category]))
                window["-TABLE-"].update(values = data, row_colors=row_colors)


    window.close()
