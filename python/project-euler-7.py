from PrimalityTest import isPrime
import time

def solution_one():
  count = i = 0

  while count != 10001:
    i = i+1
    if isPrime(i):
      count = count + 1

  return i

def solution_two():
  count = i = 1

  while count != 10001:
    i = i+2
    if isPrime(i):
      count = count + 1

  return i

if __name__ == "__main__":
  start_time = time.time()

  #print solution_one() # Execution Time: ~[0.086385, 0.092358] seconds
  print solution_two() #Execution Time: ~[0.076524, 0.082660] seconds

  print("--- %s seconds ---" % (time.time() - start_time))