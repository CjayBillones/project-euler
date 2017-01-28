from UtilityFunctions import remove_chars_from_string as rcfs
from UtilityFunctions import num_to_words as ntw
import time

def solution_one():
  sum_result = 0

  for i in range (1, 1001, 1):
    sum_result = sum_result + len(rcfs(ntw(i), " -"))
  return sum_result

def solution_two():
  return (3*summation_of_n(333) + 5*summation_of_n(199) - 15*summation_of_n(66))

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[0.007, 0.011] seconds
  print("--- %s seconds ---" % (time.time() - start_time))