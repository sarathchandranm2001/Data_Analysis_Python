# Define the Person class
class Person:
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to display person's details
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    # Method to simulate birthday
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# Create instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25

# Use methods
person1.display_details()  # Output: Name: Alice, Age: 30
person2.display_details()  # Output: Name: Bob, Age: 25

# Simulate a birthday for person1
person1.have_birthday()    
person1.display_details()  
