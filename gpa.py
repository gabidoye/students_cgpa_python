student_record = {
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

# print(student_record["courses"])

def compute_student_grade(student_record):
   """
   This computes the students grade based on the score the student gets in each course

   Parameters
   -----------
   student_record : Array of scores from the student's dictionary

   Returns
   -------
   array_like
        Array of grades mapped to alphabets A,B,C,D,E,F.

   Example
   --------
   Result=[60, 80, 40, 30]
   grade=['B','A','D','E']

   """
   grade_point_map = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}
   grade=[]
   # grade_points=[grade_point_map[grade] for grade in points if grade in grade_point_map.keys()]
   for score in student_record:
      if score >=70:
         grade.append('A')
      if score  >=60 and score <=69:
         grade.append('B')
      if score >=50 and score <=59:
         grade.append('C')
      if score >=45 and score <=49:
         grade.append('D')
      if score >=40 and score <=44:
         grade.append('E')
      if score <=39 :
         grade.append('F')
   return grade 
   

# print(compute_student_grade(Result, point))

def compute_student_grade_point(grades):
   """
   It maps the grades returned by function compute_student_grade to the point for the 
   obtained grade.  {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}

   Parameters
   -----------
   grades : Array of grade 

   Returns
   -------
   array_like ,  Array of points mapped to alphabets 5,4,3,2,1, 0.

   Example
   --------
   grade=[60, 80, 40,]
   point=[4,5,2]

   """
   grade_point_map = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}
   point=[grade_point_map[grade] for grade in grades if grade in grade_point_map.keys()]
   return point


def compute_student_gpa(fall_credit, fall_unit_score, spring_credit, spring_unit_score):
   """
   Use the score obtained in each semester(fall or spring) and the course unit credit to 
   calculates the gpa for the respective semester.

   Parameters
   -----------
   fall_credit : Array of int 
   fall_unit_score : Array of int
   spring_credit : array of int
   spring_unit_score : array of int

   Returns
   -------
   Tuple of two float values

   Example
   --------
   compute_student_gpa([4, 5], [8, 15], [2,3], [1,2])) # (2.56, 0.6)

   """
   fall_gpa= round((sum(fall_unit_score) / sum(fall_credit)), 2)
   spring_gpa= round((sum(spring_unit_score) / sum(spring_credit)), 2)
   return fall_gpa, spring_gpa



def output_box():
   """
   prints a hallow box for diplaying output

   Parameters
   ----------
   row > int
   columns > int

   """
   rows = int(5)
   columns = int(10)
   for i in range(0, rows):
      for j in range(0, columns):
         if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
               print('#',  end = '  ')
         else:
               print(' ', end = '  ')
      print()

# output_box()


def compute_cgpa(student_record):
   """
   First computes the student's gpa per semester then finds an average of the 
   two semester.

   Parameters
   ----------
   fall_gpa > float
   spring_gpa > float

   Returns
   --------
   Float
   
   """
    
   cgpa= (student_record['courses'])
   name=student_record['name']
   ID= student_record['id']
   fall_unit=[d['unit'] for d in (student_record['courses']) if d['term']=='Fall'] 
   spring_unit=[d['unit'] for d in (student_record['courses']) if d['term']=='Spring'] 
   fall_scores=[d['score'] for d in (student_record['courses'])if d['term']=='Fall'] 
   spring_scores=[d['score'] for d in (student_record['courses'])if d['term']=='Spring'] 


   fall_grade_scale = compute_student_grade(fall_scores)
   spring_grade_scale = compute_student_grade(spring_scores)

   fall_grade_score = compute_student_grade_point(fall_grade_scale)
   spring_grade_score = compute_student_grade_point(spring_grade_scale)

   fall_grade_point = [a*b for a,b in zip(fall_unit,fall_grade_score)]
   spring_grade_point = [a*b for a,b in zip(spring_unit,spring_grade_score)]

   fall_gpa,spring_gpa= compute_student_gpa(fall_unit,fall_grade_point,spring_unit,spring_grade_point)
   
   cgpa =round((spring_gpa +fall_gpa)/2,2)  

   return name, ID, cgpa, fall_gpa,spring_gpa

# print(compute_cgpa(student_record))

if __name__ == "__main__":
   gpa = compute_cgpa(student_record)
   stmt=''

   print (stmt.center(30, '#'))   
   print("Name : % 1s, ID : % 1s" %(gpa[0],gpa[1])) 
   print("CGPA: ", gpa[2])
   print("Fall : % 1.2f, Spring : % 1.2f" %(gpa[3],gpa[4]))
   print (stmt.center(30, '#'))  












    
    
# print(gpa(students))