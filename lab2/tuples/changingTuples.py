a = ("banana", "TupleItem", 5)
b = []
b = list(a)
b[0] = "Not Banana"
a = tuple(b)
print(a) 