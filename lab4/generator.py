class numSquares:
  def __init__(self, N):
    self.start = 1
    self.end = N

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.start < self.end:
      x = self.start * self.start
      self.start += 1
      return x
    else:
      raise StopIteration
    


myGenerator = numSquares(5)
myGeneratorIterator = iter(myGenerator)

print(myGeneratorIterator.__next__())
print(myGeneratorIterator.__next__())
print(myGeneratorIterator.__next__())
print(myGeneratorIterator.__next__())
print(myGeneratorIterator.__next__())
print(myGeneratorIterator.__next__())


