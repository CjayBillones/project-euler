import time

def solution_one():
  i = 1

  while True:
    doub = map(int, str(i*2))
    trip = map(int, str(i*3))
    quad = map(int, str(i*4))
    quin = map(int, str(i*5))
    sext = map(int, str(i*6))

    if set(doub) == set(trip) == set(quad) == set(quin) == set(sext):
      return i

    i = i + 1

if __name__ == "__main__":
  start_time = time.time()

  print solution_one() # Execution Time: ~[1.57, 1.59] seconds
  print("--- %s seconds ---" % (time.time() - start_time))