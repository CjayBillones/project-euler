from UtilityFunctions import conv_str_list_to_int
import time
import math

def solution_one():
  return sum(conv_str_list_to_int(str(math.factorial(100))))

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[0.00012, 0.00032] seconds
  print("--- %s seconds ---" % (time.time() - start_time))