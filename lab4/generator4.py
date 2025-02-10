class numSquares:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.start < self.end:
      x = self.start * self.start
      self.start += 1
      return x
    else:
      raise StopIteration
    


myGenerator = numSquares(5, 9)
myGeneratorIterator = iter(myGenerator)

for num in myGeneratorIterator:
  print(num)


