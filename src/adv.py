from player import Player
from room import Room

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

ACTIONS = {
    'n': 'n_to',
    'e': 'e_to',
    's': 's_to',
    'w': 'w_to',
}


def parse_user_action():
    action = input('What is your next move: ')
    return action.lower()


def handle_action(player, action):
    if action == 'q':
        return False
    elif action in ('n', 'e', 's', 'w'):
        direction = ACTIONS[action]
        room = getattr(player.current_room, direction)
        if room != None:
            player.current_room = room
        else:
            print('Unable to move %s, try again.' % action)
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
        # get user input (`parse_user_action()`)
        print(player.current_room)

        action = parse_user_action()
        continue_playing = handle_action(player, action)
        #   - if n,s,w,e: attempt to move in given direction (error if move not possible)
        #   - elif q: quit the game (`continue_playing = false`)
        #   - else: ignore and redo


if __name__ == "__main__":
    main()
