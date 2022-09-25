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
   
# Result=[60, 80, 40, 30]
# point=['B','A','D','E']
# print(compute_student_grade(Result, point))

def compute_student_grade_point(grades):
   grade_point_map = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}
   output=[grade_point_map[grade] for grade in grades if grade in grade_point_map.keys()]
   return output


def compute_student_gpa(fall_credit, fall_unit_score, spring_credit, spring_unit_score):
    fall_gpa= round((sum(fall_unit_score) / sum(fall_credit)), 2)
    spring_gpa= round((sum(spring_unit_score) / sum(spring_credit)), 2)
    return fall_gpa, spring_gpa


# print(compute_student_gpa([4, 5], [8, 15], [2,3], [1,2]))


def compute_cgpa(student_record):
    
    cgpa= (student_record['courses'])
    name=student_record['name']
    ID= student_record['id']
    fall_unit=[d['unit'] for d in (student_record['courses']) if d['term']=='Fall'] 
    spring_unit=[d['unit'] for d in (student_record['courses']) if d['term']=='Spring'] 
    fall_scores=[d['score'] for d in (student_record['courses'])if d['term']=='Fall'] 
    spring_scores=[d['score'] for d in (student_record['courses'])if d['term']=='Spring'] 
    fall_grade_scale = compute_student_grade(fall_scores)
   #  print(fall_grade_scale)
    spring_grade_scale = compute_student_grade(spring_scores)
    fall_grade_score = compute_student_grade_point(fall_grade_scale)
    spring_grade_score = compute_student_grade_point(spring_grade_scale)
    fall_grade_point = [a*b for a,b in zip(fall_unit,fall_grade_score)]
    spring_grade_point = [a*b for a,b in zip(spring_unit,spring_grade_score)]
    fall_gpa,spring_gpa= compute_student_gpa(fall_unit,fall_grade_point,spring_unit,spring_grade_point)
    cgpa =round((spring_gpa +fall_gpa)/2,2)   
    return fall_gpa,spring_gpa, name, ID, cgpa
print(compute_cgpa(student_record))







    
    
# print(gpa(students))