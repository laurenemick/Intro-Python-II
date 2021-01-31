from room import Room
from player import Player
from item import Item
from weapon import Weapon

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Weapon("gun", "shotgun"), Weapon("knife", "samurai sword")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[Weapon("gun", "rifle"),]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 
[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
[]),
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

# print('outside room name n: ', room['outside'].n_to.name )
# print('outside room name s: ', room['outside'].s_to)
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
game_active  = True

print(f'\nWelcome {lauren.name}!')

while game_active:
    print(f'\nYou are currently in the {lauren.room.name} room.\n{lauren.room.description}\n')
    if len(lauren.inventory) > 0:
        print('My items:')
        for index, item in enumerate(lauren.inventory):
            print(f"\t{index+1}. {item}")
    else:
        print(f"You currently have 0 items in your inventory")

    if len(lauren.room.items) > 0:
        print('\nThis Room contains the following items:')
        for index, item in enumerate(lauren.room.items):
            print(f"\t{index+1}. {item}")
        # i = input('\nDo you want anything? y/n ')
        # if i == 'y': 
        #     selection = input('\nPlease enter a number: ')
        #     selection = int(selection)
        #     if selection > 0 and selection <= len(lauren.room.items):
        #         print(f"You chose: {lauren.room.items[selection - 1]}")
        #         lauren.inventory.append(lauren.room.items[selection - 1])
        #         lauren.room.items.remove(lauren.room.items[selection - 1])
        #         if len(lauren.room.items) == 0:
        #             pass
        #     else:
        #         print("Please select a valid number")
        # if i == 'n':
        #     x = input('\nWhere do you want to go? ')
        #     print("\n------------------------------------------------------------")
        #     if x == 'n':
        #         if lauren.room.n_to:
        #             lauren.room = lauren.room.n_to
        #         else:
        #             print("Movement isn't allowed, try again!\n")
        #     elif x == 'e':
        #         if lauren.room.e_to:
        #             lauren.room = lauren.room.e_to
        #         else:
        #             print("Movement isn't allowed, try again!\n") 
        #     elif x == 's':
        #         if lauren.room.s_to:
        #             lauren.room = lauren.room.s_to
        #         else:
        #             print("Movement isn't allowed, try again!\n")
        #     elif x == 'w':
        #         if lauren.room.w_to:
        #             lauren.room = lauren.room.w_to
        #         else:
        #             print("Movement isn't allowed, try again!\n")    
        #     elif x == 'q':
        #         y = input('Are you sure you want to quit? y/n: ')
        #         if y == 'y':
        #             print("Okay, see you next time!")
        #             game_active = False
        #         elif y == 'n':
        #             x = input('Enter where you want to go: ')
        #         else:
        #             print('Please enter "y" to quit the game or "n" to resume game.')
        #     else: 
        #         print("Please select a valid input!")
    else:
        print(f"\nNo items in the {lauren.room.name}")

    x = input('\nWhere do you want to go? ')
    print("\n------------------------------------------------------------")
    if x == 'n':
        if lauren.room.n_to:
            lauren.room = lauren.room.n_to
        else:
            print("Movement isn't allowed, try again!\n")
    elif x == 'e':
        if lauren.room.e_to:
            lauren.room = lauren.room.e_to
        else:
            print("Movement isn't allowed, try again!\n")
    elif x == 's':
        if lauren.room.s_to:
            lauren.room = lauren.room.s_to
        else:
            print("Movement isn't allowed, try again!\n")
    elif x == 'w':
        if lauren.room.w_to:
            lauren.room = lauren.room.w_to
        else:
            print("Movement isn't allowed, try again!\n")  
    elif x == 'q':
        y = input('\nAre you sure you want to quit? y/n: ')
        if y == 'y':
            print("Okay, see you next time!")
            game_active = False
        elif y == 'n':
            pass
        else:
            print('Please enter "y" to quit the game or "n" to resume game.')
    elif len(x.split(" ")) == 2:
        muli_input = x.split(" ")
        selection = int(muli_input[1]) - 1
        if muli_input[0] == 'get':
            lauren.get(lauren.room.items[selection])
            lauren.room.items.remove(lauren.room.items[selection])
        elif muli_input[0] == 'drop':
            lauren.room.items.append(lauren.inventory[selection])
            lauren.drop(lauren.inventory[selection])
        else:
            print("try again")
    else: 
        print("Please select a valid input!")

  
  
    