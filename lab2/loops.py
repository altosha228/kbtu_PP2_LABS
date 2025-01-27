i = 0
while i < 6:
  if i == 4:
    break
  else:
    continue


#For loops are used for iterating over a collection(list, tuple, set, dictionary, string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)