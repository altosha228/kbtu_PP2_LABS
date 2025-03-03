import os

def deleteFile(path):
  if(os.path.exists(path)):
    if(os.access(path, os.X_OK)):
      os.remove(path)
    else:
      print("the program doesnt have access to edit file")
  else:
    print("error: path doesnt exist")

myPath = "C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\fileHandling\\part8files\\dummy.txt"
deleteFile(myPath)