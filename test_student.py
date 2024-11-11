import unittest
from dataclasses import dataclass

# The original code
@dataclass
class Student:
    firstname: str
    lastname: str
    roll_no: int
    grade: float

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student1 = Student(firstname="Vinoth", lastname="Raj", roll_no=1, grade=88.5)
        self.student2 = Student(firstname="Jaya", lastname="Amritha", roll_no=2, grade=91.2)

    def test_student_attributes(self):
        """Test if the student attributes are set correctly."""
        self.assertEqual(self.student1.firstname, "Vinoth")
        self.assertEqual(self.student1.lastname, "Raj")
        self.assertEqual(self.student1.roll_no, 1)
        self.assertEqual(self.student1.grade, 88.5)
        self.assertEqual(self.student2.firstname, "Jaya")
        self.assertEqual(self.student2.lastname, "Amritha")
        self.assertEqual(self.student2.roll_no, 2)
        self.assertEqual(self.student2.grade, 91.2)
        
    def test_student_comparison(self):
        """Test comparison between two Student instances."""
        self.assertNotEqual(self.student1, self.student2)
        # Create another student with the same attributes as student1
        student3 = Student(firstname="Vinoth", lastname="Raj", roll_no=1, grade=88.5)
        self.assertEqual(self.student1, student3)

    def test_student_repr(self):
        """Test the __repr__ output of the dataclass."""
        expected_repr = "Student(firstname='Vinoth', lastname='Raj', roll_no=1, grade=88.5)"
        self.assertEqual(repr(self.student1), expected_repr)

# Run the tests
if __name__ == '__main__':
    unittest.main()
