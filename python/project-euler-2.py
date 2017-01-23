import time

def solution_one(limit):
  result = nth_term = 0
  first_term = second_term = 1

  while nth_term < limit:
    nth_term = first_term + second_term
    first_term = second_term
    second_term = nth_term

    if nth_term%2 == 0:
      result = result + nth_term

  return result

def solution_two(limit):
  result = nth_term = 0
  first_term = second_term = 1

  while nth_term < limit:
    nth_term = first_term + second_term
    first_term = second_term + nth_term
    second_term = nth_term + first_term

    if nth_term < limit:
      result = result + nth_term

  return result

if __name__ == "__main__":
  start_time = time.time()
  #print solution_one(4000000) # Execution Time: ~[0.000024, 0.000055] seconds
  print solution_two(4000000) # Execution Time: ~[0.000019, 0.000055] seconds
  print("--- %s seconds ---" % (time.time() - start_time))