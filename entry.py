
from src import gpa
from src.io import read_course_csv, read_student_csv
from src.utils import convert_to_dict

# import module
from datetime import datetime

# get current date and time
current_datetime = str(datetime.now())

file_name = "result_"+current_datetime



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

computed_result =[]
for student in overall_student_information:
   results=gpa.compute_results(student)
   computed_result.append(results)
print(computed_result)

   # print(results)
   # print('\n')

with open("data/%s.txt" % file_name , 'w') as f:
   for result in computed_result:
      for key, value in result.items():
         f.write('%s:%s\n' % (key, value))
       
         







 