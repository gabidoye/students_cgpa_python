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

GRADE_POINT_MAP = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}

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
   units=[]
   scores=[]
   for record in (course_records['courses']):
      if record['term'] == term:
         units.append(record['unit'])
         scores.append(record['score'])
   return (units, scores)
   
def get_semesters(course_records):
   semesters=set()
   for d in (course_records['courses']):
      for key, value in d.items():
         if key=='term':
               semesters.add(value) 
   return list(semesters)

def compute_results(student_records):
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
   results['CGPA']= cgpa

   return results

# print(compute_results(student_records))




             
        
#     # print(semester)        
#     # return len(semester) # courses_fall, courses_spring ,len(semester)

# # print(countsems(student_record))

# def compute_cgpa(student_record):
#    """
#    First computes the student's gpa per semester then finds an average of the 
#    two semester.

#    Parameters
#    ----------
#    fall_gpa > float
#    spring_gpa > float

#    Returns
#    --------
#    Float
   
#    # return name, ID, cgpa, fall_gpa,spring_gpa


# if __name__ == "__main__":
#    # REVIEW COMMENTS
#       # I moved the data here
#    # END REVIEW COMMENTS
#    student_record = {
#       "name": "James Webb",
#       "id": "APT5005",
#       "courses":[
#          {"title": "English", "unit": 2, "code": "ENG101", "score": 60, "term": "Fall"},
#          {"title": "Chemistry I", "unit": 4, "code": "CHE101", "score": 70, "term": "Fall"},
#          {"title": "Maths", "unit": 3, "code": "MTH101", "score": 80, "term": "Spring"},
#          {"title": "Chemistry II", "unit": 4, "code": "CHE102", "score": 91, "term": "Spring"}, 
#          {"title": "History", "unit": 2, "code": "HIS102", "score": 40, "term": "Spring"}
#       ]
#    }

#    # gpa = compute_cgpa(student_record)
#    # stmt=''

#    # print (stmt.center(30, '#'))   # do we really need this centering?
#    # print("Name : % 1s, ID : % 1s" %(gpa[0], gpa[1])) 
   
#    # # REVIEW COMMENTS
#    #    # we may simplify the output by printing the per semester gpa each on a separate line 
#    #    # then followed by the CGPA like: 
#    # # END REVIEW COMMENTS
#    # print("Fall : % 1.2f" %gpa[3])
#    # print("Spring : % 1.2f" %gpa[4])
#    # print("CGPA: ", gpa[2])
#    # print (stmt.center(30, '#'))  


