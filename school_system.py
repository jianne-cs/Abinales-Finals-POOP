"""

Question 3: wo that display their liBuild two classes called SchoolOne and SchoolTst of students' average grades and GPA.

School System Implementation
Demonstrates:
- Inheritance
- Encapsulation
- Abstraction
- Class methods
"""

class Student:
    """Represents a student with their grades"""
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    @property
    def average(self):
        """Calculate the average grade"""
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def get_report(self, gpa_calculator):
        """Generate a performance report string"""
        gpa = gpa_calculator(self.average)
        return f"{self.name}: Average: {self.average:.1f}, GPA: {gpa:.1f}"


class School:
    """Base school class with shared functionality"""
    def __init__(self, name):
        self._name = name  # Protected attribute
        self._students = []  # Encapsulated list
    
    def add_student(self, name, grades):
        """Add a student with their grades"""
        self._students.append(Student(name, grades))
    
    def _calculate_gpa(self, average):
        """Protected method to convert average to GPA"""
        if average >= 90: return 4.0
        elif average >= 80: return 3.0
        elif average >= 70: return 2.0
        elif average >= 60: return 1.0
        return 0.0
    
    def show_performance(self):
        """Display all students' performance"""
        print(f"\n{self._name} Student Performance:")
        if not self._students:
            print("No students enrolled yet.")
            return
        
        for student in self._students:
            print(student.get_report(self._calculate_gpa))
        
        # Show class average
        class_avg = sum(s.average for s in self._students) / len(self._students)
        class_gpa = self._calculate_gpa(class_avg)
        print(f"\nClass Average: {class_avg:.1f}, GPA: {class_gpa:.1f}")


class SchoolOne(School):
    """First school implementation"""
    def __init__(self):
        super().__init__("School One")


class SchoolTwo(School):
    """Second school implementation"""
    def __init__(self):
        super().__init__("School Two")


def demonstrate_school_system():
    """Demonstrate the school system functionality"""
    # Create schools
    school1 = SchoolOne()
    school2 = SchoolTwo()
    
    # Add students to School One
    school1.add_student("Blossom Utonium", [92, 88, 95, 90])
    school1.add_student("Bubbles Utonium", [75, 82, 78, 80])
    
    # Add students to School Two
    school2.add_student("Buttercup Utonium", [65, 70, 68, 72])
    school2.add_student("Professor Utonium", [98, 95, 97, 99])
    
    # Display performances
    school1.show_performance()
    school2.show_performance()


if __name__ == "__main__":
    demonstrate_school_system()