# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        ret = f"{self.name}\n{self.room}\n"
        return ret

    def __repr__(self):
        return f"Player({self.name}, {self.room})"