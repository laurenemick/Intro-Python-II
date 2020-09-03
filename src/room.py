# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
        self.contents = [] # has_a

    # def print_items(items):
    #     for i in items:
    #         self.contents.append(i)

    # print_items(self.items)

    def __str__(self):
        return f"No items in {self.name}"
    def __repr__(self):
        return f"Room({self.name}, {self.description}, {self.items})"