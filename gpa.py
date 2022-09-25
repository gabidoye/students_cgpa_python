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

def compute_student_grade(student_record,points):
   grade_point_map = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}
   grade=[]
   grade_points=[grade_point_map[grade] for grade in points if grade in grade_point_map.keys()]
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
   return grade ,grade_points  
   
Result=[60, 80, 40, 30]
point=['B','A','D','E']
print(compute_student_grade(Result, point))


def compute_student_grade_point_average(unit_credit, unit_score):
   sum_units= sum(unit_credit)
   sum_score= sum(unit_score)
   return round((sum_score / sum_units), 2)

# # print(compute_student_grade_point_average([4, 5], [8, 15]))

# def compute_student_gpa(student_record):
    
#     cgpa= (student_record['courses'])
#     unit=[d['Unit'] for d in (student_record['courses'])] 
#     student_scores=[d['score'] for d in (student_record['courses'])] 
#     grade_scale = compute_student_grade(student_scores)
#     grade_score = compute_student_grade_point(grade_scale)
#     grade_point = [a*b for a,b in zip(unit,grade_score)]
#     grade_point_avg= compute_student_grade_point_average(unit,grade_point)
       
#     return grade_point_avg
# print(compute_student_gpa(students))






    
    
# print(gpa(students))