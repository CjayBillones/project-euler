#include <stdio.h>
#include "PrimalityTest.h"

int main(){
  unsigned long long int sum = 0;
  int i;

  for(i = 1; i < 2000000; i++){
    if(isPrime(i) == 1)
      sum = sum + i;
  }
  printf("%llu\n", sum);
  return 0;
}