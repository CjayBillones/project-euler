# Computes the summation of N consecutive natural numbers
def summation_of_n(n):
  return n*(n+1)/2

# Computes the summation of the squares of N consecutive natural numbers
def summation_of_n_squared(n):
  return n*(n+1)*(2*n+1)/6

# Checks if a number is prime
def is_prime(n):
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

# Checks if input is a palindrome
def isPalindrome(n):
  return str(n) == str(n)[::-1]  

# Converts list of string numbers into list of integers
def conv_str_list_to_int(str_list):
  num_list = [int(i) for i in str_list]
  return num_list