print(10 == 9)
print(2 > 1)


a = 33
b = 40

if a > b:
  print("a is greater than b")
else:
  print("a is less than b")


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


def function():
  return False

print(function())