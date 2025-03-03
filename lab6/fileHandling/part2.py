import os


def checkPath(path):
  if(not os.path.exists(path)):
    print("Path doesnt exist")
  print(f"Readable: {os.access(path, os.R_OK)}")
  print(f"Writable: {os.access(path, os.W_OK)}")
  print(f"Executable: {os.access(path, os.X_OK)}")
  

path = "C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\fileHandling\\part1.py"
path2 = "C:\\Users\\assas\\OneDrive\\Pictures\\2c3f2b02e428ab812fe18491065f37ad.png"
checkPath(path)


