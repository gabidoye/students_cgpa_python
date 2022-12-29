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