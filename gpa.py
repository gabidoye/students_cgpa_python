GRADE_POINT_MAP = {'A': 5, 'B': 4, 'C':3, 'D':2, 'E':1, 'F':0}

def compute_student_grade(student_record):
   """
   This computes the students grade and point based on the score the student gets in each course

   Parameters
   -----------
   student_record : Array of scores from the student's dictionary

   Returns
   -------
   array_like
        Array of grades mapped to alphabets A,B,C,D,E,F.
        Array of points mapped to values of constant dictionary[5,4,3,2,1,0]

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
   for score in student_record:
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



def countsems(s):

    semester=set()
    fall_unit_credit=[]
    spring_unit_credit=[]
    score_fall=[]
    score_spring=[]
    # courses_spring=set()
    courses_spring={}
    for d in (student_record['courses']):
        # print(d['term'])
        for key, value in d.items():
            if key=='term':
                semester.add(value) 
    # print(semester)
    
    for s in semester:
        for d in (student_record['courses']):
            if s == d['term'] and s=='Fall':
                fall_unit_credit.append(d['unit'])
                score_fall.append(d['score'])
            
            if s == d['term'] and s=='Spring':
                # print(d)
                spring_unit_credit.append(d['unit'])
                score_spring.append(d['score'])
                # grade
                
    print(spring_unit_credit, score_spring)
    print("######")
    print(fall_unit_credit, score_fall)
                
        
    # print(semester)        
    # return len(semester) # courses_fall, courses_spring ,len(semester)

# print(countsems(student_record))

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
   # REVIEW COMMENTS
      # the approach here might work right now, but I don't see this scaling really well
      # think of a situation where you have 3 semester or the requirement expands to multiple sessions
      # are you gonna end up with duplicating the following lines for sessions too?
      # I'm expecting an approach that allows where 
      #  given a student record, 
      #  first you determine how many unique semesters are there in the data
      #  write a loop that extracts all courses for each of the semester
      #     compute and track the gpa and other gpa quantities for the semester 
      #     e.g. the total units and grade points (i.e. total of score grade * course unit) for the semester
      #  write another loop that computes the total units across semesters and total grade points across semesters
      #  and use these two quantity to compute the cumulative gpa
      #  this function could either add a 2 new entries to the student record argument e.g. 
      #     student_record['gpa'] = [('Fall', 4.5), ('Spring', 3.6)]
      #     student_record['cgpa'] = 3.9
      #  or return a new dictionary with a structure like so: {'id':'GPY2343', 'gpa':[{'Fall':4.5}, {'Spring': 3.6}], 'cgpa': 3.9}
   # END REVIEW COMMENTS
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
   
   # REVIEW COMMENTS
      # this is not the correct way to compute CGPA
      # the correct formula is described in the link below
      # http://primaltutor.com.ng/learn-how-to-calculate-cgpa-in-nigerian-universities/#:~:text=Example%3A%20If%20in%20a%20semester,for%20all%20semesters%20to%20date.
      # refer to my comments above
   # END REVIEW COMMENTS
   cgpa =round((spring_gpa +fall_gpa)/2,2)  


   return name, ID, cgpa, fall_gpa,spring_gpa


if __name__ == "__main__":
   # REVIEW COMMENTS
      # I moved the data here
   # END REVIEW COMMENTS
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

   gpa = compute_cgpa(student_record)
   stmt=''

   print (stmt.center(30, '#'))   # do we really need this centering?
   print("Name : % 1s, ID : % 1s" %(gpa[0], gpa[1])) 
   
   # REVIEW COMMENTS
      # we may simplify the output by printing the per semester gpa each on a separate line 
      # then followed by the CGPA like: 
   # END REVIEW COMMENTS
   print("Fall : % 1.2f" %gpa[3])
   print("Spring : % 1.2f" %gpa[4])
   print("CGPA: ", gpa[2])
   print (stmt.center(30, '#'))  


