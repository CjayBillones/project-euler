from UtilityFunctions import is_prime
from UtilityFunctions import sieve_of_erastothenes
import time

def solution_one():
  result = 0

  for i in range (2, 2000001, 1):
    if is_prime(i):
      result = result + i
  return result

def solution_two():
  return sum(sieve_of_erastothenes(2000000))

if __name__ == "__main__":
  start_time = time.time()

  #print solution_one() # Execution Time: ~[4.42, 4.55] seconds
  print solution_two() # Execution Time: ~[0.55, 0.56] seconds
  print("--- %s seconds ---" % (time.time() - start_time))