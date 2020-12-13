import copy

### PART 1
# read the input
f = open('input/day11.txt', 'r')
seats = [[e for e in x.strip()] for x in f]
f.close()
# add filler "seats"/flooring to delineate the boundary
seats = [(['.']+e+['.']) for e in seats]
seats = [['.']*len(seats[0])] + seats + [['.']*len(seats[0])]
# a function to put the seat arrangement into something readable
def stringify(seats):
    return '\n'.join([''.join(e) for e in seats])
# model how the seats will be filled up
# (using immediately adjacent seats)
def updateSeats(seats):
    update_seats = copy.deepcopy(seats)
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[i])-1):
            if seats[i][j] in ['L', '#']:
                # calculate number of adjacent occupied seats
                adjacent = [
                    seats[i-1][j-1], seats[i-1][j], seats[i-1][j+1],
                    seats[i][j-1], seats[i][j+1],
                    seats[i+1][j-1], seats[i+1][j], seats[i+1][j+1]
                ]
                adjacent = sum([(1 if e=='#' else 0) for e in adjacent])
                # calculate the update itself
                if (seats[i][j]=='L') and (adjacent==0):
                    # if a seat is empty and there are 0 adjacent occupied seats
                    # it becomes occupied
                    update_seats[i][j] = '#'
                if (seats[i][j]=='#') and (adjacent>=4):
                    # if a seat is occupied and there are >=4 adjacent occupied seats
                    # it becomes empty
                    update_seats[i][j] = 'L'
    return update_seats
# keep updating the seats until they stop changing!
seats_simple = copy.deepcopy(seats)
update_seats = updateSeats(seats_simple)
while stringify(seats_simple)!=stringify(update_seats):
    seats_simple = update_seats
    update_seats = updateSeats(seats_simple)
print(sum([(1 if e=='#' else 0) for e in stringify(seats_simple)]))

### PART 2
# to save some time, pre-calculate a map of which seats each seat can see
vision_map = []
for i in range(len(seats)):
    vision_map.append([])
    for j in range(len(seats[i])):
        if seats[i][j] in ['L', '#']:
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            can_see = []
            for direction in directions:
                target = (i+direction[0], j+direction[1])
                while (target[0]>0) and (target[0]<len(seats)-1) \
                        and (target[1]>0) and (target[1]<len(seats[i])-1) \
                        and (seats[target[0]][target[1]] not in ['L', '#']):
                            target = (target[0]+direction[0], target[1]+direction[1])
                if seats[target[0]][target[1]] in ['L', '#']:
                    can_see.append(target)
            vision_map[i].append(can_see)
        else:
            vision_map[i].append([])
# model how the seats will be filled up
# (using visible adjacent seats)
def updateSeats(seats, vision_map=vision_map):
    update_seats = copy.deepcopy(seats)
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[i])-1):
            if seats[i][j] in ['L', '#']:
                # calculate number of adjacent occupied seats
                adjacent = [seats[e[0]][e[1]] for e in vision_map[i][j]]
                adjacent = sum([(1 if e=='#' else 0) for e in adjacent])
                # calculate the update itself
                if (seats[i][j]=='L') and (adjacent==0):
                    # if a seat is empty and there are 0 adjacent occupied seats
                    # it becomes occupied
                    update_seats[i][j] = '#'
                if (seats[i][j]=='#') and (adjacent>=5):
                    # if a seat is occupied and there are >=5 adjacent occupied seats
                    # it becomes empty
                    update_seats[i][j] = 'L'
    return update_seats
# keep updating the seats until they stop changing!
seats_vision = copy.deepcopy(seats)
update_seats = updateSeats(seats_vision)
while stringify(seats_vision)!=stringify(update_seats):
    seats_vision = update_seats
    update_seats = updateSeats(seats_vision)
print(sum([(1 if e=='#' else 0) for e in stringify(seats_vision)]))
