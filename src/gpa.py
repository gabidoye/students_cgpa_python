from src.utils import calculate_sum


GRADE_POINT_MAP = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0} #constant used for mapping score and grades

def compute_student_grade(scores):
   """
   This computes the students grade and point based on the score the student gets in each course
   Parameters
   -----------
   scores : List
         List of scores obtained by student
   Returns
   -------
   grade: List
         grade of scores 
   point:  int
         coresponding point for the grade obtained by the student
   Example
   --------
   scores = [60, 80, 40, 30]
   grades = ['B','A','D','E']
   point = [4, 5, 2, 1]
   """

   grade = []
   points = []
   for score in scores:
      if score >= 70:
         grade.append('A')
         points.append(GRADE_POINT_MAP['A'])
      if score  >= 60 and score <= 69:
         grade.append('B')
         points.append(GRADE_POINT_MAP['B'])
      if score >= 50 and score <= 59:
         grade.append('C')
         points.append(GRADE_POINT_MAP['C'])
      if score >= 45 and score <= 49:
         grade.append('D')
         points.append(GRADE_POINT_MAP['D'])
      if score >= 40 and score <= 44:
         grade.append('E')
         points.append(GRADE_POINT_MAP['E'])
      if score <= 39 :
         grade.append('F')
         points.append(GRADE_POINT_MAP['F'])
   return grade, points

# print(compute_student_grade([50,60,84]))
   

def compute_student_gpa(units, scores):
   """
   Use the score obtained in each semester(fall or spring) and the course unit credit to calculates the gpa for the respective semester.
   Parameters
   -----------
   units : List
         the unit credit of the course taken by the student
   scores : List
         score obtained by the student in each course
   Returns
   -------
   total_unit: int
            summed units
   total_grade_point: 
            summed grades
   gpa:  float
      computed grade point average
   Example
   --------
   compute_student_gpa([4, 5], [8, 15], [2,3], [1,2])) # (2.56, 0.6)
   """
   grade,points = compute_student_grade(scores)
   total_unit = sum(units)
   total_grade_point = sum([a*b for a,b in zip(units,points)])# 11 [a,a,e][5,5,1][3,4,2]
   gpa = round((total_grade_point / total_unit), 2)

   return total_unit,total_grade_point,gpa


   
def get_semesters(course_records):
   """
   This function retrieve the unique semesters from the student record.
   parameters
   -----------
   course_records: dict
                  student information
   Returns
   -------
   semesters: List
            unique list of semesters
   """
   semesters = set([course['term'] for course in course_records['courses']])
   return semesters

def get_sessions(course_records):
   """
   This function retrieve the unique sessions from the student record.
    parameters
   -----------
   course_records: dict
                  student information
   Returns
   -------
   sessions: List
            unique list of session
   """
   sessions = set([course['session'] for course in course_records['courses']])
   return sessions


def get_score_data(session,term,course_records):
   """
   This function takes the session,term and student record and extracts the scores and the units for the semester.
   parameters
   -----------
   session: List
            list of courses the student takes 
   term: List
            list of unique term
   course_records: dict
            student information
   return
   -------
   units: List
         list of units 
   scores:
         list of scores
   """
   units = []
   scores = []
   for record in (course_records['courses']):
      if record['term'] == term and record['session'] == session:
         units.append(int(record['unit']))
         scores.append(int(record['score']))
   return (units, scores)


def compute_results(student_records):
   """
   computes the gpa for each semester and also the cgpa based on the fomular here.
   http://primaltutor.com.ng/learn-how-to-calculate-cgpa-in-nigerian-universities/#:~:text=Example%3A%20If%20in%20a%20semester,for%20all%20semesters%20to%20date
   
   return
   -------
   final_result: List
               Computed Student Name, ID, Session, Semester, GPA and CGPA
   
   """
   #get unique semester names
   sessions = get_sessions(student_records)
   semesters = get_semesters(student_records)
   session_total_units, session_total_grade_points =[],[]


   results = list()
   final_result = {}
   final_result["Student Name"] = student_records['name']
   final_result["Student ID"] =  student_records["id"]

   gpa_results ={}
   gpa_results["Student ID"] =  student_records["id"]
   


   #student_id, num_years, num_semesters, total_num_courses, total_units, total_credit_units, cgpa

   
   for session in sessions:
      number_of_sessions = 0
      number_of_semesters = 0
      total_credit_units = 0
      total_units, total_grade_points =[],[]
      results.append(f"Year :{session}")


      for term in semesters:
         """
         compute cgpa for all terms in each session and keeping track of the units $ grades
         """
         
         units, scores = get_score_data(session,term,student_records )
         tu,tgps,gpa = compute_student_gpa(units, scores)
         total_units.append(tu)
         total_grade_points.append(tgps)
         
         results.append(f" Semester: {term}") 
         results.append(f" GPA: {gpa}") 

         number_of_sessions += 1   
         number_of_semesters += 1
         total_credit_units += int(tu)

      results.append(f" total unit: {sum(total_units)}") 
      cgpa = round(sum(total_grade_points) / sum(total_units),2)
      gpa_results['results'] = results
      
      final_result['num_years'] = number_of_sessions
      final_result['num_semesters'] = number_of_semesters
      gpa_results['CGPA'] = cgpa
         

      """
      keeping track of the total unit and grade point outside the term loop to be used for the final year computation
      """
      session_total_units.append(total_units)
      session_total_grade_points.append(total_grade_points)
      
      """
      final year computaion of cgpa with values of each session
      """
   sum_of_all_grades = sum(calculate_sum(session_total_grade_points))
   sum_of_total_units = sum(calculate_sum(session_total_units))


   final_year_cgpa = round((sum_of_all_grades / sum_of_total_units),2)
   
   final_result['total_credit_units'] = sum_of_all_grades
   final_result['total_units'] = sum_of_total_units
   
   final_result["Final_Year_CGPA"] = final_year_cgpa        
      
   return   gpa_results ,final_result
         


if __name__ == "__main__":
   compute_results()

   





