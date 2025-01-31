class Point():

  
  x = 0
  y = 0
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def show(self):
    print(f"{self.x}, {self.y}")
  def move(self, x, y):
    self.x = x
    self.y = y
  def dist(self, otherX, otherY):
    dist = 0
    distX = self.x - otherX
    distY = self.y - otherY
    dist = pow(pow(distX, 2) + pow(distY, 2), 0.5)
    print(f"this point is {dist:.2f} from other point")
  
p1 = Point(1, 1)
p2 = Point(3, 4)

p1.show()
p2.show()
p1.dist(p2.x, p2.y)