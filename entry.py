
from src import gpa
from src.io import read_course_csv, read_student_csv
from src.utils import convert_to_dict



if __name__ == "__main__":
   student_information = read_student_csv('data/student_record.csv')
   course_information = read_course_csv('data/course_records.csv')

   for course in course_information:
      student_id = course["student_id"]

      if student_id not in student_information:
         print(f"student not found: {student_id}")
         continue
      student_information[student_id].setdefault("courses", []).append(course)

overall_student_information = list(student_information.values())

for student in overall_student_information:
   results=gpa.compute_results(student)
   print(results)
   print('\n')




 