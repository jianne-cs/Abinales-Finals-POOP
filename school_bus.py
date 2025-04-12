"""
Question 1: Determine if SchoolBus is also an instance of the Vehicle class.

Implementation demonstrates:
- Inheritance
- isinstance() check
- Method overriding
"""

class Vehicle:
    """Base class representing any vehicle"""
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    
    def info(self):
        return f"{self.name} (Max speed: {self.max_speed} km/h)"

class SchoolBus(Vehicle):
    """Specialized vehicle for transporting students"""
    def __init__(self, name, max_speed, capacity):
        super().__init__(name, max_speed)
        self.capacity = capacity
    
    def info(self):
        """Extended vehicle information"""
        base_info = super().info()
        return f"{base_info}, Capacity: {self.capacity} students"

def demonstrate_inheritance():
    """Create and test SchoolBus instance"""
    bus = SchoolBus("Yellow Bus", 80, 50)
    print(bus.info())
    print(f"Is SchoolBus a Vehicle? {isinstance(bus, Vehicle)}")

if __name__ == "__main__":
    demonstrate_inheritance()