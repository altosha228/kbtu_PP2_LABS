import os

def copyContentToAnotherFile(path1, path2):
  if(os.path.exists(path1)):
    f1 = open(path1, "rt")
  else:
    print("error: path1 doesnt exist")
  
  if(os.path.exists(path1)):
    f2 = open(path2, "wt")
  else:
    print("error: path1 doesnt exist")
  
  f2.write(f1.read())


path1 = "C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\fileHandling\\part7files\\1.txt"
path2 = "C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\fileHandling\\part7files\\2.txt"
copyContentToAnotherFile(path1, path2)
