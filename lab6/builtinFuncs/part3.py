def all_elements_true(tup):
    return all(tup)


t = (True, 1, "Hello", [1, 2])  
print(all_elements_true(t))  

t2 = (True, 0, "Hello")  
print(all_elements_true(t2))  
