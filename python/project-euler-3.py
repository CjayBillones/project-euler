from PrimalityTest import isPrime
import math
import time

start_time = time.time()

limit = 600851475143

primes = []
i = 1

while i < math.sqrt(limit):
  i = i + 1
  if isPrime(i) and limit%i == 0:
    primes.append(i)

print max(primes)
print("--- %s seconds ---" % (time.time() - start_time))