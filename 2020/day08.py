### PART 1
# read the input
f = open('input/day08.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse the input into instructions
instructions = [e.split() for e in input]
instructions = [[e[0], int(e[1])] for e in instructions]
# find what the accumulator value is before first loop line
# do this by running the instructions and keeping track of the accumulator
accumulator = 0
curr_line = 0
visited = [False]*len(instructions)
while ((curr_line < len(instructions) and not visited[curr_line])):
    next_line = curr_line + 1
    # check what the instruction is
    if instructions[curr_line][0] == 'acc':
        # modify the accumulator
        accumulator += instructions[curr_line][1]
    elif instructions[curr_line][0] == 'jmp':
        # jump to instruction relative to itself
        next_line = curr_line + instructions[curr_line][1]
    elif instructions[curr_line][0] == 'nop':
        # don't do anything
        pass
    visited[curr_line] = True
    curr_line = next_line
print(accumulator)

### PART 2
# we want to change exactly one nop to a jmp (or vice versa), keeping the parameter the same
# such that it removes the infinite loop!
# do this by checking every single nop/jmp, flip them, and see if a loop is avoided
# (we know a loop is avoided if the current line run is past the end of the program)
def checkTermination(instr):
    accumulator = 0
    curr_line = 0
    visited = [False]*len(instr)
    while not visited[curr_line]:
        next_line = curr_line + 1
        # check what the instruction is
        if instr[curr_line][0] == 'acc':
            # modify the accumulator
            accumulator += instr[curr_line][1]
        elif instr[curr_line][0] == 'jmp':
            # jump to instruction relative to itself
            next_line = curr_line + instr[curr_line][1]
        elif instr[curr_line][0] == 'nop':
            # don't do anything
            pass
        # check for termination
        if next_line >= len(visited):
            return True, accumulator
        visited[curr_line] = True
        curr_line = next_line
    # if we reached here, the program didn't terminate
    return False, accumulator
# run through all instructions and flip nop/jmp instructions
flip = {'nop':'jmp', 'jmp':'nop'}
for i in range(len(instructions)):
    # if this is an instruction we can flip
    if instructions[i][0] in flip:
        # flip it!
        instructions[i][0] = flip[instructions[i][0]]
        # test it!
        terminates, accumulator = checkTermination(instructions)
        if terminates:
            print(accumulator)
            break
        # flip it back!
        instructions[i][0] = flip[instructions[i][0]]
