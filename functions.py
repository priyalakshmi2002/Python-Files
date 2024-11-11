#defining a function
def func():
    print("This is a function")

func()

#arguments in a function
def function(fname, lname):
      print(fname + " " + lname)

function("Priya", "Lakshmi")

#arbitraray arguments
def fruits_func(*fruit):
      print("My favourite fruit is " + fruit[0])
      print("My favourite fruit is " + fruit[1])
      print("My favourite fruit is " + fruit[2])

fruits_func("cherry", "lemon", "berry")

#key arguments
def fruits_func1(child3, child2, child1):
      print("The best fruit is " + child3)
      print("The best fruit is " + child2)
      print("The best fruit is " + child1)

fruits_func1(child1 = "apple", child2 = "mango", child3 = "jamun")

#default parameter
def fruits_func2(fruit= "musk melon"):
      print("My favourite fruit is " + fruit)
fruits_func2("cherry")
fruits_func2()

#return statement
def my_function(x):
      return 5 * x

print(my_function(3))
print(my_function(5))

#positional only arguments
def my_function(x, /):
      print(x)

my_function(3)

#keyword only arguments
def my_function(*, x):
      print(x)

my_function(x = 3)

#recursion function 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")

#lambda function
x=lambda a:a+10
print(x(5))