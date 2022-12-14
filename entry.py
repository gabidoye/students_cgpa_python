import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/gabidoye/Documents/data_Engineering/students_cgpa_python/src')
import gpa 




student_records = {
      "name": "James Webb",
      "id": "APT5005",
      "courses":[
         {"title": "English", "unit": 2, "code": "ENG101", "score": 60, "term": "Fall", "session":'2020'},
         {"title": "Chemistry I", "unit": 4, "code": "CHE101", "score": 70, "term": "Fall", "session":'2021'},
         {"title": "Maths", "unit": 3, "code": "MTH101", "score": 80, "term": "Spring", "session":'2020'},
         {"title": "Chemistry II", "unit": 4, "code": "CHE102", "score": 91, "term": "Spring", "session":'2021'}, 
         {"title": "History", "unit": 2, "code": "HIS102", "score": 40, "term": "Spring", "session":'2020'}
      ]
   }


if __name__ == "__main__":
    results=gpa.compute_results(student_records)
    print(results)




 