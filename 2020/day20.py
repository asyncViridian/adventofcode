import math

### PART 1
# read the input
f = open('input/day20.txt', 'r')
input = [x.strip() for x in f]
f.close()
# create our set of tiles
tiles = {}
tile_current = ['', []]
for line in input:
    if 'Tile ' in line:
        # if we begin a new tile...
        tile_current[0] = line[len('Tile '):-1]
    elif line=='' and tile_current[0]!='':
        # if we just finished a tile...
        tiles[int(tile_current[0])] = tile_current[1]
        tile_current = ['', []]
    else:
        # if we are still building up a tile...
        tile_current[1].append(line)
if tile_current[0]!='':
    tiles[int(tile_current[0])] = tile_current[1]
# check what the dimensions of our final tiling need to be
tiling_dim = int(math.sqrt(len(tiles)))
# helper function for rotation/flipping
def rotate(tile, rotations, flip):
    if rotations==0 and flip==False:
        return tile
    if flip==True:
        flipped_tile = [''.join(list(reversed(e))) for e in tile]
        return rotate(flipped_tile, rotations, False)
    output = []
    for i in range(len(tile)):
        output_line = []
        for j in range(len(tile)):
            output_line.append(tile[len(tile)-1-j][i])
        output.append(''.join(output_line))
    return rotate(output, rotations-1,flip)
#print('\n'.join(rotate(tiles[2311],0,False)))
#print()
#print('\n'.join(rotate(tiles[2311],1,False)))
#print()
#print('\n'.join(rotate(tiles[2311],2,False)))
#print()
#print('\n'.join(rotate(tiles[2311],3,False)))
# helper function and datastructure for checking border matching
fulltiling = dict([((i,j), None) for i in range(tiling_dim) for j in range(tiling_dim)])
fulltiling_ids = dict([((i,j), -1) for i in range(tiling_dim) for j in range(tiling_dim)])
def validate_fulltiling(fulltiling):
    def check_adjacent(c0, c1):
        if (c0,c1) not in fulltiling:
            return True
        if fulltiling[(c0,c1)] is None:
            return True
        # check top edge
        if (c0-1,c1) in fulltiling and fulltiling[(c0-1,c1)] is not None:
            if fulltiling[(c0,c1)][0]!=fulltiling[(c0-1,c1)][-1]:
                return False
        # check right edge
        if (c0,c1+1) in fulltiling and fulltiling[(c0,c1+1)] is not None:
            if ''.join([e[-1] for e in fulltiling[(c0,c1)]])!=''.join([e[0] for e in fulltiling[c0,c1+1]]):
                return False
        # check bottom edge
        if (c0+1,c1) in fulltiling and fulltiling[(c0+1,c1)] is not None:
            if fulltiling[(c0,c1)][-1]!=fulltiling[(c0+1,c1)][0]:
                return False
        # check left edge
        if (c0,c1-1) in fulltiling and fulltiling[(c0,c1-1)] is not None:
            if ''.join([e[0] for e in fulltiling[(c0,c1)]])!=''.join([e[-1] for e in fulltiling[c0,c1-1]]):
                return False
        return True
    return all([check_adjacent(i,j) for i,j in fulltiling])
# helper function to visualize the full tiling, not strictly necessary but eh
def print_fulltiling(fulltiling):
    output = []
    tilesize = len(tiles[list(tiles.keys())[0]])
    for i in range(tiling_dim):
        for row in range(tilesize):
            output.append(' '.join([fulltiling[(i,j)][row] if fulltiling[(i,j)] is not None else ''.join(['_']*tilesize) for j in range(tiling_dim)]))
        output.append('')
    return output
#print('\n'.join(print_fulltiling(fulltiling)))
#print(validate_fulltiling(fulltiling))
#print()
#fulltiling[(0,0)] = rotate(tiles[1951],2,True)
#fulltiling[(0,1)] = rotate(tiles[2311],2,True)
#print('\n.join(print_fulltiling(fulltiling)))
#print(validate_fulltiling(fulltiling))
# now actually do the search through tiling-space lol
def tiling_search(fulltiling, fulltiling_ids, next_tile, tiling_dim):
    if not validate_fulltiling(fulltiling):
        raise ValueError('invalid fulltiling passed into tiling_search')
    if next_tile[0]>=tiling_dim:
        print(fulltiling_ids[(0,0)]*fulltiling_ids[(0,tiling_dim-1)]*fulltiling_ids[(tiling_dim-1,0)]*fulltiling_ids[tiling_dim-1,tiling_dim-1])
        return True,print_fulltiling(fulltiling)
    # try all potential next ids to add
    for next_id in [k for k in tiles.keys() if k not in fulltiling_ids.values()]:
        # try each rotation
        for rotation in range(4):
            for flip in [False, True]:
                # apply the change try
                fulltiling[next_tile] = rotate(tiles[next_id],rotation,flip)
                fulltiling_ids[next_tile] = next_id
                if validate_fulltiling(fulltiling):
                    idx = next_tile[0]*tiling_dim+next_tile[1] + 1
                    further_next_tile = (int(idx/tiling_dim),idx%tiling_dim)
                    res = tiling_search(fulltiling, fulltiling_ids, further_next_tile, tiling_dim)
                    if res is not None and res[0]:
                        return res
                # undo the change
                fulltiling[next_tile] = None
                fulltiling_ids[next_tile] = -1
found,tilemap = tiling_search(fulltiling, fulltiling_ids, (0,0), tiling_dim)

### PART 2
# remove the borders of each tile :P
if tilemap[-1].strip()=='':
    tilemap = tilemap[:-1]
tilemap = [' '.join([i[1:-1] for i in e.split(' ')]) for e in tilemap]
tilemap = ['\n'.join(l.split('\n')[1:-1]) for l in '\n'.join(tilemap).split('\n\n')]
tilemap = '\n\n'.join(tilemap).split('\n')
# remove the gaps between each tile
tilemap = [''.join(e.split(' ')) for e in tilemap]
tilemap = [e for e in tilemap if e!='']
# define the sea monster pattern we are looking for
sea_monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
]
def matches_pattern(tilemap, pos, pattern):
    filter_tilemap = [[b for b in a] for a in tilemap]
    # check each position
    for i in range(len(pattern)):
        intersect_line = []
        for j in range(len(pattern[i])):
            # if it's out of range, it's automatically invalid
            if pos[0]+i>=len(tilemap):
                return False, tilemap
            if pos[1]+j>=len(tilemap[i]):
                return False, tilemap
            # if the pattern indicates something but theres nothing in the map...
            if pattern[i][j]!=' ' and tilemap[pos[0]+i][pos[1]+j]=='.':
                return False, tilemap
            if pattern[i][j]!=' ':
                filter_tilemap[pos[0]+i][pos[1]+j] = 'X'
    filter_tilemap = [''.join(e) for e in filter_tilemap]
    return True, filter_tilemap
hits = 0
for rotation in range(4):
    for flipped in [False,True]:
        temp_tilemap = rotate(tilemap,rotation,flipped)
        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                found, tilemap_update = matches_pattern(temp_tilemap, (i,j), sea_monster)
                if found:
                    hits += 1
                    temp_tilemap = tilemap_update
        # rotate and flip back to the original state
        # keep in mind rotate always does the flip FIRST, then does rotations
        temp_tilemap = rotate(temp_tilemap,4-rotation,False)
        temp_tilemap = rotate(temp_tilemap,0,flipped)
        tilemap = temp_tilemap
# get the rough water count
#print('\n'.join(tilemap))
water_count = len([e for e in ''.join(tilemap) if e=='#'])
print(water_count)
