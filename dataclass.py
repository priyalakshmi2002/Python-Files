from dataclasses import dataclass

@dataclass
class Student:
    firstname: str
    lastname: str
    roll_no: int
    grade: float

# Creating instances of the dataclass
student1 = Student(firstname="Vinoth", lastname="Raj", roll_no=1, grade=88.5)
student2 = Student(firstname="Jaya", lastname="Amritha", roll_no=2, grade=91.2)

# Accessing attributes
print(f"Student 1: {student1.firstname} {student1.lastname}, Roll No: {student1.roll_no}, Grade: {student1.grade}")
print(f"Student 2: {student2.firstname} {student2.lastname}, Roll No: {student2.roll_no}, Grade: {student2.grade}")

# Comparing two instances
print(student1 == student2)  # False

# Outputting the dataclass as a string (auto-generated __repr__)
print(student1)
