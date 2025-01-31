class myClass:
  string = "Initial string"
  def getString(self):
    str = input()
    return str
  def printString(self):
    print(self.string.upper())

obj = myClass()
print(obj.string)
obj.string = obj.getString()
obj.printString()