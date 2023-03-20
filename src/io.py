import csv
import pandas as pd


def read_student_file_with_course(student_file, course_file):
    # Read in the student and course files
    students = pd.read_csv(student_file)
    courses = pd.read_csv(course_file)

    # Join the two datasets on the student_id column
    student_courses = pd.merge(students, courses, on='student_id')

    # Create a list of dictionaries with the name, student_id, and list of courses and units for each student
    student_list = []
    for student_id, group in student_courses.groupby('student_id'):
        courses = []
        for i, row in group.iterrows():
            course = {}
            for col in group.columns:
                if col == 'title':
                    course['title'] = row[col]
                elif col == 'unit':
                    course['unit'] = row[col]
                elif col == 'code':
                    course['code'] = row[col]
                elif col == 'score':
                    course['score'] = row[col]
                elif col == 'term':
                    course['term'] = row[col]
                elif col == 'session':
                    course['session'] = row[col]
            courses.append(course)
        student_list.append({
            'Name': group.iloc[0]['name'],
            'student_id': student_id,
            'courses': courses,
        })

    return student_list

