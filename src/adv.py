from item import Item
from player import Player
from room import Room

items = [
    Item('stick', 'can be used to draw in the dirt'),
    Item('pebble', 'makes for a nice souvenir'),
    Item('torch', 'used to light the dark hallways'),
    Item('satchel of coins', 'makes you feel like a pirate, eh?'),
    Item('dragon skull', 'what other creatures lie beneath this mountain?')
]

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items[0:2]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items[2]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items[4]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items[3]]),
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

ACTIONS = {
    'n': 'n_to',
    'e': 'e_to',
    's': 's_to',
    'w': 'w_to',
}


def parse_user_input():
    user_input = input('What is your next move: ')
    action, *rest = user_input.split(' ')
    action = action.lower()

    action_item_combo = (None, None)
    if len(rest) >= 1:
        action_item_combo = (action, ' '.join(rest))
    else:
        action_item_combo = (action, None)
    return action_item_combo


def handle_action(player):
    action, item = parse_user_input()
    if action == 'q':
        return False
    elif action in ('n', 'e', 's', 'w'):
        direction = ACTIONS[action]
        room = getattr(player.current_room, direction)
        if room != None:
            player.current_room = room
        else:
            print('Unable to move %s, try again.' % action)
    elif action in ('get', 'take', 'pickup'):
        # if it is there, remove it from the Room contents, and add it to the Player contents.
        # else, print an error message telling the user so.
        try:
            player.items.append(
                *[i for i in player.current_room.items if i.name == item])
            player.current_room.items.remove(item)
            player.items[-1].on_take()
        except:
            print('No %s to pickup in this room.' % item)
    elif action in ('remove', 'drop', 'dispose'):
        # opposite / reverse of `get` commands
        try:
            player.current_room.items.append(
                *[i for i in player.items if i.name == item])
            player.items.remove(item)
            player.current_room.items[-1].on_drop()
        except:
            print('No %s in your inventory to drop.' % item)
    elif action in ('i', 'inventory'):
        # show a list of items currently carried by the player
        inventory = ', '.join(item.name for item in player.items) if len(
            player.items) > 0 else '[empty]'
        print(inventory)
    return True


def main():
    print('An adventure awaits…')
    # Make a new player object that is currently in the 'outside' room.

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
    player = Player('Augustine', room['outside'])
    continue_playing = True

    while continue_playing:
        # print current room and description
        # get user input (`parse_user_input()`)
        print(player.current_room)

        continue_playing = handle_action(player)
        #   - if n,s,w,e: attempt to move in given direction (error if move not possible)
        #   - elif q: quit the game (`continue_playing = false`)
        #   - else: ignore and redo


if __name__ == "__main__":
    main()
