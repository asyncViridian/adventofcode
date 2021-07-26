### PART 1
# read the input
f = open('input/day02.txt', 'r')
input = [x.strip() for x in f]
f.close()
program = [int(i) for i in input[0].split(',')]
# step through and run the program
def runProgram(program, pos_1=None, pos_2=None):
    program = program.copy()
    # set the pos_1 and pos_2 arguments if given
    if pos_1 != None:
        program[1] = pos_1
    if pos_2 != None:
        program[2] = pos_2
    # now start running the program
    instr_ptr = 0
    while (program[instr_ptr] != 99):
        # print(program)
        if instr_ptr >= len(program):
            # out of bounds in the program?
            return [-1]
        elif program[instr_ptr] == 1:
            # addition instruction
            program[program[instr_ptr+3]] = program[program[instr_ptr+1]] + program[program[instr_ptr+2]]
            instr_ptr += 4
        elif program[instr_ptr] == 2:
            # multiplication instruction
            program[program[instr_ptr+3]] = program[program[instr_ptr+1]] * program[program[instr_ptr+2]]
            instr_ptr += 4
        else:
            # something went wrong... invalid instruction
            return [-1]
    return program
print(runProgram(program, pos_1=12, pos_2=2)[0])

### PART 2
# need to figure out what values positions 1, 2 should be set to to make the output=19690720
# note that they must both be 0<=x<len(program)
for i in range(len(program)):
    for j in range(len(program)):
        result = runProgram(program, pos_1=i, pos_2=j)[0]
        if result == 19690720:
            print((100*i) + j)
            break
# https://adventofcode.com/2019/day/2
