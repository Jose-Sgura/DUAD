from actions import entering_information, general_information,top3,average_score
from data import export, import_CSV
from eliminating.failings import failed_student
from eliminating.elimination import rip_student_out
from typing import List, Dict, Any
def menu_face():  
    print("\n Main Menu")
    print("1.Entering information from the students")
    print("2.General information")
    print("3.Top 3 better scores average")
    print("4. Average score")
    print("5.Export data CSV")
    print("6.Import data previously in CSV")
    print("7. View failed students")
    print("8. Delete student (name+section)")
    print("9. Exit")

def main():
    general_info:List[Dict]=[]
    
    while True:
        menu_face()
        option=input("Enter the number you wanna pick").strip()
        if option=="1":
            entering_information(general_info)
        elif option=="2":
            general_information(general_info)
        elif option=="3":
            top3(general_info)
        elif option=="4":
            average_score(general_info)
        elif option=="5":
            export(general_info)
        elif option=="6":
            import_CSV(general_info)
        elif option=="7":
            failed_student(general_info)
        elif option=="8":
            rip_student_out(general_info)
        elif option=="9":
            print("Cya later!")
            break
        else:
            print("Invalid option!")




