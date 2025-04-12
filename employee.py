"""
Question 2: Build a class Employee with multiple constructors.

Implementation demonstrates:
- Polymorphism (via class method constructors)
- Encapsulation
- Alternative object creation patterns
"""

class Employee:
    """Employee class with multiple construction options"""
    def __init__(self, name, emp_id, department="General"):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    
    @classmethod
    def from_name_id(cls, name, emp_id):
        """Constructor with just name and ID"""
        return cls(name, emp_id)
    
    @classmethod
    def from_dict(cls, emp_dict):
        """Constructor from dictionary"""
        return cls(
            emp_dict.get('name', 'Unknown'),
            emp_dict.get('id', 0),
            emp_dict.get('department', 'General')
        )
    
    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}, Dept: {self.department})"

def demonstrate_constructors():
    """Show different ways to create Employee instances"""
    # Powerpuff Girls-themed employees
    emp1 = Employee("Blossom Utonium", 1001, "Research & Development")
    emp2 = Employee.from_name_id("Bubbles Utonium", 1002)
    emp3 = Employee.from_dict({
        'name': 'Buttercup Utonium',
        'id': 1003,
        'department': 'Security'
    })
    
    print("🧪 Townsville Company Employees:")
    for emp in [emp1, emp2, emp3]:
        print(f"✨ {emp}")

if __name__ == "__main__":
    demonstrate_constructors()