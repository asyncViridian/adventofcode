### PART 1
# read the input into a list
f = open('input/day03.txt', 'r')
input = [x.strip() for x in f]
f.close()
# calculate gamma (most common bit) value
gamma = ''
for i in range(len(input[0])):
    count_1 = sum([(1 if e[i]=='1' else 0) for e in input])
    if count_1 > 0.5*len(input):
        gamma += '1'
    else:
        gamma += '0'
# calculate epsilon value (always complement of gamma)
epsilon = ''
for i in gamma:
    if i=='1':
        epsilon += '0'
    else:
        epsilon += '1'
# calculate decimal values of each
def binary_to_decimal(value):
    result = 0
    for i in value:
        result *= 2
        if i=='1':
            result += 1
    return result
print(gamma, epsilon, binary_to_decimal(gamma) * binary_to_decimal(epsilon))

### PART 2
# TODO
