import UtilityFunctions as uf
import time

def solution_one():
  primes = uf.sieve_of_erastothenes(1000000)
  new_primes = []
  count = 4
  chars = set('024568')

  for i in primes:
    if i != 2 and i !=5 and any((c in chars) for c in str(i)):
      continue
    new_primes.append(i)
  
  for i in range (4, len(new_primes), 1):
    prime = str(new_primes[i])
    break_flag = False
    for j in range(1, len(prime), 1):
      if not int(uf.circular_shift_string(prime, j)) in new_primes:
        break_flag = True
        break
    if not break_flag:
      count = count + 1
  return count

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[0.335, 0.353] seconds
  print("--- %s seconds ---" % (time.time() - start_time))