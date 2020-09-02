from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
lauren = Player('Lauren', room['outside'])
 
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
game_active = True
while game_active:
    print(f'\nCurrent Room Name: {lauren.room.name}\nCurrent Room Description: {lauren.room.description} \n')

    x = input('Enter where you want to go: ')

    if x == 'n':
        if lauren.room == room['outside'] or lauren.room == room['narrow'] or lauren.room == room['foyer']:
            lauren.room = lauren.room.n_to
        else:
            print("Movement isn't allowed, try again!\n")

    if x == 'e':
        if lauren.room == room['foyer']:
            lauren.room = lauren.room.e_to
        else:
            print("Movement isn't allowed, try again!\n")
    
    if x == 's':
        if lauren.room == room['foyer'] or lauren.room == room['treasure'] :
            lauren.room = lauren.room.s_to
        else:
            print("Movement isn't allowed, try again!\n")

    if x == 'w':
        if lauren.room == room['narrow']:
            lauren.room = lauren.room.w_to
        else:
            print("Movement isn't allowed, try again!\n")
    
    if x == 'q':
        y = input('Are you sure you want to quit? y/n: ')
        if y == 'y':
            print("Okay, see you next time!")
            game_active = False
        elif y == 'n':
            x = input('Enter where you want to go: ')
        else:
            print('Please enter "y" to quit the game or "n" to resume game.')

    