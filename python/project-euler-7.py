from PrimalityTest import isPrime
import time

if __name__ == "__main__":
  start_time = time.time()

  count = i = 0

  while count != 10001:
    i = i+1
    if isPrime(i):
      count = count + 1

  print i
  print("--- %s seconds ---" % (time.time() - start_time))