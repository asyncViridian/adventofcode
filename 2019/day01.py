### PART 1
# read the input
f = open('input/day01.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse input into mass integers
mass = [int(i) for i in input]
# parse mass values into fuel required
fuel = [((i // 3) - 2) for i in mass]
# and get the total fuel requirements...
print(sum(fuel))

### PART 2
