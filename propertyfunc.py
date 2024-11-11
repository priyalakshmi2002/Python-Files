#property function
#It prevents direct access to internal variables 
#while still making them appear as regular attributes to users of your class.
class rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height
    
    @property    
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property    
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width = new_width
        else:
            print("Width must be positive")
    
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else: 
            print("Height must be positive")
            
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        
r = rectangle(4,8)
r.width = 0
print(r.width)
print(r.height)

del r.width
del r.height

# # Python program to illustrate property() function
# class Person:
#     def __init__(self, value):
#         self._name = value

#     # getter function
#     def get_name(self):
#         print('Getting name:')
#         return self._name

#     # setter function
#     def set_name(self, value):
#         print('Setting name to:', value)
#         self._name = value

#     # deleter function
#     def del_name(self):
#         print('Deleting name...')
#         del self._name

#     # Set property() to use get_name, set_name and del_name methods
#     name = property(get_name, set_name, del_name)

# p = Person('Priya')
# print(p.name) #get_name
# p.name = 'Sandhya' #set_name
# del p.name #del_name


# #Python program to illustate @property decorator
# class Person:
#     def __init__(self, value):
#         self._name = value

#     @property
#     def name(self):
#         print('Getting name...')
#         return self._name

#     @name.setter
#     def name(self, value):
#         print('Setting name to:', value)
#         self._name = value

#     @name.deleter
#     def name(self):
#         print('Deleting name...')
#         del self._name

# p = Person('Priya')
# print(p.name) #calls getter
# p.name = 'Sandhya' #calls setter
# del p.name #calls deleter