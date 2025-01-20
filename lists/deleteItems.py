list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]

component = "gpu"

list.remove(component)
print(list)

list.pop(0)
print(list)

list.clear()
print(list)

del list