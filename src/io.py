import csv


def read_files():
    
    with open("data/student_record.csv", "r", encoding='utf-8-sig') as students_in:
        student_information = {
            student["id"] : student 
            for student
            in csv.DictReader(students_in, skipinitialspace=True)
        }    

    with open("data/course_records.csv", "r", encoding="utf-8-sig") as classes_in:
        for student_class in csv.DictReader(classes_in):
            student_id = student_class["student_id"]
            if student_id not in student_information:
                print(f"student not found: {student_id}")
                continue
            student_information[student_id].setdefault("courses", []).append(student_class)

    student_information = list(student_information.values())
    return student_information

# read_files()
