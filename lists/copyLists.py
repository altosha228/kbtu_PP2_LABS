list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]


newList = list.copy()       #Just copies list
print(newList)

newList2 = list[:]          #Assigns the diapasone of list
print(newList2)

newList3 = [item for item in list]  #Assigns items based on conditions
print(newList3)