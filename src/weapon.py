from item import Item

class Weapon(Item):
    def __init__(self, item_name, type):
        super().__init__(item_name)
        self.type = type
    def __str__(self):
        return f"{super().__str__()}, {self.type}"
