def calculate_sum(lst):
   """
   This function sums nested list.
   parameters
   -----------
   list 
   return
   -------
   array of values
   """
      
   return list(map(sum, zip(*lst)))