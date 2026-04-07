import FreeSimpleGUI as sg
from csv_manager import save_data, data_load, Category
from expenses import show_third_window
from incomes import show_fourth_window

#consulta por el tema de categorias, no entendí para que se ocupa o cual es la funcion exacta
def show_second_window():
    data = data_load("categories.csv")
    layout = [
        [sg.Text("ADD THE CATEGORIES")],
        [sg.Text("Category:"), sg.Input(key="CATEGORY")],
        [sg.ColorChooserButton("PICK A COLOR", target = "COLOR"), sg.Input(key = "COLOR")],
        [sg.Button("ADD"), sg.Button("DELETE")],
        [sg.Text("ONCE ALL-SET GO ADDING YOUR EXPENSES AND INCOMES")],
        [sg.Button("EXPENSE"), sg.Button("INCOMES")],
        [sg.Table(values=data, headings=["TYPE", "COLOR"],
            key="-TABLE-", size=(40, 10),
            col_widths=[20, 20],
            auto_size_columns=False)]
    ]

    window = sg.Window("CATEGORIES", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            save_data("categories.csv", data)
            break
        elif event == "ADD":
            type = values["CATEGORY"]
            color = values["COLOR"]

            if not type:
                sg.popup_error("PLEASE FILL UP THE INFORMATION REQUIRED")
            else:
                item = Category(type, color)
                data.append(item.to_row())
                save_data("categories.csv", data)
                window["-TABLE-"].update(values=data)
                window["CATEGORY"].update("")
        elif event == "-TABLE-":
            picked =  values["-TABLE-"]
        elif event == "DELETE":
            picked =  values["-TABLE-"]
            if not picked:
                sg.popup_error("Please pick the row you wanna delete")
            else:
                index = picked[0]
                data.pop(index)
                save_data("categories.csv", data)
                window["-TABLE-"].update(values=data)

        elif event == "EXPENSE":
            show_third_window()
        elif event == "INCOMES":
            show_fourth_window()

    window.close()