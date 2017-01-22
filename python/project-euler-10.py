from PrimalityTest import isPrime

result = 0

for i in range (2, 2000001, 1):
  if isPrime(i):
    result = result + i

print result