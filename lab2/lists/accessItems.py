list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]

print(list[1])
print(list[-1])
print(list[1:5])
print(list[:3])
print(list[4:])

if "cpu" in list:
  print("cpu is in the list")