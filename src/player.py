# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = [] # relationship with Items, has_a
        self.gold = 0

    def __str__(self):
        return f"{self.name} is currently in {self.room}\n"
    
    def __repr__(self):
        return f"Player({self.name}, {self.room})"

    # def move(self, direction):
    #     # check if the current room has direction_to
    #     # return the current room at direction to
    #     # otherwise, tell the player they can not go that way

    def pick_up(self, item):
        self.inventory.append(item)
        return f"You picked up {item}"

    def drop(self, item):
        self.inventory.remove(item)
        return f"You dropped {item}"