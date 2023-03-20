
# import module
from src import gpa
from src.io import read_student_file_with_course
from src.utils import write_result
from datetime import datetime


today = datetime.now()
dt_string = today.strftime("%d%m%Y_%H_%M_%S")
current_datetime = str(dt_string)

file_name = "result_"+current_datetime
 


if __name__ == "__main__":
    student_file = 'data/student_record.csv'
    course_file = 'data/course_records.csv'
    overall_student_information = read_student_file_with_course(student_file, course_file)

    computed_result =[]
    for student in overall_student_information:
      results=gpa.compute_results(student)
      computed_result.append(results)


      write_result(computed_result,file_name)


    


         







 