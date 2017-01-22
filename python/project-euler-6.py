from Summation import summation_of_n_squared
from Summation import summation_of_n
import time

start_time = time.time()

n = 100

sum_n = summation_of_n(n)
sum_n_squared = summation_of_n_squared(n)

print (sum_n**2) - sum_n_squared
print("--- %s seconds ---" % (time.time() - start_time))