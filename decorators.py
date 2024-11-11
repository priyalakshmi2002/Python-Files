#Decorators in python: To modify the behaviour of the function or class

#Pre-requisites of pyhton decorators

#first class objects
#A function can be used or passed as arguments

#Treating fucntions as objects
def name(text):
    return text.lower()

print(name('Karthik'))
name_person = name
print(name_person('Rohan'))

#Passing function as an argument
def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
        
    return wrapper

def f():
    print("Hello")

x=f1(f)
x()

#Returning a function from a function
def return_to_upper():
      return str.upper

to_upper = return_to_upper() 

print(to_upper("Capitalizing")) #gets the returned value and prints it

#inner functions: functions inside function
def parent():
    print("This is the parent ")
    
    def firstchild():
        print("This is the first child")
    
    def secondchild():
        print("This is the second child")
    
    firstchild()
    secondchild()    

parent()

#inner function accessing with the variable and returning the function
def outer(message):
    def inner():
        print("Message:",message)
    return inner

msg = outer("Welcome")
msg()

#using decorator syntax - Syntatic decorators example
def f1(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)   
    return wrapper

@f1
def f(a,b=9):
    print(a,b)

x=f("Hello")

