"""
Question 4: Vector class with operator overloading.

Implementation demonstrates:
- Dunder methods
- Oper
- Immutable operationsator overloading
- Equality comparison
"""

class Vector:
    """2D vector with + operator and equality support"""
    def __init__(self, x, y):
        self.x = x  # x-component
        self.y = y  # y-component
    
    def __add__(self, other):
        """Vector addition (+ operator)"""
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """Equality comparison (== operator)"""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """String representation (print() formatting)"""
        return f"Vector({self.x}, {self.y})"

def demonstrate_vectors():
    """Show vector operations including equality"""
    # Vector addition example
    v1 = Vector(2, 3)
    v2 = Vector(5, 7)
    v3 = v1 + v2
    
    # Vector equality examples
    v4 = Vector(2, 3)  # Same values as v1
    v5 = Vector(2, 3)  # Another identical vector
    
    print("Vector Addition:")
    print(f"{v1} + {v2} = {v3}\n")
    
    print("Vector Equality:")
    print(f"{v1} == {v4}? {v1 == v4}")  # True
    print(f"{v1} == {v2}? {v1 == v2}")  # False
    print(f"{v4} == {v5}? {v4 == v5}")  # True (two identical vectors)

if __name__ == "__main__":
    demonstrate_vectors()