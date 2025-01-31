def isPrime(num):
  for i in range(2, num):
    if (num % i == 0):
      return False
  
  return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

prime_numbers = list(filter(lambda x: isPrime(x), numbers))
print(prime_numbers)