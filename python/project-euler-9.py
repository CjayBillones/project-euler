import time

def PythagoreanTripletSum():
  pyth_triplet_sum = 1000
  a = 1

  while(a <= pyth_triplet_sum/3):
    b = a + 1
    while(b <= pyth_triplet_sum/2):
      c = pyth_triplet_sum - a - b
      if(a*a + b*b == c*c):
        return a*b*c  
      b = b + 1
    a = a + 1

if __name__ == "__main__":
  start_time = time.time()
  print PythagoreanTripletSum()
  print("--- %s seconds ---" % (time.time() - start_time))