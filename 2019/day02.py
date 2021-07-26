### PART 1
# read the input
f = open('input/day02.txt', 'r')
input = [x.strip() for x in f]
f.close()
program = [int(i) for i in input[0].split(',')]
# do the initial program change needed (set pos 1 = 12, pos 2 = 2)
program[1] = 12
program[2] = 2
# now step through and run the program
program_counter = 0
while (program[program_counter] != 99):
    if program[program_counter] == 1:
        # addition opcode
        program[program[program_counter+3]] = program[program[program_counter+1]] + program[program[program_counter+2]]
    elif program[program_counter] == 2:
        # multiplication opcode
        program[program[program_counter+3]] = program[program[program_counter+1]] * program[program[program_counter+2]]
    else:
        # something went wrong
        print("something went wrong")
        break
    # now step forward 4...
    program_counter += 4
    # print(program)
print(program[0])

### PART 2
