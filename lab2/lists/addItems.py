list = ["gpu", "cpu", "motherboard", "Hard Drive", "SATA SSD", "NVMe SSD", "RAM pcb"]

#It is not convenient to every time count the index of last element
#to insert an item to the end of the list,  is there another way?
list.append("Audio card")
print(list)

anotherList = ["banana", "apple", "mango"]
list.extend(anotherList)
print(list)

