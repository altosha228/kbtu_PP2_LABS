list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]

list[0:2] = ["wifi pcb", "fan"]

print(list)

list[0:2] = ["gpu", "cpu"]
list[1:2] = ["cpu", "energy block"]
print(list)

list[3:5] = ["Hard Drive"]
print(list)

#I don't want to replace existing items. I want to add new items!
list.insert(7, "CD Drive")
print(list)

