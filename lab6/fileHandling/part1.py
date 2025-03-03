import os

def listDirectory(path):
  all = os.listdir(path)
  dirs = [dir for dir in all if os.path.isdir(os.path.join(path, dir))]
  files = [file for file in all if os.path.isfile(os.path.join(path, file))]
  return all, dirs, files


# all, dirs, files = listDirectory("C:\\Users\\assas\\OneDrive\\Desktop\\PP2")
all, dirs, files = listDirectory("C:\\Users\\assas\\OneDrive\\Desktop\\English")

print(all)
print(files)