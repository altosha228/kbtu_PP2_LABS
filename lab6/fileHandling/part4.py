import os

def countLinesInFile(file):
  cnt = 0
  for line in file :
    cnt += 1
  return cnt



f = open("C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\fileHandling\\someTextFile.txt", "rt")

lines = countLinesInFile(f)
print(lines)