from room import Room
from item import Item
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Sword", "a very sharp sword")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Rope", "a long rope")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Bat", "a wooden bat")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Torch", "a brightly burning torch")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Money Bag", "a bag of shiny gold")]),
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
a = Player("Alvin", "outside", [])

# Inventory Testing


def getItem():
    items = sorted(room[a.room].items)
    print(a.inventory)
    for i in items:
        print(i.name)
        a.inventory.append(i.name)
        print(a.inventory)


# getItem()

# Write a loop that:

# * Prints the current room name
print(f"{a.name}'s location is {a.room}")

items = sorted(room[a.room].items)

# for i in items:
#     print(i.name)

# print(f"{e.name}'s location is {items}")

# * Prints the current description (the textwrap module might be useful here).
for i in room:
    # print(e.room)
    # print(room[i])
    if i == a.room:
        print(room[i].prompt)
# * Waits for user input and decides what to do.


# passing in the direction

def game():

    while True:

        dir = input(">> Enter 'n', 's', 'e' or 'w' to move', 'i' to see inventor, 'get/drop item' or 'q' to quit.")

        # count the arguments & start at items to use args as items
        args = dir.split()[1:]
        numargs = len(args) + 1

    # If the user enters a cardinal direction, attempt to move to the room there.

        if dir == 'n':
            print(room[a.room].name)
            for r in room:
                # print(room.get(r).name)
                try:
                    room[a.room].n_to.name
                    room[a.room] = room[a.room].n_to
                    items = sorted(room[a.room].items)
                    print(f"{room[a.room].prompt}")
                    for i in items:
                        print(f"You see a {i.name} in the room")
                    break
                except AttributeError:
                    print(f"dir is {dir}")
                    print("A strong force blocks your path")
                    break
        elif dir == 's':
            print(room[a.room].name)
            for r in room:
                # print(room.get(r).name)
                try:
                    room[a.room].s_to.name
                    room[a.room] = room[a.room].s_to
                    items = sorted(room[a.room].items)
                    print(f"{room[a.room].prompt}")
                    for i in items:
                        print(f" You see a {i.name} in the room")
                    break
                except AttributeError:
                    print(f"dir is {dir}")
                    print("A strong force blocks your path")
                    break
        elif dir == 'e':
            print(room[a.room].name)
            for r in room:
                # print(room.get(r).name)
                try:
                    room[a.room].e_to.name
                    room[a.room] = room[a.room].e_to
                    items = sorted(room[a.room].items)
                    print(f"{room[a.room].prompt}")
                    for i in items:
                        print(f" You see a {i.name} in the room")
                    break
                except AttributeError:
                    print(f"dir is {dir}")
                    print("A strong force blocks your path")
                    break
        if dir == 'w':
            print(room[a.room].name)
            for r in room:
                # print(room.get(r).name)
                try:
                    room[a.room].w_to.name
                    room[a.room] = room[a.room].w_to
                    items = sorted(room[a.room].items)
                    print(f"{room[a.room].prompt}")
                    for i in items:
                        print(f" You see a {i.name} in the room")
                    break
                except AttributeError:
                    print(f"dir is {dir}")
                    print("A strong force blocks your path")
                    break

    # If the user enters "q", quit the game.

        elif dir == 'q':
            print("Goodbye")
            # print(f"{a.name}'s location is: {a.room.name}")
            break

        elif dir.startswith("get "):
            items = sorted(room[a.room].items)
            print(f"the number of items you are trying to get is {numargs}")
            if int(numargs) > 2:
                error = "You may only get 1 item at a time."
                print(error)
            else:
                item = args[0]
                for i in items:
                    if str(i.name) == str(item):
                        print(f"you picked up {item}")
                        a.inventory.append(Item(i.name, i.description))
                        for i in room[a.room].items:
                            print(i.name)
                            for item in room[a.room].items:
                                print(f"item in room is {item.name}")
                                if str(i.name) == str(item.name):
                                    room[a.room].items.remove(item)
                                    item.on_take()
                    else:
                        print(f"{item} is not in the room")
                        pass

        elif dir == "i":
            if len(a.inventory) < 1:
                print("Your inventory is empty")
            else:
                print("You have the following items in your inventory:")
                for i in a.inventory:
                    print(i.name)

        elif dir.startswith("drop "):
            items = sorted(a.inventory)
            print(f"the number of items you are trying to drop is {numargs}")
            if int(numargs) > 2:
                error = "You may only drop 1 item at a time."
                print(error)
            else:
                item = args[0]
                print(f"item is {item}")

                for i in a.inventory:
                    if str(i.name) == str(item):
                        print(f"you dropped {item}")
                        a.inventory.remove(i)

                        room[a.room].items.append(Item(i.name, i.description))
                        for i in room[a.room].items:
                            print(f"item in room is {i.name}")
                            pass


if __name__ == '__main__':
    game()


