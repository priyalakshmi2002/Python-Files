# class Employee:
#     # Class attribute
#     num_of_employees = 0
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Employee.num_of_employees += 1  # Increment the class attribute for each instance created

#     # Instance method
#     def show_info(self):
#         return f"Employee Name: {self.name}, Age: {self.age}"

#     # Class method using @classmethod decorator
#     @classmethod
#     def get_employee_count(cls):
#         return f"Total Employees: {cls.num_of_employees}"

# # Creating instances of Employee
# emp1 = Employee("John", 30)
# emp2 = Employee("Jane", 25)

# # Using class method
# print(Employee.get_employee_count()) 

#Another example for class methods
# class Details:
#     course = 'Python'
#     list_of_instances=[]
    
#     def __init__(self,name):
#         self.name = name
#         Details.list_of_instances.append(self)
    
#     @classmethod
#     def get_course(cls):
#         return f"Course:{cls.course}"
    
#     @classmethod
#     def get_instance_count(cls):
#         return f"Number of  instances: {len(cls.list_of_instances)}"
    
#     @staticmethod
#     def welcome_message():
#         return "Welcome to the Academy"
# #Creating instances
# d1=Details('Rahul')                
# d2=Details('Rohan')

# #Calling class methods 
# print(Details.get_course())
# print(Details.get_instance_count())

# #Calling static method
# print(Details.welcome_message())                

class Methods:
    school="VKM School"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    #instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def get_num(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("this is a music school")

s=Methods(90,100,89)
print(s.avg())
print(Methods.get_num())
Methods.info()