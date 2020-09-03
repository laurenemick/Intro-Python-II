# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        # self.starting_room = current_room
        self.items = items
        self.inventory = [] # relationship with Items, has_a
        self.gold = 0

    def __str__(self):
        ret = f"{self.name}\n"
        for i, item in enumerate(self.items):
            ret += "    " + str(i + 1) + ": " + item.name + "\n"
        ret += "    " + str(i + 2) + ": Exit"
    
    def __repr__(self):
        return f"Player({self.name}, {self.room}, {self.items})"

    # def move(self, direction):
    #     # check if the current room has direction_to
    #     # return the current room at direction to
    #     # otherwise, tell the player they can not go that way

    # def pick_up(self):
    #     # what could we pass into this function and pick an item up?
    #     # think of instances of obj...

    # def drop(self):
