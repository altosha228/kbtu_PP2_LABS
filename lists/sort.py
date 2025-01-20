list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.sort(key=str.lower)
print(list)