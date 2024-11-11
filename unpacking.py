#Unpacking of tuples
(a,b,c,d)=(1,2,3,4)
print(b)
print(d)

#Unpacking iterables

#Unpacking Strings
x,y,z = "Net"
print(x)
print(y)
print(z)

#Unpacking Lists
x,y,z=["Onion","Tomato","Garlic"]
print(x)
print(y)
print(z)

#Unpacking Sets
x,y,z={"forest","mountain","sea"}
print(x)
print(y)
print(z)

#Unpacking Dictionaries
#Unpacking dictionary keys
dict1={'place':'Chennai', 'state':'Tamil nadu', 'country':'India'}
a,b,c=dict1
print(a)
print(b)
print(c)

#Unpacking dictionary values
a,b,c=dict1.values()
print(a)
print(b)
print(c)

#Unpacking key-value pairs
a,b,c=dict1.items()
print(a)
print(b)
print(c)

#packing with *operator
*a,="Forest"
print(a)

*b,=('f','i','l','m')
print(b)

#unpacking the values ignoring some values at first
*_,a,b = [1,2,3,4,5,6]
print(a)
print(b)

#unpacking dictionaries with *operator
dictionary1={'value1':'Name','value2':'Age','value3':'Class'}
dictionary2={'v1':'City','v2':'Pincode'}
combine={**dictionary1,**dictionary2}
print(combine)