from UtilityFunctions import is_palindrome
import time

def solution_one():
  palindromes = []

  for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
      product = i*j
      if is_palindrome(product):
        palindromes.append(product)

  return max(palindromes)

def solution_two():
  largest_palindrome = 0

  for i in range(100, 1000, 1):
    j = i
    while j < 1000:
      product = i*j
      if is_palindrome(product) and product > largest_palindrome:
        largest_palindrome = product
      j = j+1

  return largest_palindrome

def solution_three():
  largest_palindrome = 0
  i = 999
  while i >= 100:
    j = i
    while j >= 100:
      product = i*j
      if product <= largest_palindrome:
        break
      if is_palindrome(product):
        largest_palindrome = product
      j = j - 1
    i = i - 1

  return largest_palindrome


if __name__ == "__main__":
  start_time = time.time()

  #print solution_one() # Execution Time: ~[0.393, 0.402] seconds
  #print solution_two()  # Execution Time: ~[0.208, 0.215] seconds
  print solution_three() # Execution Time: ~[0.004, 0.008] seconds

  print "--- %s seconds ---" % (time.time() - start_time)