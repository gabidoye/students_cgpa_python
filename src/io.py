import csv


def read_student_csv(filename):
    
    with open(filename, "r", encoding='utf-8-sig') as students_in:
        student_information = {
            student["id"] : student 
            for student in csv.DictReader(students_in, skipinitialspace=True)
        }    
        return student_information

def read_course_csv(filename):    
    with open(filename, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        course_dict = list(reader)

        return course_dict



