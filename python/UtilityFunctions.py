# Checks if a number n is divisible by k
def divisible(n, k):
  return n%k == 0

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

# Returns a list of all prime numbers less than or equal to n
def sieve_of_erastothenes(n):
  prime = [True for i in range(n+1)]
  
  p = 2
  while(p*p <= n): 
      if (prime[p]):
        for i in range(p * 2, n+1, p):
            prime[i] = False
      p+=1

  primes = [p for p in range(2, n) if prime[p]]
  return primes

# Checks if input is a palindrome
def isPalindrome(n):
  return str(n) == str(n)[::-1]  

# Converts list of string numbers into list of integers
def conv_str_list_to_int(str_list):
  num_list = [int(i) for i in str_list]
  return num_list

# Returns greatest common factor/denominator of a and b
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

# Returns the least common multiple of a and b
def lcm(a, b):
  return (a*b) / gcd(a,b)

# Returns the least common multiple of input numbers
def lcm_multiple(args):
  return reduce(lcm, args)

# Returns the binary representation of a decimal
def dec_to_bin(n):
  return "{0:b}".format(n)

# Shifts a string by n places
def circular_shift_string(string, n):
  return string[n:] + string[:n]

def remove_chars_from_string(string, chars):
  sc = set(chars)
  return ''.join([c for c in string if c not in sc])

def num_to_words(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + num_to_words(num % 100)

    if (num < m):
        if num % k == 0: return num_to_words(num // k) + ' thousand'
        else: return num_to_words(num // k) + ' thousand, ' + num_to_words(num % k)

    if (num < b):
        if (num % m) == 0: return num_to_words(num // m) + ' million'
        else: return num_to_words(num // m) + ' million, ' + num_to_words(num % m)

    if (num < t):
        if (num % b) == 0: return num_to_words(num // b) + ' billion'
        else: return num_to_words(num // b) + ' billion, ' + num_to_words(num % b)

    if (num % t == 0): return num_to_words(num // t) + ' trillion'
    else: return num_to_words(num // t) + ' trillion, ' + num_to_words(num % t)

    raise AssertionError('num is too large: %s' % str(num))