import itertools

def stringPermutations(string):
  permutations = [''.join(p) for p in itertools.permutations(string)]
  return permutations
  
userString = input()
print(stringPermutations(userString))