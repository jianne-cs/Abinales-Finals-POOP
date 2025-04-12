
## 🧩 Implemented OOP Concepts

### Core Requirements
| Concept          | File               | Key Implementation                     |
|------------------|--------------------|----------------------------------------|
| Inheritance      | `school_bus.py`    | `SchoolBus` inherits from `Vehicle`    |
| Polymorphism     | `employee.py`      | Multiple constructors via `@classmethod`|
| Abstraction      | `school_system.py` | Protected `_calculate_gpa()` method     |
| Encapsulation    | `school_system.py` | `_students` protected list              |
| Operator Overloading | `vector.py`    | `__add__` for vector addition          |
| Composition      | `book_author.py`   | `Book` contains `Author` object        |

### Bonus Implementations
| Concept          | File               | Key Implementation                     |
|------------------|--------------------|----------------------------------------|
| Aggregation      | `department.py`    | `Department` holds independent `Employee` objects |
| Dunder Methods   | `vector.py`        | `__str__` for pretty printing          |

## 🚀 How to Run
```bash
# Core Questions (1-5)
python school_bus.py
python employee.py
python -m school_system.school  # For Question 3
python vector.py
python book_author.py

# Bonus Implementation
python department.py