#include <stdio.h>

int SumEvenFibonacciBruteForce(int);
int SumEvenFibonacci(int);

int main(){

  printf("%d\n", SumEvenFibonacciBruteForce(4000000));
  printf("%d\n", SumEvenFibonacci(4000000));

  return 0;
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
