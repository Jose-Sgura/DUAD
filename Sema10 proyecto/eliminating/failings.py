def failed_student(general_info:list):
    there_was=False
    for numeration in general_info:
        fails=[]
        subjects= [("spanish","Spanish"), 
                    ("english", "English"),
                    ("social","Social Studies"),
                    ("science","Science")]
        for key,tag in subjects:
            try:
                score= float(numeration.get(key,0))
                if score < 60:
                    fails.append(f"{tag}:{score:g}")
            except:
                pass
        if fails:
            there_was=True
            print(f"- {numeration['name']} ({numeration['section']}): " + ", ".join(fails))
    
    if not there_was:
        print("There is not failed  students by subject")