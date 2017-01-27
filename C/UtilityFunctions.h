unsigned long long int isPrime(int n){
  
  int i;

  if(n <= 1)
    return 0;
  else if(n <= 3)
    return 1;
  else if(n%2 == 0 || n%3 == 0)
    return 0;

  i = 5;
  while(i*i <= n){
    if(n%i == 0 || n%(i+2) == 0)
      return 0;
    i = i + 6;
  }

  return 1;
}

int divisible(int dividend, int divisor){
  return (dividend%divisor == 0) ? 1 : 0;
}

int summation(int n){
  return (n * (n+1))/2.0;
}

// Brute Force Method
// Get all Fibonacci numbers and add to sum if the nth term is even
int SumEvenFibonacciBruteForce(int limit){
  int sum = 0;
  int first_term = 1;
  int second_term = 1;
  int nth_term = 0;

  while(nth_term < limit){
    nth_term = first_term + second_term;
    first_term = second_term;
    second_term = nth_term;

    if(nth_term % 2 == 0)
      sum = sum + nth_term;
  }

  return sum;
}

// Removes checking of nth term if even
// Took advantage of the fact that even numbers
// appear every multiple of 3 term
int SumEvenFibonacci(int limit){
  int sum = 0;
  int first_term = 1;
  int second_term = 1;
  int nth_term = 0;

  while(nth_term < limit){
    nth_term = first_term + second_term;
    first_term = second_term + nth_term;
    second_term = nth_term + first_term;
    
    if(nth_term < limit)
      sum = sum + nth_term;
  }
  return sum;
}