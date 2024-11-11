#list
thelist = ["apple", "banana", "cherry"]
print(thelist)

#list allows duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#length of the list
print(len(thislist))

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list() constructor
thislist = list(("apple", "banana", "cherry")) 
print(thislist)

#access items of list using index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#accessing using negative index
print(thislist[-1])

#accessing using range of index
print(thislist[0:2])

#check the presence of item in the list 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#change items of a list 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#insert an item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append item
thislist.append("orange")
print(thislist)

#remove an item from list
thislist.remove("banana")
print(thislist)

#using pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#clears the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loops over the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loops using while loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#using list comprehension
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#sort the list
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort the list in descending order
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)