list = [2, 3, 4, 5, 3, 4, 2, 4]

def filterUnique(list):
  newList = []
  for item in list:
    if item in list and item not in newList:
      newList.append(item)
      continue
  return newList

listUnique = filterUnique(list)
print(listUnique)
