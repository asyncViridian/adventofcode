### PART 1
# read the input
f = open('input/day17.txt', 'r')
input = [x.strip() for x in f]
f.close()
# Read the input into a cube slice
space = {}
timestep = 0
dimension_border = len(input)
for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y]=='#':
            space[(y-1,-x+1,0)] = True
# step 6 times
for i in range(6):
    space_step = {}
    # in each step, the dimension expands 1 in all directions
    dimension_border += 1
    # scan all cells in the dimension to see if they should be activated
    for x in range(-1*dimension_border+1, dimension_border):
        for y in range(-1*dimension_border+1, dimension_border):
            for z in range(-1*dimension_border+1, dimension_border):
                current_cell = (x,y,z)
                surroundings = [
                    (x-1,y-1,z-1), (x-1,y,z-1), (x-1,y+1,z-1),
                    (x,y-1,z-1), (x,y,z-1), (x,y+1,z-1),
                    (x+1,y-1,z-1), (x+1,y,z-1), (x+1,y+1,z-1),
                    (x-1,y-1,z), (x-1,y,z), (x-1,y+1,z),
                    (x,y-1,z), (x,y+1,z),
                    (x+1,y-1,z), (x+1,y,z), (x+1,y+1,z),
                    (x-1,y-1,z+1), (x-1,y,z+1), (x-1,y+1,z+1),
                    (x,y-1,z+1), (x,y,z+1), (x,y+1,z+1),
                    (x+1,y-1,z+1), (x+1,y,z+1), (x+1,y+1,z+1),
                ]
                # count the surrounding cells
                surrounding_active = 0
                for cell in surroundings:
                    if cell in space:
                        surrounding_active += 1
                # determine what should happen to the cell!
                if current_cell in space:
                    if surrounding_active==2 or surrounding_active==3:
                        space_step[current_cell] = True
                else:
                    if surrounding_active==3:
                        space_step[current_cell] = True
    space = space_step
print(len(space))

### PART 2
# Read the input into a 4D-cube slice!!!!
space = {}
timestep = 0
dimension_border = len(input)
for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y]=='#':
            space[(y-1,-x+1,0,0)] = True
# step 6 times
for i in range(6):
    space_step = {}
    # in each step, the dimension expands 1 in all directions
    dimension_border += 1
    # scan all cells in the dimension to see if they should be activated
    for x in range(-1*dimension_border+1, dimension_border):
        for y in range(-1*dimension_border+1, dimension_border):
            for z in range(-1*dimension_border+1, dimension_border):
                for w in range(-1*dimension_border+1, dimension_border):
                    current_cell = (x,y,z,w)
                    surroundings = [
                        (x-1,y-1,z-1,w-1), (x-1,y,z-1,w-1), (x-1,y+1,z-1,w-1),
                        (x,y-1,z-1,w-1), (x,y,z-1,w-1), (x,y+1,z-1,w-1),
                        (x+1,y-1,z-1,w-1), (x+1,y,z-1,w-1), (x+1,y+1,z-1,w-1),
                        (x-1,y-1,z,w-1), (x-1,y,z,w-1), (x-1,y+1,z,w-1),
                        (x,y-1,z,w-1), (x,y,z,w-1), (x,y+1,z,w-1),
                        (x+1,y-1,z,w-1), (x+1,y,z,w-1), (x+1,y+1,z,w-1),
                        (x-1,y-1,z+1,w-1), (x-1,y,z+1,w-1), (x-1,y+1,z+1,w-1),
                        (x,y-1,z+1,w-1), (x,y,z+1,w-1), (x,y+1,z+1,w-1),
                        (x+1,y-1,z+1,w-1), (x+1,y,z+1,w-1), (x+1,y+1,z+1,w-1),
                        (x-1,y-1,z-1,w), (x-1,y,z-1,w), (x-1,y+1,z-1,w),
                        (x,y-1,z-1,w), (x,y,z-1,w), (x,y+1,z-1,w),
                        (x+1,y-1,z-1,w), (x+1,y,z-1,w), (x+1,y+1,z-1,w),
                        (x-1,y-1,z,w), (x-1,y,z,w), (x-1,y+1,z,w),
                        (x,y-1,z,w), (x,y+1,z,w),
                        (x+1,y-1,z,w), (x+1,y,z,w), (x+1,y+1,z,w),
                        (x-1,y-1,z+1,w), (x-1,y,z+1,w), (x-1,y+1,z+1,w),
                        (x,y-1,z+1,w), (x,y,z+1,w), (x,y+1,z+1,w),
                        (x+1,y-1,z+1,w), (x+1,y,z+1,w), (x+1,y+1,z+1,w),
                        (x-1,y-1,z-1,w+1), (x-1,y,z-1,w+1), (x-1,y+1,z-1,w+1),
                        (x,y-1,z-1,w+1), (x,y,z-1,w+1), (x,y+1,z-1,w+1),
                        (x+1,y-1,z-1,w+1), (x+1,y,z-1,w+1), (x+1,y+1,z-1,w+1),
                        (x-1,y-1,z,w+1), (x-1,y,z,w+1), (x-1,y+1,z,w+1),
                        (x,y-1,z,w+1), (x,y,z,w+1), (x,y+1,z,w+1),
                        (x+1,y-1,z,w+1), (x+1,y,z,w+1), (x+1,y+1,z,w+1),
                        (x-1,y-1,z+1,w+1), (x-1,y,z+1,w+1), (x-1,y+1,z+1,w+1),
                        (x,y-1,z+1,w+1), (x,y,z+1,w+1), (x,y+1,z+1,w+1),
                        (x+1,y-1,z+1,w+1), (x+1,y,z+1,w+1), (x+1,y+1,z+1,w+1),
                    ]
                    # count the surrounding cells
                    surrounding_active = 0
                    for cell in surroundings:
                        if cell in space:
                            surrounding_active += 1
                    # determine what should happen to the cell!
                    if current_cell in space:
                        if surrounding_active==2 or surrounding_active==3:
                            space_step[current_cell] = True
                    else:
                        if surrounding_active==3:
                            space_step[current_cell] = True
    space = space_step
print(len(space))
