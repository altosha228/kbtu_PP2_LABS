list = ["nvidia", "amd", "intel", "msi", "gigabyte", "asus"]

f = open("C:\\Users\\assas\\OneDrive\\Desktop\\PP2\\lab6\\fileHandling\\someTextFile.txt", "at")

def writeListMembersToFile(file, list):
  for item in list:
    file.write(str(item) + '\n')
  file.write('\n')

writeListMembersToFile(f, list)