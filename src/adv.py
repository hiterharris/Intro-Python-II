from room import Room
from player import Player
from item import Item

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

# Initialize items
sword = Item('sword', 'Fights off enemies')
shield = Item('sheild', 'Defends you from attack')

# Add items to rooms
room['outside'].addItems(sword)
room['foyer'].addItems(shield)

username = input("What is your name? ")
player = Player(username, room['outside'])

while True:
	player.displayRoom()
	user = input("[n] North\t[s] South\t[e] East\t[w] West\n[i] Inventory\n[take item]\t[drop item]\n[q] Quit: ").lower()
	inputs = user.split()
	directions = ('n', 's', 'e', 'w')

	if len(inputs) == 1:
		if inputs[0] == 'q':
			break
		elif inputs[0] in directions:
			player.moveTo(inputs[0])
		elif inputs[0] == 'i':
			player.displayInventory()

	elif len(inputs) == 2:
		if inputs[0] == "get" or inputs[0] == "take":
			player.addItem(inputs[1])
		elif inputs[0] == "drop":
			player.dropItem(inputs[1])
	else:
		print("Invalid command.")

	print("\n")