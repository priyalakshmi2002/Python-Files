from abc import ABC,abstractmethod

#By using @abstractmethod, we can force the subclasses to define the area() method, 
# ensuring correct implementation.

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Lion(Animal):
#     def eat(self):
#         print("Lion eats meat")
        
# class Cow(Animal):
#     def eat(self):
#         print("Cow eats grass")
 
# #object cannot be created for abstract class       
# obj1=Lion()
# obj1.eat()
# obj2=Cow()
# obj2.eat()

class Animal(ABC):
    def eat(self):  # Not abstract, no enforcement
        print("Animal eats")

class Lion(Animal):
    def eat(self):  # Still provides implementation, but not required
        print("Lion eats meat")

class Cow(Animal):
    pass  # No implementation, but this will not raise an error

obj1 = Lion()
obj1.eat()  # Output: "Lion eats meat"

obj2 = Cow()
obj2.eat()  # Output: "Animal eats" (inherited method from Animal)
#function in the animal class should not be executed but this gets executed since its not an abstract class

#Another example  
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Creating instances of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

# Calling the area method
print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24
print("Triangle Area:", triangle.area())  # Output: Triangle Area: 10.5
