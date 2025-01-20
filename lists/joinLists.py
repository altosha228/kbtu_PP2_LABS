list = [1, 2, 3]
list2 = ["a", "b", "c"]

list3 = list + list2
print(list3)

list3alt = list.copy()
list3alt.extend(list2)
print(list3alt)