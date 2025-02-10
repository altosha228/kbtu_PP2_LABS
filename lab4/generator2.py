class myGenerator:
  def __init__(self, N):
    self.start = 0
    self.end = N

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.start < self.end:
      x = self.start
      self.start += 1
      return x
    else:
      raise StopIteration

myClass = myGenerator(10)
myIter = iter(myClass)

even_nums = [str(item) for item in myIter if item % 2 == 0]

print(", ".join(even_nums))