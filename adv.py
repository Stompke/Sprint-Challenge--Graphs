from room import Room
from player import Player
from world import World
from util import Stack
import random
from ast import literal_eval

# Load world
world = World()




# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

## MY CODE START
################################################################################################################################


backtrack = False
s = Stack()
journal = {}
my_visited_rooms = set()
for i in range(len(room_graph)):
    journal[i] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}



def get_opposite(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

print('Starting ROOM ID: ', player.current_room.id)
print('CURRENT EXITS: ', player.current_room.get_exits())
print('CURRENT EXITS STRING: ', player.current_room.get_exits_string())
print('Map File Length: ', len(room_graph))
print('Traversal Path Length: ', len(traversal_path)) 
print('Starting Journal: ', journal)
print('\n')

my_visited_rooms.add(player.current_room.id)

# print('current room stuff: ', journal[player.current_room.id]['n'])

# while False:

while len(my_visited_rooms) < len(room_graph):

    


    first_room = player.current_room.id

    # Fill in NONE Directions
    first_room_directions = player.current_room.get_exits()
    for direction in journal[first_room]:
        if direction not in first_room_directions:
            journal[first_room][direction] = None

    # If any unknown rooms:

    for direction in journal[first_room]:
        if journal[first_room][direction] == '?':
            print('yes There is an uknown room!')

        # if journal[first_room]['n'] == '?':
            # Set backtrack to False
            backtrack = False
            # Add to Stack
            s.push(direction)
            # Add to traversal path
            traversal_path.append(direction)
            # Go There
            player.travel(direction)
            # fill in journal 
            second_room = player.current_room.id
            journal[first_room][direction] = second_room
            opposite_dir = get_opposite(direction)
            journal[second_room][opposite_dir] = first_room
            # add to my visited rooms
            my_visited_rooms.add(second_room)

print('Final Journal: ', journal)
print('My visited rooms length: ', len(my_visited_rooms))
print('Map file length: ', len(room_graph))
print('Eding ROOM ID: ', player.current_room.id)



        # while backtrack is True:
            # Pop off direction
            # Move in opposite of that direction

        # If no unknown rooms:
            # Set backtrack to True




################################################################################################################################
## MY CODE END


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
