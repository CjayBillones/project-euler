from UtilityFunctions import is_prime
import time

if __name__ == "__main__":
  start_time = time.time()

  result = 0

  for i in range (2, 2000001, 1):
    if is_prime(i):
      result = result + i

  print result
  print("--- %s seconds ---" % (time.time() - start_time))