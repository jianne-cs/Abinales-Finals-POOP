"""
Question 5: Book and Author demonstrating composition.

Implementation demonstrates:
- Composition over inheritance
- Object collaboration
- Encapsulation
"""

class Author:
    """Represents a book author"""
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    
    def __str__(self):
        return f"{self.name} ({self.nationality})"

class Book:
    """Represents a book using composition"""
    def __init__(self, title, author_name, author_nationality, genre):
        self.title = title
        self.genre = genre
        self.author = Author(author_name, author_nationality)  # Composition
    
    def get_info(self):
        """Get complete book information"""
        return f"'{self.title}' by {self.author} [{self.genre}]"

def demonstrate_composition():
    """Create and display book information"""
    book = Book(
        "Python Crash Course",
        "Eric Matthes",
        "American",
        "Programming"
    )
    print(book.get_info())

if __name__ == "__main__":
    demonstrate_composition()