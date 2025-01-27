list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]

newList = [item.upper() for item in list if "u" in item]
print(newList)

newList = ["yo" for item in list]
print(newList)