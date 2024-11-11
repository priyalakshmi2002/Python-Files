#defining of set
theset = {"apple", "banana", "cherry"}
print(theset)

#length of the set
print(len(theset))

#sets can have different data types
set1 = {"abc", 34, True, 40, "male",6.9}
print(set1)

#datatype of set
print(type(set1))

#set() constructor
set2 = set(("apple", "banana", "cherry")) 
print(set2)

#accessing of set items
for x in theset:
  print(x)
  
#checking of item in the set
print("apple" in theset)
print("banana" not in theset)

#add items to the set
theset.add("orange")
print(theset)

#adding items of one set to other using update()
theset.update(set1)
print(theset) 

#adding list or tuple into set
mylist=["red","blue","yellow"]
set2.update(mylist)
print(set2)

#remove an item from the set
set3 = {"apple", "banana", "cherry"}
set3.remove("apple") #if item does not exist will raise error
print(set3)
set3.discard("banana")#if item does not exist will not raise error
print(set3)

#remove using pop()
x=theset.pop()
print(theset)
print("the removed item is:",x)

#clear function
theset.clear()
print(theset)

#del key- completely removes the set
'''del theset
print(theset)'''

#Join sets
#union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#union operator
set3 = set1 | set2
print(set3)

#multiple sets using union function
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#joining multiple sets using union operator
myset = set1 | set2 | set3 | set4
print(myset)

#joining a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#intersection of two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a"}
set3 = set1.intersection(set2)
print(set3)

#intersection operator
set3 = set1 & set2
print(set3)

#intersection_update() - changes the original set itself
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a"}
set1.intersection_update(set2)
print(set1)

#difference of two sets - returns the first set, removing the items common in two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

#difference operator
set3 = set1 - set2
print(set3)

#difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#symmetric difference- finds the difference and gives the items in both the sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#symmetric difference operator
set4={"banana","kiwi"}
set3 = set1 ^ set2 ^ set4
print(set3)

#symmetric_difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#copy() in sets
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#isdisjoint() returns true if none of the items are same in both the sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset() returns true if set1 is a subset of set2
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#issubset shortcut
z = x <= y
print(z)

#issuperset() returns true if set2 is a superset of set1
z = y.issuperset(x)
print(z)

#issuperset() shortcut
z = y >= x
print(z)