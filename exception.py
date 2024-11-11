#Type error
x=5
y="name"
try:
    z=x+y
except TypeError:
    print("Cannot add integer and string")
    
#Zero division error
def func(div):
    a=5
    print(a/div)
try:
    func(0)

except ZeroDivisionError:
    print("Zero division error has occurred")

#name error
a=4
try:
    print(p)  
except NameError:
    print("Variable x is not defined")
    
#exception handling with else statement
str="Active"
try:
    print(str)
except TypeError:
    print("Cannot add integer and string")
else:
    print("No errors occurred")
    
#Catching of error
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError as e:
    print(f"Value Error: {e}")
except ZeroDivisionError as e:
    print(f"Division by zero is not allowed: {e}")
    
#finally block
finally:
    print("Try and Exception handling is done")
    
#To throw or raise exception
# b=-2
# if b<0:
#     raise Exception("Numbers less than 0 are not allowed")

# #To raise exception for Type error
num="Guna"
if not type(num) is int:
    raise TypeError("Only integers are allowed")