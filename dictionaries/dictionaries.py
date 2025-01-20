thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict.keys())
print(thisdict.values())

print(thisdict.get("brand"))

thisdict.update({"brand" : "Wolksvagen"})
thisdict.update({"probeg" : 20000})
thisdict.pop("year")
print(thisdict)