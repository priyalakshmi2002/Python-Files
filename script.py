import mymodule
mymodule.reaction("Neammen")

print(mymodule.list1)
print(mymodule.list1[4])
print(mymodule.dict1["flower"])
print(mymodule.dict1.values())
print(mymodule.dict1)
print(mymodule.dict1.keys())

#from keyword
from mymodule import list1
for i in list1:
    print(i)
    
# from mymodule import * #imports all the variable name and the functions