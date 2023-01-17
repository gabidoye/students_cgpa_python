
from src import gpa
from src.io import read_files
from src.utils import convert_to_dict

student_records = read_files()
student_records = convert_to_dict(student_records)

# print(student_records)

# student_records = [{
#       "name": "James Webb",
#       "id": "APT5005",
#       "courses":[
#          {"title": "English", "unit": 2, "code": "ENG101", "score": 60, "term": "Fall", "session":'2020'},
#          {"title": "Chemistry I", "unit": 4, "code": "CHE101", "score": 70, "term": "Fall", "session":'2021'},
#          {"title": "Maths", "unit": 3, "code": "MTH101", "score": 80, "term": "Spring", "session":'2020'},
#          {"title": "Chemistry II", "unit": 4, "code": "CHE102", "score": 91, "term": "Spring", "session":'2021'}, 
#          {"title": "History", "unit": 2, "code": "HIS102", "score": 40, "term": "Spring", "session":'2020'}
#       ]
#    },
#    {
#       "name": "Ali Hocky",
#       "id": "JTQ3874",
#       "courses":[
#          {"title": "Economics", "unit": 4, "code": "ECO101", "score": 60, "term": "Fall", "session":'2020'},
#          {"title": "English I", "unit": 2, "code": "ENG101", "score": 65, "term": "Fall", "session":'2021'},
#          {"title": "Maths", "unit": 3, "code": "MTH101", "score": 62, "term": "Spring", "session":'2020'},
#          {"title": "Zoology II", "unit": 1, "code": "ZOE102", "score": 51, "term": "Spring", "session":'2021'}, 
#          {"title": "Geology", "unit": 2, "code": "HIS102", "score": 48, "term": "Spring", "session":'2020'}
#       ]
#    }]


if __name__ == "__main__":
   for student in student_records:
      results=gpa.compute_results(student)
      print(results)
      print('\n')




 