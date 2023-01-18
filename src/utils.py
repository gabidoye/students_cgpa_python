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



def write_result(computed_result, file_name):
    """
   This function writes result to file
   Parameters
   -----------
   lst: List
       A list of all the student computed results.
   str: file name
       
   Returns
   --------
   None
   """
    with open("data/%s.txt" % file_name , 'w') as f:
        for result in computed_result:
            for key, value in result.items():
                f.write('%s:%s\n' % (key, value))