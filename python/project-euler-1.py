from Summation import summation_of_n
import time

def divisible(dividend, divisor):
  return dividend%divisor == 0

def solution_one():
  sum_result = 0

  for i in range (1, 1000, 1):
    if divisible(i, 3) or divisible(i, 5):
      sum_result = sum_result + i
  return sum_result

def solution_two():
  return (3*summation_of_n(333) + 5*summation_of_n(199) - 15*summation_of_n(66))

if __name__ == "__main__":
  start_time = time.time()

  #print solution_one() # Execution Time: ~[0.000247, 0.00056] seconds
  print solution_two() # Execution Time: ~[0.000017, 0.000037] seconds
  print("--- %s seconds ---" % (time.time() - start_time))