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
