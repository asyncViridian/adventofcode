### PART 1
# read the input
f = open('input/day24.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse a direction sequence into the tile coordinate it references
# coord[0] is "move how many east" and then coord[1] is "move how many northeast"
def directionsToCoords(directions):
    i = 0
    coord = (0,0)
    while i<len(directions):
        if directions[i]=='e':
            coord = (coord[0]+1,coord[1])
        elif directions[i]=='s':
            if directions[i+1]=='e':
                coord = (coord[0]+1,coord[1]-1)
            elif directions[i+1]=='w':
                coord = (coord[0],coord[1]-1)
            i += 1
        elif directions[i]=='w':
            coord = (coord[0]-1,coord[1])
        elif directions[i]=='n':
            if directions[i+1]=='e':
                coord = (coord[0],coord[1]+1)
            elif directions[i+1]=='w':
                coord = (coord[0]-1,coord[1]+1)
            i += 1
        i += 1
    return coord
coords = [directionsToCoords(d) for d in input]
is_black = set()
for c in coords:
    if c not in is_black:
        is_black.add(c)
    else:
        is_black.remove(c)
print(len(is_black))

### PART 2
# determine which set of tiles needs to be considered for flipping
def tilesForConsideration(current_black):
    output = set()
    for t in current_black:
        # center cell
        output.add(t)
        # east
        output.add( (t[0]+1,t[1]) )
        # southeast
        output.add( (t[0]+1,t[1]-1) )
        # southwest
        output.add( (t[0],t[1]-1) )
        # west
        output.add( (t[0]-1,t[1]) )
        # northeast
        output.add( (t[0],t[1]+1) )
        # northwest
        output.add( (t[0]-1,t[1]+1) )
    return output
# determine whether a tile should end up being black or white
def willBeBlack(t, current_black):
    # count how many adjacent black tiles there are
    num_adjacent_black = 0
    if (t[0]+1,t[1]) in current_black:
        num_adjacent_black += 1
    if (t[0]+1,t[1]-1) in current_black:
        num_adjacent_black += 1
    if (t[0],t[1]-1) in current_black:
        num_adjacent_black += 1
    if (t[0]-1,t[1]) in current_black:
        num_adjacent_black += 1
    if (t[0],t[1]+1) in current_black:
        num_adjacent_black += 1
    if (t[0]-1,t[1]+1) in current_black:
        num_adjacent_black += 1
    # now determine what the output should be
    if t in current_black:
        # any black tile with zero or more than 2 adjacent black tiles becomes white
        # so for it to stay black, it must have either 1 or 2 adjacent black tiles
        return (num_adjacent_black == 1 or num_adjacent_black == 2)
    else:
        # any white tile with exactly 2 adjacent black tiles becomes black
        return (num_adjacent_black == 2)
# do the actual flipping process!
for i in range(100):
    for_consideration = tilesForConsideration(is_black)
    next_black = set()
    for t in for_consideration:
        if willBeBlack(t, is_black):
            next_black.add(t)
    is_black = next_black
print(len(is_black))
