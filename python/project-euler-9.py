import time

start_time = time.time()

pyth_triplet_sum = 1000
a = 1

while(a <= pyth_triplet_sum/3):
  b = a + 1
  while(b <= pyth_triplet_sum/2):
    c = pyth_triplet_sum - a - b
    if(a*a + b*b == c*c):
      print a*b*c
    b = b + 1
  a = a + 1

print("--- %s seconds ---" % (time.time() - start_time))