#Single level inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class 
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating instances of the child classes
dog = Dog("Buddy")

# Calling the speak method
print(dog.speak())  
 
 
#Hierarchical inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class 
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Child class 
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Creating instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method
print(dog.speak())  
print(cat.speak())  


# multiple inheritance 
# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
        
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


#Multilevel inheritence
# Base class
class Grandmother:
    grandmothername = ""
    def grandmother(self):
        print(self.grandmothername)

# Intermediate derived class
class Mother(Grandmother):
    mothername = ""
    def mother(self):
        print(self.mothername)

# Final derived class
class Son(Mother):
    def parents(self):
        print("Grandmother:", self.grandmothername)
        print("Mother:", self.mothername)

# Creating an object of the Son class
s1 = Son()
s1.grandmothername = "Kausalya"
s1.mothername = "SITA"
s1.parents()
 
#constructor of the parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Jagan", "Nadhan")
x.printname()