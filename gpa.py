students = {
   "name":"y",
   "studentid":"z",
   "courses":[
      {
         "Coursetitle":"English",
         "Unit":2,
         "CourseCode":"ENG",
         "score":60
      },
      {
         "Coursetitle":"Maths",
         "Unit":3,
         "CourseCode":"MAT",
         "score":80
      }
   ]
}

# print(students["courses"])

def compute_student_grade(student_scores):
   grade=[]
   for score in student_scores:
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

# Result=[60, 80, 40, 30]
# print(compute_student_grade(Result))

def compute_student_grade_point(student_grades):
   points=[]
   for grade in student_grades:
      if grade == 'A':
         points.append(5)
      if grade == 'B':
         points.append(4)
      if grade == 'C':
         points.append(3)
      if grade == 'D':
         points.append(2)
      if grade == 'E':
         points.append(1)
      if grade == 'F':
         points.append(0)
   return points

# print(compute_student_grade_point(['B', 'A']))

def compute_student_grade_point_average(unit_credit, unit_score):
   sum_units= sum(unit_credit)
   sum_score= sum(unit_score)
   return round((sum_score / sum_units), 2)

# print(compute_student_grade_point_average([4, 5], [8, 15]))

def compute_student_gpa(student_record):
    
    cgpa= (student_record['courses'])
    unit=[d['Unit'] for d in (student_record['courses'])] 
    student_scores=[d['score'] for d in (student_record['courses'])] 
    grade_scale = compute_student_grade(student_scores)
    grade_score = compute_student_grade_point(grade_scale)
    grade_point = [a*b for a,b in zip(unit,grade_score)]
    grade_point_avg= compute_student_grade_point_average(unit,grade_point)
       
    return grade_point_avg
print(compute_student_gpa(students))






    
    
# print(gpa(students))