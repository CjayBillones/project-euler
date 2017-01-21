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