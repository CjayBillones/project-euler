from UtilityFunctions import lcm_multiple
import time

def solution_one():
  return lcm_multiple(range(1,21))

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[0.00013, 0.00037] seconds

  print "--- %s seconds ---" % (time.time() - start_time)