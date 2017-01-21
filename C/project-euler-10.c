#include <stdio.h>

unsigned long long int isPrime(int);

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