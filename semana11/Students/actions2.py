
import csv
from typing import List
class Student:
    def __init__(self, name, section,spanish, english, social, science):
        self.name=name
        self.section=section
        self.spanish=float(spanish)
        self.english=float(english)
        self.social=float(social)
        self.science=float(science)

    def average(self):
        return (self.spanish + self.english + self.social + self.science)/4
    def __repr__(self):
        return f"{self.name}({self.section})-Average: {self.average():.1f}"
    
class export:
    def __init__(self):
        self.students: List[Student] = []
    
    def add_apprentice(self, student: Student):
        self.students.append(student)
    
    def export_csv(self, filename):
        with open(filename, mode="w", newline="", encoding="utf-8")as f:
            writer=csv.writer(f)

            writer.writerow(["name","section","spanish","english","social","science"])

            for e in self.students:
                writer.writerow([e.name,e.section,e.spanish,e.english,e.social, e.science])
            print(f"File{filename} created with {len(self.students)} students")

    def import_csv(self, filename):
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            for r in reader:
                learner=Student(r["name"], 
                                r["section"],
                                r["spanish"],
                                r["english"],
                                r["social"],
                                r["science"],)
            self.students.append(learner)
        print(f"File {filename} imported with{len(self.students)} students")
    def lis_student(self):
        if not self.students: 
            print("There are not students")
        for l in self.students:
            print(f"{l.name}| Section:{l.section}|Average:{l.average:.2f}")
if __name__ == "__main__":
    mgr = export()
    mgr.add_apprentice(Student("Ana", "A", 90, 85, 88, 92))
    mgr.add_apprentice(Student("Luis", "B", 70, 75, 72, 68))
    print(f"Students total: {len(mgr.students)}")
    for s in mgr.students:
        print(" •", s)

    mgr.export_csv("students.csv")
    print("CSV exported as " \
    "students.csv")




