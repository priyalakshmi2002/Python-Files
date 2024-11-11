#definition of dictionary
# thisdict = {
#   "brand": "Ford",
#   "year": 1964,
#   "model": "Mustang"
# }
# print(thisdict)

# for key in thisdict:
#     print(key)
    
# for key in sorted(thisdict):
#     print(key)
    
# for value in thisdict.values():
#     print(value)
      
# for key,value in thisdict.items():
#     print(f"{key}:{value}")
      
# thisdict.update({'name':'priya'})
# print(thisdict)

# thisdict.pop("name")
# print(thisdict)

# p=thisdict.popitem()
# print(p)
# print(thisdict)

# squares = {x: x * x for x in range(1, 11)}
# print(squares)

# #accessing of dictionary items using key
# print(thisdict["brand"])

# #length of dictionary
# print(len(thisdict))

# #dictionary constructor
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# #get function
# x = thisdict.get("model","key is not present")

# print(x)

# #modifying the items
# thisdict["year"] = 2018

# #delete using popitem()
# thisdict.popitem()
# print(thisdict)

# #looping through dictionary
# for x in thisdict:
#   print(thisdict[x])

#adding of new item to the dictionary  
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#get the keys
x=car.keys()
print(x)

#copy()
c=car.copy()
print(c)

# #add using update()
# thisdict.update({"year": 2020})
# print(thisdict)

# #nested dictionary 
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004,
#     "test":['a','b'],
#     "test2":[{'msg':['hello']}]
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child2"]["name"])
# print(myfamily["child1"]["test"][1])
# print(myfamily["child1"]["test2"][0]['msg'][0])

# #Checking the key-value pair of two dictionaries 
# d1 = {'a': 5, 'b': 7, 'c': 9, 'e': 3} 
# d2 = {'c': 9, 'a': 5, 'b': 7, 'e': 3} 
# x = d1 == d2 
# y = d1 != d2 
# print(x) 
# print(y) 

# #To extract dictionaries with given key from a list of dictionaries
# list1=[{'room':1,'number':2,'done':5},{'room':3,'van':7,'bus':6},{'give':9}]
# key='room'
# result = [sub for sub in list1 if key in list(sub.keys())]
# print("The filtered dictionaries:" + str(result))

# #To extract key-value from mixed dictionaries list
# test=[{"start":3,"step":4,"stop":5},
#       {"jack":9,"john":8,"hur":10},
#       {"poll":34,"hero":89,"jain":56}]
# k="poll"
# res=dict()
# for sub in test:
#   res.update(sub)
# print("The extracted value :" + str(res[k]))

# #Adding elements to nested dictionary
# Dict1={}
# print("Initial nested dictionary:-")
# print(Dict1)

# Dict1['Dict2']={}
# Dict1['Dict2']['name'] = 'Ram'
# Dict1['Dict2']['age'] = 21
# print("\nAfter adding dictionary to dict1")
# print(Dict1)

# #adding whole dictionary
# Dict1['Dict3'] = {'name':'Vino','age':22}
# print("\nAfter adding dictionary to Dict1")
# print(Dict1)
# del Dict1['Dict2']['name']
# print(Dict1)