from UtilityFunctions import is_prime
import math
import time

def solution_one(limit):
  primes = []
  i = 1

  while i < math.sqrt(limit):
    i = i + 1
    if is_prime(i) and limit%i == 0:
      primes.append(i)
  return max(primes)

def solution_two(limit):
  i = int(math.sqrt(limit))
  while i > 0:
    if is_prime(i) and limit%i == 0:
      break
    i = i - 1
  return i  

if __name__ == "__main__":
  start_time = time.time()

  limit = 600851475143 
  #print solution_one(limit) # Execution Time: ~[1.2, 1.3] seconds
  print solution_two(limit) # Execution Time: ~[1.1, 1.2] seconds
  print("--- %s seconds ---" % (time.time() - start_time))