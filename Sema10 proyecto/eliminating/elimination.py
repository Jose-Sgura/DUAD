from  typing import List
def is_valid_name(name:str)-> bool:
    if not name:
        return False
    s=name.strip()
    if not s:
        return False
    for c in s:
        if not(c.isalpha() or c.isspace()):
            return False
    return True
def is_valid_section(section:str)->bool:
    if not section or not section.strip:
        return False
    numeration=section.strip().replace("","")
    if len(numeration) < 2:
        return False
    numbers= numeration[:-1]
    letter=numeration[-1]
    return numbers.isdigit() and letter.isalpha()

def normal_name(name:str)->str:
    return "".join (name.strip().split()).title()

def normal_section(section:str)->str:
    return section.strip().replace("","").upper()

def student_existence(general_info:List, name: str, section: str)-> bool:
    named= normal_name(name)
    sec=normal_section(section)
    for numeration in general_info: 
        if normal_name (numeration["name"])== named and normal_section(numeration["section"])==sec:
            return True
    return False
def student_location(general_info:list, name:str, section:str)->int:
    named=normal_name(name)
    sec=normal_section(section)
    for i, numeration in enumerate(general_info):
        if normal_name(numeration["name"])==named and normal_section(numeration["section"])==sec:
            return i
    return -1

def rip_student_out(general_info:List):
    name = input("Name of the student you wanna eliminate: ")
    section= input("Section (ej, 10A): ")

    if not is_valid_name(name):
        print("The name is not valid(it is empty or with numbers)")
        return
    if not is_valid_section(section):
        print("The section is not valid, possibly the format is not correct")
        return
    index= student_location(general_info, name, section)
    if index == -1:
        print("There was not student with that name and section")
        return
    numeration= general_info[index]
    print(f"it will be eliminated the student: {numeration["name"]}--{numeration["section"]}")
    accept= input("do you agree?(y/n)").strip().lower()
    if accept=="y":
        general_info.pop(index)
        print("Student eliminated")
    else:
        print("The procedure was called off")









