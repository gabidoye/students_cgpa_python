
from src import gpa
from src.io import read_course_csv, read_student_csv
from src.utils import write_result

# import module
from datetime import datetime

# get current date and time
# current_datetime = str(datetime.now())
today = datetime.now()
dt_string = today.strftime("%d%m%Y_%H_%M_%S")
current_datetime = str(dt_string)

gpa_file_name = "gpa_result_"+current_datetime
cgpa_file_name = "cgpa_result_"+current_datetime


def load_data():
   student_information = read_student_csv('data/student_record.csv')
   course_information = read_course_csv('data/course_records.csv')
   for course in course_information:
      student_id = course["student_id"]
      if student_id not in student_information:
         print(f"student not found: {student_id}")
         continue
      student_information[student_id].setdefault("courses", []).append(course)

   overall_student_information = list(student_information.values())
   return overall_student_information

if __name__ == "__main__":
   overall_student_information = load_data()

   gpa_computed_result = []
   cgpa_computed_result = []
   for student in overall_student_information:
      
      gpa_results, cgpa_result = gpa.compute_results(student)
      gpa_computed_result.append(gpa_results)
      cgpa_computed_result.append(cgpa_result)


   write_result(cgpa_computed_result,cgpa_file_name)
   write_result(gpa_computed_result,gpa_file_name)


         







 