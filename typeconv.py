#implicit conversion
a=10
print("data type of a :",type(a))

b=int(input("enter an integer:"))
print("data type of b :",type(b))

c=float(input("Enter a number:"))
print(f"{c} data type is:",type(c))

#Explicit conversion
#ord() - converts a character to an integer
num='5'
b=ord(num)
print(f"ord({num}) is:",b)

#hex() - converts an integer to hexadecimal string
print("hex(72) is:",hex(72))

#oct() - converts an integer to octal string
print("oct(48) is:",oct(48))

#explicit conversion to tuple using tuple keyword
string1= "Variation"
tup=tuple(string1)
print("String to tuple:",tup)

#explicit conversion to set using set keyword
set1=set(string1)
print("String to set:",set1)

#explicit conversion to list using list keyword
list1=list(string1)
print("String to list:",list1)

#explicit conversion of tuple to dictionary
tup = (('a', 1) ,('f', 2), ('g', 3))
dict1= dict(tup)
print("Tuple to dictionary:",dict1)