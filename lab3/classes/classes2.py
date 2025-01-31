class Shape():
  area = 0
  def getArea(self):
    print(self.area)

class Square(Shape):
  side = 0
  def __init__(self, side):
    super().__init__()
    self.side = side
  
  def calculateArea(self):
    self.area = self.side * self.side

obj = Square(4)
obj.getArea()
obj.calculateArea()
obj.getArea()


class Rectangle(Shape):
  length = 0
  width = 0
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width
  def calculateArea(self):
    self.area = self.length * self.width


