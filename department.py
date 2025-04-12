"""
Bonus: Demonstrates Aggregation in OOP with Daily Planet Staff

Key Python Implementations:
1. Aggregation ("has-a" relationship with independent lifecycle)
2. Class definition and instance methods
3. List manipulation (appending objects)
4. String formatting (f-strings)
"""

class Employee:
    """Represents an employee that can exist independently of a department"""
    def __init__(self, name, emp_id):
        # Instance attributes
        self.name = name      # Public attribute
        self.emp_id = emp_id  # Public attribute

    def __str__(self):
        # String representation method (dunder method)
        return f"📰 {self.name} (Press ID: {self.emp_id})"


class Department:
    """Demonstrates aggregation - contains employees but doesn't own them"""
    def __init__(self, name):
        # Instance attributes
        self.name = name                # Public attribute
        self.employees = []             # Aggregated list (not composition!)
    
    def add_employee(self, employee):
        """Adds an existing employee to the department
        
        Implements:
        - Aggregation (employee exists independently)
        - Type checking (isinstance)
        """
        if isinstance(employee, Employee):  # Runtime type checking
            self.employees.append(employee)
        else:
            raise TypeError("Only Daily Planet employees can be added")
    
    def display_staff(self):
        """Shows all employees in the department
        
        Implements:
        - List iteration
        - String formatting
        """
        print(f"\n🪧 {self.name} Department Staff:")
        for emp in self.employees:  # Iterate through aggregated objects
            print(f"  ✏️ {emp}")      # Uses Employee.__str__


# Demonstration
if __name__ == "__main__":
    # Create standalone employees (exist without department)
    reporter1 = Employee("Clark Kent", 1948)  # Superman's debut year
    reporter2 = Employee("Lois Lane", 1938)   # First appearance year
    
    # Create department (empty at first)
    newsroom = Department("Daily Planet Newsroom")
    
    # Add existing employees to department (aggregation)
    newsroom.add_employee(reporter1)
    newsroom.add_employee(reporter2)
    
    # Show department staff
    newsroom.display_staff()
    
    # Prove employees exist independently
    print(f"\n{reporter1.name} still works freelance when not at the Daily Planet!")