#include <stdio.h>

int divisible(int, int);
int summation(int);

int main(){

  int i;
  int result = 0;

  // Brute Force Method
  // Iterate from 1 to 1000 then add number to sum if divisible by 3 or 5
  for(i = 1; i < 1000; i++){
    if(divisible(i, 3) == 1 || divisible(i,5) == 1)
      result += i;
  }
  printf("%d\n", result);

  // Other Methods
  // Taking advantage of the fact that the sum of n consecutive numbers
  // is n*(n+1)/2
  printf("%d\n", 3*summation(333) + 5*summation(199) - 15*summation(66));
  return 0;
}

int divisible(int dividend, int divisor){
  return (dividend%divisor == 0) ? 1 : 0;
}

int summation(int n){
  return (n * (n+1))/2.0;
}