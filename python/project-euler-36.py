from UtilityFunctions import dec_to_bin
from UtilityFunctions import isPalindrome
import time

def solution_one():
  
  result = 0
  
  for i in range(1, 1000000, 1):
    if isPalindrome(i) and isPalindrome(dec_to_bin(i)):
      result = result + i

  return result

def solution_two():
  
  result = 0
  
  for i in range(1, 1000000, 2):
    if isPalindrome(i) and isPalindrome(dec_to_bin(i)):
      result = result + i

  return result

if __name__ == "__main__":
  start_time = time.time()

  #print solution_one() # Execution Time: ~[0.49, 0.58] seconds
  print solution_two() # Execution Time: ~[0.259, 0.266] seconds
  print("--- %s seconds ---" % (time.time() - start_time))