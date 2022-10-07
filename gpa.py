
GRADE_POINT_MAP = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0} #constant used for mapping score and grades

def compute_student_grade(scores):
   """
   This computes the students grade and point based on the score the student gets in each course
   Parameters
   -----------
   student_record : Array of scores from the student's dictionary
   Returns
   -------
   Array of grades mapped to alphabets (A,B,C,D,E,F) and Array of points mapped to values of constant dictionary[5,4,3,2,1,0]
   Example
   --------
   Result=[60, 80, 40, 30]
   grade=['B','A','D','E']
   point =[4,5,2,1]
   """
   # REVIEW COMMENTS\
      # I'll suggest to move this map to the top of the file as a constant 
      # following python convention
      # skim this to get an idea of how you name constants 
      # https://realpython.com/python-constants/
   # END REVIEW COMMENTS
   grade=[]
   points=[]
   for score in scores:
      if score >=70:
         grade.append('A')
         points.append(GRADE_POINT_MAP['A'])
      if score  >=60 and score <=69:
         grade.append('B')
         points.append(GRADE_POINT_MAP['B'])
      if score >=50 and score <=59:
         grade.append('C')
         points.append(GRADE_POINT_MAP['C'])
      if score >=45 and score <=49:
         grade.append('D')
         points.append(GRADE_POINT_MAP['D'])
      if score >=40 and score <=44:
         grade.append('E')
         points.append(GRADE_POINT_MAP['E'])
      if score <=39 :
         grade.append('F')
         points.append(GRADE_POINT_MAP['F'])
   return grade, points

# print(compute_student_grade([50,60,84]))
   

# REVIEW COMMENTS
   # this function is not efficient
   # it should take a single semester data at a time 
   # the calling function should use a loop to call for each semester in turn
# END REVIEW COMMENTS
def compute_student_gpa(units, scores):
   """
   Use the score obtained in each semester(fall or spring) and the course unit credit to calculates the gpa for the respective semester.
   Parameters
   -----------
   units : Array of int 
   scores : Array of int
   Returns
   -------
   Tuple of two float values
   Example
   --------
   compute_student_gpa([4, 5], [8, 15], [2,3], [1,2])) # (2.56, 0.6)
   """
   grade,points=compute_student_grade(scores)
   total_unit=sum(units)
   total_grade_point = sum([a*b for a,b in zip(units,points)])# 11 [a,a,e][5,5,1][3,4,2]
   gpa= round((total_grade_point / total_unit), 2)

   return total_unit,total_grade_point,gpa

def get_score_data(term,course_records):
   """
   This function takes the term and student record and extracts the scores and the units for the semester.
   parameters
   -----------
   string and dict
   return
   -------
   array of units and scores
   """
   units=[]
   scores=[]
   for record in (course_records['courses']):
      if record['term'] == term:
         units.append(record['unit'])
         scores.append(record['score'])
   return (units, scores)
   
def get_semesters(course_records):
   """
   This function retrieve the unique semesters from the student record.
   parameters
   -----------
   dict
   return
   -------
   array of semesters
   """
   semesters=set()
   for d in (course_records['courses']):
      for key, value in d.items():
         if key=='term':
               semesters.add(value) 
   return list(semesters)

def compute_results(student_records):
   """
   computes the gpa for each semester and also the cgpa based on the fomular here.
   http://primaltutor.com.ng/learn-how-to-calculate-cgpa-in-nigerian-universities/#:~:text=Example%3A%20If%20in%20a%20semester,for%20all%20semesters%20to%20date
   
   return
   -------
   array -total_units, total_grade_points
   dictionary - cgpa
   """
   #get unique semester names
   semesters= get_semesters(student_records)
   total_units, total_grade_points =[],[]
   results = {}
   for term in semesters:
      units, scores =get_score_data(term,student_records )
      tu,tgps,gpa=compute_student_gpa(units, scores)
      total_units.append(tu)
      total_grade_points.append(tgps)
      results[term]=gpa

   cgpa = round(sum(total_grade_points) / sum(total_units),2)
   name=student_records['name']
   ID= student_records['id']
   results['CGPA']= cgpa

   return name, ID, results

# print(compute_results(student_records))


if __name__ == "__main__":

   student_records = {
      "name": "James Webb",
      "id": "APT5005",
      "courses":[
         {"title": "English", "unit": 2, "code": "ENG101", "score": 60, "term": "Fall"},
         {"title": "Chemistry I", "unit": 4, "code": "CHE101", "score": 70, "term": "Fall"},
         {"title": "Maths", "unit": 3, "code": "MTH101", "score": 80, "term": "Spring"},
         {"title": "Chemistry II", "unit": 4, "code": "CHE102", "score": 91, "term": "Spring"}, 
         {"title": "History", "unit": 2, "code": "HIS102", "score": 40, "term": "Spring"}
      ]
   }

   results=compute_results(student_records)
   # print(results)
 





