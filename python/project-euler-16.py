from UtilityFunctions import conv_str_list_to_int
import time

def solution_one():
  return sum(conv_str_list_to_int(list(str(2**1000))))

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[0.0003, 0.0005] seconds
  print("--- %s seconds ---" % (time.time() - start_time))