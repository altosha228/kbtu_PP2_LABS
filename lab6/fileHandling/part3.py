import os


def checkPath(path):
  if(os.path.exists(path)):
    print(f"path {path} exists.")
    print(f"Directory: {os.path.dirname(path)}")
    print(f"File: {os.path.basename(path)}")
  else:
    print(f"Path {path} doesnt exist")
  
checkPath("C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\builtinFuncs")