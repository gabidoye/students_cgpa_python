from json import loads, dumps
from collections import OrderedDict
import csv

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
    
    # create header row
    header = computed_result[0].keys()

    # write results to CSV file
    with open("results/%s.csv" % file_name , 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for result in computed_result:
            writer.writerow(result)
