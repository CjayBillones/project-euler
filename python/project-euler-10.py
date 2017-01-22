from PrimalityTest import isPrime
import time

start_time = time.time()

result = 0

for i in range (2, 2000001, 1):
  if isPrime(i):
    result = result + i

print result
print("--- %s seconds ---" % (time.time() - start_time))