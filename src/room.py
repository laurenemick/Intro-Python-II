# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return f"{self.name}\n{self.description}\n{self.items}"
    def __repr__(self):
        return f"Room({self.name}, {self.description}, {self.items})"