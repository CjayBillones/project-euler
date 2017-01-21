#include <stdio.h>
#include "PrimalityTest.h"

int main(int argc, char const *argv[]){
  int count = 0;
  int i = 0;

  while(count != 10001){
    i++;
    if(isPrime(i) == 1)
      count++;
  }
  printf("%d\n", i);
  return 0;
}