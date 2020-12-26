### PART 1
# read the input
f = open('input/day14.txt', 'r')
input = [x.strip() for x in f]
f.close()
# initialize memory
memory = {}
mask = 'X'*36
# apply a X/0/1 string mask to the int value, returns int result
def applyMask(mask, value):
    value = f'{value:036b}'
    value = ''.join([(value[i] if (mask[i]=='X') else mask[i]) for i in range(len(value))])
    value = int(value, 2)
    return value
for i in input:
    # iterate through instructions
    instr = i.split(' = ')
    if instr[0] == 'mask':
        # set the mask variable
        mask = instr[1]
    else:
        # write something passed through mask to memory
        location = int(instr[0][4:-1])
        value = int(instr[1])
        memory[location] = applyMask(mask, value)
print(sum(memory.values()))

### PART 2
# reset the memory :)
memory = {}
# replace all of the Xs in value with characters from replacement
def replaceFloating(value, replacement):
    value = list(value)
    p = 0
    for i in range(len(value)):
        if value[i]=='X':
            value[i] = replacement[p]
            p += 1
    return ''.join(value)
# apply the memory address mask and return all floating locations
def getLocations(mask, value):
    value = f'{value:036b}'
    value = ''.join([(value[i] if (mask[i]=='0') else mask[i]) for i in range(len(value))])
    num_floating = sum([1 for c in value if c=='X'])
    values = []
    for i in range(pow(2, num_floating)):
        floating = '{i:0{num_floating}b}'.format(i=i, num_floating=num_floating)
        values.append(int(replaceFloating(value, floating), 2))
    return values
for i in input:
    # iterate through instructions
    instr = i.split(' = ')
    if instr[0] == 'mask':
        # set the mask variable
        mask = instr[1]
    else:
        # write a value to masked memory / memory address decoder locations
        location = int(instr[0][4:-1])
        value = int(instr[1])
        for loc in getLocations(mask, location):
            memory[loc] = value
print(sum(memory.values()))
