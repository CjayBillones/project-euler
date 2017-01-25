import time

def solution_one():
  first_term = second_term = 1
  nth_term = 0
  index = 2

  while len(str(nth_term)) < 1000:
    nth_term = first_term + second_term
    first_term = second_term 
    second_term = nth_term
    index = index + 1
  return index

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[0.033, 0.038] seconds
  print("--- %s seconds ---" % (time.time() - start_time))