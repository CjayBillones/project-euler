from PrimalityTest import isPrime

count = i = 0

while count != 10001:
  i = i+1
  if isPrime(i):
    count = count + 1

print i