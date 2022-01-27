def sortedSquares(nums):
  ''' Sort array based on absolute value. Since we're going to be squaring the sorted array, only the absolute value is relevant (IE -4^2 and 4^2 = 16)'''
  sortedList = sorted(nums,key = abs)
  # using list comprehension, return a new list wth each element in the sorted array, squared. 
  return [number ** 2 for number in sortedList]

  