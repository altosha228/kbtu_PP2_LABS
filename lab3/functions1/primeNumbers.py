def isPrime(num):
  i = 2
  while(i < num):
    if(num % i == 0):
      return False
    else:
      i = i + 1
      continue
  return True

def getPrimes(numList):
  primes = [item for item in numList if isPrime(item)]
  return primes
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(getPrimes(nums))