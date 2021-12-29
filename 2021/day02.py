### PART 1
# read the input into a list
f = open('input/day02.txt', 'r')
input = [x for x in f]
f.close()
# split all sub instructions into pieces
instr = [e.split(' ') for e in input]
instr = [(e[0], int(e[1])) for e in instr]
# figure out position of (horizontal, depth)
pos = [0, 0]
for i_t, i_n in instr:
    if i_t=='forward':
        pos[0] += i_n
    elif i_t=='down':
        pos[1] += i_n
    elif i_t=='up':
        pos[1] -= i_n
print(pos, pos[0]*pos[1])

### PART 2
# TODO
