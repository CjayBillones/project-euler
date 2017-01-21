def isPrime(n):
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n%2 == 0 or n%3 == 0:
    return False
  i = 5
  while i*i <= n:
    if n%i == 0 or n%(i+2) == 0:
      return False
    i = i + 6
  return True

result = 0

for i in range (2, 2000001, 1):
  if isPrime(i):
    result = result + i

print result