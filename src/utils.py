from json import loads, dumps
from collections import OrderedDict

def calculate_sum(lst):
   """
   This function sums nested list.
   Parameters
   -----------
   lst: List
       A list of values to be summed.
       
   Returns
   --------
   total: int
         sum of all input values
   """
      
   total = list(map(sum, zip(*lst)))
   return total





def convert_to_dict(input_ordered_dict):
    """
   This function converts the read student_records files and the course_records file
   into the program required format.
   Parameters
   -----------
   lst: List
       A list of all the student information.
       
   Returns
   --------
   student_information: list
         all student to compute gpa for
   """
    return loads(dumps(input_ordered_dict))