import copy

### PART 1
# read the input
f = open('input/day12.txt', 'r')
nav = [x.strip() for x in f]
f.close()
# parse the input into instructions
nav = [[e[0], int(''.join(e[1:]))] for e in nav]
# walk through the instructions
# coordinates are in (north-ness, east-ness)
ship_loc = (0, 0)
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
ship_dir = 0 # turning R increases index by 1, L is -1
for instr in nav:
    if instr[0] == 'N':
        # move North by the given value
        ship_loc = (ship_loc[0] + instr[1], ship_loc[1])
    elif instr[0] == 'S':
        # move South by the given value
        ship_loc = (ship_loc[0] - instr[1], ship_loc[1])
    elif instr[0] == 'E':
        # move East by the given value
        ship_loc = (ship_loc[0], ship_loc[1] + instr[1])
    elif instr[0] == 'W':
        # move West by the given value
        ship_loc = (ship_loc[0], ship_loc[1] - instr[1])
    elif instr[0] == 'L':
        # turn left the given number of degrees
        ship_dir = int((ship_dir - (instr[1]/90)) % len(directions))
    elif instr[0] == 'R':
        # turn right the given number of degrees
        ship_dir = int((ship_dir + (instr[1]/90)) % len(directions))
    elif instr[0] == 'F':
        # move forward the given number of steps
        ship_loc = (
            ship_loc[0] + directions[ship_dir][0]*instr[1],
            ship_loc[1] + directions[ship_dir][1]*instr[1]
        )
print(ship_loc, abs(ship_loc[0])+abs(ship_loc[1]))

### PART 2
# Now the instructions indicate how to move the waypoint
# and F just means to move to the waypoint N times!!
# coordinates are in (north-ness, east-ness)
ship_loc = (0, 0)
waypoint = (1, 10)
for instr in nav:
    if instr[0] == 'N':
        # move waypoint North by the given value
        waypoint = (waypoint[0] + instr[1], waypoint[1])
    elif instr[0] == 'S':
        # move waypoint North by the given value
        waypoint = (waypoint[0] - instr[1], waypoint[1])
    elif instr[0] == 'E':
        # move waypoint East by the given value
        waypoint = (waypoint[0], waypoint[1] + instr[1])
    elif instr[0] == 'W':
        # move waypoint West by the given value
        waypoint = (waypoint[0], waypoint[1] - instr[1])
    elif instr[0] == 'L':
        # turn waypoint counterclockwise the given number of degrees
        for i in range(int(instr[1]/90)):
            waypoint = (waypoint[1], -1*waypoint[0])
    elif instr[0] == 'R':
        # turn waypoint clockwise the given number of degrees
        for i in range(int(instr[1]/90)):
            waypoint = (-1*waypoint[1], waypoint[0])
    elif instr[0] == 'F':
        # move to the waypoint the given number of times
        ship_loc = (
            ship_loc[0] + waypoint[0]*instr[1],
            ship_loc[1] + waypoint[1]*instr[1]
        )
print(ship_loc, abs(ship_loc[0])+abs(ship_loc[1]))
