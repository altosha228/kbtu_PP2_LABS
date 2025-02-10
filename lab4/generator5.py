class numSquares:
  def __init__(self, N):
    self.start = N
    self.end = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.start > self.end:
      x = self.start
      self.start -= 1
      return x
    else:
      raise StopIteration
    


myGenerator = numSquares(5)
myGeneratorIterator = iter(myGenerator)

nums = [str(num) for num in myGeneratorIterator]
print(", ".join(nums))
  




