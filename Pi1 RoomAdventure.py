###########################################################################################
# Name: Sage Hargrove, Ty Davis
# Date: 1/10/23
# Description: This will create a text based game for someone to interact with rooms, with a fantasy twist to it.
###########################################################################################

###########################################################################################
# the blueprint( for a room
class Room:
	# the constructor
	def __init__(self, name):
		# rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
		# items (e.g., table), item descriptions (for each item), and grabbables (things that can
		# be taken into inventory)
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions = []
		self.grabbables = []
		self.grabbableDescriptions = []
	# getters and setters for the instance variables
	# ...
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = value

	@property
	def exits(self):
		return self._exits
	
	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def exitLocations(self):
		return self._exitLocations
	
	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value

	@property
	def items(self):
		return self._items
	
	@items.setter
	def items(self, value):
		self._items = value

	@property
	def itemDescriptions(self):
		return self._itemDescriptions
	
	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value

	@property
	def grabbables(self):
		return self._grabbables
	
	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value
	
	@property
	def grabbableDescriptions(self):
		return self._grabbableDescriptions
	
	@grabbableDescriptions.setter
	def grabbableDescriptions(self, value):
		self._grabbableDescriptions = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate lists
		self._exits.append(exit)
		self._exitLocations.append(room)
	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		self._items.append(item)
		self._itemDescriptions.append(desc)	
	def delItem(self, item):
		self._items.remove(item)
	# append the item and description to the appropriate lists
	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item, desc):
		# append the item to the list
		self._grabbables.append(item)
		self._grabbableDescriptions.append(desc)
	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)
	# modify an item description once it is taken
	def itemModification(self, item, new_desc):
		if item in self.items:
			indexOfItem = self.items.index(item)
			self.itemDescriptions[indexOfItem] = new_desc


	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits:
			s += exit + " "

		return s

###########################################################################################
# creates the rooms
def createRooms():
# r1 through r4 are the four rooms in the mansion
# currentRoom is the room the player is currently in (which can
# be one of r1 through r4)
# since it needs to be changed in the main part of the program,
# it must be global
	global currentRoom
	global r6
	# create the rooms and give them meaningful names
	r1 = Room("Grand Dining Hall")
	r2 = Room("Living Space")
	r3 = Room("Library")
	r4 = Room("Brewery")
	r5 = Room("Dueling Grounds")
	r6 = Room("Dungeon")

	# add exits to room 1
	r1.addExit("east", r2) # -> to the east of room 1 is room 2
	r1.addExit("south", r3)
	# add grabbables to room 1
	r1.addGrabbable("key", "It must be used for something.")
	# add items to room 1
	r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
	r1.addItem("table", "It is made of oak. A golden key rests on it.")
	# add exits to room 2
	r2.addExit("west", r1)
	r2.addExit("south", r4)
	r2.addExit("east", r5)
	# add items to room 2
	r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
	r2.addItem("fireplace", "It is full of ashes.")
	# add exits to room 3
	r3.addExit("north", r1)
	r3.addExit("east", r4)
	# add grabbables to room 3
	r3.addGrabbable("book", "A mysterious book filled with ancient symbols.")
	# add items to room 3
	r3.addItem("bookshelves", "They are empty. Go figure.")
	r3.addItem("statue", "There is nothing special about it.")
	r3.addItem("desk", "The statue is resting on it. So is a book.")
	# add exits to room 4
	r4.addExit("north", r2)
	r4.addExit("west", r3)
	r4.addExit("south", None) # DEATH!
	# add grabbables to room 4
	r4.addGrabbable("6-pack", "What could this be used for?")
	# add items to room 4
	r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
	# add exits to room 5
	r5.addExit("west", r2)
	# add grabbables to room 5
	r5.addGrabbable("sword", "Is this Excalibur?")
	r5.addGrabbable("spear", "I can feel a gluttonous desire for power.")
	r5.addGrabbable("bow", "A wise choice, befitting a celestial archer.")
	r5.addGrabbable("shield", "I can sense a demonlike aura emanating from it.")
	# add items to room 5
	r5.addItem("weapons_rack", "There are a few weapons to pick from. I have a feeling I can only choose one. \nSword, Spear, Bow, Shield")
	# add grabbables to room 6
	r6.addGrabbable("seed-of-life", "I can sense immense power dwelling within.")
	# add items to room 6
	r6.addItem("chest", "It requires a key. Perhaps it has treasure?")
	r6.addItem("lich_king", "It looks terrifying. It must be protecting something incredibly valuable. I need to find a powerful weapon.")
	# set room 1 as the current room at the beginning of the game
	currentRoom = r1


# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
	print(" " * 17 + "u" * 7)
	print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
	print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
	print(" " * 9 + "u" + "$" * 21 + "u")
	print(" " * 8 + "u" + "$" * 23 + "u")
	print(" " * 7 + "u" + "$" * 25 + "u")
	print(" " * 7 + "u" + "$" * 25 + "u")
	print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
	print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
	print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
	print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
	print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
	print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
	print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
	print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
	print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
	print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
	print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
	print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
	print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
	print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
	print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
	print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
	print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
	print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
	print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
	exit()

###########################################################################################
# START THE GAME!!!
# give proper introduction to the player!
lichKingDefeated = False
print()
print("This is a game set in a fantasy world. Your goal is to defeat the Lich King "
	  "who has conquered this land and spread impurity throughout. \n"
	  "To do this, you must use the four action commands that this game uses to function. "
	  "These are go, use, look, and take. Not all items are\nyou able to take but all items you "
	  "can take, you can use. Now, as an example! 'go north' will bring you to the room directly above you.\n"
	  "Another command example is 'take key' which will put a key in your inventory. Use the look command "
	  "to find many of these items in this\nworld. You can look at items in the inventory and "
	  "before you pick them up. Now, use your wit as the hero of this world and save the\nland!")

inventory = [] # nothing in inventory...yet
inventoryDescriptions = []
createRooms() # add the rooms to the game
# play forever (well, at least until the player dies or asks to quit)
while (True):
	# set the status so the player has situational awareness
	# the status has room and inventory information
	status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

	# if the current room is None, then the player is dead
	# this only happens if the player goes south when in room 4
	if (currentRoom == None):
		status = "You are dead."
	# display the status
	print("========================================================")
	print(status)

	# if the current room is None (and the player is dead), exit the
	# game
	if (currentRoom == None):
		death()
		break
		
	global weapons
	if (currentRoom.name == "Dungeon"):
		weapons = ["sword", "shield", "bow", "spear"]
		haveWeapon = False
		for weapon in weapons:
			if weapon in inventory:
				haveWeapon = True
				break
		if not haveWeapon:
			print("You have walked into my realm unprepared. Only death awaits.")
			death()
	if (currentRoom.name == "Library"):
		print("I feel that something is off...")

	# prompt for player input
	# the game supports a simple language of <verb> <noun>
	# valid verbs are go, look, and take
	# valid nouns depend on the verb
	action = input("What to do? ")

	# set the user's input to lowercase to make it easier to compare
	# the verb and noun to known values
	action = action.lower()

	# exit the game if the player wants to leave (supports quit,
	# exit, and bye)
	if (action == "quit" or action == "exit" or action == "bye"):
		break

	# set a default response
	response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use."
	# split the user input into words (words are separated by spaces)
	words = action.split()

	# the game only understands two word inputs
	if (len(words) == 2):
		# isolate the verb and noun
		verb = words[0]
		noun = words[1]

		# the verb is: go
		if (verb == "go"):
		# set a default response
			response = "Invalid exit."

		# check for valid exits in the current room
			for i in range(len(currentRoom.exits)):
				# a valid exit is found
				if (noun == currentRoom.exits[i]):
					# change the current room to the one that is
					# associated with the specified exit
					currentRoom = currentRoom.exitLocations[i]

					# set the response (success)
					response = "Room changed."

					# no need to check any more exits
					break
		# the verb is: look
		elif (verb == "look"):
			# set a default response
			response = "I don't see that item."

			# check for valid items in the current room
			for i in range(len(currentRoom.items)):
				# a valid item is found
				if (noun == currentRoom.items[i]):
				# set the response to the item's description
					response = currentRoom.itemDescriptions[i]
					# no need to check any more items
					break

			# for looking at grabbable items
			for i in range(len(currentRoom.grabbables)):
				if (noun == currentRoom.grabbables[i]):
					response = currentRoom.grabbableDescriptions[i]
					break
			for i in range(len(inventory)):
				if (noun == inventory[i]):
					response = inventoryDescriptions[i]
					break

		# the verb is: take
		elif (verb == "take"):
			# set a default response
			response = "I don't see that item."
			# check for valid grabbable items in the current room
			for i in range(len(currentRoom.grabbables)):
				grabbable = currentRoom.grabbables[i]
				# a valid grabbable item is found
				if (noun == grabbable):
					# add the grabbable item to the player's
					# inventory
					inventory.append(grabbable)
					# add the grabbable item's description to the player's inventory
					inventoryDescriptions.append(currentRoom.grabbableDescriptions[i])

					# remove the grabbable item from the room
					currentRoom.delGrabbable(grabbable)

					# set the response (success)
					response = "Item grabbed."

					# set the descriptions to be the same as when using "look"
					if grabbable in currentRoom.itemDescriptions:
						pass
					weapons = ["sword", "spear", "bow", "shield"]
					if grabbable in weapons:
						for weapon in weapons:
							if weapon != grabbable and weapon in currentRoom.grabbables:
								currentRoom.delGrabbable(weapon)
								print(f"The {weapon} magically disappeared.")
					if (noun == "6-pack"):
						currentRoom.itemModification("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. The 6-pack is gone.")
					if (noun == "key"):
						currentRoom.itemModification("table", "A key used to be on this table.")
					if (noun == "book"):
						currentRoom.itemModification("desk", "I've got the magical book, now! Maybe I should try using it? I should get prepared first.")
					if (noun == "sword", "bow", "spear", "shield"):
						currentRoom.itemModification("weapons_rack", "Fascinating. The weapons are all gone, but I feel stronger than ever.")
					# no need to check any more grabbable items
					break
			if noun == "seed-of-life" and currentRoom.name == "Dungeon":
				print("You haven't even opened the chest! Foolishness!")
				death()
				break
		elif (verb == "use"): 
			# set a default response
			response = "I can't use that."

			# check that item can actually be used
			if noun in inventory:
				if (noun == "book" and currentRoom.name == "Library"):
					inventory.remove("book")
					response = "The book disappears, and the world warps around you. You find yourself in a sparsely lit dungeon!"
					currentRoom = r6

				if (noun == "6-pack" and currentRoom.name == "Dungeon" and lichKingDefeated == False):
					inventory.remove("6-pack")
					print("You give the 6-pack to the Lich King. He looks at you in confusion, but starts to drink. It falls through him.")
				elif (noun == "6-pack"):
					inventory.remove("6-pack")
					print("\nYou drink the entire 6-pack within the span of 30 seconds. You are bad with alcohol. This was unwise.")
					death()
				elif noun in ["sword", "bow", "spear", "shield"] and currentRoom.name == "Dungeon":
					currentRoom.delItem("lich_king")
					lichKingDefeated = True
					response = "\nThe Lich King has been defeated, and your fame shall spread throughout the land! Now claim your treasure, hero!"
					
					
					if lichKingDefeated == True:
						if ("key" not in inventory):
							print("\nIt would seem that I forgot the key. Is the only fate left for me to starve? Perhaps fame wasn't for me...")
							death()

				if (noun == "key" and currentRoom.name == "Dungeon"):
					if lichKingDefeated:
						print("\nCongratulations! You have opened the chest, and found immense treasure. \nYou have found the Seed of Life.")
						decision = input("Do you wish to take it, or leave it due to the certain tribulations to come from taking such a valued object? (yes/no) ")
						if decision.lower() in ["yes", "ya", "y"]:
							inventory.remove("key")
							print("You are now immortal, and shall leave your mark on the world.")
							print("Congratulations, you have completed the game! I hope you had fun playing!")
							exit()
						if decision.lower() in ["no", "n"]:
							print("A cowardly act. However, it could be commendable to retreat and live a peaceful life, and so I bid you farewell.")
							print("Congratulations, you have completed the game! I hope you had fun playing!")
							exit()
					else:
						print("Silly! You must defeat the Lich King before stealing his treasure!")
						death()

		# display the response
		print("\n{}".format(response))
		